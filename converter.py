minutes = 20
hours = minutes / 60
import math
# Konstante
MINUTES_PER_HOUR = 60

try:
    # Lietotāja izvēle
    minutes = int(input("Ievadi minūtes: "))
    # Aprēķins stundas
    hours = minutes / MINUTES_PER_HOUR
    # Nopaļošana uz augsu 2 cipari aiz komata
    hours_ceiled = math.ceil(hours * 100) / 100
    #rezultāta izvadīšana ar f-string
    print(f"{minutes} minūtes ir {hours_ceiled:.2f} stundas")
except ValueError:
    print("Kļūda: Lūdzu, ievadi derīgu minūšu skaitu.")