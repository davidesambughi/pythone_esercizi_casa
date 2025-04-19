"""
pagina 90 R2.20

LO PSEUDOCIDICESEGUENTE DESCRIVE COME SCAMBIARE DUE LETTERE IN UNA PAROLA.

DATI: LA STRINGA mystring E DUE LETTERE "e" E "a"
TRASFORMA NEL CARATTERE * TUTTE LE OCCORENZE DELLA LETTERA "e"
TRASFORMA NEL CARATTERE "e" TUTTE LE OCCORENZE DELLA LETTERA "a"
TRASFORMA NEL CARATTERE "a" TUTTE LE OCCORENZE DELLA LETTERA "*"

"""

stringa = " marmalade"
contatore = ""
contatore1 = ""
contatore2 = ""

for i in stringa:
    if i!="e":
        contatore= contatore + i
    else :
        i= "*"
        contatore= contatore + i

for j in contatore:
    if j!="a":
        contatore1= contatore1 + j
    else :
        j= "e"
        contatore1= contatore1 + j  

for m in contatore1:
    if m!="*":
        contatore2= contatore2+ m
    else :
        m= "a"
        contatore2= contatore2 + m  
        
print(contatore2)


"""

CHAT GPT ------  UTILIZZA  REPLACE !!!

stringa = "marmalade"

# Step 1: sostituisci tutte le "e" con "*"
stringa = stringa.replace("e", "*")

# Step 2: sostituisci tutte le "a" con "e"
stringa = stringa.replace("a", "e")

# Step 3: sostituisci tutte le "*" con "a"
stringa = stringa.replace("*", "a")

print(stringa)

"""

"""
P2.4
SCRIVETE UN PROGRAMMA CHE CHIEDA ALL'UTENTE DUE NUMERI INTERI , E POI VISUALIZZI:
-SOMMA
-DIFFERENZA
-PRODOTTO
-VALORE MEDIO
-DISTANZA (VALORE ASSOLUTO DELLA DIFFERENZA)
-VALORE MASSIMO
-VALORE MINIMO

"""
try:
    v1=int(input("Inserisci il primo valore: "))
    v2=int(input("Inserisci il secondo valore: "))

    def somma (a,b):
        return a+b

    ris_somma=somma(v1,v2)

    def differenza (a,b):
        return a-b

    ris_differenza=differenza(v1,v2)

    def prodotto (a,b):
        return a*b

    ris_prodotto=prodotto(v1,v2)

    def media (a,b):
        return (a+b)/2

    ris_media=media(v1,v2)

    def distanza (a,b):
        return abs(a-b)

    ris_distanza=distanza(v1,v2)

    def massimo (a,b):   # !!!! non chiamare mai la funzione con il nome delle funzioni built-in (esempio sotto)
        return max(a,b)  # def max () : return max 
                         # perche in questo modo crei un loop infinito dove la funzione richiama se stessa 

    ris_max=max(v1,v2)

    def minimo (a,b):
        return min(a,b)

    ris_min=min(v1,v2)

    print(f"la somma dei due valori e' {ris_somma}, la differrenza e'{ris_differenza}, il prodotto e' {ris_prodotto}, la media e' {ris_media}, la distanza e' {ris_distanza}, il pi' grande e' {ris_max}, il piu piccolo e' {ris_min}" )
except ValueError:
    print("Errore: devi inserire due numeri interi, riprova.")


 """
 VERSIONE COMPATTA

 v1 = int(input("Inserisci il primo valore: "))
 v2 = int(input("Inserisci il secondo valore: "))

print(f"
Somma: {v1 + v2}
Differenza: {v1 - v2}
Prodotto: {v1 * v2}
Media: {(v1 + v2) / 2}
Distanza (valore assoluto): {abs(v1 - v2)}
Massimo: {max(v1, v2)}
Minimo: {min(v1, v2)}
")

 """

"""
P2.5-----------------
MIGLIORATE L'IMPAGINAZIONE DEI RISULTATI PRODOTTI DALL'ESERCIZIO PRECEDENTE, IN MODO CHE I NUMERI
SIANO INCOLONNATI CORRETTAMENTE:
SUM:           45
DIFFERENCE:    -5
PRODUCT:      500  
ETC
"""



 