# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="ScienceSim - Conflit Cognitif", layout="centered")

st.title("🔬 ScienceSim : Défi de l'Équilibre Caché")
st.write("### Objectif : Découvrir les forces invisibles.")

# Initialisation de l'état du fil
if "fil_coupe" not in st.session_state:
    st.session_state.fil_coupe = False

st.info("💡 **Situation :** Une bille en acier est suspendue à un fil, juste à côté d'un aimant. Elle reste immobile en l'air, attirée par l'aimant mais retenue par le fil.")

# Affichage visuel textuel (ou graphique si couplé à matplotlib)
if not st.session_state.fil_coupe:
    st.code("""
       [Support]
           |
           | (Fil tendu oblique)
           |
          (O)  <====== [ AIMANT ]
         Bille 
    """, language="text")
else:
    st.code("""
       [Support]
           |
           | (Fil lâche)
           
                 (O)[ AIMANT ]
                Bille collée !
    """, language="text")

# Question provocant la représentation initiale
reponse = st.radio(
    "À ton avis, si on coupe le fil, la bille va-t-elle rester immobile grâce à l'attraction de l'aimant ?",
    ["Oui, car l'aimant est très puissant et la maintient en l'air.", 
     "Non, car le fil exerçait une force invisible essentielle à l'équilibre."]
)

if st.button("Valider mon choix et tester"):
    if reponse == "Oui, car l'aimant est très puissant et la maintient en l'air.":
        st.session_state.fil_coupe = True
        st.error("💥 **Conflit cognitif déclenché !** Regarde la simulation au-dessus : la bille s'est immédiatement collée sur l'aimant ! Ton intuition a échoué. Pourquoi ? Parce que le fil n'était pas passif : il exerçait une force indispensable appelée la tension du fil.")
    else:
        st.success("🎉 Bravo ! Tu as évité le piège. Le fil exerce bien une action mécanique de tension. Sans lui, la somme des forces ne s'annule plus et l'équilibre est rompu.")

if st.session_state.fil_coupe:
    if st.button("Réinitialiser l'expérience"):
        st.session_state.fil_coupe = False
        st.init()
