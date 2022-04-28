"""Module d'API du jeu Gobblet

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""

import requests

URL = "https://pax.ulaval.ca/gobblet/api/"


def lister_parties(idul, secret):
    """Lister les parties

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        list: Liste des parties reçues du serveur,
             après avoir décodé le json de sa réponse.
    """

    rep = requests.get(URL + 'parties', auth=(idul, secret))
    dictionnaire_rep = rep.json()

    if rep.status_code == 401:
        raise PermissionError(dictionnaire_rep)

    if rep.status_code == 406:
        raise RuntimeError(dictionnaire_rep)

    if rep.status_code not in (200, 401, 406):
        raise ConnectionError
    return dictionnaire_rep['parties']


def débuter_partie(idul, secret):
    """Débuter une partie

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie,
            de l'état du plateau de jeu et de la liste des joueurs,
            après avoir décodé le JSON de sa réponse.
    """

    partie_debutee = requests.post(URL + 'partie', auth=(idul, secret))
    dico_part_debutee = partie_debutee.json()
    if partie_debutee.status_code == 401:
        raise PermissionError(dico_part_debutee['message'])
    if partie_debutee.status_code == 406:
        raise RuntimeError(dico_part_debutee['message'])
    if partie_debutee.status_code not in (200, 401, 406):
        raise ConnectionError
    if partie_debutee.status_code == 200:
        return dico_part_debutee['id'], dico_part_debutee['plateau'], dico_part_debutee['joueurs']
    return None


def récupérer_partie(id_partie, idul, secret):
    """Récupérer une partie

    Args:
        id_partie (str): identifiant de la partie à récupérer
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie,
            de l'état du plateau de jeu et de la liste des joueurs,
            après avoir décodé le JSON de sa réponse.
    """

    rep = requests.get(URL + 'partie' + '/' + id_partie, auth=(idul, secret))
    dict_rep = rep.json()

    if rep.status_code == 401:
        raise PermissionError(dict_rep['message'])
    if rep.status_code == 406:
        raise RuntimeError(dict_rep['message'])
    if rep.status_code not in (200, 401, 406):
        raise ConnectionError
    # doit retourner un tuple qui contient les infos du dictionnaire json decodé
    if rep.status_code == 200:
        return dict_rep['id'], dict_rep['plateau'], dict_rep['joueurs'], dict_rep['gagnant']
    return None


def jouer_coup(id_partie, origine, dest, idul, secret):
    """Jouer un coup

    Args:
        id_partie (str): identifiant de la partie
        origine (int ou list): l'origine est soit un entier représentant
                               le numéro de la pile du joueur ou une liste de 2 entier [x, y]
                               représentant le Gobblet sur le plateau.
        dest (list): la destination estune liste de 2 entier [x, y]
                            représentant le Gobblet sur le plateau
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie,
            de l'état du plateau de jeu et de la liste des joueurs,
            après avoir décodé le JSON de sa réponse.
    """
    nouveau_coup = requests.put(
        URL + 'jouer',
        auth=(idul, secret),
        json={
            'id': id_partie,
            'destination': dest,
            'origine': origine,
        }
    )
    dico_nouveau_coup = nouveau_coup.json()
    if nouveau_coup.status_code == 401:
        raise PermissionError(dico_nouveau_coup['message'])
    if nouveau_coup.status_code == 406:
        raise RuntimeError(dico_nouveau_coup['message'])
    if nouveau_coup.status_code not in (200, 401, 406):
        raise ConnectionError
    if dico_nouveau_coup['gagnant'] is not None:
        raise StopIteration('le nom du gagnant est :', dico_nouveau_coup['gagnant'])
    return dico_nouveau_coup['id'], dico_nouveau_coup['plateau'], dico_nouveau_coup['joueurs']
