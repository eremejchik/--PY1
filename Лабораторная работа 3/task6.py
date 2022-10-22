list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max = list_numbers[0]

for number in list_numbers: # цикл для поиска наибольшего значения в списке
    if max < number:
        max = number

for i in range(len(list_numbers)): # цикл для поиска индекса первого максимального элемента
    if max == list_numbers[i]:
        max_index = i
        break # здесь break обрывает цикл, когда находит индекс первого максимального элемента

last_element = list_numbers[-1] # кладем в переменную последний элемент списка
list_numbers[-1] = list_numbers[max_index] # теперь последний элемент заменен на элемент с индексом max_index
list_numbers[max_index] = last_element # тот элемент, который имеет индекс max_index, заменить на элемент, который был последним
print(list_numbers)

