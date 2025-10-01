from transformers import pipeline

# Load Hugging Face summarizer (first run downloads model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_len=60):
    if not text:
        return "No description available."
    result = summarizer(text, max_length=max_len, min_length=20, do_sample=False)
    return result[0]['summary_text']
