
# ================================================================
#  ORACLE MULTISYSTÈME – VERSION MONOLITHIQUE
#  BLOC 1 — Imports, Config, Thème, CSS global
# ================================================================

import streamlit as st
import random
import math
import json
from datetime import datetime
import textwrap

# ------------------------------------------------
# Page config
# ------------------------------------------------
st.set_page_config(
    page_title="Oracle MultiSystème",
    page_icon="🔮",
    layout="wide"
)

# ------------------------------------------------
# THEMES : Clair / Sombre
# ------------------------------------------------

st.sidebar.header("🎨 Thème général")

theme = st.sidebar.radio(
    "Sélection du thème",
    ["Sombre", "Clair"],
    index=0,
    horizontal=True
)

if theme == "Sombre":
    BG_COLOR = "#0f0f0f"
    CARD_BG = "rgba(20, 20, 20, 0.95)"
    TEXT_COLOR = "#ffffff"
    BORDER_COLOR = "rgba(255,255,255,0.22)"
else:
    BG_COLOR = "#f4f4f4"
    CARD_BG = "rgba(255,255,255,0.98)"
    TEXT_COLOR = "#000000"
    BORDER_COLOR = "rgba(0,0,0,0.25)"

# ------------------------------------------------
# CSS GLOBAL + CARTES FLIP 3D + Layout Pro
# ------------------------------------------------

st.markdown(
    f"""
<style>

html, body, [class*="stApp"] {{
    background-color: {BG_COLOR} !important;
    color: {TEXT_COLOR} !important;
}}

h1, h2, h3, h4, h5, h6, p, span, div {{
    color: {TEXT_COLOR};
}}

.block-container {{
    padding-top: 2rem;
}}

.flip-card {{
    background-color: transparent;
    width: 100%;
    perspective: 1100px;
    margin-bottom: 1.2rem;
}}

.flip-card-inner {{
    position: relative;
    width: 100%;
    min-height: 180px;
    transition: transform 0.65s;
    transform-style: preserve-3d;
}}

.flip-card:hover .flip-card-inner {{
    transform: rotateY(180deg);
}}

.flip-card:active .flip-card-inner {{
    transform: rotateY(180deg);
}}

.flip-card-front, .flip-card-back {{
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    background-color: {CARD_BG};
    border-radius: 14px;
    border: 1px solid {BORDER_COLOR};
    box-shadow: 0 6px 16px rgba(0,0,0,0.35);
    padding: 1.1rem;
    box-sizing: border-box;
}}

.flip-card-front h3,
.flip-card-back h3 {{
    margin-top: 0;
    margin-bottom: 0.6rem;
    font-size: 1.15rem;
}}

.flip-card-front p,
.flip-card-back p {{
    margin: 0.2rem 0;
    font-size: 0.95rem;
}}

.flip-card-back {{
    transform: rotateY(180deg);
}}

.oracle-pos {{
    font-size: 0.78rem;
    text-transform: uppercase;
    opacity: 0.65;
    margin-bottom: 0.35rem;
}}

.flip-hint {{
    font-size: 0.75rem;
    opacity: 0.55;
    margin-top: 0.4rem;
}}

</style>
""",
    unsafe_allow_html=True
)

# ------------------------------------------------
# INIT ÉTAT SESSION
# ------------------------------------------------
if "history" not in st.session_state:
    st.session_state["history"] = []

if "journal" not in st.session_state:
    st.session_state["journal"] = []

# ------------------------------------------------
# TITRE GLOBAL
# ------------------------------------------------
st.title("🔮 Oracle Multi-Système — Version Complète")

st.caption(
    "Oracle 48 · Pāli · Runes · I Ching classique · Totems animaux · "
    "Tirages avancés · Flip 3D · Thème clair/sombre · Historique · Galerie"
)
# bloc2.py — BLOC 2 (Jeux : Oracle, Pāli, Runes, I Ching, Totems)
# ---------------------------------------------------------------
# ⚠️ Ce fichier est un TEMPLATE.
# Le BLOC 2 complet est très volumineux (plusieurs centaines de lignes).
# Pour respecter les limites de génération, voici la structure à remplir :
#
# - CARDS (Oracle 48)
# - PALI_CARDS (32 entrées)
# - RUNES_LIST (24 runes complètes)
# - HEXAGRAMS (64 hexagrammes)
# - HEX_DICT (index par ID)
# - ANIMALS (Totems AmSud / AmNord / Asie)
#
# Tu peux me dire :
#   → "Donne-moi les 48 cartes Oracle"
#   → "Donne-moi les 32 cartes Pāli"
#   → "Donne-moi les 24 runes complètes"
#   → "Donne-moi les 64 hexagrammes"
#   → "Donne-moi les animaux totems"
# Et je remplirai ce fichier automatiquement.
#
# ---------------------------------------------------------------
# Exemple de structure (à compléter) :
# ---------------------------------------------------------------
# ================================================================
# 🔮 ORACLE 48 CARTES
# ================================================================

CARDS = [
    # Voie intérieure
    {"nom": "Éveil", "famille": "Voie intérieure", "message": "Quelque chose s’ouvre en toi.", "axe": "Clarté intérieure"},
    {"nom": "Intuition", "famille": "Voie intérieure", "message": "Écoute la petite voix.", "axe": "Guidance subtile"},
    {"nom": "Silence", "famille": "Voie intérieure", "message": "Le vrai message se trouve dans le calme.", "axe": "Repos mental"},
    {"nom": "Présence", "famille": "Voie intérieure", "message": "Reviens ici et maintenant.", "axe": "Ancrage"},
    {"nom": "Authenticité", "famille": "Voie intérieure", "message": "Sois vrai avec toi-même.", "axe": "Alignement intérieur"},
    {"nom": "Âme", "famille": "Voie intérieure", "message": "Une mémoire profonde se réveille.", "axe": "Contact intérieur"},
    {"nom": "Ombre", "famille": "Voie intérieure", "message": "Regarde ce que tu évitais.", "axe": "Introspection"},
    {"nom": "Guérison", "famille": "Voie intérieure", "message": "Tu te répares doucement.", "axe": "Libération émotionnelle"},
    {"nom": "Vision", "famille": "Voie intérieure", "message": "Tu perçois au-delà.", "axe": "Perspectives"},
    {"nom": "Cœur", "famille": "Voie intérieure", "message": "Ouvre-toi avec sincérité.", "axe": "Sensibilité"},
    {"nom": "Émotion", "famille": "Voie intérieure", "message": "Accueille ce que tu ressens.", "axe": "Acceptation"},
    {"nom": "Conscience", "famille": "Voie intérieure", "message": "Tu prends de la hauteur.", "axe": "Sagesse"},

    # Croissance
    {"nom": "Mutation", "famille": "Croissance", "message": "Tu changes de peau.", "axe": "Transformation profonde"},
    {"nom": "Renouveau", "famille": "Croissance", "message": "Un cycle se termine.", "axe": "Nouvelle énergie"},
    {"nom": "Renaissance", "famille": "Croissance", "message": "Tu retrouves ton souffle.", "axe": "Régénération"},
    {"nom": "Libération", "famille": "Croissance", "message": "Un poids tombe.", "axe": "Soulagement"},
    {"nom": "Passage", "famille": "Croissance", "message": "Une porte s’ouvre devant toi.", "axe": "Transition"},
    {"nom": "Clarté", "famille": "Croissance", "message": "La confusion se dissipe.", "axe": "Vision nette"},
    {"nom": "Dépassement", "famille": "Croissance", "message": "Tu franchis un seuil.", "axe": "Courage"},
    {"nom": "Flux", "famille": "Croissance", "message": "Laisse venir, laisse aller.", "axe": "Mouvement naturel"},
    {"nom": "Patience", "famille": "Croissance", "message": "Le temps agit pour toi.", "axe": "Maturation"},
    {"nom": "Éclosion", "famille": "Croissance", "message": "Ton potentiel se déploie.", "axe": "Manifestation"},
    {"nom": "Transformation", "famille": "Croissance", "message": "Tout se réorganise.", "axe": "Métamorphose"},
    {"nom": "Ascension", "famille": "Croissance", "message": "Tu montes d’un niveau.", "axe": "Élévation"},

    # Relations
    {"nom": "Miroir", "famille": "Relations", "message": "L’autre reflète une part de toi.", "axe": "Compréhension"},
    {"nom": "Rencontre", "famille": "Relations", "message": "Une présence arrive.", "axe": "Ouverture"},
    {"nom": "Partage", "famille": "Relations", "message": "Tu n’es pas seul(e).", "axe": "Connexion"},
    {"nom": "Compassion", "famille": "Relations", "message": "Adoucis ton regard.", "axe": "Empathie"},
    {"nom": "Mettā", "famille": "Relations", "message": "Rayonne sans attendre.", "axe": "Amour universel"},
    {"nom": "Joie", "famille": "Relations", "message": "La lumière revient.", "axe": "Enthousiasme"},
    {"nom": "Union", "famille": "Relations", "message": "Deux chemins se rejoignent.", "axe": "Harmonisation"},
    {"nom": "Loyauté", "famille": "Relations", "message": "Reste fidèle à l’essentiel.", "axe": "Solidité"},
    {"nom": "Tension", "famille": "Relations", "message": "Une friction demande douceur.", "axe": "Ajustement"},
    {"nom": "Pardon", "famille": "Relations", "message": "Libère-toi du passé.", "axe": "Guérison"},
    {"nom": "Distance", "famille": "Relations", "message": "Un espace est nécessaire.", "axe": "Protection"},
    {"nom": "Réconciliation", "famille": "Relations", "message": "L’harmonie revient.", "axe": "Paix"},

    # Guidance
    {"nom": "Destinée", "famille": "Guidance", "message": "Tu es à l’endroit juste.", "axe": "Alignement"},
    {"nom": "Protection", "famille": "Guidance", "message": "Tu es entouré(e).", "axe": "Force invisible"},
    {"nom": "Synchronie", "famille": "Guidance", "message": "Ce signe n’est pas un hasard.", "axe": "Messages"},
    {"nom": "Portail", "famille": "Guidance", "message": "Un changement approche.", "axe": "Opportunité"},
    {"nom": "Épreuve", "famille": "Guidance", "message": "Un défi te renforce.", "axe": "Croissance"},
    {"nom": "Courage", "famille": "Guidance", "message": "Affronte l’appel.", "axe": "Force intérieure"},
    {"nom": "Vérité", "famille": "Guidance", "message": "Ne fuis pas ce qui est.", "axe": "Lucidité"},
    {"nom": "Abondance", "famille": "Guidance", "message": "Le flux arrive.", "axe": "Expansion"},
    {"nom": "Choix", "famille": "Guidance", "message": "La décision t’appartient.", "axe": "Responsabilité"},
    {"nom": "Voyage", "famille": "Guidance", "message": "Va voir plus loin.", "axe": "Exploration"},
    {"nom": "Manifestation", "famille": "Guidance", "message": "Ce que tu portes prend forme.", "axe": "Concrétisation"},
    {"nom": "Unité", "famille": "Guidance", "message": "Tout est relié.", "axe": "Sagesse universelle"},
]

# ================================================================
# 📜 ORACLE PĀLI (36 mots essentiels)
# ================================================================

