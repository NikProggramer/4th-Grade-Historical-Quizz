#Run -> Run current script in terminal si bagam comanda de mai jos:
#python -m streamlit run veri_col_quz.py

import streamlit as st

css_content = """
<style>
::-webkit-scrollbar {width: 0px; background: transparent;}
* {scrollbar-width : none;}
.block-container {padding-top:2rem; padding-bottom: 0rem;}
img {max-height: 60vh; object-fit:cover;}
</style>
"""
st.markdown( css_content, unsafe_allow_html = True)

st.set_page_config(page_title="Historical quiz by NQM", layout = "wide", initial_sidebar_state = "collapsed")

st.title("4th Grade Historical Quizz")

questions = [
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images/image_1.png",
        "question": "What was the biggest country in Europe in the 1950's?",
        "options": ["East Germany", "Romania", "Vatican", "USSR"],
        "answer": "USSR"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_2.png",
        "question": "Who is the real roman?",
        "options": ["USA", "Germany", "Russia", "Greece and Italy"],
        "answer": "Greece and Italy"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_3.png",
        "question": "Who conquered Dacia?",
        "options": ["Egypt", "Roman Empire","USSR", "Canada"],
        "answer": "Roman Empire"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_4.png",
        "question" : "When did WW2 end?",
        "options" : ["1980", "1945", "2026"],
        "answer" : "1945"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_5.png",
        "question" : "What was the biggest empire?",
        "options" : ["Dacia", "British Empire", "Mongolian Empire"],
        "answer" : "British Empire"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_6.png",
        "question" : "Who did the soviets fight in the cold war?",
        "options" : ["Russia", "NATO", "Moldova"],
        "answer" : "NATO"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_7.jpg",
        "question" : "What Ideology in history involved Kings and queens?",
        "options" : ["Communism", "Monarchy", "Democracy"],
        "answer" : "Monarchy"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_8.webp",
        "question" : "Who was the founding father of the United States?",
        "options" : ["Stalin", "George Washington", "Burebista"],
        "answer" : "George Washington"
    },
    {
        
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_9.jpg",
        "question" : "When did WW1 end?",
        "options" : ["1918", "1946", "2014"],
        "answer" : "1918"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_10.jpg",
        "question" : "How Costly was WW2?",
        "options" : ["Not costly", "Insanely Costly", "Mildy Costly"],
        "answer" : "Insanely Costly"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_11.webp",
        "question" : "What was the best ruler of Romania?",
        "options" : ["Burebista", "Andrei", "Alexandru Ioan Cuza"],
        "answer" : "Alexandru Ioan Cuza"
    },
    {
        
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_12.jpg",
        "question" : "What is the motive of WW1?",
        "options" : ["Serbian assination of Franz Ferdinand", "Attack on poland", "Russian civil war"],
        "answer" : "Serbian assination of Franz Ferdinand"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_13.webp",
        "question" : "How long did the Romanian Peoples Republic last?",
        "options" : ["18 years", "1 hr", "2 years"],
        "answer" : "18 years"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_14.webp",
        "question" : "What was the most greatest era of Germany?",
        "options" : ["Re unfication of 1990", "The Great Depression", "WW2"],
        "answer" : "Re unfication of 1990"
    },
    {
        "image": "https://github.com/NikProggramer/4th-Grade-Historical-Quizz/tree/main/images\image_15.webp",
        "question" : "What was the last emperor of the Byzantine empire?",
        "options" : ["Trajan", "Pupienius", "Constantine XI"],
        "answer" : "Constantine XI"
    }
]



TOTAL = len(questions)

# ===== Initializare stare =====
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.last_correct = False

# ===== Final Quiz =====
if st.session_state.index >= TOTAL:
    st.subheader("🏁 Final Quiz!")
    st.write("Scor:", st.session_state.score, "/", TOTAL)

    if st.button("Restart Quiz", type="primary"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.session_state.last_correct = False
        st.rerun()

# ===== Inca sunt intrebari =====
else:
    q = questions[st.session_state.index]

    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.image(q["image"], caption="Look Closely")

    with  col2:
        st.subheader(f"Question {st.session_state.index + 1} / {TOTAL}")

        # ===== Afisare intrebare =====
        if not st.session_state.show_feedback:
            choice = st.radio(q["question"], q["options"], key=f"q{st.session_state.index}")

            if st.button("Raspunde", type="primary"):
                if choice == q["answer"]:
                    st.session_state.last_correct = True
                    st.session_state.score += 1
                else:
                    st.session_state.last_correct = False

                st.session_state.show_feedback = True
                st.rerun()

        # ===== Afisare feedback =====
        else:
            if st.session_state.last_correct:
                st.success("Corect! 🎉")
            else:
                st.error(f"Gresit ❌ Raspuns corect: {q['answer']}")

            # Verificam daca este ultima intrebare
            is_last = (st.session_state.index == TOTAL - 1)

            btn_text = "See result" if is_last else "Urmatoarea intrebare"

            if st.button(btn_text, type="primary"):
                st.session_state.index += 1
                st.session_state.show_feedback = False
                st.rerun()
