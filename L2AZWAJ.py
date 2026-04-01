import streamlit as st
import random

# إعداد قائمة الأسئلة
if "questions" not in st.session_state:
    st.session_state.questions = [
        {
            "question": "En quelle année la Première Guerre mondiale a-t-elle commencé ?",
            "options": ["1912", "1914", "1916", "1918"],
            "answer": "1914"
        },
        {
            "question": "Quel événement a déclenché la guerre ?",
            "options": ["L'invasion de la Pologne", "L'assassinat de l'archiduc François-Ferdinand", "Le naufrage du Titanic", "La bataille de Verdun"],
            "answer": "L'assassinat de l'archiduc François-Ferdinand"
        },
        {
            "question": "Quel pays ne faisait PAS partie de la Triple-Entente ?",
            "options": ["La France", "Le Royaume-Uni", "L'Allemagne", "La Russie"],
            "answer": "L'Allemagne"
        },
        {
            "question": "Comment appelait-on les soldats français ?",
            "options": ["Les Gars", "Les Poilus", "Les Bleus", "Les Braves"],
            "answer": "Les Poilus"
        },
        {
            "question": "Quand l'armistice a-t-il été signé ?",
            "options": ["11 novembre 1918", "14 juillet 1919", "8 mai 1945", "1er septembre 1914"],
            "answer": "11 novembre 1918"
        }
    ]

if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "selected" not in st.session_state:
    st.session_state.selected = None

st.title("Quiz: La Première Guerre Mondiale")

# زر إضافة سؤال
with st.expander("➕ Ajouter une Question"):
    new_q = st.text_input("La question :")
    ans = st.text_input("Réponse correcte :")
    o2 = st.text_input("Fausse option 1 :")
    o3 = st.text_input("Fausse option 2 :")
    o4 = st.text_input("Fausse option 3 :")
    if st.button("Ajouter"):
        if all([new_q, ans, o2, o3, o4]):
            st.session_state.questions.append({
                "question": new_q,
                "options": [ans, o2, o3, o4],
                "answer": ans
            })
            st.success("Question ajoutée avec succès ✅")

# تحميل السؤال الحالي
if st.session_state.current_question < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}: {q['question']}")

    opts = list(q["options"])
    random.shuffle(opts)

    st.session_state.selected = st.radio("Choisissez une réponse :", opts)

    if st.button("Valider"):
        if st.session_state.selected == q["answer"]:
            st.session_state.score += 1
            st.success("✅ Correct !")
        else:
            st.error(f"❌ Faux ! La bonne réponse est : {q['answer']}")

        if st.button("Suivant ➔"):
            st.session_state.current_question += 1
            st.experimental_rerun()
else:
    st.info(f"🎉 Fin du quiz ! Score final: {st.session_state.score}/{len(st.session_state.questions)}")
    if st.button("Rejouer"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.experimental_rerun()

st.sidebar.markdown(f"**Score actuel :** {st.session_state.score}")