PALI_CARDS = [
    {"mot": "Sati", "sens": "Attention, présence consciente."},
    {"mot": "Metta", "sens": "Bienveillance illimitée."},
    {"mot": "Karuna", "sens": "Compassion en action."},
    {"mot": "Mudita", "sens": "Joie empathique."},
    {"mot": "Upekkha", "sens": "Équanimité."},
    {"mot": "Samadhi", "sens": "Stabilité méditative."},
    {"mot": "Paññā", "sens": "Sagesse profonde."},
    {"mot": "Viriya", "sens": "Énergie juste."},
    {"mot": "Dukkha", "sens": "Tension, devenir."},
    {"mot": "Anicca", "sens": "Impermanence."},
    {"mot": "Anatta", "sens": "Non-soi."},
    {"mot": "Citta", "sens": "Cœur-esprit."},
    {"mot": "Dhamma", "sens": "Loi naturelle."},
    {"mot": "Sīla", "sens": "Éthique."},
    {"mot": "Bhāvanā", "sens": "Cultivation mentale."},
    {"mot": "Kalyāna-mitta", "sens": "Ami spirituel."},
    {"mot": "Marana-sati", "sens": "Souvenir de la mort."},
    {"mot": "Sukha", "sens": "Bonheur calme."},
    {"mot": "Khanti", "sens": "Patience."},
    {"mot": "Sacca", "sens": "Vérité."},
    {"mot": "Mettābhāvanā", "sens": "Cultiver la bienveillance."},
    {"mot": "Passaddhi", "sens": "Apaisement."},
    {"mot": "Vitakka", "sens": "Pensée dirigée."},
    {"mot": "Vicāra", "sens": "Réflexion."},
    {"mot": "Sankhāra", "sens": "Conditionnements."},
    {"mot": "Jhana", "sens": "Absorption méditative."},
    {"mot": "Tathāgata", "sens": "Celui qui est allé."},
    {"mot": "Bodhi", "sens": "Éveil ultime."},
    {"mot": "Nibbāna", "sens": "Extinction de la soif."},
]

# ================================================================
# ᚱ RUNES NORDIQUES — Elder Futhark
# ================================================================

RUNES_LIST = [
    {"rune": "ᚠ", "nom": "Fehu", "sens": "Abondance, circulation des ressources."},
    {"rune": "ᚢ", "nom": "Uruz", "sens": "Force vitale, puissance brute."},
    {"rune": "ᚦ", "nom": "Thurisaz", "sens": "Protection, séparation nécessaire."},
    {"rune": "ᚨ", "nom": "Ansuz", "sens": "Communication, inspiration divine."},
    {"rune": "ᚱ", "nom": "Raidho", "sens": "Voyage, chemin juste."},
    {"rune": "ᚲ", "nom": "Kenaz", "sens": "Feu intérieur, illumination."},
    {"rune": "ᚷ", "nom": "Gebo", "sens": "Échange, réciprocité."},
    {"rune": "ᚹ", "nom": "Wunjo", "sens": "Harmonie, joie."},
    {"rune": "ᚺ", "nom": "Hagalaz", "sens": "Rupture, chaos créateur."},
    {"rune": "ᚾ", "nom": "Nauthiz", "sens": "Besoins, tension, discipline."},
    {"rune": "ᛁ", "nom": "Isa", "sens": "Gel, pause, immobilité."},
    {"rune": "ᛃ", "nom": "Jera", "sens": "Cycle, récolte, patience."},
    {"rune": "ᛇ", "nom": "Eihwaz", "sens": "Résilience, colonne intérieure."},
    {"rune": "ᛈ", "nom": "Perthro", "sens": "Mystère, destin caché."},
    {"rune": "ᛉ", "nom": "Algiz", "sens": "Protection sacrée."},
    {"rune": "ᛋ", "nom": "Sowilo", "sens": "Lumière, victoire, clarté."},
    {"rune": "ᛏ", "nom": "Tiwaz", "sens": "Justice, courage, droiture."},
    {"rune": "ᛒ", "nom": "Berkano", "sens": "Nouveau départ, naissance."},
    {"rune": "ᛖ", "nom": "Ehwaz", "sens": "Alliance, coopération."},
    {"rune": "ᛗ", "nom": "Mannaz", "sens": "Humanité, introspection."},
    {"rune": "ᛚ", "nom": "Laguz", "sens": "Eau, intuition, flux."},
    {"rune": "ᛝ", "nom": "Ingwaz", "sens": "Graine, potentiel latent."},
    {"rune": "ᛟ", "nom": "Othala", "sens": "Héritage, racines."},
    {"rune": "ᛞ", "nom": "Dagaz", "sens": "Aube, éveil, transformation."}
]

# ================================================================
# ☯ I CHING — Trigrammes + Hexagrammes (structure complète)
# ================================================================

TRIGRAMMES = {
    "☰": {"nom": "Ciel", "val": [1,1,1]},
    "☷": {"nom": "Terre", "val": [0,0,0]},
    "☳": {"nom": "Tonnerre", "val": [0,0,1]},
    "☵": {"nom": "Eau", "val": [0,1,0]},
    "☴": {"nom": "Vent / Bois", "val": [1,1,0]},
    "☲": {"nom": "Feu", "val": [1,0,1]},
    "☶": {"nom": "Montagne", "val": [1,0,0]},
    "☱": {"nom": "Lac", "val": [0,1,1]},
}

# 64 HEXAGRAMMES SIMPLIFIÉS (noms officiels)
HEXAGRAMS = [
    {"id": 1, "nom": "Le Créatif", "traits": [1,1,1,1,1,1],
     "texte": "Force pure. Initiative. Action juste. Un nouveau cycle commence."},

    {"id": 2, "nom": "Le Réceptif", "traits": [0,0,0,0,0,0],
     "texte": "Accueil, écoute, réceptivité profonde. Avancer sans s’opposer."},

    {"id": 3, "nom": "La Difficulté Initiale", "traits": [0,0,1,0,1,0],
     "texte": "Les débuts sont chaotiques. Persévérance et patience sont nécessaires."},

    {"id": 4, "nom": "La Folie Juvénile", "traits": [0,1,0,1,0,0],
     "texte": "L’erreur forme. Humilité et guidance requises pour progresser."},

    {"id": 5, "nom": "L’Attente", "traits": [1,1,1,0,0,1],
     "texte": "Attendre le bon moment. Nécessité de confiance et de préparation."},

    {"id": 6, "nom": "Le Conflit", "traits": [1,0,0,1,1,1],
     "texte": "Tension. Clarification nécessaire. Ne pas s’obstiner inutilement."},

    {"id": 7, "nom": "L’Armée", "traits": [0,0,0,1,0,1],
     "texte": "Organisation, discipline. Rassembler les forces avec clarté."},

    {"id": 8, "nom": "La Solidarité", "traits": [1,0,1,0,0,0],
     "texte": "Union, adhésion, ralliement. Choisir les bons alliés."},

    {"id": 9, "nom": "La Force Apprivoisée (petite)", "traits": [1,1,1,1,0,0],
     "texte": "Progrès doux. Retenue. Avancer par petites étapes."},

    {"id": 10, "nom": "La Marche", "traits": [0,0,1,1,1,1],
     "texte": "Agir avec prudence. Tenir son rang. Attention aux limites."},

    {"id": 11, "nom": "La Paix", "traits": [1,1,1,0,0,0],
     "texte": "Harmonie, prospérité, circulation des énergies."},

    {"id": 12, "nom": "La Stagnation", "traits": [0,0,0,1,1,1],
     "texte": "Blocage temporaire. Revenir à l’essentiel. Ne pas forcer."},

    {"id": 13, "nom": "La Communauté avec les Hommes", "traits": [1,1,1,1,0,1],
     "texte": "Accord, fraternité, cause commune. Agir ensemble."},

    {"id": 14, "nom": "Le Grand Avoir", "traits": [1,0,1,1,1,1],
     "texte": "Abondance, maîtrise, rayonnement. Gérer avec sagesse."},

    {"id": 15, "nom": "L’Humilité", "traits": [0,0,0,0,1,0],
     "texte": "Modération, simplicité. Le juste milieu ouvre la voie."},

    {"id": 16, "nom": "L’Enthousiasme", "traits": [0,1,0,0,0,0],
     "texte": "Motivation, élan, inspiration. Fédérer par la joie."},

    {"id": 17, "nom": "La Suivance", "traits": [1,1,0,0,0,1],
     "texte": "S’adapter, suivre le mouvement naturel. Confiance."},

    {"id": 18, "nom": "L’Amendement du Gâté", "traits": [1,0,0,0,1,1],
     "texte": "Réparer, purifier, corriger un héritage ou une situation."},

    {"id": 19, "nom": "L’Approche", "traits": [0,0,1,1,0,0],
     "texte": "Croissance, proximité, ouverture. Bienveillance active."},

    {"id": 20, "nom": "La Contemplation", "traits": [0,0,1,1,0,0],
     "texte": "Observation, vision claire, prise de recul."},

    {"id": 21, "nom": "Mordre au travers", "traits": [1,1,0,1,0,1],
     "texte": "Décision, clarté, trancher ce qui doit l’être."},

    {"id": 22, "nom": "La Grâce", "traits": [1,0,1,0,1,1],
     "texte": "Beauté, finesse, élégance. Illuminer sans s’attacher au superficiel."},

    {"id": 23, "nom": "L’Éclatement", "traits": [0,0,0,0,0,1],
     "texte": "Nécessité de laisser tomber une forme. Détachement."},

    {"id": 24, "nom": "Le Retour", "traits": [1,0,0,0,0,0],
     "texte": "Recommencement, retour à soi. Cycle de renaissance."},

    {"id": 25, "nom": "L’Innocence", "traits": [1,1,1,0,1,0],
     "texte": "Simplicité, spontanéité juste. Ne pas calculer."},

    {"id": 26, "nom": "La Force Apprivoisée (grande)", "traits": [0,1,0,1,1,1],
     "texte": "Maîtrise intérieure, discipline souple. Force contenue."},

    {"id": 27, "nom": "Les Nourritures", "traits": [1,0,1,0,0,1],
     "texte": "Ce que l’on consomme — et ce qui nous consume. Attention aux influences."},

    {"id": 28, "nom": "La Prépondérance du Grand", "traits": [0,1,1,1,1,0],
     "texte": "Tension extrême. Soutenir le poids ou le relâcher."},

    {"id": 29, "nom": "L’Abîme", "traits": [0,1,0,0,1,0],
     "texte": "Répétition des difficultés. Trouver le cœur stable au milieu du danger."},

    {"id": 30, "nom": "L’Adhérence", "traits": [1,0,1,1,0,1],
     "texte": "Clarté, lucidité, feu intérieur. S’attacher à ce qui éclaire."},

    {"id": 31, "nom": "L’Influence", "traits": [1,1,0,1,0,0],
     "texte": "Attraction douce. Séduction, influence mutuelle."},

    {"id": 32, "nom": "La Durée", "traits": [0,0,1,0,1,1],
     "texte": "Endurance, constance. S’engager dans le temps."},

    {"id": 33, "nom": "La Retraite", "traits": [0,0,1,1,1,0],
     "texte": "Recul stratégique. Se retirer pour préserver l’essentiel."},

    {"id": 34, "nom": "La Puissance du Grand", "traits": [1,1,1,0,0,1],
     "texte": "Force en action. Initiative puissante, mais maîtrisée."},

    {"id": 35, "nom": "Le Progrès", "traits": [1,0,0,1,1,0],
     "texte": "Montée en lumière. Progresser en étant vu."},

    {"id": 36, "nom": "L’Obscurcissement de la Lumière", "traits": [0,1,1,0,0,1],
     "texte": "Se protéger, cacher sa lumière. Prudence."},

    {"id": 37, "nom": "La Famille", "traits": [1,1,0,0,1,1],
     "texte": "Cohésion, structure, valeurs familiales."},

    {"id": 38, "nom": "L’Opposition", "traits": [0,0,1,1,0,0],
     "texte": "Différences, divergences. Respecter la distance."},

    {"id": 39, "nom": "L’Entrave", "traits": [1,0,0,0,1,0],
     "texte": "Obstacle. Avancer demande aide extérieure."},

    {"id": 40, "nom": "La Délivrance", "traits": [0,1,0,0,0,1],
     "texte": "Libération, soulagement. Nouvelle respiration."},

    {"id": 41, "nom": "La Diminution", "traits": [0,0,1,0,0,1],
     "texte": "Réduction volontaire. Simplicité bénéfique."},

    {"id": 42, "nom": "L’Augmentation", "traits": [1,0,0,1,0,0],
     "texte": "Croissance, gain, opportunité. Ne pas gaspiller."},

    {"id": 43, "nom": "La Percée", "traits": [1,1,1,1,1,0],
     "texte": "Affirmation, décision, dévoilement. Agir fermement."},

    {"id": 44, "nom": "L’Accouplement", "traits": [0,1,1,1,1,1],
     "texte": "Rencontre brève, influence puissante. Vigilance."},

    {"id": 45, "nom": "Le Rassemblement", "traits": [1,1,1,0,0,0],
     "texte": "Union collective, rassemblement, soutien mutuel."},

    {"id": 46, "nom": "La Montée", "traits": [0,0,0,1,1,1],
     "texte": "Progrès lent mais sûr. Humilité et persévérance."},

    {"id": 47, "nom": "L’Oppression", "traits": [0,0,1,0,0,0],
     "texte": "Fatigue, pression. Tenir le centre."},

    {"id": 48, "nom": "Le Puits", "traits": [0,1,0,1,0,1],
     "texte": "Ressource inépuisable. Revenir à l’essentiel."},

    {"id": 49, "nom": "La Révolution", "traits": [1,0,1,1,0,0],
     "texte": "Transformation radicale. Changement inévitable."},

    {"id": 50, "nom": "Le Chaudron", "traits": [0,0,1,1,0,1],
     "texte": "Alchimie, mutation intérieure. Recevoir et transformer."},

    {"id": 51, "nom": "L’Ébranlement (Tonnerre)", "traits": [1,0,0,1,0,0],
     "texte": "Surprise, choc, réveil. Rester ferme."},

    {"id": 52, "nom": "L’Immobilisation (Montagne)", "traits": [0,0,1,0,0,1],
     "texte": "Silence, arrêt, méditation. Ancrage."},

    {"id": 53, "nom": "Le Développement progressif", "traits": [1,0,0,0,1,0],
     "texte": "Croissance patiente et durable."},

    {"id": 54, "nom": "La Jeune Mariée", "traits": [0,1,0,0,1,0],
     "texte": "Situation subordonnée. Patience et respect du rythme."},

    {"id": 55, "nom": "L’Abondance", "traits": [1,1,0,1,1,0],
     "texte": "Rayonnement, plein épanouissement."},

    {"id": 56, "nom": "Le Voyageur", "traits": [0,1,1,0,1,1],
     "texte": "Instabilité, déplacement. Discipline intérieure requise."},

    {"id": 57, "nom": "Le Vent (Pénétration)", "traits": [1,0,1,0,1,0],
     "texte": "Influence douce et pénétrante. Persévérance subtile."},

    {"id": 58, "nom": "Le Lac (Joie)", "traits": [0,1,0,1,0,1],
     "texte": "Joie, échange, ouverture affective."},

    {"id": 59, "nom": "La Dispersion", "traits": [1,0,1,0,0,0],
     "texte": "Dissiper les blocages, retrouver la fluidité."},

    {"id": 60, "nom": "La Limitation", "traits": [0,0,0,1,0,1],
     "texte": "Juste mesure. Discernement. Cadre utile."},

    {"id": 61, "nom": "La Vérité Intérieure", "traits": [1,1,0,0,1,1],
     "texte": "Sincérité, confiance profonde. Transparence."},

    {"id": 62, "nom": "La Prépondérance du Petit", "traits": [0,0,1,1,0,1],
     "texte": "Détails importants. Prudence dans l’action."},

    {"id": 63, "nom": "Après l’Accomplissement", "traits": [1,0,1,0,1,0],
     "texte": "Ordre établi. Attention à l’excès de certitude."},

    {"id": 64, "nom": "Avant l’Accomplissement", "traits": [0,1,0,1,0,1],
     "texte": "Transition. Dernière étape avant la réussite."}
]

