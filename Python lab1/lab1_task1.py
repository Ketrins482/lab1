numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


# Найти пропущенный элемент
missing_num = sum(num for num in numbers if num is not None)

# Заменить пропущенный элемент средним арифметическим всех остальных элементов списка
average = sum(num for num in numbers if num is not None)/len(numbers)
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average
        break



print("Измененный список:", numbers)
