import psutil
from colorama import Fore, Style

def user_info():
    user = psutil.users()[0]
    print(f"{Fore.CYAN}Имя пользователя:{Style.RESET_ALL} {user.name}")
    print(f"{Fore.CYAN}Терминал:{Style.RESET_ALL} {user.terminal}")
    print(f"{Fore.CYAN}Имя хоста:{Style.RESET_ALL} {user.host}")
    print(f"{Fore.CYAN}Время подключения:{Style.RESET_ALL} {user.started}")
    print(f"{Fore.CYAN}Процесс входа в систему:{Style.RESET_ALL} {user.pid}")

def disk_info():
    disk = psutil.disk_partitions()[0]
    print(f"{Fore.GREEN}Путь к устройству:{Style.RESET_ALL} {disk.device}")
    print(f"{Fore.GREEN}Путь к точке монтирования:{Style.RESET_ALL} {disk.mountpoint}")
    print(f"{Fore.GREEN}Файловая система раздела:{Style.RESET_ALL} {disk.fstype}")
    print(f"{Fore.GREEN}Параметры монтирования:{Style.RESET_ALL} {disk.opts}")
    print(f"{Fore.GREEN}Максимальная длина имени файла:{Style.RESET_ALL} {disk.maxfile}")
    print(f"{Fore.GREEN}Максимальная длина имени пути:{Style.RESET_ALL} {disk.maxpath}")

def memory_info():
    memory = psutil.virtual_memory()
    print(f"{Fore.MAGENTA}Общая физическая память:{Style.RESET_ALL} {memory.total}")
    print(f"{Fore.MAGENTA}Используется:{Style.RESET_ALL} {memory.used}")
    print(f"{Fore.MAGENTA}Свободно:{Style.RESET_ALL} {memory.free}")
    print(f"{Fore.MAGENTA}Процент использования:{Style.RESET_ALL} {memory.percent}%")

def swapmemory_info():
    swapmemory = psutil.swap_memory()
    print(f"{Fore.YELLOW}Общая память подкачки:{Style.RESET_ALL} {swapmemory.total}")
    print(f"{Fore.YELLOW}Используется памяти подкачки:{Style.RESET_ALL} {swapmemory.used}")
    print(f"{Fore.YELLOW}Свободная память подкачки:{Style.RESET_ALL} {swapmemory.free}")
    print(f"{Fore.YELLOW}Процент использования:{Style.RESET_ALL} {swapmemory.percent}%")

def lan_info():
    lan = psutil.net_io_counters()
    print(f"{Fore.BLUE}Отправлено байтов:{Style.RESET_ALL} {lan.bytes_sent}")
    print(f"{Fore.BLUE}Получено байтов:{Style.RESET_ALL} {lan.bytes_recv}")

def get_all_processes():
    all_processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            all_processes.append({
                'pid': process.info['pid'],
                'name': process.info['name']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return all_processes

if __name__ == "__main__":
    user_info()
    print("\n---\n")
    disk_info()
    print("\n---\n")
    memory_info()
    print("\n---\n")
    swapmemory_info()
    print("\n---\n")
    lan_info()
    print("\n---\n")

    all_processes = get_all_processes()

    if all_processes:
        print(f"{Fore.CYAN}Запущенные процессы:{Style.RESET_ALL}")
        for process in all_processes:
            print(f"{Fore.CYAN}PID:{Style.RESET_ALL} {process['pid']}, {Fore.CYAN}Name:{Style.RESET_ALL} {process['name']}")
    else:
        print(f"{Fore.CYAN}Нет запущенных процессов.{Style.RESET_ALL}")
