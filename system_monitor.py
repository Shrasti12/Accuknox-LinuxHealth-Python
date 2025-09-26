import psutil
import logging
import time

# Set thresholds
CPU_THRESHOLD = 80   # %
MEM_THRESHOLD = 80   # %
DISK_THRESHOLD = 90  # %

# Configure logging
logging.basicConfig(filename='system_monitor.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def alert(message):
    print(message)
    logging.warning(message)

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        alert(f'CPU usage high: {cpu}%')
    return cpu

def check_memory():
    mem = psutil.virtual_memory().percent
    if mem > MEM_THRESHOLD:
        alert(f'Memory usage high: {mem}%')
    return mem

def check_disk():
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        alert(f'Disk usage high: {disk}%')
    return disk

def check_processes():
    proc_count = len(psutil.pids())
    # Example: Alert if process count exceeds 300
    if proc_count > 300:
        alert(f'Number of running processes is high: {proc_count}')
    return proc_count

def monitor(interval=60):
    while True:
        cpu = check_cpu()
        mem = check_memory()
        disk = check_disk()
        procs = check_processes()
        logging.info(f'CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%, Processes: {procs}')
        print(f'CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%, Processes: {procs}')
        time.sleep(interval)

if __name__ == "__main__":
    monitor()
