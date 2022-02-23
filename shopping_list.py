lista_zakupów={"piekarnia":["chleb", "pączek", "bułki"], "warzywniak":["marchew","seler","rukola"]}
zakupy = (lista_zakupów["piekarnia"]+lista_zakupów["warzywniak"])
for sklep, produkt in lista_zakupów.items():
    print("Idę do",sklep.capitalize(),",","kupuję tu następujące rzeczy:",produkt)
print("W sumie kupuję", (len(zakupy)),"produktów")