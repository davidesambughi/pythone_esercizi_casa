""" 
pagina 89 esercizi da R2.13 a R2.15
"""
      
"""
--R2.13---------------------------------------------------------------
Scrivete lo pseudocodice per un programma che legge una parola e ne visualizza il primo carattere,
l'ultimo e quello centrale (se è pari ,il primo dei due centrali)
-----------------

utente = input("Inserisci il tuo nome: ")
x = len(utente)

if x%2!=0:
    print(utente[0],utente[x//2],utente[-1])
else:
    print(utente[0],utente[x//2-1],utente[-1]) 
 """
    
    
"""
--R2.14------------------------------------------------------------------
Scrivete lo pseudocodice per un programma che chiede all utentedi fornire un 
nome completo(come Harold James Morgan) e visualizza un monogramma composto dalle iniziali dei nomi
----------------------

lista=[0]
contatore=0
utente= input('inserisci un nome: ')

for i in utente:
    contatore+=1
    if i== " ":
        lista.append(contatore)
        
print(lista)

for n in lista:
  print(utente[n].upper(),end="")
  """
  
"""
--R2.15-----------------------------------------------------
Scrivete lo pseudocodice per un programma che calcola la prima e l'ultima cifra di un numero.
Se,ad esempio, il dato in ingresso è  23456, il programma deve visualizzare 2 e 6.
usate % e log(x,10)--------
"""












    



