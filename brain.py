from ollama import chat
from config import MODEL_NAME, SYSTEM_PROMPT


def ask_ai(question):
    """
    Send a question to Ollama and return the response.
    """

    try:

        response = chat(

            model=MODEL_NAME,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": question
                }

            ]

        )

        return response["message"]["content"]

    except Exception as e:

        return f"Error talking to Ollama: {e}"