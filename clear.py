import re

def extraire_email(text):
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    return emails[0] if emails else None

  

import re

def nettoyer_message(message):
    
    cleaned_message = message.strip()

    cleaned_message = re.sub(r'\s+', ' ', cleaned_message)


    signature_pattern = r'(?:Best regards|Sincerely|Yours truly|Kind regards)[\s\S]*$'
    cleaned_message = re.sub(signature_pattern, '', cleaned_message, flags=re.IGNORECASE)

    cleaned_message = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[email supprimé]', cleaned_message)


    cleaned_message = re.sub(r'\+?\d[\d -]{8,12}\d', '[numéro supprimé]', cleaned_message)
    return cleaned_message