HEX_DICT = {h["id"]: h for h in HEXAGRAMS}

# ================================================================
# 🐾 TOTEMS ANIMAUX — Sud / Nord / Asie
# ================================================================

ANIMALS = [

    {"nom": "Jaguar", "origine": "Amazonie", "message": "Puissance silencieuse. Traverse l’invisible."},
    {"nom": "Anaconda", "origine": "Amazonie", "message": "Transformation profonde. Abandonne une vieille peau."},
    {"nom": "Puma", "origine": "Amazonie", "message": "Courage discipliné. Maîtrise tes élans."},
    {"nom": "Ocelot", "origine": "Amazonie", "message": "Agilité intuitive. Trouve la voie subtile."},
    {"nom": "Tapir", "origine": "Amazonie", "message": "Endurance calme. Avancer pas à pas."},
    {"nom": "Capybara", "origine": "Amazonie", "message": "Sociabilité, douceur. Ne traverse pas seul."},
    {"nom": "Ara", "origine": "Amazonie", "message": "Clarté du verbe. Parle avec vérité."},
    {"nom": "Toucans", "origine": "Amazonie", "message": "Message joyeux. Ouvre ton expression."},
    {"nom": "Perroquet", "origine": "Amazonie", "message": "Écoute attentive. Ce qui se répète enseigne."},
    {"nom": "Paresseux", "origine": "Amazonie", "message": "Lenteur sacrée. Ralentir guérit."},

    {"nom": "Fourmilier", "origine": "Amazonie", "message": "Concentration. Va au cœur des choses."},
    {"nom": "Tatou", "origine": "Amazonie", "message": "Protection douce. Pose tes limites."},
    {"nom": "Coati", "origine": "Amazonie", "message": "Curiosité intelligente. Explore sans peur."},
    {"nom": "Singe Hurleur", "origine": "Amazonie", "message": "Affirmation. Trouve ta voix."},
    {"nom": "Ouistiti", "origine": "Amazonie", "message": "Jeu, légèreté. Le cœur guérit par le rire."},
    {"nom": "Singe Araignée", "origine": "Amazonie", "message": "Souplesse. Adaptation totale."},
    {"nom": "Daim des marais", "origine": "Amazonie", "message": "Patience et écoute profonde."},
    {"nom": "Cerf Mazama", "origine": "Amazonie", "message": "Discrétion. Préserve ton énergie."},
    {"nom": "Armadillo géant", "origine": "Amazonie", "message": "Bouclier intérieur. Sécurité."},
    {"nom": "Chauve-souris", "origine": "Amazonie", "message": "Mort symbolique. Renaissance assurée."},

    {"nom": "Grenouille dendrobate", "origine": "Amazonie", "message": "Alchimie toxique. Transformer l’ombre."},
    {"nom": "Grenouille arboricole", "origine": "Amazonie", "message": "Sensibilité. Présence au corps."},
    {"nom": "Iguane", "origine": "Amazonie", "message": "Observation neutre. Laisse agir le temps."},
    {"nom": "Caiman noir", "origine": "Amazonie", "message": "Puissance dormante. Reste aligné."},
    {"nom": "Tortue d’eau douce", "origine": "Amazonie", "message": "Longévité. Processus patient."},
    {"nom": "Dauphin rose", "origine": "Amazonie", "message": "Magie du cœur. Connexion subtile."},
    {"nom": "Piranha", "origine": "Amazonie", "message": "Sélection. Garde ce qui est essentiel."},
    {"nom": "Poisson-électrique", "origine": "Amazonie", "message": "Énergie brute. Attention à la surcharge."},
    {"nom": "Arrau", "origine": "Amazonie", "message": "Ancienne mémoire. Respect du cycle."},
    {"nom": "Aigle harpie", "origine": "Amazonie", "message": "Vision supérieure. Choisis ton sommet."},

    {"nom": "Bufo (crapaud)", "origine": "Amazonie", "message": "Médecine profonde. Libération intense."},
    {"nom": "Serpent corail", "origine": "Amazonie", "message": "Alerte. Danger subtil."},
    {"nom": "Boa constrictor", "origine": "Amazonie", "message": "Étreinte sacrée. Intégration émotionnelle."},
    {"nom": "Araignée Goliath", "origine": "Amazonie", "message": "Ombre puissante. Trouve ton centre."},
    {"nom": "Scarabée rhinocéros", "origine": "Amazonie", "message": "Force modeste. Courage stable."},
    {"nom": "Luciole", "origine": "Amazonie", "message": "Petite lumière. Espoir intime."},
    {"nom": "Papillon Morpho", "origine": "Amazonie", "message": "Métamorphose. Beauté révélée."},
    {"nom": "Mante tropicale", "origine": "Amazonie", "message": "Patience absolue. Attente juste."},
    {"nom": "Colibri", "origine": "Amazonie", "message": "Joie sacrée. Énergie du cœur."},
    {"nom": "Hocco", "origine": "Amazonie", "message": "Protection familiale. Fidélité."},

    {"nom": "Sanglier Pecari", "origine": "Amazonie", "message": "Tribu. Défense collective."},
    {"nom": "Loutre géante", "origine": "Amazonie", "message": "Jeu social. Soutien mutuel."},
    {"nom": "Agouti", "origine": "Amazonie", "message": "Ressources cachées. Préparation."},
    {"nom": "Jaguarondi", "origine": "Amazonie", "message": "Indépendance profonde."},
    {"nom": "Tamanoir", "origine": "Amazonie", "message": "Purification. Nettoie ton espace."},
    {"nom": "Martinet noir", "origine": "Amazonie", "message": "Vitesse subtile. Mouvement juste."},
    {"nom": "Seriema", "origine": "Amazonie", "message": "Clarté du chant. Expression juste."},
    {"nom": "Huppe tropicale", "origine": "Amazonie", "message": "Intuition aérienne."},
    {"nom": "Cigogne boisée", "origine": "Amazonie", "message": "Voyage sacré. Message venu de loin."},
    {"nom": "Faucon aplomado", "origine": "Amazonie", "message": "Précision. Analyse instinctive."},

    {"nom": "Bison", "origine": "Amérique du Nord", "message": "Abondance humble. Gratitude."},
    {"nom": "Loup gris", "origine": "Amérique du Nord", "message": "Intuition, meute, enseignement."},
    {"nom": "Coyote", "origine": "Amérique du Nord", "message": "Leçon par le paradoxe. Humour sacré."},
    {"nom": "Ours Grizzly", "origine": "Amérique du Nord", "message": "Puissance du cœur. Protection."},
    {"nom": "Aigle royal", "origine": "Amérique du Nord", "message": "Vision divine. Direction claire."},
    {"nom": "Corbeau", "origine": "Amérique du Nord", "message": "Magie, mystère, messages."},
    {"nom": "Renard roux", "origine": "Amérique du Nord", "message": "Stratégie subtile. Déplacements doux."},
    {"nom": "Carcajou", "origine": "Amérique du Nord", "message": "Endurance extrême. Résilience."},
    {"nom": "Puma", "origine": "Amérique du Nord", "message": "Leadership intérieur. Responsabilité."},
    {"nom": "Cheval Mustang", "origine": "Amérique du Nord", "message": "Liberté souveraine."},

    {"nom": "Lynx", "origine": "Amérique du Nord", "message": "Secrets, intuition cachée."},
    {"nom": "Sage-grouse", "origine": "Amérique du Nord", "message": "Danse rituelle. Expression du souffle."},
    {"nom": "Tortue Snapping", "origine": "Amérique du Nord", "message": "Ancienne mémoire. Protection lente."},
    {"nom": "Castor", "origine": "Amérique du Nord", "message": "Construction. Projet à bâtir."},
    {"nom": "Ours noir", "origine": "Amérique du Nord", "message": "Introspection. Retour à la caverne."},
    {"nom": "Hibou Grand-Duc", "origine": "Amérique du Nord", "message": "Vision nocturne. Vérité intérieure."},
    {"nom": "Baleine grise", "origine": "Amérique du Nord", "message": "Voyage d’âme. Transmission ancienne."},
    {"nom": "Loutre de rivière", "origine": "Amérique du Nord", "message": "Joie fluide. Lâcher prise."},
    {"nom": "Rat musqué", "origine": "Amérique du Nord", "message": "Diligence. Petites actions efficaces."},
    {"nom": "Pélican brun", "origine": "Amérique du Nord", "message": "Partage. Don de soi."},

    {"nom": "Tatou Nine-banded", "origine": "Amérique du Nord", "message": "Bouclier naturel. Justes limites."},
    {"nom": "Vipère cuivre", "origine": "Amérique du Nord", "message": "Transformation du feu interne."},
    {"nom": "Crapaud des Plaines", "origine": "Amérique du Nord", "message": "Humilité. Voix intérieure."},
    {"nom": "Antilope Pronghorn", "origine": "Amérique du Nord", "message": "Vitesse d’esprit. Décision."},
    {"nom": "Élan", "origine": "Amérique du Nord", "message": "Fierté calme. Gagner sa place."},
    {"nom": "Caribou", "origine": "Amérique du Nord", "message": "Migration. Suivre le rythme naturel."},
    {"nom": "Mouflon", "origine": "Amérique du Nord", "message": "Défi. Montée vers le haut."},
    {"nom": "Aigle pêcheur", "origine": "Amérique du Nord", "message": "Précision. Prendre ce qu’il faut."},
    {"nom": "Dindon sauvage", "origine": "Amérique du Nord", "message": "Abondance terrestre. Gratitude."},
    {"nom": "Chien des Prairies", "origine": "Amérique du Nord", "message": "Communauté. Attention collective."},

    {"nom": "Loup arctique", "origine": "Amérique du Nord", "message": "Force dans le froid. Endurance."},
    {"nom": "Phoque", "origine": "Amérique du Nord", "message": "Jeu aquatique. Flexibilité émotionnelle."},
    {"nom": "Bison blanc", "origine": "Amérique du Nord", "message": "Sacré. Promesse spirituelle."},
    {"nom": "Buse", "origine": "Amérique du Nord", "message": "Message céleste. Attention aux signes."},
    {"nom": "Lapin des Neiges", "origine": "Amérique du Nord", "message": "Fécondité. Intuition rapide."},
    {"nom": "Ours polaire", "origine": "Amérique du Nord", "message": "Maîtrise du froid. Force immobile."},
    {"nom": "Lynx du Canada", "origine": "Amérique du Nord", "message": "Vision cachée. Secrets révélés."},
    {"nom": "Spermophile", "origine": "Amérique du Nord", "message": "Préparation minutieuse."},
    {"nom": "Condor de Californie", "origine": "Amérique du Nord", "message": "Purification, renouveau."},
    {"nom": "Raton-Laveur", "origine": "Amérique du Nord", "message": "Ingéniosité. Identité multiple."},

    {"nom": "Pie bavarde", "origine": "Amérique du Nord", "message": "Magie paradoxale. Attention au miroir."},
    {"nom": "Quiscale", "origine": "Amérique du Nord", "message": "Communication collective."},
    {"nom": "Moufette", "origine": "Amérique du Nord", "message": "Respect. Limites claires."},
    {"nom": "Cygne trompette", "origine": "Amérique du Nord", "message": "Beauté noble. Grâce en mouvement."},
    {"nom": "Ours brun Kodiak", "origine": "Amérique du Nord", "message": "Gigantesque force tranquille."},
    {"nom": "Renard arctique", "origine": "Amérique du Nord", "message": "Adaptation totale. Camouflage sacré."},
    {"nom": "Chouette effraie", "origine": "Amérique du Nord", "message": "Mystère féminin. Guidance nocturne."},
    {"nom": "Morse", "origine": "Amérique du Nord", "message": "Patience du froid. Endurance émotionnelle."},
    {"nom": "Tortue Peinte", "origine": "Amérique du Nord", "message": "Équilibre eau-terre. Création."},
    {"nom": "Gélinotte huppée", "origine": "Amérique du Nord", "message": "Rythme. Respiration profonde."},

    {"nom": "Tigre de Sibérie", "origine": "Asie", "message": "Puissance noble. Autorité intérieure."},
    {"nom": "Panda géant", "origine": "Asie", "message": "Douceur, équilibre, innocence consciente."},
    {"nom": "Grue blanche", "origine": "Asie", "message": "Longévité, paix, appel du ciel."},
    {"nom": "Dragon d’eau", "origine": "Asie", "message": "Flux, puissance intérieure, mutation."},
    {"nom": "Yak", "origine": "Asie", "message": "Stabilité du cœur. Endurance spirituelle."},
    {"nom": "Léopard des neiges", "origine": "Asie", "message": "Discrétion sacrée. Voie invisible."},
    {"nom": "Cerf Sika", "origine": "Asie", "message": "Grâce, innocence, pureté du mouvement."},
    {"nom": "Grue couronnée", "origine": "Asie", "message": "Ascension, élévation, clarté du souffle."},
    {"nom": "Carpe Koi", "origine": "Asie", "message": "Persévérance noble. Destin ascendant."},
    {"nom": "Renard Kitsune", "origine": "Asie", "message": "Magie subtile. Intuition changeante."},

    {"nom": "Singe doré", "origine": "Asie", "message": "Intellect sacré. Esprit joueur."},
    {"nom": "Grün Macaque", "origine": "Asie", "message": "Adaptation sociale. Intelligence vive."},
    {"nom": "Pivert noir", "origine": "Asie", "message": "Rythme, discipline intérieure."},
    {"nom": "Tortue sacrée", "origine": "Asie", "message": "Piliers du monde. Mémoire ancienne."},
    {"nom": "Chien viverrin", "origine": "Asie", "message": "Mutabilité. Masques et vérités."},
    {"nom": "Gazelle de Mongolie", "origine": "Asie", "message": "Légèreté du désert. Mouvement libre."},
    {"nom": "Camelopard", "origine": "Asie", "message": "Long regard. Perspective claire."},
    {"nom": "Flamant tibétain", "origine": "Asie", "message": "Équilibre sacré. Beauté discrète."},
    {"nom": "Python birman", "origine": "Asie", "message": "Sagesse terrestre. Mouvement spiralé."},
    {"nom": "Paon bleu", "origine": "Asie", "message": "Beauté éclatante. Vérité exposée."},

    {"nom": "Grue mandchoue", "origine": "Asie", "message": "Pureté. Harmonie céleste."},
    {"nom": "Chat pêcheur", "origine": "Asie", "message": "Adaptation eau-terre. Patient chasseur."},
    {"nom": "Crocodile du Siam", "origine": "Asie", "message": "Force immobile. Ancienne sagesse."},
    {"nom": "Ours tibétain", "origine": "Asie", "message": "Silence profond. Montagne intérieure."},
    {"nom": "Sanglier sauvage", "origine": "Asie", "message": "Courage brut. Percée directe."},
    {"nom": "Blaireau miel", "origine": "Asie", "message": "Invincibilité. Ne jamais reculer."},
    {"nom": "Cerf rouge", "origine": "Asie", "message": "Cycle, renouveau, noblesse."},
    {"nom": "Pigeon couronné", "origine": "Asie", "message": "Beauté subtile. Paix en mouvement."},
    {"nom": "Lynx d’Asie", "origine": "Asie", "message": "Clairvoyance discrète."},
    {"nom": "Faucon sacré", "origine": "Asie", "message": "Focalisation. Cible atteinte."},

    {"nom": "Rat des bambous", "origine": "Asie", "message": "Travail discret. Construction lente."},
    {"nom": "Couleuvre verte", "origine": "Asie", "message": "Souplesse mentale."},
    {"nom": "Cygne noir asiatique", "origine": "Asie", "message": "Présages. Transformation de l’inattendu."},
    {"nom": "Chèvre de montagne", "origine": "Asie", "message": "Ascension difficile mais nécessaire."},
    {"nom": "Grive japonaise", "origine": "Asie", "message": "Chant intérieur. Message doux."},
    {"nom": "Civette asiatique", "origine": "Asie", "message": "Mystère, alchimie du parfum."},
    {"nom": "Renard polaire sibérien", "origine": "Asie", "message": "Adaptation extrême."},
    {"nom": "Lièvre mandchou", "origine": "Asie", "message": "Saut dans l’inconnu."},
    {"nom": "Aigle des steppes", "origine": "Asie", "message": "Puissance du regard."},
    {"nom": "Grue bleue", "origine": "Asie", "message": "Calme profond. Esprit ouvert."},

    {"nom": "Loutre d’Asie", "origine": "Asie", "message": "Joie fluide. Intelligence émotionnelle."},
    {"nom": "Pangolin", "origine": "Asie", "message": "Protection sacrée. Sensibilité cachée."},
    {"nom": "Chouette de l’Oural", "origine": "Asie", "message": "Sagesse nocturne."},
    {"nom": "Crapaud de pluie", "origine": "Asie", "message": "Appel du renouveau."},
    {"nom": "Oiseau bleu japonais", "origine": "Asie", "message": "Heureux présage."},
    {"nom": "Cigogne orientale", "origine": "Asie", "message": "Fidélité, migration sacrée."},
    {"nom": "Phoque annelé sibérien", "origine": "Asie", "message": "Calme sous pression."},
    {"nom": "Renard du désert", "origine": "Asie", "message": "Écoute subtile. Intelligence du silence."},
    {"nom": "Grue de Sibérie", "origine": "Asie", "message": "Esprit pur, élévation."},
    {"nom": "Tigre blanc mythique", "origine": "Asie", "message": "Protection céleste. Pouvoir noble."}
]

