salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
summ = spend
need_money = 0  # количество денег, чтобы прожить 10 месяцев
all_salary = salary * 10
for i in range(2, months + 1):
    spend += (spend * increase)
    summ += spend
need_money = summ - all_salary
print(round(need_money))
