# `camarade`

Affiche des fiches de figures révolutionnaires et de mouvements politiques dans le terminal — marxisme, anarchisme, décolonisation et plus.

![Langue](https://img.shields.io/badge/Langue-Français-blue.svg)
![Licence](https://img.shields.io/badge/licence-GPL--3.0-red?style=flat-square)
![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey?style=flat-square&logo=linux)
![Terminal](https://img.shields.io/badge/terminal-bash%20%7C%20zsh%20%7C%20fish-black?style=flat-square)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)

---

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple de sortie](#exemple-de-sortie)
- [Mise à jour](#mise-à-jour)
- [Personnalisation](#personnalisation)
- [Désinstallation](#désinstallation)
- [Infos diverses](#infos-diverses)
- [Licence](#licence)

---

## Prérequis

- Python 3.x
- Git

---

## Installation

```bash
git clone https://github.com/Kzaark/camarade.git
cd camarade/
chmod +x install.sh
sudo ./install.sh
```

---

## Utilisation

```bash
camarade                      → Fiche aléatoire (auteur ou mouvement)
camarade <nom>                → Cherche une figure ou un mouvement précis
camarade --list               → Liste tous les auteurs et mouvements
camarade --search <mot>       → Recherche dans toutes les fiches
camarade --no-color           → Désactive la colorisation
camarade --update             → Met à jour camarade
camarade --version            → Affiche la version installée
camarade --help               → Affiche l'aide
```

---

## Exemple de sortie

```
$ camarade luxemburg

Rosa Luxemburg
1871 — 1919
marxisme, spartakisme, internationalisme, anti-guerre

Rosa Luxemburg est l'une des figures les plus brillantes et les plus
attachantes du marxisme révolutionnaire...

Œuvres majeures :
  • Réforme sociale ou révolution ? (1899)
  • L'Accumulation du capital (1913)

Positions :
  Critique du révisionnisme de Bernstein...

« La liberté, c'est toujours la liberté de celui qui pense autrement. »
```

---

## Mise à jour

```bash
camarade --update
```

---

## Personnalisation

### Ajouter une figure historique

1. Crée un fichier JSON dans `data/auteurs/` :
```bash
nano ~/camarade/data/auteurs/nouveau-camarade.json
```

2. Respecte ce format :
```json
{
  "id": "nouveau-camarade",
  "nom": "Nom Complet",
  "dates": "1850 — 1920",
  "courant": ["courant1", "courant2"],
  "description": "...",
  "oeuvres": ["Œuvre 1 (année)", "Œuvre 2 (année)"],
  "positions": "...",
  "citation": "..."
}
```

### Ajouter un mouvement

1. Crée un fichier JSON dans `data/mouvements/` :
```bash
nano ~/camarade/data/mouvements/nouveau-mouvement.json
```

2. Respecte ce format :
```json
{
  "id": "nouveau-mouvement",
  "nom": "Nom du mouvement",
  "période": "Années 1900 — aujourd'hui",
  "description": "...",
  "figures_majeures": ["Figure 1", "Figure 2", "Figure 3"],
  "oeuvres_majeures": ["Œuvre 1", "Œuvre 2"],
  "cas_concrets": ["Cas 1", "Cas 2"]
}
```

3. Vérifie que le JSON est valide :
```bash
python3 -m json.tool ~/camarade/data/auteurs/nouveau-camarade.json > /dev/null && echo "JSON valide"
```

---

## Désinstallation

```bash
sudo ./uninstall.sh
```

---

## Infos diverses

- 44 figures historiques et 25 mouvements politiques
- Couvre le marxisme, le léninisme, le trotskisme, la gauche communiste, l'anarchisme sous toutes ses formes, le situationnisme, le panafricanisme et les luttes de décolonisation
- Refuse toute référence aux régimes autoritaires se réclamant faussement du marxisme (stalinisme, maoïsme, etc.)

---

## Licence
[GNU GPL-3.0](https://github.com/Kzaark/camarade/blob/main/LICENCE)
