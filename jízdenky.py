mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""
print("Dobrý den,vítáme vás na stránkách destiantio.")
print(cara)
print("Vyberte si z nabídky a posléze níže zadejte číslo destinace.")
print(nabidka)
print(cara)
destinace = int(input("číslo destinace: "))
if destinace > 6:
    print("zadejte platnou destinaci")
jmeno = input("Jméno: ")
prijeni = input("Přijmení: ")
email = input("Email: ")
print(cara)
cil = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]
print(cil)
print(cena, "-Kč", sep=" ")
print(cara)
print("Cestující: ",jmeno, prijeni)
print("Cena celkem: ",cena,"Kč")
print("Jízdenky byly odeslány na email: ",email)
print(cara)