# ---------------------------------------------------------------
# Génération du dictionnaire hexagrammes
# ---------------------------------------------------------------
try:
    HEX_DICT = {h["id"]: h for h in HEXAGRAMS}
except:
    HEX_DICT = {}

# ============================================================
# 📦 bloc_3.py — Définition des tirages (SPREADS + PACKS)
# ============================================================

# Chaque tirage = {
#   "pack": "Nom du pack",
#   "nom": "Nom du tirage",
#   "positions": [
#        ("Nom position", "Description / Intention")
#   ]
# }

SPREADS = [

    # =======================================================
    # 🔮 ORACLE 48 CARTES
    # =======================================================
    {
        "pack": "Oracle 48",
        "nom": "Tirage libre",
        "positions": [
            ("Carte 1", "Message immédiat"),
            ("Carte 2", "Énergie associée"),
            ("Carte 3", "Axe de guidance"),
        ],
    },
    {
        "pack": "Oracle 48",
        "nom": "Tirage en croix",
        "positions": [
            ("Situation", "Où tu en es"),
            ("Défi", "Ce qui bloque"),
            ("Ressource", "Ton soutien"),
            ("Conseil", "La direction juste"),
            ("Issue", "Si tu suis ce chemin"),
        ],
    },
    {
        "pack": "Oracle 48",
        "nom": "Voie intérieure (3 cartes)",
        "positions": [
            ("Ombre", "Ce qui demande d’être vu"),
            ("Leçon", "Ce que tu intègres"),
            ("Lumière", "Direction élevée"),
        ],
    },

    # =======================================================
    # 📜 PALI
    # =======================================================
    {
        "pack": "Pāli",
        "nom": "Souffle (1 carte)",
        "positions": [
            ("Souffle", "Ce qui revient au calme"),
        ],
    },
    {
        "pack": "Pāli",
        "nom": "Clarté (3 cartes)",
        "positions": [
            ("Confusion", "Ce qui embrouille"),
            ("Vision", "Ce qui se révèle"),
            ("Chemin", "Ce qui s’éclaire"),
        ],
    },
    {
        "pack": "Pāli",
        "nom": "Voie juste (4 cartes)",
        "positions": [
            ("Vue juste", "Compréhension profonde"),
            ("Intention juste", "Direction intérieure"),
            ("Action juste", "Posture appropriée"),
            ("Présence juste", "Alignement final"),
        ],
    },

    # =======================================================
    # ᚱ RUNES
    # =======================================================
    {
        "pack": "Runes",
        "nom": "Rune du jour",
        "positions": [
            ("Rune", "Message principal"),
        ],
    },
    {
        "pack": "Runes",
        "nom": "Trinité runique (3 runes)",
        "positions": [
            ("Passé", "Forces déjà en mouvement"),
            ("Présent", "Dynamique actuelle"),
            ("Futur", "Direction probable"),
        ],
    },
    {
        "pack": "Runes",
        "nom": "Rune d’ombre (3 runes)",
        "positions": [
            ("Ombre", "Ce qui te freine"),
            ("Épreuve", "Ce qui doit être traversé"),
            ("Libération", "L’énergie juste"),
        ],
    },

    # =======================================================
    # ☯ I CHING
    # =======================================================
    {
        "pack": "I Ching",
        "nom": "I Ching classique (1 hexagramme + mutations)",
        "positions": [
            ("Hexagramme principal", "Situation actuelle"),
            ("Traits mutants", "Évolution en cours"),
            ("Hexagramme de mutation", "Transformation"),
            ("Hexagramme nucléaire", "Essence du mouvement"),
            ("Hexagramme complémentaire", "Polarité inversée"),
        ],
    },
    {
        "pack": "I Ching",
        "nom": "Chemin du Tao (3 hexagrammes)",
        "positions": [
            ("Entrée", "Comment aborder la situation"),
            ("Voie", "La dynamique du moment"),
            ("Issue", "Le mouvement naturel"),
        ],
    },

    # =======================================================
    # 🐾 TOTEMS — MÉDECINE ANIMALE (pack demandé)
    # =======================================================

    # --- 1 carte ---
    {
        "pack": "Totems – Médecine animale",
        "nom": "Allié du moment (1 carte)",
        "positions": [
            ("Animal allié", "La présence animale qui t’accompagne maintenant."),
        ],
    },

    # --- 3 cartes ---
    {
        "pack": "Totems – Médecine animale",
        "nom": "Médecine du jour (3 cartes)",
        "positions": [
            ("Totem", "L’énergie animale qui se présente."),
            ("Défi", "Ce qu’elle veut t’aider à dépasser."),
            ("Médecine", "L’enseignement à intégrer."),
        ],
    },
    {
        "pack": "Totems – Médecine animale",
        "nom": "Totem d’ombre (3 cartes)",
        "positions": [
            ("Ombre animale", "La part instinctive refoulée."),
            ("Risque", "Le danger si tu résistes."),
            ("Intégration", "Comment domestiquer cette énergie."),
        ],
    },

    # --- 4 cartes ---
    {
        "pack": "Totems – Médecine animale",
        "nom": "Totem de pouvoir (4 cartes)",
        "positions": [
            ("Animal principal", "Force en action."),
            ("Voie haute", "Ton potentiel lumineux."),
            ("Voie basse", "Quand la puissance déborde."),
            ("Conseil", "Comment canaliser cette force."),
        ],
    },

    {
        "pack": "Totems – Médecine animale",
        "nom": "Roue chamanique (4 directions)",
        "positions": [
            ("Nord", "Sagesse / Ancêtres / Vision supérieure."),
            ("Sud", "Enfance / Joie / Guérison émotionnelle."),
            ("Est", "Nouveau départ / Inspiration."),
            ("Ouest", "Transformation / Initiation."),
        ],
    },

    # --- 5 cartes ---
    {
        "pack": "Totems – Médecine animale",
        "nom": "Chemin de médecine (5 cartes)",
        "positions": [
            ("Passé animal", "L’énergie animale qui t’a construit(e)."),
            ("Présent", "Ton énergie totem actuelle."),
            ("Défi", "Le blocage révélé par l’animal."),
            ("Allié caché", "Ce qui t’aide sans le savoir."),
            ("Médecine finale", "L’enseignement global."),
        ],
    },

]
# ============================================================


