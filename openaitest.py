import openai
from config import apikey
import os

openai.api_key = openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.Completion.create(
  model="text-davinci-003",
  messages=[
    {
      "role": "user",
      "content": "write a resignation letter"
    }
  ],
  temperature=0,
)

print(completion.choices[0].message.content)


