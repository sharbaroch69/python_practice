letter = '''dear <|name|>, 
            you are selected 
            <|date|>'''

print(letter.replace("<|name|>", "Awais").replace("<|date|>","15 Aug 2025"))