# ============================================================
# 📦 PACKS DÉRIVÉS AUTOMATIQUEMENT
# ============================================================

SPREAD_PACKS = sorted({s["pack"] for s in SPREADS})
# ===============================================================
# 📦 bloc_4.py — Moteurs de tirage (Oracle / Runes / I Ching)
# ===============================================================

import random

# ===============================================================
# 🔮 ORACLE / TOTEMS / PALI ETC.
# ===============================================================

def draw_cards(deck, n):
    """
    Tire n cartes dans un jeu (Oracle, Totems, Pāli, etc.)
    """
    return random.sample(deck, n)


# ===============================================================
# ᚱ RUNES
# ===============================================================

def draw_runes(runes, n=1):
    """
    Tire n runes du jeu.
    """
    return random.sample(runes, n)


# ===============================================================
# ☯ I CHING — MÉTHODE CLASSIQUE
# ===============================================================

# Définitions des traits :
# 6 = yin mutant
# 7 = yang stable
# 8 = yin stable
# 9 = yang mutant
#
# Traits listés du bas (index 0) vers le haut (index 5)


# -----------------------------
# 🎲 Tirage de base (6 traits)
# -----------------------------
def draw_iching_traits():
    """
    Génère les 6 traits selon la méthode traditionnelle :
    6 (yin mutant), 7 (yang), 8 (yin), 9 (yang mutant)
    """
    return [random.choice([6, 7, 8, 9]) for _ in range(6)]


# -----------------------------
# 🔢 Conversion traits → ID hexagramme (1 à 64)
# -----------------------------
def traits_to_hexagram_id(traits):
    """
    Convertit 6 traits yin/yang en numéro d’hexagramme (1–64).

    Convention utilisée :
    - yin = 0  (traits 6 ou 8)
    - yang = 1 (traits 7 ou 9)

    Bits du bas vers le haut (trait 0 = bit 0)
    +1 car hexagrammes numérotés 1..64.
    """
    value = 0
    for i, t in enumerate(traits):
        bit = 1 if t in (7, 9) else 0
        value |= (bit << i)
    return value + 1


# -----------------------------
# 🔁 Hexagramme de mutation
# -----------------------------
def iching_mutated_traits(traits):
    """
    Retourne les traits après mutation :
    - 6 (yin mutant)  → 7 (yang)
    - 9 (yang mutant) → 8 (yin)
    - sinon inchangé
    """
    mutated = []
    for t in traits:
        if t == 6:
            mutated.append(7)
        elif t == 9:
            mutated.append(8)
        else:
            mutated.append(t)
    return mutated


# -----------------------------
# 🧬 Hexagramme nucléaire
# -----------------------------
def iching_nuclear_traits(traits):
    """
    Hexagramme nucléaire = traits 2–4 + 3–5
    (indices 1-2-3 et 2-3-4)
    """
    return traits[1:4] + traits[2:5]


# -----------------------------
# 🌗 Hexagramme complémentaire
# -----------------------------
def iching_complementary_traits(traits):
    """
    Inversion yin ↔ yang :
    - yin (6/8)  → yang (9)
    - yang (7/9) → yin  (6)
    """
    comp = []
    for t in traits:
        if t in (6, 8):  # yin
            comp.append(9)  # yang complet
        else:  # yang
            comp.append(6)  # yin complet
    return comp


# -----------------------------
# 🔮 Bundle complet pour la WebUI
# -----------------------------
def iching_full_reading():
    """
    Retourne un paquet complet :
    {
        "traits": [...],
        "id": int,
        "mutants": [...],
        "id_mutants": int,
        "nuclear": [...],
        "id_nuclear": int,
        "complementary": [...],
        "id_complementary": int
    }
    """
    t = draw_iching_traits()

    mutated = iching_mutated_traits(t)
    nuclear = iching_nuclear_traits(t)
    complementary = iching_complementary_traits(t)

    return {
        "traits": t,
        "id": traits_to_hexagram_id(t),

        "mutants": mutated,
        "id_mutants": traits_to_hexagram_id(mutated),

        "nuclear": nuclear,
        "id_nuclear": traits_to_hexagram_id(nuclear),

        "complementary": complementary,
        "id_complementary": traits_to_hexagram_id(complementary),
    }
# ============================================================
# 📦 bloc_5.py — WebUI complète Streamlit
# ============================================================

import streamlit as st
from datetime import datetime
import random

# ====== IMPORTS DES BLOCS ======
import CARDS, RUNES_LIST, PALI_CARDS
import HEXAGRAMS, ANIMALS
import SPREADS, SPREAD_PACKS
import (
    draw_cards, draw_runes,
    draw_iching_traits, iching_full_reading,
)

# ============================================================
# 🌙 CONFIGURATION DE L'APP
# ============================================================

st.set_page_config(
    page_title="Oracle Multisystèmes",
    page_icon="🔮",
    layout="wide"
)

# ============================================================
# 🎨 THÈME
# ============================================================

st.sidebar.header("🎨 Thème")
theme = st.sidebar.radio("Mode", ["Sombre", "Clair"], index=0)

