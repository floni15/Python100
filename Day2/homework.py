# EASY
# ZADANIE 1
float_but_int = 50 / 2
print(type(float_but_int))
print(dir(float_but_int))
print(float_but_int.__class__)

# ZADANIE 2
# 11011010
# 128	64	0	16	8	0	2	0	218

# ZADANIE 3
x = "Sun"
y = "is"
z = "setting"

print(f"{x}\n\t{y}\n\t\t{z}")

# MEDIUM
# 4
number = int(input ("Podaj Liczbe"))
print(f"Szescian liczby {number} wynosi: {number**3}, natomiast kwadrat wynosi: {number**2}")

# CHALLENGING
# 4
temperatura = int(input ("Podaj temperature"))
zimno = 10
cieplo = 20
goraco = 30
if temperatura <= zimno:
    print("zimno")
elif temperatura >= zimno and temperatura < goraco:
    print("cieplo")
else: print("goraco")

#5

n = int(input("Podaj liczbe"))

liczba = 1;
if n < 0:
    print("Nie mogę obliczyć silni");
elif (n == 0):
    print("Silnia dla zero jest równa 1");
else:
    while (n > 0):
        liczba = liczba * n

        n = n - 1

    print(f"Silnia wynosi ")
    print(liczba)