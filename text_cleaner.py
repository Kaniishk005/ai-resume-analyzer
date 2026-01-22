import re

def clean_text(text):
    text = text.lower() 
    text = re.sub(r'\n+',' ',text) #flattens multi line doc into single continous block of text
    text = re.sub(r'[^a-zA-Z0-9+.# ]', ' ', text) #removes puncutations like .,? etc
    text = re.sub(r'\s+', ' ', text) #replaces multiple spaces and tabs with single space
    return text.strip()#removes traling and leading spaces