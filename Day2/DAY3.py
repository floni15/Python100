zdanie = "encyklopedia"

# print(zdanie[4])
# print(zdanie[-3])
# print(zdanie[2:8])
# print(zdanie[:7])
# print(zdanie[8:])
# print(zdanie[1:7:2])
# print(zdanie[::-1]) # odwrocenie co jeden znak
# print(zdanie[::2])  # wez całe zdanie co drugi znak

# ZADANIE

zdanie = input ("Wpisz zdanie")
pierwsza_litera = "a"
ostatnia_litera = "z"

if (zdanie.lower()[0])==pierwsza_litera:
    print("Zdanie zaczyna sie od pierwszej litery alfabetu")
elif (zdanie.lower()[-1]) ==ostatnia_litera:
    print("Zdanie zaczyna sie od ostatniej litery alfabetu")
else: print("inna litera niz a i z ")

# METODA

# zdanie = 'halo'
# if zdanie.find('ha') >= 0:
#     print("success")

# LISTA
# wyswietli 6 bo liczy od zera wiec najpierw 4,5,6 i potem znowu od zera czyli 6 bo drugi element
# lista = [
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
#          ]
#
# print(lista[1][2])