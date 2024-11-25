# ChatBot: Your Friendly Virtual Assistant 🤖

Welcome to the **ChatBot** project! This is a simple yet powerful chatbot built in Python, designed to simulate conversational interactions with a user. Whether you're curious about facts, need a quick joke, or want to learn about programming concepts like AI and Python, this bot has got you covered!

---

## 🚀 Features

### ✅ **Smart Question Matching**
- The bot uses `difflib` to find the closest match for user queries, ensuring accurate responses even for similar phrasing.

### ✅ **Rich Knowledge Base**
- Includes answers to common questions about general knowledge, fun facts, trivia, and more.

### ✅ **Interactive & User-Friendly**
- Gracefully handles unrecognized inputs and lets you exit the conversation easily with commands like `exit`, `quit`, or `bye`.

### ✅ **Customizable**
- Easily expand the knowledge base by adding more question-answer pairs to the `brain` dictionary.

---

## 📋 How It Works

1. **User Input**: The bot takes your query as input.
2. **Matching Logic**: It matches your query to its knowledge base using similarity checks (`difflib`).
3. **Response**: Provides a matching response or falls back with a polite "I don’t understand" message.
4. **Real-Time Exit**: Ends the conversation cleanly when the user types `exit`, `quit`, or `bye`.

---

## 🛠️ Installation & Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/chatbot.git
   cd chatbot
   ```

2. **Ensure Python is Installed**:
   - This project works with Python 3.9 or higher.
   - Install Python [here](https://www.python.org/downloads/) if you don't have it.

3. **Run the Script**:
   ```bash
   python chatbot.py
   ```

---

## 🗃️ Example Questions

Here are some example interactions to try:

| **Question**                  | **Response**                                                                          |
|-------------------------------|--------------------------------------------------------------------------------------|
| `hello`                       | "Hey there! How can I assist you today?"                                             |
| `what is python`              | "Python is a versatile and popular programming language."                            |
| `tell me a fun fact`          | "Did you know? Honey never spoils."                                                  |
| `what is 2 + 2`               | "2 + 2 is 4."                                                                        |
| `what is ai`                  | "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence." |
| `what is the meaning of life` | "The meaning of life is subjective; some say it’s 42!"                               |
| `bye`                         | "Goodbye! Have a great day!"                                                         |

---

## 📚 Code Highlights

### Key Components:
1. **Similarity Matching**:
   ```python
   def get_best_match(user_question: str, questions: dict) -> str | None:
       matches = get_close_matches(user_question, list(questions.keys()), n=1, cutoff=0.6)
       return matches[0] if matches else None
   ```
   - This ensures flexibility in user inputs by allowing slight variations.

2. **Graceful Exit**:
   ```python
   if user_input in ['exit', 'quit', 'bye']:
       print("Bot: Goodbye! Have a great day!")
       break
   ```

3. **Knowledge Base (`brain` Dictionary)**:
   - Easily customizable for specific domains or topics of interest.

---

## 🎨 Screenshots

### **Conversation Example**
```
You: hello
Bot: Hey there! How can I assist you today?

You: tell me a joke
Bot: Why did the computer show up late to work? It had a hard drive!

You: what is 2 + 2
Bot: 2 + 2 is 4.

You: bye
Bot: Goodbye! Have a great day!
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:
1. Fork the repository.
2. Create a new branch (`feature/amazing-feature`).
3. Commit your changes.
4. Push the branch and submit a Pull Request.

---

## 🙌 Acknowledgments

- **Python** for making scripting so enjoyable.
- **Difflib** for enabling smart string matching.
- Everyone contributing to the open-source ecosystem!

---

Have questions or suggestions? Feel free to reach out or create an issue in the repository. Let's make this chatbot even smarter! 😊
