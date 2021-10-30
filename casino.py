from random import randrange
from math import  ceil
import os
ContinueLaPartie=True
ng=randrange(50)
print("Hello\nvoici les regles du jeux :")
print("-Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout).\n En choisissant son numéro, il y dépose la somme qu'il souhaite miser.\n-La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros pairs sont de couleur noire, les numéros impairs sont de couleur rouge. Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête, relève le numéro de la case dans laquelle la bille s'est arrêtée. Dans notre programme, nous ne reprendrons pas tous ces détails « matériels » mais ces explications sont aussi à l'intention de ceux qui ont eu la chance d'éviter les salles de casino jusqu'ici. Le numéro sur lequel s'est arrêtée la bille est, naturellement, le numéro gagnant.\n-Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée.\n-Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. Si ce n'est pas le cas, le joueur perd sa mise.")
while ContinueLaPartie==True:
  argent=input("-veuillez donner la somme que vous avez : ")
  try:
    argent=int(argent)
  except:
    print("Erreur! Veuillez entrer un nombre entier")
    continue
  else:
    NbrMise=-1
    while NbrMise<0 or NbrMise>49 :
      NbrMise=input("Veuillez tapez le nombre que vous voulez misez entre (0 et 49)  :")
      try:
        NbrMise=int(NbrMise)
      except:
        print("Erreur!")
      else:
        if NbrMise<=0:
            print("Erreur!ce nombre est null ou negatif ,\n vous devez saisir un nombre strictement  positif:")
        if NbrMise>49:
            print("Erreur!ce nombre est superieur à 49 ,\n vous devez saisir un nombre inferieur ou egale à 49 :")
  mise=0
  while mise<0 or mise>argent:
    mise=input("tapez le montant de votre mise :")
    try:
      mise=int(mise)
    except:
      print("Erreur ,\n saisie un nombre s'il vous plait :")
    else:
      if mise==0:
          ContinueLaPartie=False
      if mise<=0:
        print("Erreur,\n la mise que vous tapez est nul ou negative vous devez saisir un nombre positive :")
      if mise>argent :
        print("Erreur,\n vous n'avez pas cette somme ")
  print("le nombre gangant est : {}".format(ng))
  if NbrMise%2==0:
         couleur="noir"
         print("la couleur est noir")
  else:
         couleur="rouge"
         print("la couleur est rouge ")
  #print("le nombre gangant est : {}".format(ng))
  if ng==NbrMise :
         argent=mise*3
         print("Felicitation ,\nvous avez obtenez {} $ ".format(argent))
  elif ng%2==NbrMise%2:
         argent=mise*(0.5)
         print("vous avez misez la bonne couleur ,\n vou avez obtenez {} $".format(argent))
  else:
         print("oups ,\n vous perdez tout votre argent  ")
  if argent==0:
      print("c'est la fin ")
      ContinueLaPartie=False
  print("1-voulez vous quittez le jeux")
  print("2-voulez vous continue")
  quitter=int(input("donner votre choix : "))
  quitter=int(quitter)
  if quitter==1:
        ContinueLaPartie=False
