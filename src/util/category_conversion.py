import json

def translate_category(category):
    with open('src/conversion.json', 'r', encoding='utf-8') as file:
        translations = json.load(file)
        
    return translations.get(category, category)