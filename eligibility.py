# pārvauda vecumu un citas prasības, lai noteiktu, vai persona ir piemērota vakcinācijai
def get_iegut_vecumu (prompt):
    while True:
        try:
            vecums = int(input(prompt +": ").strip())
            if vecums < 0:
                print("Kļūda: Vecums nevar būt negatīvs.")
                continue
            return vecums
        except ValueError:
            print("Kļūda: Lūdzu, ievadi derīgu vecumu.")
vecums = get_iegut_vecumu("Ievadi personas vecumu")
if vecums >= 18:
    print("Persona ir balsstiesīga.")
else:
    print("Persona ir pārāk jauna, lai būtu balsstiesīga.")
# Īrēt auto (vecums >=21 un vai ir autovadītāja apliecība)

def iegut_vecumu(prompt):
    while True:
        try:
            vecums = int(input(prompt + ": ").strip())
            if vecums < 0:
                print("Kļūda: Vecums nevar būt negatīvs.")
                continue
            return vecums
        except ValueError:
            print("Kļūda: Lūdzu, ievadi derīgu skaitli.")

# Funkcija, kas prasa jā/nē jautājumu un atgriež True/False
def get_bool_input(prompt):
    while True:
        autovaditaja_aplieciba = input(prompt + " (jā/nē): ").strip().lower()
        if autovaditaja_aplieciba == "jā":
            return True
        elif autovaditaja_aplieciba == "nē":
            return False
        else:
            print("Lūdzu ievadi 'jā' vai 'nē'.")

# Iegūstam datus
vecums = iegut_vecumu("Ievadi savu vecumu")
ir_aplieciba = get_bool_input("Vai tev ir autovadītāja apliecība")

# Loģiska izteiksme: vai persona drīkst īrēt auto
var_iret_auto = (vecums >= 21) and ir_aplieciba

# Rezultāta izvada
print(f"Persona drīkst īrēt auto: {var_iret_auto}")
