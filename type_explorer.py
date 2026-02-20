# STR
vieta = "Riga"
grupa = "Calis"
# INT
vecums = 4
skaits = 10
# FLOAT
cena = 35.00
stundas_laiks = 0.20
# BOOL
ir_aktivs = True    
ir_nokavejjis = False
# NONE (nav vertibas)
rezultats = None
print("vieta:", "| tips:", type(vieta))
print("grupa:", "| tips:", type(grupa)) 
print("vecums:", "| tips:", type(vecums)) 
print("cena:", "| tips:", type(cena))
print("ir_aktivs:", "| tips:", type(ir_aktivs))
print("ir_nokavejjis:", "| tips:", type(ir_nokavejjis))
print("rezultats:", "| tips:", type(rezultats))
if stundas_laiks == 0.00:
    cena = 0.00 
print("stundas_laiks:", "| tips:", type(stundas_laiks))
print("cena:", "| tips:", type(cena))
if stundas_laiks <= 0.05:
    cena = 0.00
try:
    stundas_laiks = float(input("Ievadi stundas laiku: "))
except ValueError:
    print("Kļūda: Lūdzu, ievadi derīgu stundas laiku.")
    