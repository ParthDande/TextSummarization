from flask import Flask, request, render_template
from transformers import pipeline
max_length = 500
min_length = 100
app = Flask(__name__)

# Create summarization pipeline
summarizer = pipeline('summarization', model="Falconsai/text_summarization")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/summarize', methods=['POST'])
def summarize():
    article = request.form['article']
    print(f'The words in the article are {len(article)}')
    max_length = int(len(article)/7)
    min_length = int(len(article)/10)
    summary_text = summarizer(article, max_length=max_length,min_length=min_length,truncation=True, do_sample=False)[0]['summary_text']
    return render_template('index.html', article=article, summary=summary_text)
