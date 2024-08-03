import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
print("API KEY", os.getenv('OPENAI_API_KEY'))

response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt="Tell me a joke.",
  max_tokens=50
)

print(response.choices[0].text.strip())
