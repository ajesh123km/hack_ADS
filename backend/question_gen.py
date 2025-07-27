from transformers import pipeline

question_generator = pipeline(
    "text2text-generation",
    model="iarfmoose/t5-base-question-generator",
    tokenizer="iarfmoose/t5-base-question-generator",
    use_fast=False  # This is critical to avoid tokenizer issues
)

def generate_questions(text):
    prompt = f"generate question: {text}"
    result = question_generator(prompt, max_length=128, do_sample=False)
    return result[0]['generated_text']
