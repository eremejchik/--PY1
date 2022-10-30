

def get_count_char(str_):
    changed_str = str_.lower()  # опускаем буквы в нижний регистр
    normal_str = "".join(c for c in changed_str if c.isalpha())  # оставляем только буквы и склеиваем все символы в одну строку
    necessary_dict = {}
    for symbol in normal_str:
        if symbol in necessary_dict:
            necessary_dict[symbol] += 1
        else:
            necessary_dict[symbol] = 1
    return necessary_dict   # возвращаем словарь c частотой каждого символа

def function_for_dict(dict_):
    for key in dict_.kyes():   # перебираем ключи из принятого словаря
        dict_[key] = (dict_[key]/sum(dict_.values()))*100  # для каждого ключа перезаписываем значение
    return dict_   # на выходе перезаписанный словарь


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))