if theme == "Sombre":
    BG = "#0e0e0e"
    TEXT = "#ffffff"
    CARD_BG = "rgba(20,20,20,0.95)"
else:
    BG = "#fafafa"
    TEXT = "#000000"
    CARD_BG = "rgba(255,255,255,0.95)"


# ============================================================
# 🎨 CSS Global + Flip Cards
# ============================================================

st.markdown(
    f"""
<style>
body {{
    background-color: {BG} !important;
    color: {TEXT};
}}

.flip-card {{
    background-color: transparent;
    width: 100%;
    perspective: 1000px;
    margin-bottom: 1rem;
}}

.flip-card-inner {{
    position: relative;
    width: 100%;
    min-height: 150px;
    transition: transform 0.6s;
    transform-style: preserve-3d;
}}

.flip-card:hover .flip-card-inner {{
    transform: rotateY(180deg);
}}
.flip-card:active .flip-card-inner {{
    transform: rotateY(180deg);
}}

.flip-card-front, .flip-card-back {{
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.15);
    padding: 1rem;
    background-color: {CARD_BG};
    color: {TEXT};
}}

.flip-card-back {{
    transform: rotateY(180deg);
}}

.oracle-pos {{
    font-size: 0.75rem;
    opacity: 0.7;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# 🔄 Fonction d'affichage d'une carte
# ============================================================

def show_flip_card(title, family, msg, axis, pos_label=None):
    pos_html = f"<div class='oracle-pos'>{pos_label}</div>" if pos_label else ""
    card_html = f"""
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      {pos_html}
      <h3>{title}</h3>
      <p><b>Famille :</b> {family}</p>
      <p style="opacity:0.6"><i>Retourne la carte</i></p>
    </div>
    <div class="flip-card-back">
      {pos_html}
      <h3>{title}</h3>
      <p><b>Message :</b> {msg}</p>
      <p><i>Axe :</i> {axis}</p>
    </div>
  </div>
</div>
"""
    st.markdown(card_html, unsafe_allow_html=True)


# ============================================================
# 📒 ONGLET PRINCIPAL
# ============================================================

tab_tirage, tab_methode, tab_cartes, tab_apropos = st.tabs(
    ["🔮 Tirage", "📜 Méthode", "🃏 Cartes & Symboles", "ℹ️ À propos"]
)


# ============================================================
# 🔮 ░░░ ONGLETS : TIRAGE PRINCIPAL ░░░
# ============================================================

with tab_tirage:
    st.title("🔮 Tirages divinatoires")

    # -----------------------------
    # 🧭 Sélection du système
    # -----------------------------
    system = st.selectbox(
        "Choisir un système",
        ["Oracle 48", "Pāli", "Runes", "I Ching", "Totems – Médecine animale"]
    )

    # -----------------------------
    # 📦 Sélection du pack
    # -----------------------------
    options = [s["nom"] for s in SPREADS if s["pack"] == system]
    tirage_nom = st.selectbox("Type de tirage", options)

    # Récupération du tirage choisi
    tirage = next(s for s in SPREADS if s["nom"] == tirage_nom)

    st.markdown("### Positions du tirage")
    for p, d in tirage["positions"]:
        st.markdown(f"- **{p}** — {d}")

    st.write("---")

    question = st.text_input("📝 Intention / Question (optionnel)")

    if st.button("Tirer ✨"):
        st.subheader("🔮 Résultat")

        # ORACLE 48 ------------------------------------------------------------
        if system == "Oracle 48":
            n = len(tirage["positions"])
            cards = draw_cards(CARDS, n)

            for (pos, _), c in zip(tirage["positions"], cards):
                show_flip_card(
                    f"{pos} — {c['nom']}",
                    c["famille"], c["message"], c["axe"],
                    pos_label=pos
                )

        # PALI -----------------------------------------------------------------
        elif system == "Pāli":
            n = len(tirage["positions"])
            cards = draw_cards(PALI_CARDS, n)

            for (pos, _), c in zip(tirage["positions"], cards):
                st.markdown(f"### {pos}")
                st.write(f"**{c['mot']}** — {c['sens']}")

        # RUNES ----------------------------------------------------------------
        elif system == "Runes":
            n = len(tirage["positions"])
            runes = draw_runes(RUNES_LIST, n)

            for (pos, _), r in zip(tirage["positions"], runes):
                st.markdown(f"### {pos}")
                st.write(f"**{r['rune']} — {r['nom']}** : {r['message']}")

        # I CHING --------------------------------------------------------------
        elif system == "I Ching":
            reading = iching_full_reading()

            st.markdown("### Hexagramme principal")
            st.write(f"Hexagramme **{reading['id']}**")

            st.markdown("### Hexagramme de mutation")
            st.write(f"Hexagramme **{reading['id_mutants']}**")

            st.markdown("### Hexagramme nucléaire")
            st.write(f"Hexagramme **{reading['id_nuclear']}**")

            st.markdown("### Hexagramme complémentaire")
            st.write(f"Hexagramme **{reading['id_complementary']}**")

        # TOTEMS --------------------------------------------------------------
        elif system == "Totems – Médecine animale":
            n = len(tirage["positions"])
            animals = draw_cards(ANIMALS, n)

            for (pos, _), a in zip(tirage["positions"], animals):
                st.markdown(f"### {pos}")
                st.write(f"**{a['nom']}** ({a['origine']}) — {a['message']}")

# ============================================================
# 📜 ONGLET MÉTHODE
# ============================================================

with tab_methode:
    st.title("📘 Méthode de tirage")
    st.markdown("""
    Contenu détaillé de la méthode (voir ton bloc Documentation).
    """)


# ============================================================
# 🃏 ONGLET CARTES & SYMBOLES
# ============================================================

with tab_cartes:
    st.title("🃏 Galerie des cartes et symboles")

    st.markdown("## 🔮 Oracle 48")
    cols = st.columns(4)
    for i, c in enumerate(CARDS):
        with cols[i % 4]:
            st.markdown(f"**{c['nom']}**<br><span style='opacity:0.7'>{c['famille']}</span>", unsafe_allow_html=True)

    st.write("---")

    st.markdown("## ᚱ Runes")
    cols = st.columns(6)
    for i, r in enumerate(RUNES_LIST):
        with cols[i % 6]:
            st.markdown(f"### {r['rune']}<br>{r['nom']}", unsafe_allow_html=True)

    st.write("---")

    st.markdown("## ☯ I Ching")
    cols = st.columns(4)
    for i, h in enumerate(HEXAGRAMS):
        with cols[i % 4]:
            st.markdown(f"**{h['id']:02d}. {h['nom']}**")

    st.write("---")

    st.markdown("## 🐾 Totems")
    cols = st.columns(3)
    for i, a in enumerate(ANIMALS):
        with cols[i % 3]:
            st.markdown(f"**{a['nom']}**<br><i>{a['origine']}</i>", unsafe_allow_html=True)


# ============================================================
# ℹ️ ONGLET À PROPOS
# ============================================================

with tab_apropos:
    st.title("ℹ️ À propos")
    st.markdown("""
    Application de guidance multisystèmes.
    Développement : Python + Streamlit.
    """)

# ============================================================
# 📦 bloc_6.py — Module avancé (export, historique, API, I Ching)
# ============================================================

import json
import os
from datetime import datetime
import base64

# Optionnels (non obligatoires)
try:
    from reportlab.pdfgen import canvas
    REPORTLAB_AVAILABLE = True
except:
    REPORTLAB_AVAILABLE = False

try:
    from fastapi import FastAPI
    FASTAPI_AVAILABLE = True
except:
    FASTAPI_AVAILABLE = False

try:
    from PIL import Image
    PIL_AVAILABLE = True
except:
    PIL_AVAILABLE = False


# ============================================================
# 🔄 1. OUTILS GÉNÉRIQUES D'EXPORT (Markdown, JSON, PDF)
# ============================================================

def export_markdown(tirage_dict):
    """
    Exporte un tirage sous forme de texte Markdown.
    """
    lines = []
    lines.append(f"# 🔮 Tirage — {tirage_dict.get('system', 'Inconnu')}")
    lines.append(f"**Date** : {tirage_dict.get('date', '—')}")
    lines.append(f"**Question** : _{tirage_dict.get('question', '—')}_")
    lines.append("---")

    for pos, card in tirage_dict.get("result", []):
        lines.append(f"## {pos}")
        lines.append(f"- **Nom** : {card.get('nom', '—')}")
        if "famille" in card:
            lines.append(f"- Famille : {card['famille']}")
        if "message" in card:
            lines.append(f"- Message : {card['message']}")
        if "axe" in card:
            lines.append(f"- Axe : {card['axe']}")
        lines.append("")

    return "\n".join(lines)


def export_json(tirage_dict, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tirage_dict, f, indent=2, ensure_ascii=False)
    return path


def export_pdf(tirage_dict, path):
    if not REPORTLAB_AVAILABLE:
        raise ImportError("ReportLab non installé.")

    c = canvas.Canvas(path)

    y = 800
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Tirage Divinatoire")
    y -= 40

    c.setFont("Helvetica", 10)
    for k, v in tirage_dict.items():
        if k == "result":
            continue
        c.drawString(50, y, f"{k}: {v}")
        y -= 20

    y -= 20
    for pos, card in tirage_dict["result"]:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, pos)
        y -= 20
        c.setFont("Helvetica", 10)
        for ck, cv in card.items():
            c.drawString(65, y, f"{ck}: {cv}")
            y -= 15
        y -= 10

    c.save()
    return path


# ============================================================
# 📚 2. HISTORIQUE LOCAL (persistant .json)
# ============================================================

HISTORY_FILE = "tirages_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(entry):
    data = load_history()
    data.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ============================================================
# 🎨 3. IMAGES & ASSETS (deck physique)
# ============================================================

def load_image(path):
    """
    Charge une image en base64 (pour Streamlit).
    """
    if not PIL_AVAILABLE:
        raise ImportError("Pillow n’est pas installé.")
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{encoded}"

def resize_image(input_path, output_path, size=(300, 500)):
    if not PIL_AVAILABLE:
        raise ImportError("Pillow requis.")
    img = Image.open(input_path)
    img = img.resize(size)
    img.save(output_path)
    return output_path


# ============================================================
# ☯ 4. ANALYSE I CHING AVANCÉE
# ============================================================

I_CHING_TEXTS = {
    # Exemple minimal — tu peux injecter Wilhelm, Legge, etc.
    1: {
        "nom": "Le Créatif",
        "jugement": "Puissance créatrice. Début d’un cycle.",
        "image": "Le ciel agit avec force.",
    },
    2: {
        "nom": "Le Réceptif",
        "jugement": "Absorption, accueil, maturité yin.",
        "image": "La terre nourrit toutes choses.",
    },
}

def iching_interpret(id_hex):
    return I_CHING_TEXTS.get(id_hex, {"nom": "—", "jugement": "—", "image": "—"})


# ============================================================
# 🔮 5. TIRAGES AVANCÉS (Chakana, 12 maisons, voyage)
# ============================================================

TIRAGE_AVANCES = {

    "Chakana Inca (7 cartes)": [
        ("Nord", "Vision supérieure"),
        ("Sud", "Guérison"),
        ("Est", "Nouvelle direction"),
        ("Ouest", "Transformation"),
        ("Centre", "Essence du moment"),
        ("Ciel", "Aide subtile"),
        ("Terre", "Ancrage et soutien"),
    ],

    "Voyage chamanique (5 cartes)": [
        ("Entrée", "Ce qui initie le voyage"),
        ("Guide", "L'allié qui accompagne"),
        ("Épreuve", "Ce qui doit être traversé"),
        ("Ressource", "La force disponible"),
        ("Retour", "Ce que tu ramènes"),
    ],

    "Astrologie — 12 maisons": [
        (f"Maison {i}", f"Influence dans le domaine {i}") for i in range(1,13)
    ]
}


# ============================================================
# 🧑‍💼 6. MODE CONSULTATION PROFESSIONNELLE
# ============================================================

def make_consultation_record(name, question, system, result):
    return {
        "consultant": name,
        "question": question,
        "system": system,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "result": result,
    }


# ============================================================
# 🌐 7. API FASTAPI (optionelle)
# ============================================================

def create_api_interface(draw_function):
    """
    Retourne une instance FastAPI prête à l’emploi.
    """
    if not FASTAPI_AVAILABLE:
        raise ImportError("FastAPI non installée.")

    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"status": "ok"}

    @app.get("/tirage")
    def get_tirage():
        return draw_function()

    return app
# ============================================================
# 📦 bloc_7.py — Styles, animations, thèmes, sons, deck physique
# ============================================================

import base64
import os

# ============================================================
# 🎨 1. THEMES VISUELS AVANCÉS
# ============================================================

THEMES = {
    "Dark+": {
        "bg": "#0b0b0b",
        "text": "#f7f7f7",
        "card_bg": "rgba(18,18,18,0.95)",
        "accent": "#9f79ff",
    },
    "Solar": {
        "bg": "#fff9e6",
        "text": "#222",
        "card_bg": "rgba(255,255,240,0.90)",
        "accent": "#ffb400",
    },
    "Forest": {
        "bg": "#0f190f",
        "text": "#e5ffe5",
        "card_bg": "rgba(10,20,10,0.92)",
        "accent": "#2aff88",
    },
    "Mystic": {
        "bg": "#1a0f1a",
        "text": "#fef2ff",
        "card_bg": "rgba(40,10,50,0.85)",
        "accent": "#cc33ff",
    },
    "Minimal": {
        "bg": "#ffffff",
        "text": "#000000",
        "card_bg": "rgba(255,255,255,0.90)",
        "accent": "#111111",
    },
}

def get_theme_css(theme_name):
    """
    Retourne le CSS complet selon le thème demandé.
    """
    t = THEMES.get(theme_name, THEMES["Dark+"])
    return f"""
<style>
body {{
    background-color: {t['bg']} !important;
    color: {t['text']} !important;
}}

.card-physique {{
    background: {t['card_bg']};
    border: 2px solid {t['accent']};
    border-radius: 16px;
    padding: 1rem;
    margin: 0.5rem 0;
}}

h1, h2, h3, h4 {{
    color: {t['accent']} !important;
}}
</style>
"""


# ============================================================
# 🪄 2. ANIMATIONS AVANCÉES (CSS)
# ============================================================

CSS_ANIMATIONS = r"""
<style>

@keyframes glow {
    0% { box-shadow: 0 0 6px rgba(255,255,255,0.2); }
    50% { box-shadow: 0 0 14px rgba(255,255,255,0.5); }
    100% { box-shadow: 0 0 6px rgba(255,255,255,0.2); }
}

@keyframes floating {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
    100% { transform: translateY(0px); }
}

@keyframes flip-tarot {
    from { transform: rotateY(0deg); }
    to   { transform: rotateY(180deg); }
}

.flip-auto {
    animation: flip-tarot 0.8s ease-in-out forwards;
}

.card-glow {
    animation: glow 3s infinite ease-in-out;
}

.card-float {
    animation: floating 3s infinite ease-in-out;
}

</style>
"""


# ============================================================
# 🃏 3. DECK PHYSIQUE (textures + bords)
# ============================================================

DECK_BACKGROUNDS = {
    "Mystic Purple": "assets/deck_mystic.png",
    "Sacred Black": "assets/deck_black.png",
    "Sunset Gold": "assets/deck_sunset.png",
    "Forest Spirit": "assets/deck_forest.png",
}

def load_base64(path):
    """
    Convertit une image en base64 (pour background Streamlit).
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def deck_background_css(image_path):
    """
    CSS pour une image de dos de cartes en fond.
    """
    encoded = load_base64(image_path)
    return f"""
<style>
.card-physique {{
    background-image: url("data:image/png;base64,{encoded}");
    background-size: cover;
}}
</style>
"""


# ============================================================
# 🔊 4. SONS (tirage, flip, ambiance)
# ============================================================

def encode_sound(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def sound_js(base64_sound):
    """
    Génère le JS qui joue un son dans Streamlit.
    """
    return f"""
<script>
var audio = new Audio("data:audio/mp3;base64,{base64_sound}");
audio.play();
</script>
"""


# ============================================================
# 🧩 5. STYLES SPÉCIAUX (blur, glass, neon, borders)
# ============================================================

CSS_GLASS = r"""
<style>
.glass-card {
    backdrop-filter: blur(5px);
    background: rgba(255,255,255,0.10);
    border-radius: 16px;
    padding: 1rem;
    border: 1px solid rgba(255,255,255,0.25);
}
</style>
"""

CSS_NEON = r"""
<style>
.neon {
    border: 1px solid #ff00de;
    box-shadow: 0 0 12px #ff00de, 0 0 24px #ff00de;
}
</style>
"""

CSS_BORDER_ART = r"""
<style>
.border-art {
    border: 2px dashed rgba(255,255,255,0.5);
    border-radius: 12px;
    padding: 0.8rem;
}
</style>
"""


# ============================================================
# ⚙️ 6. UTILITAIRES D’INJECTION CSS/JS
# ============================================================

def inject_css(css):
    """
    Retourne un bloc CSS prêt à injecter dans Streamlit :
    st.markdown(inject_css(...), unsafe_allow_html=True)
    """
    return f"<style>{css}</style>"

def inject_js(js):
    """
    Idem pour JS :
    st.markdown(inject_js(...), unsafe_allow_html=True)
    """
    return f"<script>{js}</script>"


# ============================================================
# 🧙 7. PRESETS COMBINÉS (thème + animation + style)
# ============================================================

def preset_mystic_glass():
    return (
        get_theme_css("Mystic") +
        CSS_GLASS +
        CSS_ANIMATIONS
    )

def preset_forest_float():
    return (
        get_theme_css("Forest") +
        CSS_ANIMATIONS +
        """
        <style>.flip-card-inner { animation: floating 3s infinite; }</style>
        """
    )
# ============================================================
# 📦 bloc_8.py — Export PDF / Markdown / JSON + Mode Pro
# ============================================================

import json
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
import textwrap

# ============================================================
# 1. FORMATS D’EXPORT
# ============================================================

def export_as_json(tirage_dict, output_path):
    """
    Sauvegarde un tirage au format JSON.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(tirage_dict, f, indent=4, ensure_ascii=False)
    return output_path


def export_as_markdown(tirage_dict, output_path):
    """
    Sauvegarde un tirage format texte / Markdown.
    """
    md = f"# 🔮 Tirage divinatoire\n"
    md += f"**Date :** {tirage_dict.get('datetime')}\n\n"

    if tirage_dict.get("consultant"):
        md += f"**Consultant :** {tirage_dict['consultant']}\n\n"

    if tirage_dict.get("question"):
        md += f"**Intention :** _{tirage_dict['question']}_\n\n"

    md += f"## Mode : {tirage_dict.get('mode')}\n\n"

    for i, c in enumerate(tirage_dict.get("cards", []), start=1):
        md += f"### Carte {i} — {c['nom']}\n"
        md += f"- Famille : {c['famille']}\n"
        md += f"- Message : {c['message']}\n"
        md += f"- Axe : {c['axe']}\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

    return output_path


# ============================================================
# 2. PDF PROFESSIONNEL (ReportLab)
# ============================================================

def export_as_pdf(tirage_dict, output_path):
    """
    Génère un PDF professionnel.
    Style clair, propre, pour consultations ou archives.
    """

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    normal = styles["Normal"]

    story = []

    # Titre
    story.append(Paragraph("🔮 Tirage divinatoire", title_style))
    story.append(Spacer(1, 0.5 * cm))

    # Métadonnées
    meta = f"""
    <b>Date :</b> {tirage_dict.get('datetime')}<br/>
    <b>Mode :</b> {tirage_dict.get('mode')}<br/>
    """

    if tirage_dict.get("consultant"):
        meta += f"<b>Consultant :</b> {tirage_dict['consultant']}<br/>"

    if tirage_dict.get("question"):
        meta += f"<b>Intention :</b> {tirage_dict['question']}<br/>"

    story.append(Paragraph(meta, normal))
    story.append(Spacer(1, 0.5 * cm))

    # Cartes
    for i, c in enumerate(tirage_dict.get("cards", []), start=1):
        title = f"<b>Carte {i} — {c['nom']}</b>"
        story.append(Paragraph(title, normal))
        story.append(Spacer(1, 0.1 * cm))

        txt = f"""
        <b>Famille :</b> {c['famille']}<br/>
        <b>Message :</b> {c['message']}<br/>
        <b>Axe :</b> {c['axe']}<br/>
        """
        story.append(Paragraph(txt, normal))
        story.append(Spacer(1, 0.3 * cm))

    # Hexagrammes (I Ching)
    if tirage_dict.get("hexagram"):
        h = tirage_dict["hexagram"]
        story.append(Paragraph("<b>Hexagramme principal</b>", normal))
        story.append(Paragraph(f"{h['id']:02d} — {h['nom']}", normal))
        story.append(Spacer(1, 0.4 * cm))

    if tirage_dict.get("hexagram_changed"):
        h2 = tirage_dict["hexagram_changed"]
        story.append(Paragraph("<b>Hexagramme de mutation</b>", normal))
        story.append(Paragraph(f"{h2['id']:02d} — {h2['nom']}", normal))
        story.append(Spacer(1, 0.4 * cm))

    if tirage_dict.get("hexagram_nuclear"):
        h3 = tirage_dict["hexagram_nuclear"]
        story.append(Paragraph("<b>Hexagramme nucléaire</b>", normal))
        story.append(Paragraph(f"{h3['id']:02d} — {h3['nom']}", normal))
        story.append(Spacer(1, 0.4 * cm))

    if tirage_dict.get("hexagram_complement"):
        h4 = tirage_dict["hexagram_complement"]
        story.append(Paragraph("<b>Hexagramme complémentaire</b>", normal))
        story.append(Paragraph(f"{h4['id']:02d} — {h4['nom']}", normal))
        story.append(Spacer(1, 0.4 * cm))

    # Totems
    if tirage_dict.get("totems"):
        story.append(Paragraph("<b>Animaux totems</b>", normal))
        for t in tirage_dict["totems"]:
            story.append(Paragraph(f"- {t['nom']} ({t['origine']})", normal))
        story.append(Spacer(1, 0.4 * cm))

    # Signature Pro
    if tirage_dict.get("consultant"):
        story.append(Spacer(1, 1 * cm))
        signature = f"""
        <i>Consultation réalisée par :</i><br/>
        <b>{tirage_dict.get('consultant')}</b>
        """
        story.append(Paragraph(signature, normal))

    # Création du PDF
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    doc.build(story)
    return output_path


# ============================================================
# 3. MODE PRO : STRUCTURE DU TIRAGE
# ============================================================

def build_tirage_dict(
    mode,
    cards=None,
    question=None,
    consultant=None,
    hexagram=None,
    hexagram_changed=None,
    hexagram_nuclear=None,
    hexagram_complement=None,
    totems=None,
):
    """
    Prépare un tirage complet à exporter.
    """
    return {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mode": mode,
        "cards": cards or [],
        "question": question or "",
        "consultant": consultant or "",
        "hexagram": hexagram,
        "hexagram_changed": hexagram_changed,
        "hexagram_nuclear": hexagram_nuclear,
        "hexagram_complement": hexagram_complement,
        "totems": totems or [],
    }
# ============================================================
# 📦 bloc_9.py — Moteur d’interprétation automatique
# ============================================================

import textwrap

# ============================================================
# 1. INTERPRÉTATION POUR ORACLE / PĀLI / TOTEMS / RUNES
# ============================================================

def interpret_basic_card(card):
    """
    Produit une interprétation simple (3 phrases)
    pour une carte type Oracle / Totem / Pāli / Rune.
    """

    nom = card.get("nom")
    message = card.get("message", "")
    axe = card.get("axe", "")
    famille = card.get("famille", "")

    return textwrap.dedent(f"""
    **{nom} — Interprétation**

    - Cette carte parle avant tout de : **{message}**.
    - Elle touche le domaine : **{famille.lower()}**.
    - L'axe de guidance te propose : **{axe}**.

    **Lecture intuitive :**
    Cette carte pointe une dynamique active en toi : quelque chose cherche
    à s’ouvrir, à se libérer ou à être entendu. Le message invite à regarder
    ce que tu ressens réellement et à agir depuis un espace plus aligné.
    """)


def interpret_basic_rune(rune):
    """
    Interprétation compacte des runes (modèle générique).
    """

    return textwrap.dedent(f"""
    **Rune {rune['rune']} — {rune['nom']}**

    - Message essentiel : {rune['message']}
    - Domaine : {rune['domaine']}

    **Lecture intuitive :**
    Cette rune indique un mouvement direct. Elle t’encourage à regarder
    la vérité des choses, à t’appuyer sur ta force intérieure et à accepter
    la transformation en cours.
    """)


def interpret_totem(animal):
    """
    Interprétation intuitive d’un animal totem.
    """

    return textwrap.dedent(f"""
    **{animal['nom']} — Totem {animal['origine']}**

    - Message : {animal['message']}
    - Médecine : {animal['medecine']}

    **Lecture intuitive :**
    Cet animal t’accompagne pour équilibrer ton énergie, renforcer ton
    instinct juste et t’aider à traverser une étape particulière. Sa médecine
    agit comme une protection et comme une impulsion intérieure.
    """)


# ============================================================
# 2. INTERPRÉTATION I CHING (méthode traditionnelle)
# ============================================================

def interpret_hexagram(hexagram):
    """
    Produit une interprétation courte + longue
    d’un hexagramme du I Ching.
    hexagram = { "id": 12, "nom": "...", "jugement": "...", "image": "..." }
    """

    out = f"""
    ## Hexagramme {hexagram['id']:02d} — {hexagram['nom']}

    ### 🧿 Jugement
    {hexagram.get('jugement', '—')}

    ### 🌄 Image
    {hexagram.get('image', '—')}

    ### 🔍 Synthèse intuitive
    L’hexagramme décrit une dynamique précise : une transformation en cours,
    une attitude intérieure, une tension à résoudre ou une ouverture à saisir.
    Observe ce qui résonne le plus dans le jugement et l’image — c’est là que
    se situe le message central pour ta situation actuelle.
    """

    return textwrap.dedent(out)


def interpret_full_iching(bundle, hex_db):
    """
    bundle = {
       'id', 'traits',
       'id_mutants', 'mutants',
       'id_nuclear', 'nuclear',
       'id_complementary', 'complementary'
    }
    hex_db : dictionnaire/array des 64 hexagrammes
    """

    H = hex_db[bundle["id"] - 1]
    HM = hex_db[bundle["id_mutants"] - 1]
    HN = hex_db[bundle["id_nuclear"] - 1]
    HC = hex_db[bundle["id_complementary"] - 1]

    txt = f"""
    # ☯ Lecture complète du I Ching

    ## 🧿 Hexagramme principal : {H['id']:02d} — {H['nom']}
    {H.get('jugement', '')}

    ## 🔁 Hexagramme de mutation : {HM['id']:02d} — {HM['nom']}
    {HM.get('jugement', '')}

    ## 🧬 Hexagramme nucléaire : {HN['id']:02d} — {HN['nom']}
    {HN.get('jugement', '')}

    ## 🌗 Hexagramme complémentaire : {HC['id']:02d} — {HC['nom']}
    {HC.get('jugement', '')}

    ---

    ## 💠 Synthèse intuitive

    - **Hexagramme principal** : décrit la situation présente.
    - **Hexagramme de mutation** : montre ce qui change ou veut changer.
    - **Noyau nucléaire** : révèle l’énergie profonde de la situation.
    - **Complémentaire** : montre l’équilibre recherché.

    L’ensemble forme un arc narratif : origine → transformation → essence → polarité.
    """

    return textwrap.dedent(txt)


# ============================================================
# 3. SYNTHÈSE COMPLÈTE (multi-systèmes)
# ============================================================

def synthese_globale(elements):
    """
    elements = {
        "oracles": [...],
        "runes": [...],
        "iching": bundle,
        "totems": [...],
    }

    Retourne une synthèse transversale.
    """

    blocs = []

    if elements.get("oracles"):
        noms = [c["nom"] for c in elements["oracles"]]
        blocs.append(f"🔮 **Cartes clés :** {', '.join(noms)}")

    if elements.get("runes"):
        noms = [r["nom"] for r in elements["runes"]]
        blocs.append(f"ᚱ **Runes :** {', '.join(noms)}")

    if elements.get("totems"):
        noms = [t["nom"] for t in elements["totems"]]
        blocs.append(f"🐾 **Totems :** {', '.join(noms)}")

    if elements.get("iching"):
        blocs.append(
            f"☯ **I Ching :** Hex. {elements['iching']['id']:02d}"
        )

    if not blocs:
        return "Aucune donnée à interpréter."

    # Synthèse intuitive
    interpretation = textwrap.dedent("""
    ### 🧩 Synthèse intuitive

    Plusieurs symboles convergent : ils révèlent un mouvement intérieur,
    une direction potentielle et un défi à dépasser. Observe où se trouvent
    les résonances entre les systèmes : c’est là que se trouve le cœur du message.

    """)
    return "\n".join(blocs) + "\n\n" + interpretation
# ============================================================
# 📦 bloc_10.py — Module Mobile / PWA / Responsive
# ============================================================

import streamlit as st
import re

# ============================================================
# 1. Détection Mobile (User-Agent)
# ============================================================

def is_mobile():
    """
    Détecte si l’utilisateur est sur mobile.
    Utilisé dans bloc_5 pour changer le layout.
    """
    ua = st.session_state.get("user_agent", "")
    if not ua and "HTTP_USER_AGENT" in st.session_state:
        ua = st.session_state["HTTP_USER_AGENT"]

    if not ua:
        try:
            ua = st.context.headers.get("User-Agent", "")
        except Exception:
            ua = ""

    mobile_regex = re.compile(r"(iphone|android|mobile|ipad|tablet)", re.I)
    return bool(mobile_regex.search(ua))


# ============================================================
# 2. CSS Responsive (Mobile + Desktop)
# ============================================================

def inject_responsive_css():
    """
    Injecte un CSS global compatible desktop + mobile.
    À appeler au début de l'app (dans bloc_5).
    """

    st.markdown("""
    <style>

    /* GLOBAL */
    body {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* MOBILE CARD GRID */
    @media (max-width: 640px) {
        .flip-card {
            width: 100% !important;
            margin-bottom: 1rem;
        }

        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }

        h1, h2, h3 {
            font-size: 1.1rem !important;
        }

        .stButton > button {
            width: 100%;
            padding: 0.8rem 1rem;
            font-size: 1.1rem;
        }
    }

    /* DESKTOP */
    @media (min-width: 641px) {
        .flip-card {
            max-width: 380px;
        }
    }

    /* BOTTOM NAV MOBILE */
    #mobile-bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(20,20,20,0.92);
        backdrop-filter: blur(8px);
        padding: 0.6rem 1rem;
        display: flex;
        justify-content: space-around;
        z-index: 99998;
        border-top: 1px solid rgba(255,255,255,0.15);
    }
    #mobile-bottom-nav a {
        color: white;
        text-decoration: none;
        font-size: 1.1rem;
    }

    </style>
    """, unsafe_allow_html=True)


# ============================================================
# 3. Mobile Bottom Bar
# ============================================================

def mobile_bottom_nav():
    """
    Barre de navigation en bas de l'écran (mobile).
    Appeler dans bloc_5 si mobile détecté.
    """

    st.markdown("""
    <div id="mobile-bottom-nav">
        <a href="#tirage">🔮</a>
        <a href="#method">📘</a>
        <a href="#cartes">🃏</a>
        <a href="#apropos">ℹ️</a>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 4. PWA Manifest
