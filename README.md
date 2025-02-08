# AI-Powered Chatbot with Flask

This project is an AI-powered chatbot developed using the **Flask** framework and **Natural Language Processing (NLP)**. The chatbot can answer basic queries by utilizing machine learning techniques to understand user inputs and provide dynamic responses. The project is designed as a simple web application that can be extended with more complex functionalities.

## Features
- **Flask Web Framework**: Used to build a RESTful API for interacting with the chatbot.
- **Natural Language Processing (NLP)**: Incorporates NLP methods to process user messages and generate relevant responses.
- **Machine Learning Model**: The chatbot uses a basic ML model to recognize user intents and produce appropriate responses.
- **JSON API**: The chatbot operates via HTTP POST requests, accepting and responding in JSON format.
- **Extensible**: This chatbot can easily be extended to support more intents and responses as needed.

## Getting Started

### Prerequisites
Before you can run the chatbot, you need to have the following installed:
- Python 3.x
- Pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git

   Navigate into your project folder:

cd your-repository-name
Create a virtual environment:


python -m venv venv
Activate the virtual environment:

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate
Install the required dependencies:

pip install -r requirements.txt
Running the App
Start the Flask server by running:

python app.py
The server will be running at http://127.0.0.1:5000/.

Testing the Chatbot API
You can interact with the chatbot via Postman or cURL by sending a POST request to the /chat endpoint.

Example request body:

{
  "message": "Hello"
}
Example cURL Command:
bash
Copy
Edit
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello"}' http://127.0.0.1:5000/chat
Example Response:
json
Copy
Edit
{
  "response": "Hello! How can I assist you today?"
}
Project Structure
bash
Copy
Edit
/your-repository-name
│
├── app.py                # Flask application
├── chatbot.py            # Chatbot logic and intent recognition
├── intents.json          # Intents and patterns for chatbot
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
Contributing
Feel free to fork this repository and submit pull requests. If you find any issues, feel free to open an issue in the repository.
