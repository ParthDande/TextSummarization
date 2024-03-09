from transformers import pipeline
summarizer = pipeline('summarization')

article =input('Enter  an article: ')
summarized_text=summarizer(article,max_length=100,min_length = 50,do_sample =False)
first_dict = summarized_text[0]
summary_text = first_dict['summary_text']
print(f"Summary of the Article:\n{summarizer([article])[0]['summary_text']}")

