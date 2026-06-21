limport streamlit as st
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
        ax.text(1.5, 3.2, f"⬅️ Force de Poussée : {U_val:.1f}", color='red', weight='bold', ha='center')
    elif highlight_type == "block":
        ax.text(4, 2.9 + pipe_thickness/2, f"🚧 Étranglement (Obstacle)", color='brown', weight='bold', ha='center')
    
    ax.text(6.5, 3.2, f"🌊 Débit de l'eau : {I_val:.2f}", color='blue', weight='bold', ha='center')
    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4)
    ax.axis('off')
    return fig

# ----------------- NIVEAUX DU JEU -----------------

# NIVEAU 1 : Découverte du Courant et de la Tension
if st.session_state.level == 1:
    st.subheader("🕹️ Niveau 1 : Le mystère de l'eau immobile")
    st.info("💡 **Constat Phénoménologique :** L'eau ne bouge pas dans le tuyau car il n'y a aucune force pour la pousser. La lampe est éteinte !")
    st.warning("🎯 **Votre Mission :** Augmentez la 'Force de Poussée' pour que le débit de l'eau dépasse **2.5** afin d'allumer la lampe.")
    
    push_force = st.slider("🔴 Ajuster la Force de Poussée (Tension électrique U) :", min_value=0.0, max_value=20.0, value=2.0, step=0.5)
    fixed_resistance = 4.0  # Obstacle constant pour le niveau 1
    resulting_current = push_force / fixed_resistance
    
    st.pyplot(draw_simulation(push_force, fixed_resistance, resulting_current, "push"))
    
    if resulting_current >= 2.5:
        st.success("🎉 Bravo ! La force est suffisante, l'eau s'écoule et la lampe s'allume !")
        if st.button("Passer au Niveau 2 ➡️"):
            st.session_state.score += 50
            st.session_state.level = 2
            st.rerun()

# NIVEAU 2 : Découverte de la Résistance
elif st.session_state.level == 2:
    st.subheader("🕹️ Niveau 2 : Alerte à l'inondation (Le besoin de freiner)")
    st.info("💡 **Constat Phénoménologique :** La pompe est bloquée à puissance maximale ! Le débit est trop dangereux, les fils chauffent et la lampe risque de griller !")
    st.warning("🎯 **Votre Mission :** Créez un 'Étranglementength, 0, head_width=0.2, head_length=0.2, fc='red', ec='red', lw=4, label='...'
