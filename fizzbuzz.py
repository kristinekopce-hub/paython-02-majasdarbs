import sys

# ---- 1. Pārbaude vai N ir dots gamma ---->
if len(sys.argv) < 2:
    print("Kļūda: lūdzu norādi skaitli N.")
    print("Piemērs: python fizzbuzz.py 20")
    sys.exit()

# ---- 2. Pārbaude vai N ir vesels skaitlis ----
try:
    N = int(sys.argv[1])
except ValueError:
    print("Kļūda: N jābūt veselam skaitlim.")
    sys.exit()

# ---- 3. Noteikumi (parametrizācija) ----
rules = {
    3: "Fizz",
    5: "Buzz",
    7: "Jazz"   # Bonuss
}

# ---- 4. Cikls no 1 līdz N ----
for i in range(1, N + 1):

    # 🔹 Klasiskā secība (3 un 5 vispirms)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        result = ""

        # Bonusa dinamiskā daļa
        for divisor, word in rules.items():
            if i % divisor == 0:
                result += word

        if result:
            print(result)
        else:
            print(i)