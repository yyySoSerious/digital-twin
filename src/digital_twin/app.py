import re

from styles import CSS, JS, EXAMPLES
import gradio as gr
from openai import OpenAI
from context import SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL_NAME = "gpt-5.4-mini"
MAX_ITERATIONS = 10

openai = OpenAI()

def normalize_message(item: dict):
    """
    Normalize a chat message item to ensure consistent structure.

    Args:
        item (dict): The chat message item to normalize.

    Returns:
        dict: The normalized chat message item.
    """
    role = item["role"]
    content = item["content"]

    if isinstance(content, str):
       return {"role": role, "content": content}

    normalized_content = []
    for block in content:
       if block["type"] == "text":
           normalized_content.append({
               "type": "input_text" if role == "user" else "output_text",
               "text": block["text"]
           })

    return {"role": item["role"], "content": normalized_content}

def get_sources(response):
    """
    Extract the sources from the response output.
    
    Args:
        response (dict): The response object from which to extract sources.
        
    Returns:
        list: Sorted, unique filenames extracted from the response.
    """
    sources = set()

    for item in response.output:
        if item.type == "message":
            for content in item.content:
                if content.type == "output_text":
                    for annotation in content.annotations:
                        if annotation.type == "file_citation":
                            sources.add(annotation.filename)

    return sorted(sources)

def format_response(response):
    """Return the response text with any cited files listed below it."""
    text = re.sub(r"\ue200filecite\ue202[^\ue200\ue201\n]*\ue201", "", response.output_text)
    sources = get_sources(response)
    if sources:
        return f"{text}\n\nSources:\n" + "\n".join(
            f"- {source}" for source in sources
        )
    return text

def chat(message, history):
    """
    Handle a chat message from the user and return the response from the digital twin.

    Args:
        message (str): The user's message.
        history (list): The chat history.
    """
    input_list = [
        normalize_message(item) 
        for item in history 
        if item["role"] in ("user", "assistant")
    ]
    input_list.append({"role": "user", "content": message})
    response = openai.responses.create(
        model=MODEL_NAME, 
        instructions=SYSTEM_PROMPT, 
        input=input_list,
        tools=tools,
    ) 

    for _ in range(MAX_ITERATIONS):
        tool_calls = [item for item in response.output if item.type == "function_call"]


        if not tool_calls:
            return format_response(response)

        tool_outputs = handle_tool_calls(tool_calls)
        response = openai.responses.create(
            model=MODEL_NAME,
            instructions=SYSTEM_PROMPT,
            previous_response_id=response.id,
            input=tool_outputs,
            tools=tools,
        )

    return "Maximum tool execution iterations reached."


if __name__ == "__main__":
    gr.ChatInterface(
        fn=chat,
        examples=EXAMPLES,
        title="Ope Adegbemi's Digital Twin",
        description="A conversation about my work, experience, and ideas.",
        chatbot=gr.Chatbot(
            elem_id="twin-chat",
            show_label=False,
            height="min(58vh, 570px)",
            min_height=340,
            placeholder=(
                '<div class="welcome-mark">OA</div>'
                '<div class="welcome-title">A little more about me.</div>'
                '<div class="welcome-copy">Ask a question, or start with one of these.</div>'
            ),
        ),
        textbox=gr.Textbox(
            elem_id="twin-input",
            placeholder="Ask about my work...",
            show_label=False,
            submit_btn="Send",
            stop_btn=True,
        ),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())