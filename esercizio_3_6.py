lista_invitati = ["antonio", "edoardo", "samuele"]

print ("olala, abbiamo trovato un tavolo ancor più grande")

lista_invitati.insert (0, "mirko")

lista_invitati.insert (len(lista_invitati)//2, "matteo")

lista_invitati.append ("marcello")

for invitati in lista_invitati:
    print (f"{lista_invitati},sei invitato a cena")
