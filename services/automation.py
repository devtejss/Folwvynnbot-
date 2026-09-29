def process_message(text:str):

    text = text.lower().strip()

    responses = {
        "hi":"👋 Hey! I'm FolwynnBot.",
        "hello":"👋 Hello! How can i help?",
        "hey":"⚡ Hey there!",
        "thanks":"You're welcome!😄",
        "thank you":"You're welcome!😄",
    }

    return responses.get(text)