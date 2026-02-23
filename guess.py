import random
print("Minēšanas spēle!")
skaitlis = random.randint(1,100)
meginajumi = 0
max_meginajumi = 10
print("Uzmini skaitli no 1 līdz 100!")
print("Tev ir 10 mēģinājumi.")
while meginajumi < max_meginajumi:
    try:
        minejums = int(input("Tavs minējums: "))
    except ValueError:
        print("Lūdzu ievadi veselu skaitli!")
        continue
    meginajumi += 1
    if minejums < skaitlis:
        print("Par mazu!")  
    elif minejums > skaitlis:
        print("Par lielu!")
    else:
        print(f"Apsveicu! Tu uzminēji ar {meginajumi} mēģinājumiem!")
        break
else:
    print("Mēģinājumi beigušies!")  
print(f"Pareizais skaitlis bija: {skaitlis}") 
