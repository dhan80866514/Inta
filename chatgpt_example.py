import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {'role': 'user', 'content': 'Hello, ChatGPT!'}
    ]
)

print(response['choices'][0]['message']['content'])
