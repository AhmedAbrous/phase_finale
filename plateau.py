"""Module Joueur

Functions:
    * Plateau - Classe représentant un Plateau.
"""

from gobblet import Gobblet, GobbletError


class Plateau:
    """
    Plateau
    """

    def __init__(self, plateau):
        """Constructeur de Plateau

        Vous ne devez PAS modifier cette méthode

        Args:
            plateau (list): Plateau à construire tel que représenté dans l'énoncé
        """
        self.plateau = self.valider_plateau(plateau)

    def valider_plateau(self, plateau):
        """Validateur de Plateau

        Args:
            plateau (list): Plateau tel que représenté dans l'énoncé

        Returns:
            list: Plateau composé de liste de Gobblets ou None pour l'absence de Gobblet

        Raises:
            GobbletError: Le plateau doit être une liste
            GobbletError: Le plateau ne possède pas le bon nombre de ligne
            GobbletError: Le plateau ne possède pas le bon nombre de colonne dans les lignes
            GobbletError: Les Gobblets doivent être des listes de paires ou une liste vide
        """
        # initialiser un plateau pour le return
        plateau_list = []
        if not isinstance(plateau, list):
            raise GobbletError('Le plateau doit être une liste')
        if len(plateau) != 4:
            raise GobbletError('Le plateau ne possède pas le bon nombre de ligne')
        for ligne in plateau:
            # initialiser une liste pour la ligne
            ligne_list = []
            if len(ligne) != 4:
                raise GobbletError("Le plateau ne possède pas le bon nombre de colonnes dans les lignes")
            for pile in ligne:
                if pile and len(pile) != 2:
                    raise GobbletError("Les Gobblets doivent être des listes de paires ou une liste vide")
                ligne_list.append(Gobblet(pile[1], pile[0]) if pile else None)
            plateau_list.append(ligne_list)
        return plateau_list

    def __str__(self):
        """Formater un plateau

        Returns:
            str: Représentation du plateau avec ses Gobblet
        """
        # repr_plateau est la representation du plateau
        repr_plateau = ''
        for i, ligne in enumerate(self.plateau):
            repr_plateau += str(3 - i)
            for pile in ligne:
                repr_plateau += (str(pile) if pile else '   ') + '|'
            if i != 3:
                repr_plateau = repr_plateau[:-1] + ('\n ' + (('─' * 3) + '┼') * 4)[:-1] + '\n'
        repr_plateau = repr_plateau[:-1] + "\n  0   1   2   3 "
        return repr_plateau

    def retirer_gobblet(self, no_colonne, no_ligne):
        """Retirer un Gobblet du plateau

        Args:
            no_colonne (int): Numéro de la colonne
            no_ligne (int): Numéro de la ligne

        Returns:
            Gobblet: Gobblet retiré du plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le plateau ne possède pas de Gobblet pour la case demandée
        """
        # faire les vérifications:
        # le numero de ligne est normalisé pour que ca fit avec la représentation
        no_ligne_norm = 3 - no_ligne

        if not isinstance(no_ligne, int) or not isinstance(no_colonne, int):
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if no_ligne not in range(0, 4):
            raise GobbletError("Le numéro de la ligne doit être 0, 1, 2 ou 3")
        if no_colonne not in range(0, 4):
            raise GobbletError("Le numéro de la colonne doit être 0, 1, 2 ou 3")
        if self.plateau[no_ligne_norm][no_colonne] is None:
            raise GobbletError("Le plateau ne possède pas de Gobblet pour la case demandée")
        return self.plateau[no_ligne_norm][no_colonne]

    def placer_gobblet(self, no_colonne, no_ligne, gobblet):
        """Placer un Gobblet dans le plateau

        Args:
            no_colonne (int): Numéro de la colonne (0, 1, 2 ou 3)
            no_ligne (int): Numéro de la ligne (0, 1, 2 ou 3)
            gobblet (Gobblet): Gobblet à placer dans le plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le Gobblet ne peut pas être placé sur la case demandée
        """
        # faire les vérifications:
        # le numero de ligne est normalisé pour que ca fit avec la représentation
        no_ligne_norm = 3 - no_ligne

        if not isinstance(no_ligne, int) or not isinstance(no_colonne, int):
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if no_ligne not in range(0, 4):
            raise GobbletError("Le numéro de la ligne doit être 0, 1, 2 ou 3")
        if no_colonne not in range(0, 4):
            raise GobbletError("Le numéro de la colonne doit être 0, 1, 2 ou 3")
        if gobblet < self.plateau[no_ligne_norm][no_colonne]:
            raise GobbletError("Le Gobblet ne peut pas être placé sur la case demandée")
        self.plateau[no_ligne_norm][no_colonne] = gobblet

    def état_plateau(self):
        """Obtenir l'état du plateau

        Returns:
            list: Liste contenant l'état du plateau tel que représenté dans l'énoncé
        """
        # on définit une liste pour l'état du plateau

        liste_totale = []
        for element in self.plateau:
            list_plateau = []
            for gobblet in element:
                list_plateau.append([gobblet.no_joueur, gobblet.grosseur] if gobblet else [])
            liste_totale.append(list_plateau)
        return liste_totale
