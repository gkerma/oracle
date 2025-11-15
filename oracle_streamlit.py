
import streamlit as st
import random
from datetime import datetime

# =========================
# Données de base de l'Oracle
# =========================

CYCLES = [
    "1. Germe 🌱 — quelque chose commence à peine",
    "2. Expansion 🚀 — l'énergie monte, tout s'ouvre",
    "3. Exploration 🧭 — tester, chercher, errer",
    "4. Friction ⚡ — résistance, tensions, ajustements",
    "5. Crise 🌪️ — point de bascule, fatigue, saturation",
    "6. Seuil 🕯️ — juste avant le changement",
    "7. Chute 🕳️ — lâcher-prise, effondrement, descente",
    "8. Gestation 🌚 — incubation, secret, travail invisible",
    "9. Métamorphose 🦋 — mutation profonde, reconfiguration",
    "10. Intégration 💎 — digérer, stabiliser, comprendre",
    "11. Partage 🔊 — offrir au monde, diffuser",
    "12. Repos 🌊 — pause, silence, régénération",
]

# Cartes inspirées de ton univers visuel
CARTES = [
    {
        "nom": "Le Champignon-Antenne",
        "symbole": "🍄📡",
        "mots_cles": ["réception", "sensibilité", "signaux cachés"],
        "message": "Tu captes plus de choses que tu ne l’admets. Note ce qui insiste au fond de toi.",
    },
    {
        "nom": "Le Gardien Ailé",
        "symbole": "👁️‍🗨️🪽",
        "mots_cles": ["veille", "intuition", "protection douce"],
        "message": "Une partie de toi veille déjà. Donne-lui la parole quelques instants.",
    },
    {
        "nom": "Le Labyrinthe Rouge",
        "symbole": "🌀🟥",
        "mots_cles": ["complexité", "détour", "cartographie"],
        "message": "Tu n’es pas perdu·e, tu es en train de dessiner la carte en avançant.",
    },
    {
        "nom": "La Goutte Suspendue",
        "symbole": "💧⏸️",
        "mots_cles": ["tension", "suspension", "juste avant"],
        "message": "Reste avec la question un peu plus longtemps avant d’agir.",
    },
    {
        "nom": "L’Horloge Fragmentée",
        "symbole": "⏰💥",
        "mots_cles": ["temps", "urgence", "priorités"],
        "message": "Ce n’est pas le temps qui manque, c’est la hiérarchie entre tes élans.",
    },
    {
        "nom": "Le Triangle de Lumière",
        "symbole": "🔺✨",
        "mots_cles": ["focus", "alignement", "choix"],
        "message": "Choisis une direction claire, même petite. Le reste pourra se réorganiser.",
    },
    {
        "nom": "La Pierre Silencieuse",
        "symbole": "🪨🤍",
        "mots_cles": ["ancrage", "corps", "gravité"],
        "message": "Reviens à ton corps : respiration, contact, lourdeur, appuis. Puis repose ta question.",
    },
    {
        "nom": "La Fumée Iridescente",
        "symbole": "🌫️🌈",
        "mots_cles": ["flou", "entre-deux", "liminal"],
        "message": "Tu traverses une zone de brume. Accepte de ne pas tout comprendre tout de suite.",
    },
    {
        "nom": "L’Œil dans le Triangle",
        "symbole": "🔺👁️",
        "mots_cles": ["conscience", "prise de recul", "vision"],
        "message": "Observe la scène depuis au-dessus. Que verrais-tu si tu n’étais pas au centre ?",
    },
    {
        "nom": "Le Cœur Prismatique",
        "symbole": "💖🔮",
        "mots_cles": ["désir", "vulnérabilité", "authenticité"],
        "message": "Qu’est-ce que tu veux vraiment, derrière le discours raisonnable ?",
    },
    {
        "nom": "Le Câblage Secret",
        "symbole": "🧷🧬",
        "mots_cles": ["back-end", "sous-jacent", "structures invisibles"],
        "message": "Regarde les structures sous la surface : habitudes, contrats, promesses implicites.",
    },
    {
        "nom": "La Porte Oblique",
        "symbole": "🚪📐",
        "mots_cles": ["accès indirect", "ruse", "contournement"],
        "message": "Si l’entrée principale est bloquée, où est l’accès latéral que tu refuses de voir ?",
    },
    {
        "nom": "Le Circuit Nocturne",
        "symbole": "🌒💾",
        "mots_cles": ["rêves", "inconscient", "traitement offline"],
        "message": "Laisse la nuit travailler pour toi. Tu n’as pas besoin de tout résoudre en journée.",
    },
    {
        "nom": "La Constellation Brisée",
        "symbole": "💫🧩",
        "mots_cles": ["morcellement", "recomposition", "puzzle"],
        "message": "Prends un seul morceau à la fois. L’image globale se révélera en avançant.",
    },
    {
        "nom": "Le Fil Rouge",
        "symbole": "🧵🔗",
        "mots_cles": ["cohérence", "lien", "narration"],
        "message": "Quelle est l’histoire commune derrière tous ces événements dispersés ?",
    },
]

