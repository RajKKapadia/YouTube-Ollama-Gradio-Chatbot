import gradio as gr
import ollama


def format_messages(query: str, chatbot: list[tuple[str, str]]) -> list[dict[str, str]]:
    formatted_messages = []
    for cb in chatbot:
        formatted_messages.append(
            {
                'role': 'user',
                'content': cb[0],
            }
        )
        formatted_messages.append(
            {
                'role': 'assistant',
                'content': cb[1]
            }
        )
    formatted_messages.append(
        {
            'role': 'user',
            'content': query,
        }
    )
    return formatted_messages


def handle_user_query(msg: str, chatbot: list[tuple[str, str]]) -> tuple:
    chatbot += [(msg, None)]
    return '', chatbot


def generate_response(chatbot: list[tuple[str, str]]) -> tuple:
    query = chatbot[-1][0]
    print(f'Query -> {query}')
    formatted_messages = format_messages(query, chatbot[:-1])
    response = ollama.chat(model='gemma:2b', messages=formatted_messages)
    response = response['message']['content']
    print(f'Response -> {response}')
    chatbot[-1][1] = response
    return chatbot


with gr.Blocks() as demo:

    chatbot = gr.Chatbot(label='Ollama Chatbot', height=750)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(handle_user_query, [msg, chatbot], [msg, chatbot]).then(
        generate_response, [chatbot], [chatbot])

if __name__ == '__main__':
    demo.launch()
