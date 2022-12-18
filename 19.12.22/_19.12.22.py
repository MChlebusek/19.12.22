#Задание 3: Бесполезные числа
def useless(lst):
    return max(lst) / len(lst)
print(useless([134, 4949, 12]))
print(useless([1, 8.3, -84, 3993, 0, 58]))
print(useless([-75, -0.09, 555, 11.2, 13.12, 55, 7.1]))



#Задание 4: Сортировка
from math import *
from random import *

a=list(map(int, input("Sisestage loend, eraldades need tähega [,]:").split(",")))
b=input("Mida soovite teha, sorteerige väikseimast suurimaks - 1 või suurimast väikseimani - 2:")
if b=='1':
    a.sort()
    print(a)
elif b=="2":
    a.sort(reverse=True)
    print(a)
else:
    print("ainult 1 või 2")




#Задание 5:
def all_eq(lst):

 max_item = max(lst, key=lambda x: len(x))

 max_len = len(max_item)

 return [item.ljust(max_len, '_') for item in lst]


print(all_eq(['крот', 'белка', 'выхухоль']))

print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))

print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))



#2.Перемена мест

list =[1,2,3,4,5,6,7,8]
a = int(input("arv: "))
k=-1
for i in range(a):
  list[i], list[k] = list[k], list[i]
  k -= 1
print(list)


#Почтовый индекс
maad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]

index=""
n=0
while type(index)!=int or n!=5:
    try:
        index=int(input("Index:"))
        n=len(str(index))
    except:
        print("Vale index!")
#12345


index_list=list(str(index))
print(maad[int(index_list[0])-1])