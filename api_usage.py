from openai import OpenAI
import os
from dotenv import load_dotenv

class Bot():
    
    llm = ""
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_KEY")
        self.llm = OpenAI(api_key=api_key)
    
    def generate_response(self):
        response = self.llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Write 2-3 sentences about the ethical use of AI"
            }
        ]
    )
        
        print(response.choices[0].message.content)


if __name__ == "__main__":
    bot = Bot()
    bot.generate_response()   