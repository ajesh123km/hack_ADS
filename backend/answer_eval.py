
def evaluate_answer(user_answer: str, correct_answer: str) -> str:
    # Example evaluation logic (basic)
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return "Correct"
    else:
        return "Incorrect or partially correct"



from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
model_name = "google/flan-t5-base"  # or "flan-t5-small"

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

evaluator = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)



def evaluate_answer_llm(question, user_answer, correct_answer):
    prompt = (
        f"Evaluate the user's answer:\n"
        f"Question: {question}\n"
        f"Correct Answer: {correct_answer}\n"
        f"User Answer: {user_answer}\n"
        f"Give feedback like 'Correct', 'Incomplete', 'Needs Elaboration' and suggest improvements."
    )
    result = evaluator(prompt, max_length=256)
    return result[0]['generated_text']
