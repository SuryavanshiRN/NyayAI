import os
import google.genai as genai
from google.genai import types

def ask_constitution_bot(prompt: str) -> str:
    """
    Asks the specialized Constitutional chatbot a question using the Gemini API.

    This function configures the model with:
    1. A System Instruction to maintain the Constitutional expert persona.
    2. The Google Search tool for grounded, up-to-date factual answers.

    Args:
        prompt: The user's question (e.g., "What does Article 22 say?").

    Returns:
        The model's generated response as a string.
    """
    
    # --- 1. Define the Constitutional Persona (System Instruction) ---
    '''SYSTEM_INSTRUCTION = (
        "You are a specialized chatbot for the Indian Constitution. Your primary function is to "
        "provide accurate and detailed answers about the provisions, articles, parts, and judicial "
        "interpretations of the Constitution of India. All answers must be strictly framed within "
        "this context, using the formal language of constitutional law. If you cannot find a specific "
        "constitutional answer, give a general, helpful, and contextually relevant answer, but NEVER "
        "admit to lacking information. Always aim for clarity and legal precision."
        "Strictly give all responses by considering Indian Constitution only."
    )
'''
    try:
        client = genai.Client(api_key="AIzaSyBKUHzWZpY11cTnwCOaa34H2i3e_NezCPs")


        search_tool = types.Tool(google_search=types.GoogleSearch())

    
        config = types.GenerateContentConfig(
           # system_instruction=SYSTEM_INSTRUCTION,
            tools=[search_tool]
        )

        print(f"-> Asking the bot: '{prompt}'")
        print("-" * 30)

   
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt,
            config=config,
        )

        return response.text

    except Exception as e:
        return f"An error occurred: {e}"