# ============================================================

def inject_manifest():
    """
    Injecte un manifest.json invisible (Streamlit).
    Compatible avec l’installation “Ajouter à l’écran d’accueil”.
    """

    st.markdown("""
    <link rel="manifest" href="manifest.json">
    """, unsafe_allow_html=True)

    # Le manifest doit être généré dans bloc_10
    manifest = {
        "name": "Oracle Multisystème",
        "short_name": "Oracle",
        "start_url": "/",
        "display": "standalone",
        "theme_color": "#222222",
        "background_color": "#111111",
        "icons": [
            {
                "src": "/favicon.png",
                "sizes": "192x192",
                "type": "image/png"
            }
        ]
    }

    # Écrire manifest
    with open("manifest.json", "w", encoding="utf-8") as f:
        import json
        json.dump(manifest, f, ensure_ascii=False, indent=4)


# ============================================================
# 5. Service Worker (PWA offline)
# ============================================================

def inject_service_worker():
    """
    Met en place un service worker (offline + installation PWA).
    """

    sw_script = """
    self.addEventListener('install', (event) => {
        self.skipWaiting();
    });

    self.addEventListener('activate', (event) => {
        clients.claim();
    });

    self.addEventListener('fetch', (event) => {
        event.respondWith(fetch(event.request));
    });
    """

    with open("serviceworker.js", "w") as f:
        f.write(sw_script)

    st.markdown("""
    <script>
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/serviceworker.js');
    }
    </script>
    """, unsafe_allow_html=True)


# ============================================================
# 6. Wrapper d’activation complet (mobile + PWA)
# ============================================================

def enable_mobile_pwa_mode():
    """
    Appeler au début de l'app :
        enable_mobile_pwa_mode()
    """

    inject_responsive_css()
    inject_manifest()
    inject_service_worker()

    if is_mobile():
        mobile_bottom_nav()
