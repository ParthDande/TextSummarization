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
    summary_text = summarizer(article, max_length=500, min_length=500, do_sample=False)[0]['summary_text']
    return render_template('index.html', article=article, summary=summary_text)
if __name__ == '__main__':
    app.run(debug=True)
