🍳 Smart Recipe AI

Smart Recipe AI is an AI-powered web app that suggests delicious recipes based on the ingredients you have! No more “what to cook today?” dilemmas — just enter your ingredients and let the AI do the magic. ✨

🚀 Features

🥕 Ingredient-Based Suggestions: Enter what’s in your kitchen and get creative recipes.

🍽️ Recipe Details: Step-by-step instructions, cooking time, and nutritional info.

🤖 AI-Powered Recommendations: Suggests recipes intelligently based on your inputs.

📱 Responsive Design: Works perfectly on desktop, tablet, and mobile.

🛠️ Tech Stack
Frontend	Backend	AI/ML	Deployment
HTML, CSS, JS	Python, Flask	Optional AI model	Render, Gunicorn
📂 Project Structure
recipe-app/
│
├── app.py               # Main Flask app
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── requirements.txt     # Python dependencies
├── Procfile             # Render deployment config
└── runtime.txt          # Python version for Render

💻 Local Setup

Clone the repository

git clone <YOUR_REPO_URL>
cd recipe-app


Create and activate virtual environment

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


Run the app

python app.py


Open in your browser

http://127.0.0.1:5000
