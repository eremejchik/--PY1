src = not False and True or False and not True

# TODO расписать упрощение выражения

result = True and True or False and False # преобразуем отрицания
result = True or False # избавились от AND
result = True # избавляемся от OR
print(src == result)
