import streamlit as st
from backend.summarizer import summarize_text, extract_text_from_pdf
from backend.question_gen import generate_questions
from backend.answer_eval import evaluate_answer
from backend.chatbot import chat_with_summary
from backend.tts_engine import speak_text

st.set_page_config(page_title="Smart Study Assistant", layout="wide")
st.title("📚 Smart Study Assistant")

st.markdown("Welcome! Choose a feature from the sidebar to begin.")

option = st.sidebar.selectbox("Choose Feature", ["Summarizer", "Question Generator", "Answer Evaluator", "Chatbot", "Text-to-Speech"])

st.write(f"You selected: {option}")


if option == "Summarizer":
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        summary = summarize_text(text)
        st.success("Summary:")
        st.write(summary)

elif option == "Question Generator":
    content = st.text_area("Enter Summary:")
    if st.button("Generate Questions"):
        questions = generate_questions(content)
        st.write(questions)

elif option == "Answer Evaluator":
    q = st.text_input("Question:")
    correct = st.text_input("Expected Answer:")
    user_ans = st.text_input("Your Answer:")
    if st.button("Evaluate"):
        feedback = evaluate_answer(q, user_ans, correct)
        st.write(feedback)

elif option == "Chatbot":
    context = st.text_area("Enter Summary:")
    followup = st.text_input("Ask a question:")
    if st.button("Ask AI Buddy"):
        reply = chat_with_summary(context, followup)
        st.write(reply)

elif option == "Text-to-Speech":
    tts_input = st.text_area("Enter text to speak:")
    if st.button("Play Audio"):
        audio_file = speak_text(tts_input)
        audio_bytes = open(audio_file, 'rb').read()
        st.audio(audio_bytes, format='audio/mp3')
