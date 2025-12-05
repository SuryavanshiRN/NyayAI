# NyayAI — AI for Your Nyay 🏛️

**NyayAI** is an AI-powered legal assistant designed to provide accessible, practical, and lawful guidance based on Indian law. Built as an academic project, NyayAI helps users understand legal provisions, navigate the Indian legal system, and receive clear, actionable advice on various legal matters.

## 🌟 Features

- **Legal Guidance**: Provides guidance based on Indian legal frameworks including IPC, CrPC, Constitution, IT Act, and Consumer Protection Act
- **AI-Powered Responses**: Leverages Google's Gemini 2.5 Flash model with Google Search integration for accurate and up-to-date information
- **User-Friendly Interface**: Clean, modern web interface with an intuitive chatbot experience
- **Constitutional Knowledge**: Specialized in Indian Constitutional law and legal provisions
- **Actionable Advice**: Delivers step-by-step guidance with clear, practical instructions
- **Secure & Privacy-Focused**: Does not store personal information or user queries

## 🚀 Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 2.5 Flash API
- **Frontend**: HTML, CSS, JavaScript
- **CORS Support**: Flask-CORS for cross-origin requests
- **Data**: JSON-based knowledge base with constitutional and legal information

## 📁 Project Structure

```
├── app.py                          # Main Flask application
├── core.py                         # AI chatbot core logic (Gemini API integration)
├── front.py                        # Frontend testing script
├── try.py                          # Testing/development script
├── combined_qa.json                # Combined Q&A dataset
├── constitution_enhanced (1).json  # Enhanced constitutional data
├── constitution_of_india.json      # Constitution of India data
├── templates/                      # HTML templates
│   ├── index.html                 # Main chat interface
│   ├── login.html                 # Login page
│   ├── dashboard.html             # User dashboard
│   └── bye.html                   # Goodbye page
├── static/                        # Static assets
│   ├── assembly.webp              # Assembly image
│   └── constitution.webp          # Constitution image
└── logic/                         # Additional logic modules
```

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key

### Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd "PBL - NyayAI\Code"
   ```

2. **Install required dependencies**:

   ```bash
   pip install flask flask-cors google-genai
   ```

3. **Configure API Key**:

   - Open `core.py`
   - Replace the API key with your own Google Gemini API key:
     ```python
     client = genai.Client(api_key="YOUR_API_KEY_HERE")
     ```

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`

## 📖 Usage

### Web Interface

1. Start the Flask server by running `app.py`
2. Navigate to the login page at `http://localhost:5000`
3. Access the chat interface through the index page
4. Ask legal questions in natural language
5. Receive structured responses with:
   - Relevant legal sections
   - Plain-language explanations
   - Step-by-step actionable guidance
   - Important notes and cautions
   - Confidence level

### Command Line Testing

Use `front.py` for quick testing:

```bash
python front.py
```

Enter your query when prompted, and the bot will return a response.

## 🤖 AI Response Format

NyayAI provides responses in a structured format:

```
Relevant Law: <Applicable legal sections or acts>

Explanation: <Plain-language meaning>

What to Do:
- Step 1
- Step 2
- Step 3

Important Note: <Risk, caution, or practical awareness>

Confidence: High / Medium / Low
```

## 🛡️ Security & Privacy

- **No Personal Data Storage**: NyayAI does not store or retain user information
- **No Personal Details Required**: Users are not asked to provide personal information
- **Responsible Guidance**: Does not encourage illegal, harmful, or confrontational actions
- **Emergency Situations**: Advises contacting police or legal authorities for dangerous situations

## 🎯 Core Responsibilities

- Identify relevant legal sections from Indian law
- Explain laws in simple, everyday language
- Provide clear, actionable steps for users
- Include FIR filing guidance where appropriate
- Maintain a supportive and respectful tone

## 📊 API Endpoints

### `GET /`

Returns the login page

### `GET /index`

Returns the main chat interface

### `GET /dashboard`

Returns the user dashboard

### `GET /bye`

Returns the goodbye page

### `POST /ask`

Accepts a legal query and returns AI-generated guidance

**Request Body**:

```json
{
  "prompt": "Your legal question here"
}
```

**Response**:

```json
{
  "response": "AI-generated legal guidance"
}
```

## 🔍 Data Sources

The project includes several JSON files containing:

- Indian Constitution articles and provisions
- Combined Q&A datasets for common legal queries
- Enhanced constitutional knowledge base

## ⚠️ Disclaimer

NyayAI is an educational project designed to provide general legal information based on Indian law. It is **not a substitute for professional legal advice**. For specific legal matters, always consult a qualified lawyer or legal professional.

## 🤝 Contributing

This is an academic project. Contributions, suggestions, and feedback are welcome:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📝 License

This project is developed as part of an academic curriculum (PBL - Project Based Learning).

## 👥 Authors

Developed as an Academic Project at PBL - NyayAI

## 🙏 Acknowledgments

- Google Gemini AI for powering the chatbot
- Indian Constitution and legal frameworks
- Flask framework and community
- All contributors and testers

---

**Note**: Remember to keep your API keys secure and never commit them to public repositories. Consider using environment variables for sensitive configuration.
