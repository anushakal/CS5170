# OpenAI Usage Project

This project demonstrates how to use the OpenAI API to generate responses to user prompts. The script, `api_usage.py`, initializes a chatbot that interacts with the OpenAI GPT-3.5-turbo model to provide helpful responses.

## Project Files

 - api_usage.py: Main Python script for the chatbot.
 - requirements.txt: Contains necessary Python dependencies.
 - .env: File to store environment variables, especially the OpenAI API key.

## Dependencies
 - Python environment (3.7+)
 - OpenAI API Key (Can be obtained by signing up for one at their website)

## Setup Instructions
1) Clone this repository
    git clone <repo-url>
    cd <repo-folder>

2) Install dependencies defined in requirements.txt using pip
    pip install -r requirements.txt

3) Create a .env file in the root folder of the project and add the OpenAI key there as follows:
    OPENAI_KEY = "your_api_key"

4) Running the script
    python api_usage.py

## Remarks
 - The prompt can be changed according to what the user wants in the api_usage.py
 - The API key can be directly given to the OpenAI instance, but encoding it in .env file makes it more secure and eliminates the hard coding.

