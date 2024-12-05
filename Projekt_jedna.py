
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vít Vondráček
email: vitvondr95@seznam.cz
""")

from collections import Counter

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#slovník uživatelu pro přihlášení.
uzivatele = {
    "bob" : "123", 
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

# Vstup pro uživ jméno a heslo.
jmeno = input("Zadejte uživatelksé jméno: ")
heslo = input("Zadejte heslo: ")

# ověření přihlášení
if jmeno in uzivatele and uzivatele[jmeno] == heslo:
    print("Přihášení bylo uspěšné, vítejte",(jmeno))
else:
    print("Špatně zadané uživatelské údaje. Ukončuji program.")
    exit()
# Zobrazení výzvy pro uživatele
print("Máme na výběr ze 3 textů, vyberte text zadáním čísla 1, 2 nebo 3:")

# Získání vstupu od uživatele
vyber = input("Zadejte číslo textu: ")

# Kontrola vstupu
if vyber in ["1", "2", "3"]:
    text = TEXTS[int(vyber) - 1]
else:
     print("Chyba: Musíte zadat číslo 1, 2 nebo 3. Ukončuji program.")
     exit()

# Rozdeleni textu na slova
slova = text.split()

# Inicializace počítadel
pocet_slov = len(slova)
pocet_velka_pismena = 0
pocet_vse_velka = 0
pocet_mala_pismena = 0
pocet_cisel = 0
suma_cisel = 0
# Získání délek slov
delky_slov = [len(slovo.strip(",.?!")) for slovo in slova]

"""
 # Ruční počítání četností délek pomocí slovníku
cetnosti = {}
for delka in delky_slov:
    if delka in cetnosti:
        cetnosti[delka] += 1
    else:
        cetnosti[delka] = 1

"""
# dosazení jednoduší metody importováním counteru
delky_count = Counter(delky_slov)


# Samotné počítání
for slovo in slova:
    # Kontrola na velké první písmeno.
    if slovo.istitle():
        pocet_velka_pismena += 1
    # Kontrola na všechna velká písmena.
    if slovo.isupper() and slovo.isalpha():
        pocet_vse_velka += 1
    # Kontrola malých písmen.
    if slovo.islower():
        pocet_mala_pismena += 1
    # Kontrola čísel.
    if slovo.isdigit():
        pocet_cisel += 1
        suma_cisel += int(slovo)
    
# Výsledky analýzy
print("\n--- Výsledky analýzy ---")
print(f"Celkový počet slov: {pocet_slov}")
print(f"Počet slov začínajících velkým písmenem: {pocet_velka_pismena}")
print(f"Počet slov psaných velkými písmeny: {pocet_vse_velka}")
print(f"Počet slov psaných malými písmeny: {pocet_mala_pismena}")
print(f"Počet čísel: {pocet_cisel}")
print(f"Součet všech čísel: {suma_cisel}")

# Výpis textového grafu
print("\n--- Textový graf četnosti délek slov ---")
for delka, pocet in sorted(delky_count.items()):
    print(f"{delka:2}| {'*' * pocet} {pocet}")