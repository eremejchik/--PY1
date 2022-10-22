salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
def skolko_nujno_deneg(zp, trati,mesiaci, inf, dolg):
    for mesiac in range(mesiaci):
        if mesiac > 1:
            dolg = dolg - zp + trati
        else:
            trati = trati*(1 + inf)
            dolg = dolg - zp + trati
    print(round(dolg))
skolko_nujno_deneg(salary, spend, months, increase, need_money)