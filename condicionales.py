números = [5, 8, 15, 22, 31]

for n in números:
    if n % 2 == 0 and n > 10:
        print(f"{n} es par y mayor que 10")
    elif n % 2 == 0:
        print(f"{n} es par pero menor o igual a 10")
    else:
        print(f"{n} es impar")
print ("hola joaquin")