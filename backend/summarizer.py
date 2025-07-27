from transformers import pipeline
from PyPDF2 import PdfReader
import torch

# Check if CUDA is available
device = 0 if torch.cuda.is_available() else -1

# Load summarization model with GPU support if available
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize_text(text):
    if len(text) > 1024:
        text = text[:1024]  # Limit input to model size
    summary = summarizer(text, max_length=900, min_length=40, do_sample=False)
    return summary[0]['summary_text']
