import ollama

response = ollama.chat(model='gemma:2b', messages=[
    {
        'role': 'user',
        'content': 'hi',
    },
    {
        'role': 'assistant',
        'content': "Hello! 👋 It's nice to hear from you. What can I do for you today? 😊"
    },
    {
        'role': 'user',
        'content': 'how are you doing?'
    }
])

print(response['message']['content'])

# embeddings = ollama.embeddings(
#     model='gemma:2b', prompt='The sky is blue because of rayleigh scattering')

# print(len(embeddings['embedding']))
