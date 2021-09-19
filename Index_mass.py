m = float (input("Введите ваш вес в кг: "))
h = float (input("Введите ваш рост в см: "))
h = h/100
index_mass = float(m / (h*h))
if float(index_mass) < 18.5:
    print ("Недостаточная масса")
elif float(index_mass) >= 18.5 and float(index_mass) <= 24.99:
    print ("Оптимальная масса")
elif float(index_mass) > 25:
    print ("Избыточная масса")
