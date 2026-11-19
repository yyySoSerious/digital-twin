import json
import os
import requests
from dotenv import load_dotenv
from database import initialize_database, add_user

load_dotenv(override=True)

initialize_database()
pushover_user_key = os.getenv("PUSHOVER_USER_KEY")
pushover_token_key = os.getenv("PUSHOVER_TOKEN_KEY")
vector_store_id = os.getenv("VECTOR_STORE_ID")

pushover_api_url = "https://api.pushover.net/1/messages.json"

def send_pushover_notification(title: str, message: str):
    """
    Send a notification using the Pushover API.

    Args:
        title (str): The title of the notification.
        message (str): The message content of the notification.
    """
    payload = {
        "token": pushover_token_key,
        "user": pushover_user_key,
        "title": title,
        "message": message
    }

    response = requests.post(pushover_api_url, data=payload)

    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}, Response: {response.text}")


def record_user_details(email: str, name="Name not provided", notes="Notes not provided"):
    """
    Record user details in the database and send a notification.

    Args:
        email (str): The user's email address.
        name (str): The user's name. Defaults to "Name not provided".
        notes (str): Additional notes about the user. Defaults to "Notes not provided".
    """
    add_user(email, name, notes)
    send_pushover_notification("New User Recorded", f"Recording interest from {name} with email: {email}. Notes: {notes}")

    return "OK"

def record_unknown_question(question: str):
    """
    Record a question that the digital twin could not answer.
    
    Args:
        question (str): The question that could not be answered.
    """

    send_pushover_notification("Unknown Question Recorded", f"The following question could not be answered: {question}")

    return "OK"

record_user_details_json = {
    "type": "function",
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in getting in contact with the engineer and must have provided at least their email address.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The user's email address."
            },
            "name": {
                "type": "string",
                "description": "The user's name, if they provided it."
            },
            "notes": {
                "type": "string",
                "description": "Any additional info about the conversation that is worth recording to give context to the engineer",
            },
        },
        "additionalProperties": False,
        "required": ["email"],
    },
}

record_unknown_question_json = {
    "type": "function",
    "name": "record_unknown_question",
    "description": "Use this tool to record any question that you could not answer.",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question that you could not answer.",
            },
        },
        "additionalProperties": False,
        "required": ["question"],
    },
}


tools = [record_user_details_json, record_unknown_question_json, 
         
         {
             "type": "file_search",
             "vector_store_ids": [vector_store_id],
             "max_num_results": 5,
         },
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}

def handle_tool_calls(tool_calls: list):
    """
    Handle tool calls made by the digital twin.

    Args:
        tool_calls (list): A list of tool calls made by the digital twin.

    Returns:
        tool_results (list): A list of results from the tool calls.
    """
    tool_results = []
    for tool_call in tool_calls:
        tool_name = tool_call.name
        tool_args = json.loads(tool_call.arguments)
        print(f"Tool call: {tool_name} with arguments: {tool_args}")
        tool_function = tool_map.get(tool_name)
        result = tool_function(**tool_args) if tool_function else f"Tool not found: {tool_name}"
        tool_results.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": json.dumps(result),
        })

    return tool_results
