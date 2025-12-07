HOURS_IN_DAY = 24  # количество часов в дне постоянно
total_hours = 5000  # дано по задаче

days =  total_hours // HOURS_IN_DAY # TODO найти полное количество дней
hours = total_hours % HOURS_IN_DAY  # TODO найти оставшееся количество часов

print("Количество дней =", days)
print("Оставшееся количество часов =", hours)
