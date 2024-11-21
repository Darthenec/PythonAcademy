zamestnanci = ["František", "Anna", "Jakub", "Klára"]

print("zamestnanci na začátku:", zamestnanci)

zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")

print("nová jména přidána:", zamestnanci_a)

zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")

print("nová jména vložena:", zamestnanci_b)