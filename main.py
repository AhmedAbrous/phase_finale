# -*- coding: utf-8 -*-
"""Jeu Gobblet

Ce programme permet de joueur au jeu Gobblet.
"""
import joueur
from api import débuter_partie, lister_parties, jouer_coup
from gobblet import (
    formater_jeu,
    formater_les_parties,
    interpréteur_de_commande,
)
from plateau import Plateau

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = "8a0ad6ae-beb8-4227-9b7e-2b674506ac31"


if __name__ == "__main__":
    args = interpréteur_de_commande()
    if args.lister:
        parties = lister_parties(args.IDUL, SECRET)
    else:
        id_partie, plateau, joueurs = débuter_partie(args.IDUL, SECRET)

        while True:
            # Implémentez votre boucle de jeu
            # définir les objets joueurs à partir de la base de données:
            joueur_1 = joueur.Joueur(joueurs[0]['nom'], 1, joueurs[0]['piles'])
            joueur_2 = joueur.Joueur(joueurs[1]['nom'], 2, joueurs[1]['piles'])
            joueurs_list = [joueur_1, joueur_2]

            # objet plateau à utiliser:
            plateau_obj = Plateau(plateau)

            print(formater_jeu(plateau_obj, joueurs_list))

            # Demander au joueur de choisir son prochain coup
            origine, dest = joueur_1.récupérer_le_coup(plateau_obj)

            # Envoyez le coup au serveur
            id_partie, plateau, joueurs = jouer_coup(id_partie, origine, dest, args.IDUL, SECRET)
