from openai import OpenAI  # Import the OpenAI library to access its API.
import os  # Import the os module to interact with environment variables.
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file.

class Bot():
    # Define a class named Bot to encapsulate the behavior of the OpenAI-powered assistant.
    
    llm = ""  # Initialize a variable to store the OpenAI API instance.
    
    def __init__(self):
        # Constructor to initialize the Bot instance and configure the OpenAI API.
        load_dotenv()  # Load environment variables from a .env file.
        api_key = os.getenv("OPENAI_KEY")  # Retrieve the API key for OpenAI from environment variables.
        self.llm = OpenAI(api_key=api_key)  # Initialize the OpenAI API with the provided key.
    
    def generate_response(self):
        # Method to generate a response from the OpenAI API based on a specific prompt.
        response = self.llm.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the OpenAI model to use for the response.
            messages=[  # Define the prompt messages for the API.
                {
                    "role": "system", 
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Write 2-3 sentences about the ethical use of AI"  # User prompt.
                }
            ]
        )
        
        print(response.choices[0].message.content)  # Print the AI's response to the user prompt.

# Main entry point to execute the script.
if __name__ == "__main__":
    bot = Bot()  # Instance of the bot
    bot.generate_response()  # Call the method to generate and display a response.
