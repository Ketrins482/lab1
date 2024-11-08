# TODO Напишите функцию для поиска индекса товара

def find_item_index(items_list, target_item):
    try:
        # Метод index() возвращает индекс первого вхождения элемента
        return items_list.index(target_item)
    except ValueError:
        # Если элемент не найден, выбрасывается исключение ValueError
        return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

find_items = ['банан', 'груша', 'персик']
for find_item in find_items:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")



