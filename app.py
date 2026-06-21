# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuration de la page TICE
st.set_page_config(page_title="ScienceSim - Jeu Interactif", layout="centered")

# Initialisation des variables de session (Score et Progression)
if "score" not in st.session_state:
    st.session_state.score = 0
if "defi_etape" not in st.session_state:
    st.session_state.defi_etape = 1
if "jeu_termine" not in st.session_state:
    st.session_state.jeu_termine = False

# En-tête de l'application
st.title("🔬 ScienceSim : Le Défi de l'Équilibre")
st.write("Bienvenue Professeur ! Voici la version de simulation scénarisée sous forme de jeu.")

# Fonction pour réinitialiser le jeu
def recommencer():
    st.session_state.score = 0
    st.session_state.defi_etape = 1
    st.session_state.jeu_termine = False

# Barre latérale : Tableau de bord de l'élève
with st.sidebar:
    st.header("🏆 Tableau de Bord")
    st.metric(label="Score Actuel", value=f"{st.session_state.score} pts")
    st.metric(label="Mission en cours", value=f"Étape {st.session_state.defi_etape} / 3")
    if st.button("Réinitialiser la partie"):
        recommencer()

# LOGIQUE DU JEU & DES MISSIONS
if not st.session_state.jeu_termine:
    
    if st.session_state.defi_etape == 1:
        st.subheader("🎯 Mission 1 : La Règle de l'Intensité Égale")
        st.info("Consigne : Un solide est tiré vers la gauche par un dynamomètre D1 avec une force F1 = 4 N. Ajustez la force F2 du dynamomètre D2 (vers la droite) pour maintenir le système en parfait équilibre !")
        
        # Commande interactive (Curseur)
        f1 = 4.0
        f2 = st.slider("Ajustez l'intensité de la Force F2 (en Newtons) :", min_value=0.0, max_value=8.0, value=1.0, step=0.5)
        
        # Génération de la simulation graphique
        fig, ax = plt.subplots(figsize=(6, 2))
        ax.axhline(0, color='#7f8c8d', linestyle='--')
        # Dessin du solide au centre
        ax.plot(0, 0, 's', color='#e67e22', markersize=20, label="Solide")
        # Vecteurs forces
        ax.quiver(0, 0, -f1, 0, angles='xy', scale_units='xy', scale=1, color='#e74c3c', label="F1 (Gauche)")
        ax.quiver(0, 0, f2, 0, angles='xy', scale_units='xy', scale=1, color='#2cecc71' if f1==f2 else '#3498db', label="F2 (Droite)")
        
        ax.set_xlim(-6, 6)
        ax.set_ylim(-1, 1)
        ax.axis('off')
        st.pyplot(fig)
        
        # Validation du défi
        if st.button("Valider l'équilibre"):
            if f2 == f1:
                st.success("🎉 Excellent ! Les deux forces ont la même intensité, le solide reste immobile.")
                st.session_state.score += 10
                st.session_state.defi_etape = 2
                st.rerun()
            else:
                st.error("❌ Échec de l'équilibre ! Le solide se déplace du côté de la force la plus intense. Réessayez !")

    elif st.session_state.defi_etape == 2:
        st.subheader("🎯 Mission 2 : Le Piège de la Droite d'Action")
        st.info("Consigne : Pour que le solide soit en équilibre, la géométrie des forces est cruciale. Choisissez la bonne configuration pour la droite d'action :")
        
        choix_geometrie = rel_choix = st.radio(
            "Quelle condition géométrique doivent remplir les lignes d'action des deux forces ?",
            ["Elles doivent être parallèles mais décalées", "Elles doivent être perpendiculaires", "Elles doivent être confondues (Même droite d'action)", "Elles n'ont pas d'importance"]
        )
        
        if st.button("Soumettre la réponse"):
            if choix_geometrie == "Elles doivent être confondues (Même droite d'action)":
                st.success("🎉 Bravo ! C'est la condition de colinéarité essentielle pour éviter la rotation du solide.")
                st.session_state.score += 15
                st.session_state.defi_etape = 3
                st.rerun()
            else:
                st.error("❌ Mauvaise analyse. Si les droites d'action ne sont pas confondues, le solide va tourner ou pivoter.")

    elif st.session_state.defi_etape == 3:
        st.subheader("🎯 Mission 3 : L'Équation Vectorielle Finale")
        st.info("Consigne : Complétez la relation mathématique vectorielle qui caractérise l'état d'un corps en équilibre sous deux forces :")
        
        formule = st.selectbox("Sélectionnez la relation correcte :", ["F1 + F2 = 1", "F1 + F2 = 0 (Vecteur nul)", "F1 - F2 = 2", "F1 * F2 = 0"])
        
        if st.button("Finaliser le Défi"):
            if formule == "F1 + F2 = 0 (Vecteur nul)":
                st.success("🎉 Parfait ! C'est la loi de compensation des actions mécaniques.")
                st.session_state.score += 20
                st.session_state.jeu_termine = True
                st.rerun()
            else:
                st.error("❌ Faux. La somme vectorielle doit s'annuler pour maintenir l'immobilité complète.")

else:
    # Écran de fin de jeu (Idéal pour placer un appel à l'action Premium)
    st.balloons()
    st.subheader("🏁 Félicitations ! Vous avez terminé le module interactif.")
    st.write(f"Votre score final est de : **{st.session_state.score} points**.")
    
    # Stratégie de madkhoul / Monétisation visible à la fin
    st.markdown("""
    ---
    ### 🔓 Débloquez la suite de ScienceSim !
    Vous voulez accéder aux **15 autres simulations du programme officiel de Physique-Chimie (3ASC)** ainsi qu'aux fiches techniques téléchargeables au format PDF ?
    
    👉 **Passez à la version Premium !** Contactez l'administrateur pour obtenir votre code d'activation.
    """)
    
    if st.button("Rejouer"):
        recommencer()
        st.rerun()