def tirer_cycle():
    return random.choice(CYCLES)

def tirer_carte():
    return random.choice(CARTES)

# =========================
# Mise en page Streamlit
# =========================

st.set_page_config(
    page_title="Oracle du Labyrinthe des Cycles",
    page_icon="🌀",
    layout="centered",
)

# Sidebar navigation
st.sidebar.title("🌀 Oracle du Labyrinthe")
page = st.sidebar.radio(
    "Naviguer",
    (
        "🔮 Tirage",
        "ℹ️ À propos",
        "📘 Mode d’emploi",
        "🎴 Toutes les cartes",
    ),
)

st.sidebar.markdown("---")
st.sidebar.caption("Prototype WebUI — Streamlit")

# Initialiser l'historique si besoin
if "historique" not in st.session_state:
    st.session_state.historique = []

# =========================
# Page : Tirage
# =========================
if page == "🔮 Tirage":
    st.title("🔮 Tirage d'une carte de l’Oracle")
    st.markdown(
        """
Bienvenue dans l’espace de **tirage**.

> Ce n’est pas un test, ni un verdict.  
> Juste une conversation symbolique avec toi-même. ✨
"""
    )

    st.subheader("🧩 Ta question")

    question = st.text_area(
        "Formule une question (ou laisse vide pour un message libre du Labyrinthe) :",
        placeholder="Ex : De quoi ai-je besoin pour traverser cette période ?",
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        action = st.button("🎴 Tirer une carte maintenant")
    with col2:
        reset = st.button("🧹 Effacer l’historique")

    if reset:
        st.session_state.historique = []
        st.success("🧹 Historique effacé. Le Labyrinthe est de nouveau silencieux.")

    if action:
        carte = tirer_carte()
        cycle = tirer_cycle()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        tirage = {
            "question": question.strip() if question else "(question non précisée)",
            "carte": carte,
            "cycle": cycle,
            "timestamp": timestamp,
        }

        st.session_state.historique.insert(0, tirage)

    if st.session_state.historique:
        dernier = st.session_state.historique[0]

        st.subheader("🪄 Dernier tirage")

        st.markdown(f"**🕒 Date** : `{dernier['timestamp']}`")
        st.markdown(f"**❔ Question** : _{dernier['question']}_")
        st.markdown("---")

        st.markdown(f"### {dernier['carte']['symbole']} {dernier['carte']['nom']}")
        st.markdown(
            "🌟 **Mots-clés** : " + ", ".join(dernier["carte"]["mots_cles"])
        )
        st.markdown(f"🔁 **Cycle associé** : {dernier['cycle']}")
        st.markdown("")
        st.markdown(f"💬 **Message de l’Oracle** : {dernier['carte']['message']}")

        st.info(
            "Lis ce tirage comme tu lis un rêve ou une métaphore : "
            "tu peux en garder des morceaux, en laisser d’autres, y revenir plus tard."
        )

        with st.expander("📜 Voir l’historique des tirages"):
            for i, tirage in enumerate(st.session_state.historique):
                st.markdown(f"#### Tirage #{len(st.session_state.historique) - i}")
                st.markdown(f"- 🕒 **Date** : `{tirage['timestamp']}`")
                st.markdown(f"- ❔ **Question** : _{tirage['question']}_")
                st.markdown(
                    f"- 🎴 **Carte** : {tirage['carte']['symbole']} {tirage['carte']['nom']}"
                )
                st.markdown(f"- 🔁 **Cycle** : {tirage['cycle']}")
                st.markdown(
                    f"- 💬 **Message** : {tirage['carte']['message']}"
                )
                st.markdown("---")
    else:
        st.markdown("💭 Aucun tirage pour l’instant. Pose une question et tire une carte pour commencer.")

# =========================
# Page : À propos
# =========================
elif page == "ℹ️ À propos":
    st.title("ℹ️ À propos de l’Oracle du Labyrinthe des Cycles")

    st.markdown(
        """
**Oracle du Labyrinthe des Cycles** est une expérience entre :

- 🖼️ le dessin et l’imaginaire,
- 💾 l’électronique et le code,
- 🌌 l’intériorité et le rituel.

Ce n’est pas une machine pour prédire le futur,  
mais un **miroir augmenté** pour t’aider à voir où tu en es dans tes propres cycles. 🔮
"""
    )

    st.subheader("🌗 Les 12 cycles")
    for cycle in CYCLES:
        st.markdown(f"- {cycle}")

    st.subheader("🧙‍♂️ Le Gardien du Labyrinthe")
    st.markdown(
        """
Dans la légende de l’Oracle, le **Gardien** est une figure ailée perchée sur un dôme-champignon.  
Il ne donne pas d’ordres, il **veille** simplement :

- sur les questions qu’on ose poser,
- sur les symboles qui répondent,
- sur la qualité de l’attention qu’on porte à tout ça.

Il te rappelle que **l’interprétation finale t’appartient** toujours. ✋
"""
    )

    st.subheader("🎨 Esprit du projet")
    st.markdown(
        """
- Pas de fatalisme, pas de destin figé.  
- Pas d’autorité absolue : l’Oracle ne remplace pas ton discernement.  
- Co-création : tu peux enrichir les cartes, changer les mots, détourner les tirages.  

L’Oracle est pensé comme un **organisme vivant** qui évolue avec celles et ceux qui l’utilisent. 🌱
"""
    )

# =========================
# Page : Mode d’emploi
# =========================
elif page == "📘 Mode d’emploi":
    st.title("📘 Mode d’emploi")

    st.markdown(
        """
Ce mode d’emploi propose une manière de jouer avec l’Oracle.  
Tu es libre de l’adapter, le hacker, le détourner. 🛠️
"""
    )

    st.header("1️⃣ Préparer l’espace")
    st.markdown(
        """
- Choisis un moment où tu peux être un minimum tranquille.  
- Option idéal : cartes physiques, cercle des 12 cycles, pendule…  
- Version numérique : la WebUI suffit pour commencer.  

Prends un instant pour **respirer**, poser une intention, ou juste reconnaître que tu entres dans un temps différent. 🕯️
"""
    )

    st.header("2️⃣ Formuler une question")
    st.markdown(
        """
Quelques exemples :

- « De quoi ai-je besoin pour traverser cette période ? »  
- « Qu’est-ce qui cherche à changer dans ma situation actuelle ? »  
- ou simplement : « Quel message le Labyrinthe a pour moi aujourd’hui ? »

L’important n’est pas la perfection de la question, mais **ta sincérité**. 💖
"""
    )

    st.header("3️⃣ Tirer une carte")
    st.markdown(
        """
Dans cette interface :

1. Tu écris (ou pas) ta question.  
2. Tu cliques sur **« 🎴 Tirer une carte maintenant »**.  
3. Tu découvres la carte, le cycle associé et le message.

Lis d’abord avec le ventre et le cœur,  
le mental analysera plus tard. 😉
"""
    )

    st.header("4️⃣ Interpréter sans se piéger")
    st.markdown(
        """
Tu peux te demander :

- Qu’est-ce que cette carte touche en moi en premier ?  
- Est-ce que ça confirme quelque chose que je savais déjà, mais que j’évitais ?  
- Qu’est-ce que ça m’invite à ajuster dans ma façon d’agir ou de percevoir ?

Souviens-toi :  
> Tu as le droit de ne pas être d’accord avec l’Oracle,  
> de ne garder qu’un fragment du message,  
> ou d’y revenir plus tard.
"""
    )

    st.header("5️⃣ Clore le tirage")
    st.markdown(
        """
Pour clôturer :

- Remercie (toi, le symbole, le Gardien, peu importe).  
- Note éventuellement 2–3 mots dans un carnet.  
- Reviens à quelque chose de concret : boire un verre d’eau, marcher un peu, etc.

L’idée n’est pas de flotter hors du réel,  
mais de **revenir au réel avec un angle un peu différent**. 🌍
"""
    )

# =========================
# Page : Toutes les cartes
# =========================
elif page == "🎴 Toutes les cartes":
    st.title("🎴 Toutes les cartes de ce prototype")

    st.markdown(
        """
Voici les cartes actuellement disponibles dans cette version WebUI.  
Elles peuvent évoluer, être renommées, complétées, augmentées. ♻️
"""
    )

    for carte in CARTES:
        st.markdown(f"### {carte['symbole']} {carte['nom']}")
        st.markdown("**Mots-clés** : " + ", ".join(carte["mots_cles"]))
        st.markdown("**Message** : " + carte["message"])
        st.markdown("---")
