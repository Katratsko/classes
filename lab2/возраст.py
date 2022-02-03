money = int(input("сколько денег на карточке"))
n = 0
while True:
    cost = int(input("введите расход"))
    if cost <= money:
        money -= cost
        n += 1
        print(money)
    else:
        print("расходы превышают баланс")
        print(f"количество покупок {n}, количество денег на карте {money}")
        break









