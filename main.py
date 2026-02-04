# uloha 1
with open("text.txt", "r") as file:
    ctenicko=file.readlines()
    print(len(ctenicko))

# uloha 2
asd=0
with open("text.txt","r") as f:
    abc=f.readlines()
    for i in abc:
        if len(i) > asd: asd=len(i)
    print(asd)

# uloha 3
soucet=0
with open("cisla.txt", "r") as file:
    cteni=file.readlines()
    for i in cteni: soucet=soucet+int(i)
print(soucet)

# uloha 4
soucet=0
with open("cisla.txt", "r") as file:
    cteni=file.readlines()
    for i in cteni: soucet=soucet+int(i)
    prumer=soucet/len(cteni)
print(round(prumer, 2))

# uloha 5
with open("text.txt", "r") as file:
    cteni=file.read()
    with open("text_kopie.txt", "w") as file2:
        file2.write(cteni.upper())