from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from openai import AzureOpenAI
import os
from pydantic import BaseModel
from dotenv import load_dotenv
from prompts import system_prompt_sahil

# Load environment variables from .env file - makes sure our API keys stay secure
load_dotenv()

# Create our FastAPI application instance
app = FastAPI()

# Set up static file serving for CSS, JavaScript, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 for HTML templating - helps us render dynamic web pages
templates = Jinja2Templates(directory="templates")

# Set up our connection to Azure OpenAI 
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Get the specific AI model we're using from environment variables
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Define the structure for chat requests coming from the frontend
class ChatRequest(BaseModel):
    message: str

# Route for the main page - serves our chat interface
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint that processes chat messages and returns AI responses
@app.post("/chat")
async def chat(chat_request: ChatRequest):
    user_message = chat_request.message
    
    # Use your own personality for the AI responses
    system_prompt = system_prompt_sahil
    
    try:
        # Send the user's message to Azure OpenAI and get a response
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=250,  # Limit response length to keep it concise
            temperature=0.7,  # Add some creativity but not too random
            n=1  # Just get one response option
        )

        # Extract and clean up the response text
        answer = response.choices[0].message.content.strip()
        return {"answer": answer}
    except Exception as e:
        # Log any errors
        print(f"Azure OpenAI API Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Start the web server 
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
