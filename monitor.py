import os
import time
import platform
from datetime import datetime

LOG_FILE = "monitor.log"

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def get_cpu_usage():
    if platform.system() == "Windows":
        return os.popen('powershell "Get-CimInstance Win32_Processor | Select-Object LoadPercentage"').read()
    else:
        return os.popen("top -bn1 | grep 'Cpu(s)'").read()

def get_memory_usage():
    if platform.system() == "Windows":
        return os.popen('powershell "Get-CimInstance Win32_OperatingSystem | Select FreePhysicalMemory,TotalVisibleMemorySize"').read()
    else:
        return os.popen("free -h").read()

def get_processes():
    if platform.system() == "Windows":
        return os.popen("tasklist").read()
    else:
        return os.popen("ps -eo pid,cmd,%mem,%cpu --sort=-%cpu | head").read()

def log_data(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {data}\n")

def main():
    try:
        while True:
            clear_screen()
            print("===== SYSTEM MONITOR =====\n")

            cpu = get_cpu_usage()
            memory = get_memory_usage()
            processes = get_processes()

            print("🔹 CPU Usage:")
            print(cpu)

            print("🔹 Memory Usage:")
            print(memory)

            print("🔹 Top Processes:")
            print(processes[:1000])

            log_data("System checked")

            print("\nPress CTRL+C to exit...")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nExiting System Monitor...")

if __name__ == "__main__":
    main()
