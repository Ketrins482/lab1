salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


def calculate_safety_capital(salary, spend, months, increase):
    # Переменная для накопления необходимой подушки безопасности
    money_capital = 0

    # Расчет вычетов по месяцам
    for month in range(months):
        # Если это не первый месяц, применяем увеличение расходов
        if month > 0:
            spend *= (1 + increase)

        # Определяем, сколько денег не хватает
        deficit = spend - salary

        # Если есть нехватка, добавляем ее к подушке безопасности
        if deficit > 0:
            money_capital += deficit

    return round(money_capital)



# Рассчитываем необходимую подушку безопасности
required_capital = calculate_safety_capital(salary, spend, months, increase)


# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {required_capital}" )
