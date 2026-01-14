fogyasztas = float(input("Fogyasztás (l/100km): "))
ar = float(input("Benzin ára (Ft/l): "))
ut = float(input("Út hossza (km): "))

szukseges_uzemanyag = (ut / 100) * fogyasztas
koltseg = szukseges_uzemanyag * ar

print("Útiköltség:", koltseg, "Ft")