"""Module Gobblet

Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobelets des joueurs.

Functions:
    * Gobblet - Classe représentant un Gobblet.
    * GobbletError - Classe gérant les exceptions GobbletError.
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
"""

from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}


class GobbletError(Exception):
    """ Raises:
            GobbletError: Le nom du joueur doit être une chaine de caractères non vide.
            GobbletError: Le numéro du joueur doit être 1 ou 2.
            GobbletError: Les piles de gobelets doivent être spécifiés sous la forme d'une liste.
            GobbletError: Le joueur doit possèder 3 piles.
            GobbletError: Une pile doit être une liste de deux entiers ou une liste vide.
        """
    '''Raises:
            GobbletError: Le numéro de la pile doit être un entier.
            GobbletError: Le numéro de la pile doit être 0, 1 ou 2.
            GobbletError: Le joueur ne possède pas de gobelet pour la pile demandée.'''
    '''Raises:
            GobbletError: Le numéro de la pile doit être un entier.
            GobbletError: Le numéro de la pile doit être 0, 1 ou 2.
            GobbletError: Le gobelet doit appartenir au joueur.
            GobbletError: Vous ne pouvez pas placer un gobelet à cet emplacement.'''
    '''Raises:
            GobbletError: L'origine doit être un entier ou une liste de 2 entiers.
            GobbletError: L'origine n'est pas une pile valide.
            GobbletError: L'origine n'est pas une case valide du plateau.
            GobbletError: L'origine ne possède pas de gobelet.
            GobbletError: Le gobelet d'origine n'appartient pas au joueur.
            GobbletError: La destination doit être une liste de 2 entiers.
            GobbletError: La destination n'est pas une case valide du plateau'''
    '''Raises:
            GobbletError: La grosseur doit être un entier.
            GobbletError: La grosseur doit être comprise entre 0 et 3.
            GobbletError: Le numéro du joueur doit être un entier.
            GobbletError: Le numéro du joueur doit être 1 ou 2.'''
    '''   Raises:
            GobbletError: Le plateau doit être une liste
            GobbletError: Le plateau ne possède pas le bon nombre de ligne
            GobbletError: Le plateau ne possède pas le bon nombre de colonne dans les lignes
            GobbletError: Les Gobblets doivent être des listes de paires ou une liste vide'''
    '''Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le plateau ne possède pas de Gobblet pour la case demandée'''
    '''Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le Gobblet ne peut pas être placé sur la case demandée'''
    pass


class Gobblet:
    """
    Gobblet
    """

    def __init__(self, grosseur: int, no_joueur: int):
        """Constructeur de gobelet.

        Ne PAS modifier cette méthode.

        Args:
            grosseur (int): Grosseur du Gobblet [0, 1, 2, 3].
            no_joueur (int): Numéro du joueur [1, 2].
        """
        self.grosseur, self.no_joueur = self.valider_gobblet(grosseur, no_joueur)

    def valider_gobblet(self, grosseur, no_joueur):
        """Validateur de gobelet.

        Args:
            grosseur (int): la grosseur du gobelet [0, 1, 2, 3].
            no_joueur (int): le numéro du joueur [1, 2].

        Returns:
            tuple[int, int]: un tuple contenant la grosseur et le numéro du joueur.

        Raises:
            GobbletError: La grosseur doit être un entier.
            GobbletError: La grosseur doit être comprise entre 0 et 3.
            GobbletError: Le numéro du joueur doit être un entier.
            GobbletError: Le numéro du joueur doit être 1 ou 2.
        """
        if not isinstance(grosseur, int):
            raise GobbletError("La grosseur doit être un entier.")
        if grosseur not in range(0, 4):
            raise GobbletError("La grosseur doit être comprise entre 0 et 3.")
        if not isinstance(no_joueur, int):
            raise GobbletError('Le numéro du joueur doit être un entier.')
        if no_joueur not in range(1, 3):
            raise GobbletError('Le numéro du joueur doit être 1 ou 2.')
        return grosseur, no_joueur

    def __str__(self):
        """Formater un gobelet.

        Returns:
            str: Représentation du gobelet pour le joueur.
        """

        return " " + GOBBLET_REPRÉSENTATION[self.no_joueur][self.grosseur] + " "

    def __eq__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si les deux gobelets sont de même taille.
        """
        # On vérifie si autre est de type Gobblet, sinon on retourne Faux
        # on vérifie aussi pour deux types Gobblets si les grosseurs sont égales, alors on retourne Vrai.

        if not isinstance(autre, Gobblet) or not isinstance(self, Gobblet):
            return False
        return self.grosseur == autre.grosseur

    def __gt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus gros que l'autre.
        """

        return not (self.__eq__(autre)) and not (self.__lt__(autre))

    def __lt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit que l'autre.
        """
        if not isinstance(self, Gobblet) or not isinstance(autre, Gobblet):
            return False
        return self.grosseur < autre.grosseur

    def __ne__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet n'est pas équivalent à l'autre.
        """

        return not (self.__eq__(autre))

    def __ge__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus grand ou égal à l'autre.
        """
        return not self.__lt__(autre)

    def __le__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit ou égal à l'autre.
        """
        return self.__lt__(autre) or self.__eq__(autre)

    def état_gobblet(self):
        """Obtenir l'état du gobelet.

        Returns:
            list: la paire d'entiers représentant l'état du gobelet (numéro du joueur et grosseur du gobelet).
        """
        if not isinstance(self, Gobblet):
            return None
        return [self.no_joueur, self.grosseur]


def interpréteur_de_commande():
    """Interpreteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut IDUL représentant l'idul du joueur
                   et l'attribut lister qui est un booléen True/False.
    """
    parser = ArgumentParser(description='Gobblet')

    parser.add_argument('IDUL', help='IDUL du joueur')

    parser.add_argument('-l', '--lister',
                        action="store_true",
                        dest='lister',
                        help="Lister les parties existantes",
                        )
    # parser.add_argument('-a', '--automatique',
    #                     action="store_true",
    #                     dest="automatique",
    #                     help="Activer le mode automatique")

    args = parser.parse_args()
    return args


def formater_jeu(plateau, joueurs):
    """Formater un jeu.

    Args:
        plateau (Plateau): le plateau de jeu.
        joueurs (list): la liste des deux Joueurs.

    Returns:
        str: Représentation du jeu.
    """
    # max de longueur des caracteres des joueurs

    longeur_carac = max(len(joueurs[0].nom), len(joueurs[1].nom))
    # long est la longueur maximale de la ligne a afficher
    long = 13 + longeur_carac

    representation_jeu = '0   1   2 '.rjust(long) + '\n'
    for i in range(2):
        representation_jeu += str(joueurs[i]).rjust(long) + '\n'
    representation_jeu = representation_jeu + '\n' + str(plateau)
    return representation_jeu


def formater_les_parties(parties):
    """Formater une liste de parties.

    L'ordre doit être exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): une liste des parties.

    Returns:
        str: Représentation des parties.
    """
    # repr_jeu est la representation du jeu
    repr_jeu = ''

    for i, dico_parties in enumerate(parties):
        repr_jeu += f'{i + 1 :^2}: {dico_parties["date"]}' + ', '
        repr_jeu += f'{dico_parties["joueurs"][0]} vs {dico_parties["joueurs"][1]}'
        if dico_parties.get("gagnant") is None:
            repr_jeu += '\n'
        else:
            repr_jeu += f', {list(dico_parties.keys())[3]}: {list(dico_parties.values())[3]}' \
                        + '\n'
    return repr_jeu
