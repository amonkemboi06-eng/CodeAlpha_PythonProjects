# Basic Python Chatbot

## Project Description

This project is a simple rule-based chatbot developed using Python and Flask. It accepts messages from the user through a web page and responds based on predefined rules. The chatbot recognizes basic inputs such as greetings and simple questions.

## Objective

The objective of this project is to demonstrate the use of Python functions, conditional statements, loops, and basic web development by creating a chatbot that interacts with users.

## Tools and Technologies Used

### Python
Python is the main programming language used to implement the chatbot logic because it is easy to read and suitable for beginners.

### Flask
Flask is used to create a simple web server (API) that connects the chatbot to the web page. It receives messages from the user and returns chatbot responses.

### HTML
HTML is used to create the structure of the chatbot webpage, including the chat area, input field, and send button.

### CSS
CSS is used to style the webpage by adding colors, chat bubbles, spacing, and making the interface more user-friendly.

### JavaScript
JavaScript is used to send user messages to the Flask server without reloading the page and display chatbot responses dynamically.

## Files in the Project

- **ChatBot.py** – Contains the chatbot response logic.
- **App.py** – Runs the Flask application and handles communication between the webpage and the chatbot.
- **templates/index.html** – Defines the chatbot interface.
- **static/style.css** – Styles the chatbot interface.
- **static/script.js** – Handles sending messages and displaying responses.

## How the Chatbot Works

1. The user types a message in the webpage.
2. JavaScript sends the message to the Flask server.
3. Flask receives the message and passes it to the chatbot.
4. The chatbot checks the user's input using `if-elif-else` statements.
5. A predefined response is returned.
6. The response is displayed on the webpage.

## Python Concepts Used

- Functions
- if-elif-else statements
- Strings
- User input
- Flask routes
- JSON data exchange

## Sample Inputs

- Hello
- Hi
- How are you?
- Bye

## Sample Outputs

- Hello! How can I help you?
- I am doing great! Thanks for asking.
- Goodbye!
- Sorry, I don't understand.

## Conclusion

This project demonstrates how a simple rule-based chatbot can be created using Python and connected to a web interface using Flask. It also shows the integration of HTML, CSS, and JavaScript with a Python backend.