#!/usr/bin/env python3
# camarade — Fiches de figures révolutionnaires dans le terminal
# Copyright (C) 2026 Kzaark
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import os
import random
import subprocess
import sys

# Version
VERSION = "1.0.0"

# Chemins
DATA_DIR        = "/usr/local/share/camarade/data"
AUTEURS_DIR     = os.path.join(DATA_DIR, "auteurs")
MOUVEMENTS_DIR   = os.path.join(DATA_DIR, "mouvements")

# Couleurs ANSI
class Couleurs:
    ROUGE    = "\033[91m"
    JAUNE    = "\033[93m"
    VERT     = "\033[92m"
    GRIS     = "\033[90m"
    ITALIQUE = "\033[3m"
    BOLD     = "\033[1m"
    RESET    = "\033[0m"

# ─────────────────────────────────────────
# Fiches
# ─────────────────────────────────────────

def lire_historique(fichier: str) -> dict:
    chemin = os.path.join(AUTEURS_DIR, fichier)
    if not os.path.exists(chemin):
        return {}
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)

def lire_tous_historiques() -> list:
    """Lit tous les fichiers JSON des auteurs ET des mouvements."""
    fiches = []
    if os.path.exists(AUTEURS_DIR):
        for f in os.listdir(AUTEURS_DIR):
            if f.endswith(".json"):
                fiche = lire_historique(f)
                if fiche:
                    fiche["type"] = "auteur"
                    fiches.append(fiche)
    if os.path.exists(MOUVEMENTS_DIR):
        for f in os.listdir(MOUVEMENTS_DIR):
            if f.endswith(".json"):
                fiche = lire_mouvement(f)
                if fiche:
                    fiche["type"] = "mouvement"
                    fiches.append(fiche)
    return fiches

def lire_mouvement(fichier: str) -> dict:
    """Lit un fichier JSON de mouvement."""
    chemin = os.path.join(MOUVEMENTS_DIR, fichier)
    if not os.path.exists(chemin):
        return {}
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)

def lire_tous_mouvements() -> list:
    """Lit tous les fichiers JSON des mouvements."""
    if not os.path.exists(MOUVEMENTS_DIR):
        return []
    fiches = []
    for f in os.listdir(MOUVEMENTS_DIR):
        if f.endswith(".json"):
            fiche = lire_mouvement(f)
            if fiche:
                fiches.append(fiche)
    return fiches

def afficher_historique(fiche: dict):
    """Affiche une fiche (auteur OU mouvement)."""
    if fiche.get("type") == "auteur":
        nom       = fiche.get("nom", "?")
        dates     = fiche.get("dates", "?")
        courant   = fiche.get("courant", [])
        desc      = fiche.get("description", "")
        oeuvres   = fiche.get("oeuvres", [])
        positions = fiche.get("positions", "")
        citation  = fiche.get("citation", "")

        print(f"\n{Couleurs.BOLD}{Couleurs.ROUGE}{nom}{Couleurs.RESET}")
        print(f"{Couleurs.JAUNE}{dates}{Couleurs.RESET}")

        if courant:
            print(f"{Couleurs.GRIS}{Couleurs.ITALIQUE}{', '.join(courant)}{Couleurs.RESET}")

        print(f"\n{desc}")

        if oeuvres:
            print(f"\n{Couleurs.BOLD}Œuvres majeures :{Couleurs.RESET}")
            for o in oeuvres:
                print(f"  • {o}")

        if positions:
            print(f"\n{Couleurs.BOLD}Positions :{Couleurs.RESET}")
            print(f"  {positions}")

        if citation:
            print(f"\n{Couleurs.JAUNE}{Couleurs.ITALIQUE}« {citation} »{Couleurs.RESET}")

    elif fiche.get("type") == "mouvement":
        nom       = fiche.get("nom", "?")
        periode   = fiche.get("période", "?")
        desc      = fiche.get("description", "")
        figures   = fiche.get("figures_majeures", [])
        oeuvres   = fiche.get("oeuvres_majeures", [])
        cas       = fiche.get("cas_concrets", [])

        print(f"\n{Couleurs.BOLD}{Couleurs.VERT}{nom}{Couleurs.RESET}")
        print(f"{Couleurs.JAUNE}{periode}{Couleurs.RESET}")

        if figures:
            print(f"\n{Couleurs.BOLD}Figures majeures :{Couleurs.RESET}")
            for fig in figures:
                print(f"  • {fig}")

        print(f"\n{desc}")

        if oeuvres:
            print(f"\n{Couleurs.BOLD}Œuvres majeures :{Couleurs.RESET}")
            for o in oeuvres:
                print(f"  • {o}")

        if cas:
            print(f"\n{Couleurs.BOLD}Cas concrets :{Couleurs.RESET}")
            for c in cas:
                print(f"  • {c}")

    print()

# ─────────────────────────────────────────
# Commandes
# ─────────────────────────────────────────

