# Параметры

disk_capacity_mb = 1.44  # Объем дискеты в Мб
pages = 100               # Количество страниц в книге
lines_per_page = 50      # Число строк на странице
chars_per_line = 25      # Количество символов в строке
bytes_per_char = 4       # Количество байт для хранения одного символа

# Расчет объема одной книги
total_chars = pages * lines_per_page * chars_per_line  # Общее количество символов в книге
book_size_bytes = total_chars * bytes_per_char          # Объем книги в байтах

# Конвертация объема дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 Кб, 1 Кб = 1024 байт

# Расчет количества книг, которые поместятся на дискету
number_of_books = disk_capacity_bytes // book_size_bytes


print("Количество книг, помещающихся на дискету:", round(number_of_books))
