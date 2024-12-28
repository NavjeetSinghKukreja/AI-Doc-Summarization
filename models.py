from summarizer import Summarizer
import torch
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

# Load BERT Summarizer model
bert_model = Summarizer()

# Load BART tokenizer and model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn').to(device)

# Load sentiment-analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Function for BERT extractive summarization
def generate_extractive_summary(text, ratio=0.5):
    if not isinstance(text, str) or not text.strip():  # Skip empty content
        return ""
    return bert_model(text, ratio=ratio)

# Function for BART abstractive summarization
def generate_abstractive_summary(text, max_length=250, min_length=100, num_beams=4):
    if not isinstance(text, str) or not text.strip():  # Skip empty content
        return ""
    inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True).to(device)
    summary_ids = bart_model.generate(
        inputs['input_ids'],
        max_length=max_length,
        min_length=min_length,
        num_beams=num_beams,
        length_penalty=2.0,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Combined summarization pipeline
def generate_combined_summary(content, bert_ratio=0.5, bart_max_length=250, bart_min_length=100, bart_num_beams=4):
    # Step 1: Generate an extractive summary using BERT
    extractive_summary = generate_extractive_summary(content, ratio=bert_ratio)
    
    # Step 2: Generate an abstractive summary from the extractive summary using BART
    combined_summary = generate_abstractive_summary(extractive_summary, 
                                                    max_length=bart_max_length, 
                                                    min_length=bart_min_length, 
                                                    num_beams=bart_num_beams)
    return combined_summary

# Function to analyze sentiment of the summary or text
def get_sentiment(text):
    if not isinstance(text, str) or not text.strip():  # Skip empty content
        return None
    sentiment = sentiment_analyzer(text)
    return sentiment[0]['label']  # Returns the label ('POSITIVE', 'NEGATIVE', 'NEUTRAL')
