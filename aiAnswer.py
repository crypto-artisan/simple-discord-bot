from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = OPENAI_API_KEY)

def generateAnswer(prompt):
    try:
        response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant.words limit is 60"},
            {"role": "user", 
             "content": f"{prompt}"
            }
        ]
        )
        return response.choices[0].message.content
    except:
        pass
    return ""