# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников
    participants_list_1 = group1.split(separator)
    participants_list_2 = group2.split(separator)

    # Находим общих участников с помощью множества
    common_participants = set(participants_list_1) & set(participants_list_2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

# Участники групп
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

# Проверяем работу функции с разделителем '|'
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники (разделитель '|'):", common_participants)

# Проверяем работу функции с разделителем ',' (по умолчанию)
common_participants_default = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники (разделитель ','):", common_participants_default)




