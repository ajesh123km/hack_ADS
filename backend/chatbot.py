from transformers import pipeline

chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

def chat_with_summary(summary, user_question):
    prompt = f"You are a study assistant. Based on the following content:\n{summary}\nAnswer: {user_question}"
    result = chatbot(prompt, max_length=256)
    return result[0]['generated_text']
    