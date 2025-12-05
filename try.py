import os
from google import genai
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
    SYSTEM_INSTRUCTION = (
        "You are a specialized chatbot for the Indian Constitution. Your primary function is to "
        "provide accurate and detailed answers about the provisions, articles, parts, and judicial "
        "interpretations of the Constitution of India. All answers must be strictly framed within "
        "this context, using the formal language of constitutional law. If you cannot find a specific "
        "constitutional answer, give a general, helpful, and contextually relevant answer, but NEVER "
        "admit to lacking information. Always aim for clarity and legal precision."
    )

    try:
        # Initialize the client. It automatically uses the GEMINI_API_KEY environment variable.
        client = genai.Client(api_key="AIzaSyBKUHzWZpY11cTnwCOaa34H2i3e_NezCPs")

        # --- 2. Configure the Google Search Tool ---
        # This allows the model to search the web for current, factual information.
        search_tool = types.Tool(google_search=types.GoogleSearch())

        # Combine configurations
        config = types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            tools=[search_tool]
        )

        print(f"-> Asking the bot: '{prompt}'")
        print("-" * 30)

        # --- 3. Call the Gemini API ---
        response = client.models.generate_content(
            model='gemini-2.5-flash', # A fast and capable model for grounded chat
            contents=prompt,
            config=config,
        )

        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

# --- Example Usage ---

if __name__ == "__main__":
    # # Example 1: A specific, factual question requiring the Search tool
    # question_1 = "What are the six fundamental freedoms guaranteed by Article 19?"
    # answer_1 = ask_constitution_bot(question_1)
    # print("✅ Constitutional Bot Response:")
    # print(answer_1)
    
    # print("\n" + "="*50 + "\n")

    # Example 2: A general question where the persona is maintained
    question_2 =  "What is 2nd ammendment"
    answer_2 = ask_constitution_bot(question_2)
    print("✅ Constitutional Bot Response:")
    print(answer_2)
