import spacy
from skills import SKILLS
nlp = spacy.load("en_core_web_sm")#loading pre trained english language model
def extract_skills(text):
    doc = nlp(text)#input text processed by spacy and converted into tokens
    found_skills = set()#empty set initially
    for token in doc:
        token_text = token.text.lower()
        if token_text in SKILLS:
            found_skills.add(token_text)
    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return sorted(found_skills)