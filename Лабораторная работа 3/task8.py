money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

def kak_prozjit_na_zp(zp, podushka, rashodi, mesiac, inf): # создаем функцию

    while podushka > 0:
        if mesiac > 1:
            rashodi = rashodi*(inf+1)
            podushka = podushka - rashodi + zp
        else:
            podushka = podushka - rashodi + zp
        mesiac = mesiac + 1
    print(mesiac)

kak_prozjit_na_zp(salary, money_capital, spend, month, increase) # вызываем функцию