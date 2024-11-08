money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
def calculate_months_without_debt(money_capital, salary, spend, increase):
    months = 0

    while True:
        # Подсчет бюджета текущего месяца
        current_budget = salary + money_capital

        # Проверяем, можем ли мы покрыть расходы
        if current_budget >= spend:
            # Если можем, уменьшаем подушку безопасности на (расходы - зарплата)
            money_capital -= (spend - salary)
            months += 1

            # Увеличиваем расходы на 5% для следующего месяца
            spend *= (1 + increase)
        else:
            break  # Не можем покрыть расходы, заканчиваем цикл

    return months



# Рассчитываем количество месяцев без долгов
months_without_debt = calculate_months_without_debt(money_capital, salary, spend, increase)


print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)
