from multiprocessing import Process
import os
import time

def worker(name, iterations=10):
    for i in range(iterations):
        print(f"Процесс {name}, итерация {i}, PID: {os.getpid()}")
        time.sleep(0.1)  # Имитация работы

if __name__ == "__main__":
    # Создаем список процессов
    processes = []
    process_names = ["Worker-1", "Worker-2", "Worker-3"]
    
    # Создаем и запускаем все процессы
    for name in process_names:
        p = Process(target=worker, args=(name,))
        processes.append(p)
        p.start()
        print(f"Запущен процесс: {name}")
    
    # Ожидаем завершения всех процессов
    for p in processes:
        p.join()
    
    print("Все процессы завершены!")