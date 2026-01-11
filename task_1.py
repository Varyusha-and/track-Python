money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0

for i in range(1, 10):
    if i == 1:
        money_capital = money_capital - (spend - salary)
        count += 1
    if i >= 2 and money_capital > (spend - salary) :
        s = spend * increase
        spend = spend + s
        money_capital = money_capital - (spend - salary)
        count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)