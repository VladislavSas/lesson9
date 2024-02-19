import psutil

def user_info():
    user = psutil.users()[0]
    print(f"Имя пользователя: {user.name}")
    print(f"{user.terminal}")
    print(f"Имя хоста: {user.host}")
    print(f"Время подключения:{user.started}")
    print(f"Процесс входа в систему:{user.pid}")

def disk_info():
    disk = psutil.disk_partitions()[0]
    print(f"Путь к устройсву: {disk.device}")
    print(f"Путь к точке монтирования: {disk.mountpoint}")
    print(f"Файловая система раздела: {disk.fstype}")
    print(f"Подключения для диска: {disk.opts}")
    print(f"Максимальная длина, которую может иметь имя файла: {disk.maxfile}")
    print(f"Максимальная длина, которую может иметь имя пути (имя каталога + имя базового файла: {disk.maxpath}")
    
def memory_info():
    memory = psutil.virtual_memory()
    print(f"Общая физическая память: {memory.total}")
    print(f"Используемая: {memory.used}")
    print(f"Не используется: {memory.free}")
    print(f"Процент использования: {memory.percent}%")
    
def swapmemory_info():
    swapmemory = psutil.swap_memory()
    print(f"Общая память подкачки в байтах: {swapmemory.total}")
    print(f"Используемая память подкачки в байтах: {swapmemory.used}")
    print(f"Свободная память подкачки в байтах: {swapmemory.free}")
    print(f"Процент использования: {swapmemory.percent}%")

def lan_info():
    lan = psutil.net_io_counters()
    print(f"Количество отправленных байтов: {lan.bytes_sent}")
    print(f"Количество полученных байтов: {lan.bytes_recv}")

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
    disk_info()
    memory_info()
    swapmemory_info()
    lan_info()
    
    all_processes = get_all_processes()

    if all_processes:
        for process in all_processes:
            print(f"PID: {process['pid']}, Name: {process['name']}")
    else:
        print("Нет запущенных процессов.")

