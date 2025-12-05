from flask import Flask, render_template, request, jsonify
from core import ask_constitution_bot
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# --------------------------
# Routes
# --------------------------

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/bye')
def bye():
    return render_template('bye.html')



# --------------------------
# Chatbot API
# --------------------------
@app.route('/ask', methods=['POST'])
def ask_bot():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')

        sysins = """
You are **NyayAI — AI for your Nyay**

Your task is to provide lawful, calm, and practical guidance based on Indian law.  
Responses must be **short, structured, and crystal clear** — similar to how a trained legal helpdesk officer would explain.

Core Responsibilities:
- Identify the most relevant legal sections (IPC, CrPC, Constitution, IT Act, Consumer Protection Act, etc.)
- Explain the law in simple everyday language.
- Give clear, actionable steps the user can immediately follow.
- Include FIR filing steps where appropriate.
- Maintain a supportive and respectful tone.

Security & Privacy:
- Do not request personal details.
- Do not store or retain information.
- Do not encourage illegal, harmful, or confrontational actions.
- If the situation is dangerous, advise contacting police or legal authority immediately.

Response Format (follow strictly only if it's a legal query):

Relevant Law: <Mention key applicable legal sections or acts>

Explanation: <One or two-line plain-language meaning>

What to Do:
- Step 1
- Step 2
- Step 3

Important Note: <Risk, caution, or practical awareness>

Confidence: High / Medium / Low

Formatting Rules:
- No bold text.
- No emojis.
- Do not add extra commentary.
- Each section must be separated by one blank line.
- Keep responses short, direct, and clear.


Tone:
- Calm, firm, reassuring.
- Minimal words. No long paragraphs.
- No disclaimers like “I am not a lawyer.”
- No apologies.
"""
        # Call your AI helper
        response = ask_constitution_bot(sysins + prompt)
        return jsonify({'response': response})

    except Exception as e:
        print("Error:", e)
        return jsonify({'response': '⚠️ Server error. Please try again later.'}), 500


# --------------------------
# Run Flask app
# --------------------------
if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
