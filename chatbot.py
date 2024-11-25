from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    """
    Finds the closest matching question from the given dictionary keys 
    based on the user's input using difflib's get_close_matches.

    Args:
        user_question (str): The question entered by the user.
        questions (dict): A dictionary with questions as keys and answers as values.

    Returns:
        str | None: The closest matching question or None if no match is found.
    """
    # Extract all questions (keys) from the knowledge dictionary
    question_list: list[str] = list(questions.keys())
    
    # Find the best match with at least 60% similarity
    matches: list = get_close_matches(user_question, question_list, n=1, cutoff=0.6)
    
    # Return the best match if any, otherwise None
    return matches[0] if matches else None

def chat_bot(knowledge: dict):
    """
    Simulates a chatbot that responds to user input by finding the closest 
    match from a predefined set of questions and answers.

    Args:
        knowledge (dict): A dictionary containing questions as keys 
                          and their corresponding answers as values.
    """
    while True:
        # Get user input
        user_input: str = input('You: ').strip().lower()
        
        # Allow user to exit the chatbot
        if user_input in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break

        # Find the closest matching question
        best_match: str | None = get_best_match(user_input, knowledge)
        
        # Respond with the answer or a fallback message
        if best_match and (answer := knowledge.get(best_match)):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand what you are trying to say...')

if __name__ == '__main__':
    # Predefined questions and answers in the chatbot's knowledge base
    brain: dict = {
        'hello': 'Hey there! How can I assist you today?',
        'how are you': 'I am just a bot, but I am functioning perfectly!',
        'what is your name': 'I am your friendly chatbot.',
        'what can you do': 'I can answer your questions, provide information, and have a chat with you!',
        'current time': 'You can check the current time using your device!',
        'who created you': 'I was created by a developer using Python.',
        'what is python': 'Python is a versatile and popular programming language.',
        'tell me a joke': 'Why did the computer show up late to work? It had a hard drive!',
        'what is ai': 'AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.',
        'what is the weather': 'I cannot provide real-time weather, but you can check online using a weather app.',
        'what is the capital of india': 'The capital of India is New Delhi.',
        'what is 2 + 2': '2 + 2 is 4.',
        'tell me a fun fact': 'Did you know? Honey never spoils. Archaeologists have found 3,000-year-old honey in ancient tombs that is still edible!',
        'what is the largest mammal': 'The largest mammal is the blue whale.',
        'what is the speed of light': 'The speed of light in a vacuum is approximately 299,792 kilometers per second.',
        'who is the president of the usa': 'As of 2024, the President of the United States is Joe Biden.',
        'what is the meaning of life': 'The meaning of life is subjective; some say it’s 42!',
    }

    # Start the chatbot
    print("Bot: Hello! You can ask me questions or type 'exit' to quit.")
    chat_bot(brain)
