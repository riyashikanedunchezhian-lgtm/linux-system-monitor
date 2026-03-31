import os
import time
from datetime import datetime

LOG_FILE = "monitor.log"

def get_cpu_usage():
    output = os.popen("top -bn1 | grep 'Cpu(s)'").read()
    return output

def get_memory_usage():
    return os.popen("free -h").read()

def get_processes():
    return os.popen("ps -eo pid,cmd,%mem,%cpu --sort=-%cpu | head").read()

def log_data(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {data}\n")

def clear_screen():
    os.system("clear")

def check_alert(cpu_output):
    try:
        cpu_percent = float(cpu_output.split(',')[0].split()[1])
        if cpu_percent > 80:
            print("⚠️ HIGH CPU USAGE ALERT!")
    except:
        pass

def main():
    try:
        while True:
            clear_screen()
            print("===== LINUX SYSTEM MONITOR =====\n")

            cpu = get_cpu_usage()
            memory = get_memory_usage()
            processes = get_processes()

            print("🔹 CPU Usage:")
            print(cpu)
            check_alert(cpu)

            print("\n🔹 Memory Usage:")
            print(memory)

            print("🔹 Top Processes:")
            print(processes)

            log_data("CPU checked")

            print("\nPress CTRL+C to exit...")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nExiting System Monitor...")

if __name__ == "__main__":
    main()
