money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

inf = spend * increase
while money_capital + salary >= 0:
    if money_capital + salary > 0:
        money_capital -= spend
        money_capital -= inf
        month += 1

print(month)
