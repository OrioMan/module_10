import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Время начала выполнения функций
start_time = time()

# Вызываем функции с разными аргументами
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Время окончания выполнения функций
end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Время начала выполнения потоков
start_time_threads = time()

# Создаем потоки
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

# Запускаем потоки
for thread in threads:
    thread.start()

# Ожидаем завершения потоков
for thread in threads:
    thread.join()

# Время окончания выполнения потоков
end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")
