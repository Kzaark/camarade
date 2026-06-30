# Contribuer à `camarade`

Merci de ton intérêt ! Voici comment contribuer.

---

## Ajouter une figure historique

1. Crée un fichier JSON dans `data/auteurs/` :
```bash
nano data/auteurs/nouveau-camarade.json
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

3. Vérifie que le JSON est valide :
```bash
python3 -m json.tool data/auteurs/nouveau-camarade.json > /dev/null && echo "JSON valide"
```

---

## Ajouter un mouvement

1. Crée un fichier JSON dans `data/mouvements/` :
```bash
nano data/mouvements/nouveau-mouvement.json
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

---

## Critères éditoriaux

Les figures et mouvements acceptés concernent :
- Le marxisme, le léninisme, le trotskisme, la gauche communiste
- L'anarchisme sous toutes ses formes
- Le situationnisme, le panafricanisme, les luttes de décolonisation
- Les militants des droits civiques, le féminisme socialiste et anarchiste

Les figures et mouvements **refusés** :
- Tout ce qui concerne des régimes autoritaires se réclamant faussement du marxisme (stalinisme, maoïsme, régimes de type Kim, etc.)
- Les mouvements d'extrême droite ou nationalistes réactionnaires

---

## Faire une Pull Request

1. Fork le dépôt
2. Crée une branche :
```bash
git checkout -b ajout/nouvelle-figure
```
3. Fais tes modifications
4. Vérifie le JSON modifié
5. Commit :
```bash
git add .
git commit -m "data: ajout de [nom]"
```
6. Push et ouvre une Pull Request sur GitHub

---

## Signaler un problème ou suggérer une figure

Ouvre une [issue](https://github.com/Kzaark/camarade/issues).
