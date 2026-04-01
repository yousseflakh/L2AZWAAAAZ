import streamlit as st
import random

st.set_page_config(page_title="Quiz WW1", layout="centered")

# تهيئة session state
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
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None

# عنوان
st.title("🎯 Quiz: La Première Guerre Mondiale")

# إضافة سؤال
st.sidebar.header("➕ Ajouter une Question")

new_q = st.sidebar.text_input("Question")
correct = st.sidebar.text_input("Réponse correcte")
o2 = st.sidebar.text_input("Option 2")
o3 = st.sidebar.text_input("Option 3")
o4 = st.sidebar.text_input("Option 4")

if st.sidebar.button("Ajouter"):
    if new_q and correct and o2 and o3 and o4:
        st.session_state.questions.append({
            "question": new_q,
            "options": [correct, o2, o3, o4],
            "answer": correct
        })
        st.sidebar.success("Question ajoutée !")

# عرض السؤال
if st.session_state.current < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.current]
    
    st.subheader(f"Question {st.session_state.current + 1}")
    st.write(q["question"])

    options = q["options"].copy()
    random.shuffle(options)

    # اختيار جواب
    choice = st.radio("Choisissez une réponse :", options, key=st.session_state.current)

    if st.button("Valider") and not st.session_state.answered:
        st.session_state.selected = choice
        st.session_state.answered = True

        if choice == q["answer"]:
            st.success("✅ Bonne réponse !")
            st.session_state.score += 1
        else:
            st.error("❌ Mauvaise réponse")
            st.info(f"✔️ Bonne réponse: {q['answer']}")

    # زر التالي
    if st.session_state.answered:
        if st.button("➡️ Suivant"):
            st.session_state.current += 1
            st.session_state.answered = False
            st.session_state.selected = None

# نهاية اللعبة
else:
    st.success(f"🎉 Score final: {st.session_state.score}/{len(st.session_state.questions)}")
    
    if st.button("🔄 Rejouer"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False

# عرض السكور
st.markdown(f"### ⭐ Score: {st.session_state.score}")