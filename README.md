# Application de Quiz Personnalisable

## Description

Cette application de quiz a été développée pour démontrer le potentiel de **Streamlit** dans la création d’outils interactifs et simples à utiliser. Elle permet de :
- Créer des quiz personnalisés avec des questions et réponses enregistrées dans un fichier JSON.
- Interagir avec un quiz en répondant aux questions une par une.
- Obtenir un récapitulatif des résultats avec des fonctionnalités supplémentaires optionnelles.

Ce projet a été réalisé dans un cadre pédagogique en deux jours.

---

## Fonctionnalités

### Fonctionnalités obligatoires

1. **Page de création de quiz** :
   - Ajout d’une question avec plusieurs réponses possibles.
   - Validation des questions et réponses via un modèle `Pydantic`.
   - Enregistrement des données dans un fichier JSON.

2. **Page de quiz interactif** :
   - Affichage des questions une par une.
   - Enregistrement des réponses sélectionnées par l’utilisateur.
   - Écran final récapitulatif avec :
     - Le nombre de bonnes réponses.
     - Un bouton pour réinitialiser le quiz et recommencer.

---

## Technologies utilisées

- **Python** : Langage principal pour le développement.
- **Streamlit** : Framework utilisé pour créer l’interface utilisateur interactive.
- **Pydantic** : Utilisé pour valider les questions et réponses avant leur enregistrement.

---

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone <git@github.com:khadmalek/streamlit.simplon.git>
 
