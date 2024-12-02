import requests
import time
import sys

def main():
    # Проверка аргументов командной строки
    if len(sys.argv) < 2:
        print("Использование: python script.py <url> [num_requests]")
        sys.exit(1)

    url = sys.argv[1]
    num_requests = int(sys.argv[2]) if len(sys.argv) > 2 else 100  # Количество запросов по умолчанию 100
    timeout = 5  # Тайм-аут для каждого запроса в секундах

    response_times = []

    print(f"Начало теста производительности на {url}")

    for i in range(num_requests):
        start_time = time.time()
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Ошибка при запросе {i + 1}: {e}")
            response_times.append(None)
            continue

        elapsed_time = time.time() - start_time
        response_times.append(elapsed_time)
        print(f"Запрос {i + 1} выполнен за {elapsed_time:.4f} сек.")

    # Статистика теста
    successful_requests = [t for t in response_times if t is not None]
    if successful_requests:
        avg_time = sum(successful_requests) / len(successful_requests)
        print(f"\nСреднее время отклика: {avg_time:.4f} сек.")
    else:
        print("\nВсе запросы завершились ошибкой.")

    print(f"Общее количество запросов: {num_requests}")
    print(f"Успешных запросов: {len(successful_requests)}")
    print(f"Ошибок: {num_requests - len(successful_requests)}")

if __name__ == "__main__":
    main()
