from openai import OpenAI
import os

client = OpenAI(api_key = os.environ["OPENAI_API_KEY"])
import json
import time

def generate_prompts():
    prompt_instruction = """
    Generate 10 unique questions that Kanye West might respond to. These questions should relate to his views on life, music, fashion, creativity, fame, and success.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_instruction}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content.strip().split("\n")
    except Exception as e:
        print(f"Error generating prompts: {e}")
        return []

def get_kanye_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using the provided model
            messages=[
                {"role": "system", "content": "You are a helpful assistant who responds like Kanye West."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating response for prompt '{prompt}': {e}")
        return None

all_prompts = []

kanye_conversations = []

while len(all_prompts) < 1000:
    new_prompts = generate_prompts()
    if new_prompts:
        all_prompts.extend(new_prompts)
        print(f"Generated {len(new_prompts)} new prompts. Total: {len(all_prompts)} prompts.")

    time.sleep(1.2)

all_prompts = all_prompts[:1000]

for prompt in all_prompts:
    response = get_kanye_response(prompt)
    if response:
        kanye_conversations.append({
            "Prompt": prompt,
            "Response": response
        })
        print(f"Generated response for prompt: {prompt}")

    time.sleep(1.2)

with open('kanye_1000_conversations.json', 'w') as f:
    json.dump(kanye_conversations, f)

print(f"Saved {len(kanye_conversations)} prompt-response pairs to 'kanye_1000_conversations.json'.")