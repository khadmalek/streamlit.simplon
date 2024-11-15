import streamlit as st
import json

# Chemin du fichier JSON
json_file = 'questions.json'
questions = []

# Charger les questions existantes si le fichier existe
with open(json_file, "r") as f:
        questions = json.load(f)



st.title("QUIZ INTERACTIF")

# Initialiser les variables d'état de la session si elles n'existent pas
if "user_answers" not in st.session_state:
    st.session_state['user_answers'] = []  
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0
if 'score' not in st.session_state:
    st.session_state['score'] = 0

if not questions:
    st.warning("Aucune question disponible. Ajoutez des questions dans la page de création.")

else:    # Si toutes les questions sont répondues
    if st.session_state['current_question'] == len(questions):
        st.title("Quiz terminé !")
        st.write(f"Votre score final : {st.session_state.score} / {len(questions)}")
        st.write("Voici vos réponses :")
        
    
     
        for index, (question, user_answer) in enumerate(zip(questions, st.session_state['user_answers'])):
            st.write(f"**Question {index + 1}** : {question['question']}")
            st.write(f"Votre réponse : {user_answer}")
            st.write(f"Réponse correcte : {question['correct_answer']}")
            st.write("---")
            
            # Réinitialiser le quiz
        if st.button("Recommencer"):
            st.session_state['current_question'] = 0
            st.session_state['score'] = 0
            st.session_state['user_answers'] = []
            st.rerun()

        if st.session_state['score'] >= len(questions) / 2:
            st.balloons() 
    else:
            # Afficher la question actuelle
        current_question = questions[st.session_state['current_question']]
        st.write(f"**Question {st.session_state['current_question'] + 1}/{len(questions)}**")
        st.write(current_question["question"])
            
            # Afficher les options sous forme de boutons radio
        user_choice = st.radio(
                "Choisissez une réponse :", 
        options=current_question["options"], 
        key=f"q{st.session_state['current_question']}"
        )
            
            # Bouton "Valider"
        if st.button("Valider la réponse"):
            st.session_state['user_answers'].append(user_choice)
                
                # Vérifier la réponse
            if user_choice == current_question["correct_answer"]:
                st.session_state['score'] += 1
                
                # Passer à la question suivante
            st.session_state['current_question'] += 1
            st.rerun()  
            