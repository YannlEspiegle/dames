# Jeu de dames

Ce jeu de dames a été créé pour le projet de programmation orientée
objet de NSI. Elle respecte les règles contenue sur [cette page](http://www.ffjd.fr/Web/index.php?page=reglesdujeu).
Seul la règle n.11 n'a pas été implémentée car trop compliquée à coder.

Tous les graphismes, que ce soit les pièces ou le message de fin ont été réalisés avec paint.

# Installation
Pour installer les dépendances, il suffit d'exécuter la commande suivante

``` sh
pip install -r requirements.txt
```
Puis pour exéctuer le programme, il faut lancer la commande

``` sh
python main.py
```

# Contrôles
- Pour déplacer une pièce, on clique sur la pièce à sélectionner puis on clique sur la case d'arrivée (après une rafle, 
  la pièce est déjà sélectionnée)
- Pour abandonner, il faut appuyer sur _CTRL+A_
- Si vous décidez de terminer la partie avec une égalité, appuyez sur _CTRL+E_

# Implémentation

## Classe Game

La classe `Game` sert à gérer tout ce qui se passe par rapport à la partie en général :

- Elle vérifie quand la partie est finie
- Lorsqu'on clique sur le tableau, c'est cette classe qui décide de quoi faire avec `on_click(pos)`
- Elle dessine les éléments sur l'écran avec `draw()`

## Classe Board

La classe `Board` gère les pièces en général notamment avec l'attribut `plateau` dont les codes utilisés sont expliqués plus bas.

- Il vérifie la légalité des coups avec la méthode `deplacer()` tout en vérifiant la promotion de la pièce à déplacer.
  Cette méthode anticipe aussi la gestion de la rafle en renvoyant un deuxième booléen `prise`.
- Il peut sélectionner une pièce pour ensuite la déplacer avec la méthode `select()` et la désélectionner avec `deselect()`
- Il renvoie les pièces qui peuvent prendre avec `pieces_pouvant_prendre(couleur)`, cette méthode sert à la classe Game car ont ne peut que jouer les pièces pouvant prendre.
- La classe peut renvoyer diverses informations sur les pièces avec `get_color(pos)` et `piece_from(pos)`.

### Codes Pièces
| code | pièce correspondante |
|------|----------------------|
| 0    | case vide            |
| 1    | pion blanc           |
| 2    | pion noir            |
| 10   | dame blanche         |
| 20   | dame noire           |

## Classe Piece

La classe `Piece` gère les actions qui se passent sur une pièce en particulier. 

- La méthode `coups_possibles()` renvoie les coups possibles de la pièce, si elle peut prendre, elle renvoie les cases d'arrivée de ces prises
- La méthode `prises_possibles()` renvoie la case d'arrivée de la prise puis la case de l'adversaire à supprimer
- La méthode `deplacer(arrivee)` déplace la case sans se souvier de l'arrivée ou de la légalité du coup
- La méthode `promotion()` transforme la pièce en dame
- La méthode `diagonale(x, y, direction, l)` renvoie la diagonale par rapport à `(x, y)` dans la direction `direction` et de longueur `l`.
