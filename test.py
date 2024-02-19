import psutil
from colorama import Fore, Style
import functools
from tabulate import tabulate

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        filename = f"{func.__name__}_log.txt"
        
        with open(filename, 'a') as file:
            file.write(f"Выполнение функции {func.__name__}...\n")
            
            result = func(*args, **kwargs)
            
            file.write(f"Результат: {result}\n\n")
        
        return result
    
    return wrapper

def print_table(title, data):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{title}{Style.RESET_ALL}")
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
    print("\n")

@log_execution
def user_info():
    user = psutil.users()[0]
    return {
        'Имя пользователя': user.name,
        'Терминал': user.terminal,
        'Имя хоста': user.host,
        'Время подключения': user.started,
        'Процесс входа в систему': user.pid
    }

@log_execution
def disk_info():
    disk = psutil.disk_partitions()[0]
    return {
        'Путь к устройству': disk.device,
        'Путь к точке монтирования': disk.mountpoint,
        'Файловая система раздела': disk.fstype,
        'Параметры монтирования': disk.opts,
        'Максимальная длина имени файла': disk.maxfile,
        'Максимальная длина имени пути': disk.maxpath
    }

@log_execution
def memory_info():
    memory = psutil.virtual_memory()
    return {
        'Общая физическая память': memory.total,
        'Используется': memory.used,
        'Свободно': memory.free,
        'Процент использования': memory.percent
    }

@log_execution
def swapmemory_info():
    swapmemory = psutil.swap_memory()
    return {
        'Общая память подкачки': swapmemory.total,
        'Используется памяти подкачки': swapmemory.used,
        'Свободная память подкачки': swapmemory.free,
        'Процент использования': swapmemory.percent
    }

@log_execution
def lan_info():
    lan = psutil.net_io_counters()
    return {
        'Отправлено байтов': lan.bytes_sent,
        'Получено байтов': lan.bytes_recv
    }

@log_execution
def get_all_processes():
    all_processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            all_processes.append({
                'PID': process.info['pid'],
                'Name': process.info['name']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return all_processes

if __name__ == "__main__":
    user_result = user_info()
    disk_result = disk_info()
    memory_result = memory_info()
    swapmemory_result = swapmemory_info()
    lan_result = lan_info()
    all_processes_result = get_all_processes()

    print_table("Информация о пользователе", [user_result])
    print_table("Информация о диске", [disk_result])
    print_table("Информация о памяти", [memory_result])
    print_table("Информация о памяти подкачки", [swapmemory_result])
    print_table("Информация о сети", [lan_result])

    if all_processes_result:
        print_table("Запущенные процессы", all_processes_result)
    else:
        print(f"{Fore.CYAN}Нет запущенных процессов.{Style.RESET_ALL}")
