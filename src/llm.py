from openai import OpenAI
from src.prompt import system_instruction 

TOGETHER_API_KEY ="fd518c5bfe5aad21e194745d7e6f02af0a42e60a39017d47504c21cf95b69db2"

client = OpenAI(
  api_key=TOGETHER_API_KEY,
  base_url='https://api.together.xyz/v1',
)
messages = [
    {"role": "system", "content": system_instruction}
]


def ask_order(messages, model="togethercomputer/llama-2-70b-chat",temperature=0):
    response = client.chat.completions.create(
        model= model,
        messages=  messages,
        temperature= temperature 
    )

    return response.choices[0].message.content