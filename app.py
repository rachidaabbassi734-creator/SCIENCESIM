# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="ScienceSim - Le Choc Cognitif", layout="centered")

st.title("🔬 ScienceSim : Mission Rupture Pédagogique")
st.write("## Défi : L'énigme du panneau publicitaire suspendu")

# 1. INITIALISATION DES ÉTAPES DE PROGRESSION
# L'élève commence à l'étape 1 et ne progresse que s'il réussit
if "etape_jeu" not in st.session_state:
    st.session_state.etape_jeu = 1
if "erreur_declenchee" not in st.session_state:
    st.session_state.erreur_declenchee = False

# Fonction pour réinitialiser le jeu
def reinitialiser():
    st.session_state.etape_jeu = 1
    st.session_state.erreur_declenchee = False

# Barre latérale de suivi
with st.sidebar:
    st.header("📋 Progression")
    st.write(f"**Étape actuelle :** {st.session_state.etape_jeu} / 3")
    if st.button("Recommencer le défi"):
        reinitialiser()
        st.rerun()

# --- ÉTAPE 1 : ÉMERGENCE DE LA REPRÉSENTATION (Le Piège) ---
if st.session_state.etape_jeu == 1:
    st.subheader("🎯 Étape 1 : Testez votre intuition")
    st.info("💡 **Situation :** Un panneau publicitaire lourd est suspendu au milieu d'un câble d'acier bien tendu entre deux poteaux. Le panneau est parfaitement immobile au milieu de l'air.")
    
    st.write("🤔 **D'après toi, combien de forces s'exercent au total sur ce panneau pour qu'il reste ainsi suspendu sans bouger ?**")
    
    choix_1 = st.radio(
        "Sélectionnez votre réponse :",
        [
            "Aucune force. S'il ne bouge pas, c'est que les forces s'annulent ou n'existent pas.",
            "Une seule force : celle du câble qui le tire vers le haut.",
            "Trois forces : la Terre qui l'attire vers le bas (Poids), et les deux côtés du câble qui le tirent."
        ],
        key="radio_etape_1"
    )
    
    if st.button("Valider l'Étape 1"):
        if choix_1 == "Trois forces : la Terre qui l'attire vers le bas (Poids), et les deux côtés du câble qui le tirent.":
            st.success("🎉 Incroyable ! Tu as une excellente intuition scientifique. Tu as vu les forces invisibles.")
            st.session_state.etape_jeu = 2
            st.session_state.erreur_declenchee = False
            st.rerun()
        else:
            # On active le mode conflit cognitif
            st.session_state.erreur_declenchee = True

    # Déclenchement du conflit cognitif si l'élève s'est trompé
    if st.session_state.erreur_declenchee:
        st.error("💥 **CONFLIT COGNITIF DÉCLENCHÉ !** Votre intuition vient d'échouer.")
        st.markdown("""
        **Pourquoi c'est faux ?** * Si tu penses qu'il n'y a *aucune force*, le panneau devrait tomber par terre à cause de la gravité ! 
        * Si tu penses qu'il n'y a qu'*une seule force vers le haut*, qu'arrive-t-il si on coupe le câble du côté gauche ? Le panneau va glisser et tomber vers la droite ! 
        
        👉 **Pour passer à l'étape suivante, vous devez admettre que le panneau subit 3 forces simultanées (Le Poids + l'action du câble Gauche + l'action du câble Droite) ! Modifiez votre choix pour débloquer le jeu.**
        """)

# --- ÉTAPE 2 : LA CONFRONTATION GÉOMÉTRIQUE ---
elif st.session_state.etape_jeu == 2:
    st.subheader("🎯 Étape 2 : L'Équilibre des Forces")
    st.info("Le panneau subit l'action de deux forces horizontales opposées exercées par le câble (F1 à gauche et F2 à droite). Pour que le panneau ne bouge pas du tout, quelle condition fondamentale doivent vérifier ces forces ?")
    
    choix_2 = st.selectbox(
        "Choisissez la règle géométrique exacte :",
        [
            "La force de droite doit être un peu plus forte pour compenser le vent.",
            "Les deux forces doivent avoir strictement la même intensité, des sens opposés et la même droite d'action.",
            "Les forces n'ont pas besoin d'être alignées."
        ],
        key="select_etape_2"
    )
    
    if st.button("Valider l'Étape 2"):
        if choix_2 == "Les deux forces doivent avoir strictement la même intensité, des sens opposés et la même droite d'action.":
            st.success("🎉 Parfait ! C'est la loi mathématique de l'équilibre sous deux forces.")
            st.session_state.etape_jeu = 3
            st.rerun()
        else:
            st.error("❌ Erreur géométrique ! Si l'une des forces change d'axe ou d'intensité, le panneau va entrer en mouvement ou pivoter. Réessayez !")

# --- ÉTAPE 3 : LA MODÉLISATION VECTORIELLE FINALE ---
elif st.session_state.etape_jeu == 3:
    st.subheader("🎯 Étape 3 : La traduction mathématique (Modèle APC)")
    st.info("Dernière étape pour valider votre compétence. Comment les physiciens traduisent-ils graphiquement et mathématiquement cet état de compensation complète ?")
    
    # Simulation graphique dynamique avec Matplotlib
    fig, ax = plt.subplots(figsize=(5, 1.5))
    ax.plot(0, 0, 's', color='#2c3e50', markersize=25) # Le panneau
    ax.quiver(0, 0, -3, 0, angles='xy', scale_units='xy', scale=1, color='#e74c3c', label="F1 (Gauche)")
    ax.quiver(0, 0, 3, 0, angles='xy', scale_units='xy', scale=1, color='#2ecc71', label="F2 (Droite)")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    st.pyplot(fig)
    
    choix_3 = st.radio(
        "Quelle est l'égalité vectorielle correcte ?",
        ["F1 - F2 = 1", "F1 + F2 = 0 (Vecteur nul)", "F1 x F2 = F_total"],
        key="radio_etape_3"
    )
    
    if st.button("Terminer le Défi"):
        if choix_3 == "F1 + F2 = 0 (Vecteur nul)":
            st.balloons()
            st.success("🏆 Félicitations ! Vous avez surmonté le conflit cognitif et validé le module de Mécanique !")
            
            # Message de monétisation (Madkhoul)
            st.markdown("""
            ---
            ### 🔓 Envie d'aller plus loin ?
            Ce module interactif fait partie de la suite **ScienceSim Premium**. Pour débloquer les 12 autres situations-problèmes du programme officiel avec suivi personnalisé, achetez votre clé de licence !
            """)
        else:
            st.error("❌ Non ! Rappelez-vous que les vecteurs s'annulent lorsqu'ils sont opposés et de même longueur. La somme doit être nulle.")
