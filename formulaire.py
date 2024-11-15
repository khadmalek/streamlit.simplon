import streamlit as st
import json


# Chemin du fichier JSON
json_file = "questions.json"

questions = []

# Interface de création de quiz
st.title("CRÉER UN QUIZ")
st.image("./img.png")

question_text = st.text_input("Entrez la question")
option_1 = st.text_input("Option 1")
option_2 = st.text_input("Option 2")
option_3 = st.text_input("Option 3")
option_4 = st.text_input("Option 4")
correct_answer = st.selectbox("Sélectionnez la bonne réponse", [option_1, option_2, option_3, option_4])

if st.button("Ajouter la question"):
    if question_text and option_1 and option_2 and option_3 and option_4:
        new_question = {
            "question": question_text,
            "options": [option_1, option_2, option_3, option_4],
            "correct_answer": correct_answer
        }
        
        with open(json_file, "r") as f:
            if f.read() : 
                f.seek(0)
                donnees = json.load(f)
                donnees.append(new_question)
                questions = donnees
            else : 
                questions.append(new_question)

        # Sauvegarde dans le fichier JSON
        with open(json_file, "w") as f:
            json.dump(questions, f, indent=4)

        st.success("Question ajoutée avec succès!")
    else:
        st.error("Veuillez remplir tous les champs")
