import streamlit as st
import random
import time

# إعدادات الصفحة
st.set_page_config(page_title="Quiz: Le mur de glace", layout="centered")

# تخصيص التصميم عبر CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 18px !important;
    }
    .question-style {
        font-size: 24px !important;
        font-weight: bold;
        color: #f1c40f;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_config=True)

# تهيئة حالة الجلسة (Session State) لحفظ البيانات بين التحديثات
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {"question": "Où se situe l’Antarctique ?", "options": ["Nord", "Centre", "Sud", "L'est"], "answer": "Sud"},
        {"question": "Quelle est la capitale de la France ?", "options": ["Lyon", "Marseille", "Paris", "Lille"], "answer": "Paris"}
    ]
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'wrong_attempts' not in st.session_state:
    st.session_state.wrong_attempts = []
if 'answered_correctly' not in st.session_state:
    st.session_state.answered_correctly = False
if 'first_try' not in st.session_state:
    st.session_state.first_try = True

def next_question():
    st.session_state.current_question += 1
    st.session_state.wrong_attempts = []
    st.session_state.answered_correctly = False
    st.session_state.first_try = True

def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.wrong_attempts = []
    st.session_state.answered_correctly = False

# الواجهة الرئيسية
st.title("❄️ Quiz: Le mur de glace")
st.sidebar.header("لوحة التحكم")

# إضافة سؤال جديد
with st.sidebar.expander("➕ Ajouter une Question"):
    new_q = st.text_input("La question :")
    ans = st.text_input("Réponse correcte :")
    o2 = st.text_input("Fausse option 1 :")
    o3 = st.text_input("Fausse option 2 :")
    o4 = st.text_input("Fausse option 3 :")
    if st.button("Enregistrer"):
        if new_q and ans and o2 and o3 and o4:
            st.session_state.questions.append({"question": new_q, "options": [ans, o2, o3, o4], "answer": ans})
            st.success("Ajouté avec succès !")

# عرض الأسئلة
if st.session_state.current_question < len(st.session_state.questions):
    q_idx = st.session_state.current_question
    q_data = st.session_state.questions[q_idx]
    
    st.markdown(f"<p class='question-style'>Question {q_idx + 1}: {q_data['question']}</p>", unsafe_allow_config=True)

    # عرض الخيارات
    options = q_data['options']
    
    for i, opt in enumerate(options):
        # تحديد لون وحالة الزر
        button_type = "secondary"
        button_label = opt
        
        if opt in st.session_state.wrong_attempts:
            button_label = f"❌ {opt}"
        elif st.session_state.answered_correctly and opt == q_data['answer']:
            button_label = f"✅ {opt}"

        if st.button(button_label, key=f"btn_{i}", disabled=st.session_state.answered_correctly or opt in st.session_state.wrong_attempts):
            if opt == q_data['answer']:
                if st.session_state.first_try:
                    st.session_state.score += 1
                st.session_state.answered_correctly = True
                st.rerun()
            else:
                st.session_state.wrong_attempts.append(opt)
                st.session_state.first_try = False
                st.rerun()

    # إظهار زر "التالي" فقط عند الإجابة الصحيحة
    if st.session_state.answered_correctly:
        st.success("Bravo ! C'est la bonne réponse.")
        st.button("Suivant ➔", on_click=next_question)

else:
    st.balloons()
    st.header("🏁 Fin du Quiz !")
    st.subheader(f"Votre score final: {st.session_state.score} / {len(st.session_state.questions)}")
    st.button("Recommencer 🔄", on_click=restart_quiz)

# عرض النتيجة في الأسفل
st.write("---")
st.info(f"Score actuel: {st.session_state.score}")