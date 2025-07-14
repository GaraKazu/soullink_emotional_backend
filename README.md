# SoulLink Emotional Dialogue Engine

## Overview

SoulLink is an AI-powered emotional dialogue engine designed to create deep, realistic interactions through emotional modelling. It tracks relationship levels, emotional states, and memory to produce natural, evolving conversations with an AI named Noel.

This project was created for the Gen.AI Hackathon 2025.

---

## Features

- Tracks emotional states like hurt, trust, empathy, and affection.  
- Dynamic relationship progression (Strangers → Soulmates).  
- Memory system for storing and recalling key interactions.  
- AI responses adapt based on current emotions and relationship status.  
- FastAPI backend providing a REST API for chat.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher  
- Virtual environment (recommended)

### Installation

1. Clone the repository:

Bash
git clone https://github.com/yourusername/soullink-emotional-backend.git
cd soullink-emotional-backend

2.Create and activate a virtual environment:

Bash
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

bash
pip install -r requirements.txt

4. Running the server
Start the FastAPI backend server with:

Bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload

Using the API
Send POST requests to the /chat endpoint with JSON containing a text field:

json
Copy
Edit
{
  "text": "Hello, Noel!"
}
Example using curl:

bash
curl -X POST http://127.0.0.1:8000/chat \
-H "Content-Type: application/json" \
-d '{"text": "Hello, Noel!"}'
Noel will respond based on the emotional context and relationship status.

Project Structure
bash
Copy
Edit
/soullink-emotional-backend
│
├── main.py               # FastAPI app and routes
├── noel_ai.py            # Noel AI emotional dialogue logic
├── emotional_engine.py   # Emotional states, memory, and relationships
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── ...
Future Improvements
Persistent memory storage and loading

Enhanced emotion recognition from input

Multi-turn conversations with memory context

Frontend UI for easier chat interaction

Contact
Created by John Gabriel for Gen.AI Hackathon 2025.
Feel free to contact me with questions or feedback!

Email: 
xjohn9002@gmailcom
j.xavierantonyana@sydstu.catholic.edu.au