def cmd_aleatoire():
    fiches = lire_tous_historiques()
    if not fiches:
        print("Aucune fiche trouvée.")
        return
    afficher_historique(random.choice(fiches))

def cmd_chercher(nom: str):
    fiches = lire_tous_historiques()
    nom_lower = nom.lower()
    resultats = [
        f for f in fiches
        if nom_lower in f.get("nom", "").lower()
        or nom_lower in f.get("id", "").lower()
    ]
    if not resultats:
        print(f"Aucune fiche trouvée pour '{nom}'.")
        return
    for fiche in resultats:
        afficher_historique(fiche)
        if len(resultats) > 1:
            print("─" * 40)

def cmd_list():
    fiches = lire_tous_historiques()
    if not fiches:
        print("Aucune fiche historique trouvée.")
        return

    auteurs = [f for f in fiches if f.get("type") == "auteur"]
    mouvements = [f for f in fiches if f.get("type") == "mouvement"]

    print(f"\n{Couleurs.BOLD}{Couleurs.ROUGE}Figures historiques disponibles :{Couleurs.RESET}\n")
    for f in sorted(auteurs, key=lambda x: x.get("nom", "")):
        courant = f.get("courant", [])
        print(f"  {Couleurs.ROUGE}{f.get('nom', '?')}{Couleurs.RESET} — {Couleurs.GRIS}{', '.join(courant)}{Couleurs.RESET}")

    print(f"\n{Couleurs.BOLD}{Couleurs.VERT}Mouvements disponibles :{Couleurs.RESET}\n")
    for f in sorted(mouvements, key=lambda x: x.get("nom", "")):
        print(f"  {Couleurs.VERT}{f.get('nom', '?')}{Couleurs.RESET} — {Couleurs.GRIS}{f.get('période', '?')}{Couleurs.RESET}")

    print()

def cmd_search(mot: str):
    fiches = lire_tous_historiques()
    mot_lower = mot.lower()
    resultats = [
        f for f in fiches
        if mot_lower in f.get("nom", "").lower()
        or mot_lower in f.get("description", "").lower()
        or mot_lower in f.get("positions", "").lower()
        or mot_lower in f.get("période", "").lower()
        or mot_lower in " ".join(f.get("courant", [])).lower()
        or mot_lower in " ".join(f.get("figures_majeures", [])).lower()
    ]
    if not resultats:
        print(f"Aucune fiche trouvée pour '{mot}'.")
        return
    print(f"\n{len(resultats)} résultat(s) pour '{mot}' :\n")
    for fiche in resultats:
        afficher_historique(fiche)
        if len(resultats) > 1:
            print("─" * 40)

def cmd_mettre_a_jour():
    print("Mise à jour de camarade...")
    result = subprocess.run(
        ["git", "-C", "/usr/local/share/camarade", "pull"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print("✓ Mise à jour réussie !")
        print(result.stdout)
    else:
        print("✗ Erreur lors de la mise à jour :")
        print(result.stderr)

def cmd_version():
    print(f"camarade v{VERSION}")

def desactiver_couleurs():
    Couleurs.ROUGE    = ""
    Couleurs.JAUNE    = ""
    Couleurs.VERT     = ""
    Couleurs.GRIS     = ""
    Couleurs.ITALIQUE = ""
    Couleurs.BOLD     = ""
    Couleurs.RESET    = ""

def cmd_aide():
    print("""
camarade — Fiches de figures révolutionnaires et mouvements dans ton terminal

Usage :
  camarade                      Figure ou mouvement aléatoire
  camarade <nom>                Cherche une figure ou un mouvement précis
  camarade --list               Liste toutes les figures et mouvements
  camarade --search <mot>       Recherche dans les fiches (auteurs ET mouvements)
  camarade --no-color           Désactive la colorisation
  camarade --update             Met à jour camarade
  camarade --version            Affiche la version installée
  camarade --help               Affiche ce message

Exemples :
  camarade
  camarade luxemburg
  camarade anarchisme
  camarade --search féminisme
  camarade --list
""")

# ─────────────────────────────────────────
# Point d'entrée
# ─────────────────────────────────────────

def parse_args():
    args = sys.argv[1:]

    if "--no-color" in args:
        desactiver_couleurs()
        args = [a for a in args if a != "--no-color"]

    if not args:
        cmd_aleatoire()

    elif args[0] in ("--help", "-h"):
        cmd_aide()

    elif args[0] in ("--version", "-v"):
        cmd_version()

    elif args[0] == "--update":
        cmd_mettre_a_jour()

    elif args[0] == "--list":
        cmd_list()

    elif args[0] == "--search":
        if len(args) < 2:
            print("Usage : camarade --search <mot>")
        else:
            cmd_search(args[1])

    elif args[0].startswith("--"):
        print(f"Option inconnue : '{args[0]}'. Lance 'camarade --help'.")

    else:
        cmd_chercher(args[0])

if __name__ == "__main__":
    parse_args()
