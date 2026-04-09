# BlueQuery – Natural Language to SQL (Offline AI)

BlueQuery is an Offline AI-powered system that converts natural language queries into SQL and executes them on a local database. It enables users to interact with structured data without writing SQL.

## Features

- Convert plain English queries into SQL
- Fully offline (no external API required)
- Execute queries on a local SQLite database
- Interactive Streamlit UI
- Dark/Light theme toggle with animations
- Real-time results display

## How It Works

1. User enters a query in natural language
2. A fine-tuned T5 model converts it into SQL
3. The SQL query is executed using SQLite
4. Results are displayed in the UI

## Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (T5)
- PyTorch
- SQLite

## How to Run the Application

Follow these steps to run BlueQuery on your system: 1. Clone the repository(git clone <repository-url>) 2. (Optional) Create and activate a virtual environment(python -m venv venv) 3. Install dependencies(pip install -r requirements.txt)
4.Initialize the database (run once)(python setup_db.py)You can upload your own csv file to the database by modifying the setup_db.py file.
5.Start the application(streamlit run app.py)
