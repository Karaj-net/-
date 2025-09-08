ves = int(input("Введите вес"))
rost = float(input("Введите рост"))

BMI = ves / (rost ** 2)
print("Ваш BMI: ", round(BMI, 3))

if BMI < 18.5:
    print("У вас недостаток веса")
elif 18.5 <= BMI < 25:
    print("У вас норма веса")
elif 25 <= BMI < 30:
    print("У вас избытычный вес")
elif 30 <= BMI:
    print("У вас ожирение")