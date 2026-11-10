# Animal Merge

Jeu de fusion en Python : on lâche des animaux dans une caisse, deux animaux
identiques qui se touchent fusionnent en un animal plus gros. La partie est
perdue quand la pile dépasse la ligne rouge.

Développé avec **pygame-ce** (affichage, clavier, souris) et **pymunk** (moteur
physique 2D : gravité, collisions, rotation des animaux).

## Installation


Prérequis : Python 3.10 ou plus récent (développé avec Python 3.15).

```bash
git clone <url-du-depot>
cd jeux-animaux
python -m venv .venv
```

Activer l'environnement virtuel :

- Windows : `.venv\Scripts\activate`
- macOS / Linux : `source .venv/bin/activate`

Puis installer les dépendances :

```bash
pip install -r requirements.txt
```

> `pygame-ce` remplace `pygame` : si `pygame` est déjà installé dans
> l'environnement, le désinstaller d'abord (`pip uninstall pygame`), les deux
> ne peuvent pas cohabiter.

## Lancer le jeu

Depuis le dossier `jeux-animaux/` :

```bash
python main.py
```

## Comment jouer

1. Dans le menu, taper un pseudo (obligatoire), puis **Entrée** ou clic sur **PLAY**.
2. Viser avec la **souris** : l'animal en attente suit le curseur au-dessus de la caisse.
3. **Espace** pour lâcher l'animal (une demi-seconde minimum entre deux lâchers).
4. Deux animaux identiques qui se touchent fusionnent en l'animal suivant.
5. Si un animal reste au-dessus de la **ligne rouge** pendant 2 secondes, la partie est perdue.
6. Sur l'écran de fin, **Espace** pour revenir au menu.

### Les animaux

Seuls les trois premiers apparaissent en jeu (souris 60 %, hamster 30 %,
renard 10 %) ; les autres s'obtiennent uniquement par fusion.

| Niveau | Animal  | Points de la fusion |
|--------|---------|---------------------|
| 1      | Souris  | 1                   |
| 2      | Hamster | 3                   |
| 3      | Renard  | 15                  |
| 4      | Chien   | 21                  |
| 5      | Mouton  | 28                  |
| 6      | Vache   | 36                  |
| 7      | Dragon  | 70                  |

Deux dragons qui fusionnent disparaissent en rapportant leurs points :
c'est la seule façon de faire de la place sans perdre.

## Scores

Le meilleur score de chaque pseudo est sauvegardé dans
`animal_merge/scores.json`, créé à la première partie terminée. Un pseudo
déjà connu ne garde que son meilleur score. Le record du joueur est rechargé
au lancement de la partie et affiché à côté du score en cours.

Ce fichier est ignoré par git : chaque installation a ses propres scores.

## Organisation du code

```
jeux-animaux/
├── main.py              point d'entrée
├── requirements.txt     dépendances
└── animal_merge/
    ├── app.py           fenêtre, boucle principale, passage d'une scène à l'autre
    ├── menu.py          scène d'accueil : saisie du pseudo, bouton PLAY
    ├── game.py          scène de jeu : physique, lâcher, détection de défaite
    ├── game_over.py     scène de fin : enregistrement du score
    ├── animal.py        classe Animal et les 7 animaux (taille, points, sprite)
    ├── merge.py         détection des collisions et fusions
    ├── container.py     la caisse : murs physiques et affichage
    ├── ui.py            affichage du score pendant la partie
    ├── scores.py        lecture et écriture de scores.json
    ├── config.py        constantes du jeu (fenêtre, physique, règles)
    └── assets/          images
```

Chaque scène (`Menu`, `Game`, `GameOver`) expose les mêmes méthodes
`handle_event`, `update` et `draw`. `App` appelle celles de la scène courante
sans savoir laquelle c'est, et change de scène quand celle-ci renseigne
`next_scene`. Les données qui doivent passer d'une scène à l'autre (pseudo,
score, record) circulent dans un dictionnaire `session` partagé.

## Réglages

Les valeurs d'équilibrage sont regroupées dans `animal_merge/config.py` :
délai avant défaite (`LOSE_DELAY`), délai entre deux lâchers
(`DROP_COOLDOWN`), gravité, taille et position de la caisse, taille de la
fenêtre.

## Crédits

Sprites, fonds et éléments d'interface générés avec des outils d'IA
(PixelLab, Gemini), puis retouchés et intégrés à la main.
