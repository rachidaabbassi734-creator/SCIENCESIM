import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Configuration de la page en mode large
st.set_page_config(page_title="ScienceSim - Mission Loi d'Ohm", layout="wide")

# Gestion de la progression du jeu (State Management)
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("🎮 Mission Phénoménologique : Sauvez le Système Hydraulique & Électrique")
st.write(f"🏆 **Score actuel :** {st.session_state.score} points | 🕹️ **Niveau :** {st.session_state.level} / 3")

st.markdown("---")

# ----------------- FONCTION VISUELLE DE SIMULATION -----------------
def draw_simulation(U_val, R_val, I_val, highlight_type):
    fig, ax = plt.subplots(figsize=(7, 3))
    pipe_thickness = max(0.3, 2.0 - (R_val / 10.0))
    
    # Dessin du tuyau hydraulique
    ax.add_patch(patches.Rectangle((0, 1), 3, 2, color='lightblue', alpha=0.4))
    ax.add_patch(patches.Rectangle((3, 2 - pipe_thickness/2), 2, pipe_thickness, color='skyblue', alpha=0.8))
    ax.add_patch(patches.Rectangle((5, 1), 3, 2, color='lightblue', alpha=0.4))
    
    ax.plot([0, 3, 5, 8], [1, 2 - pipe_thickness/2, 2 - pipe_thickness/2, 1], color='black', lw=3)
    ax.plot([0, 3, 5, 8], [3, 2 + pipe_thickness/2, 2 + pipe_thickness/2, 3], color='black', lw=3)
    
    # Molécules d'eau (Courant résultant)
    num_particles = int(I_val * 12)
    np.random.seed(42)
    x_p = np.random.uniform(0.5, 7.5, num_particles)
    y_p = np.random.uniform(1.2, 2.8, num_particles)
    y_p = np.where((x_p >= 3) & (x_p <= 5), np.random.uniform(2 - pipe_thickness/2 + 0.1, 2 + pipe_thickness/2 - 0.1, num_particles), y_p)
    
    ax.scatter(x_p, y_p, color='blue', s=40, alpha=0.6)
    
    # Flèche représentant la force de poussée
    arrow_len = min(2.5, U_val / 8)
    ax.arrow(0.3, 2, arrow_len, 0, head_width=0.15, head_length=0.15, fc='red', ec='red', lw=4)
    
    # Textes descriptifs phénoménologiques
    if highlight_type == "push":
        ax.text(1.5, 3.2, f"Force de Poussee : {U_val:.1f}", color='red', weight='bold', ha='center')
    elif highlight_type == "block":
        ax.text(4, 2.9 + pipe_thickness/2, f"Etranglement (Obstacle)", color='brown', weight='bold', ha='center')
    
    ax.text(6.5, 3.2, f"Debit de l'eau : {I_val:.2f}", color='blue', weight='bold', ha='center')
    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4)
    ax.axis('off')
    return fig

# ----------------- NIVEAUX DU JEU -----------------

# NIVEAU 1
if st.session_state.level == 1:
    st.subheader("🕹️ Niveau 1 : Le mystere de l'eau immobile")
    st.info("💡 **Constat Phenomenologique :** L'eau ne bouge pas dans le tuyau car il n'y a aucune force pour la pousser. La lampe est eteinte !")
    st.warning("🎯 **Votre Mission :** Augmentez la 'Force de Poussere' pour que le debit de l'eau depasse 2.5 afin d'allumer la lampe.")
    
    push_force = st.slider("🔴 Ajuster la Force de Poussee (Tension electrique U) :", min_value=0.0, max_value=20.0, value=2.0, step=0.5)
    fixed_resistance = 4.0
    resulting_current = push_force / fixed_resistance
    
    st.pyplot(draw_simulation(push_force, fixed_resistance, resulting_current, "push"))
    
    if resulting_current >= 2.5:
        st.success("🎉 Bravo ! La force est suffisante, l'eau s'ecoule et la lampe s'allume !")
        if st.button("Passer au Niveau 2 ➡️"):
            st.session_state.score += 50
            st.session_state.level = 2
            st.rerun()

# NIVEAU 2
elif st.session_state.level == 2:
    st.subheader("🕹️ Niveau 2 : Alerte a l'inondation")
    st.info("💡 **Constat Phenomenologique :** La pompe est bloquee a puissance maximale ! Le debit est trop dangereux !")
    st.warning("🎯 **Votre Mission :** Creez un 'Etranglement' (Obstacle) pour freiner l'eau et stabiliser le debit entre 1.0 et 1.8.")
    
    fixed_push = 18.0
    block_force = st.slider("🟤 Serrer l'etranglement du tuyau (Resistance R) :", min_value=1.0, max_value=20.0, value=2.0
