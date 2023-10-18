import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a business analyst, skilled in writing ecommerce user stories for ecommerce website development."},
    {"role": "user", "content": "Compose a user story that explains the home page hero banner."}
  ]
)

print(completion.choices[0].message)
