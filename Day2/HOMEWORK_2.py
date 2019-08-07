# 4. Napisz funkcję, która przyjmuje dowolną ilość parametrów
# - zaloz ze beda podawane liczbowe, funkcja ma wypisywac te parametry, uzywajac petli for in

def myFun(*argv):
    for arg in argv:
        print(int(arg))

myFun(1,2,3)

# 5. Zmodyfikuj funkcje z zadania wyzej tak, aby na koncu wypisala sume liczb podanych do funckji

def myFun(*argv):
    for arg in argv:
        print(int(arg))
    print(sum(argv))

myFun(1,2,3,5)

# 6. Inside - out - napisz dwie funckje - dodawanie (np o nazwie add) oraz
# mnozenie dwoch liczb (np o nazwie multiply), nastapnie wywolaj operację
#multiply(add(2, 6), 2)

def add(first_number, second_number):
    return first_number + second_number

print(add(1,2))

def multiply(first_num, second_num):
    return first_num * second_num

print(multiply(2, 6))
print(multiply(add(2, 6), 2))

# 7. Napisz funkcję rozbijajaca zdanie na slowa (ma zwracac liste ze slowami)
# oraz funkcje sortujaca liste slow, nastepnie wywolaj sortowanie na slowach podanego przez uzytkownika zdania
#sort_words(split_sentence_to_words(sentence))

def split_sentence_to_words(sentence):
    return (sentence.split())

def sort_words(list):
    list.sort()
    return list

print(split_sentence_to_words("aaa zzz  ccc ggg"))
print(sort_words(split_sentence_to_words('aaa zzz  ccc ggg')))
