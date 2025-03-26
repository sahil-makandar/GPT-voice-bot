# GPT-voice-bot
This project is a voice-enabled assistant that uses Azure OpenAI to impersonate a specific personality and provide intelligent responses to your questions. The application features a clean, modern interface with speech recognition capabilities.

## Features

- 🎤 Voice recognition 
- 🤖 AI-powered personality impersonation using Azure OpenAI
- 💬 Text-to-speech functionality to hear responses
- 🎨 Clean, modern UI with a tech-inspired design
- 👤 Customizable personality profiles through prompt engineering

## Easy Setup

### Prerequisites

- Python 3.8 or higher
- A web browser that supports speech recognition (Chrome recommended)
- Azure OpenAI API access

### Installation

1. **Set up environment variables**: Add your Azure OpenAI Credentials in the `.env` file in the project root:

```
AZURE_OPENAI_API_KEY="your-api-key-here"
AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT_NAME="your-deployment-name"
```

2. **One-step setup**: Run the following command in your terminal to install and start the application:

```bash
pip install -r requirements.txt && python app.py
```

3. **Open the application**: Visit [http://localhost:8000](http://localhost:8000) in your web browser

That's it! The application is now running and ready to use.

## How to Use

1. Click the "Tap & Speak Question" button
2. Ask your question using your voice
3. Wait for the AI to process and respond with the configured personality
4. The response will be displayed and spoken aloud

## Project Structure

```
GPT Personality Voice Bot/
├── app.py                 # Main FastAPI application
├── prompts.py             # AI system prompts with personality configuration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── static/                
│   └── js/
│       └── main.js        # JavaScript for voice recognition
└── templates/
    └── index.html         # Main application interface
```

## Customizing the Personality

To change the personality that the bot impersonates, edit the `prompts.py` file and modify the system prompt with the desired personality details.


## License

MIT

## Contact

For questions or support, please contact:
- Email: mahaboobsab.goa@gmail.com
- LinkedIn: [Mahaboobsab Makandar](https://www.linkedin.com/in/mahaboobsab-makandar)
