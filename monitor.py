
import os
import time

def get_cpu_usage():
    return os.popen("top -bn1 | grep 'Cpu(s)'").read()

def get_memory_usage():
    return os.popen("free -h").read()

def get_processes():
    return os.popen("ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head").read()

def clear_screen():
    os.system("clear")

def main():
    try:
        while True:
            clear_screen()
            print("===== LINUX SYSTEM MONITOR =====\n")

            print("🔹 CPU Usage:")
            print(get_cpu_usage())

            print("🔹 Memory Usage:")
            print(get_memory_usage())

            print("🔹 Top Processes:")
            print(get_processes())

            print("\nPress CTRL+C to exit...")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nExiting System Monitor...")

if __name__ == "__main__":
    main()
