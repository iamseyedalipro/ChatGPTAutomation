from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

app = FastAPI()
chat = None

@app.on_event("startup")
def startup_event():
    global chat
    try:
        chat = ChatGPTAutomation()
        chat.DelayTimes.CHECK_RESPONSE_STATUS_DELAY = 2
        chat.DelayTimes.SEND_PROMPT_DELAY = 2
        chat.DelayTimes.OPEN_NEW_CHAT_DELAY = 4
    except Exception as e:
        print(f"Error initializing ChatGPT Automation: {e}")

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Prompt(BaseModel):
    prompt: str

@app.post("/send_prompt/")
async def generate_response(prompt: Prompt):
    if chat is None:
        return {"message": "ChatGPT Automation is not ready yet"}, 503

    try:
        # Assuming these methods are synchronous; if not, they should be managed accordingly.
        chat.send_prompt_to_chatgpt(prompt.prompt)
        if chat.check_response_status():
            response = chat.return_last_response()
            chat.open_new_chat()
            return {"response": response}
        else:
            chat.open_new_chat()
            return {"message": "Error generating response"}, 400
    except Exception as e:
        return {"message": str(e)}, 500
