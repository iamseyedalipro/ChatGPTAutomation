# ChatGPTAutomation 🤖💻🧠

## Description
ChatGPTAutomation is a Python package that automates interactions with ChatGPT using Selenium, streamlining the process for developers and testers. 🚀

## Features
- Automated messaging to ChatGPT. 📩
- File upload support. 📁
- ChatGPT conversation retrieval and storage. 🗂️
- Customizable WebDriver for browser management. 🌐

## Installation
Install with:
```bash
pip install ChatGPTAutomation
```

## Usage

**Chrome WebDriver Download**:

- **Latest Chrome Version**: Download [here](https://googlechromelabs.github.io/chrome-for-testing/).
- **Older Chrome Versions**: Find compatible drivers [here](https://chromedriver.chromium.org/downloads).

**Setup**:

Automatic setup (without paths):
```python
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

chat_bot = ChatGPTAutomation(
    username="<your username here>", # Optional
    password="<your password here>"  # Optional
)
```

Manual setup (with paths):
```python
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

chat_bot = ChatGPTAutomation(chrome_path="path/to/chrome.exe", chrome_driver_path="path/to/chromedriver.exe",
username="<your username here>", # Optional
password="<your password here>" # Optional
)

# Send prompt
chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")

# Save conversation
chat_bot.save_conversation("conversation.txt")
```

File upload:
```python
chat_bot.upload_file_for_prompt("test_file.txt")
chat_bot.send_prompt_to_chatgpt("Explain this file?")
```

Check response status:
```python
if chat_bot.check_response_status():
    print("Response ready.")
else:
    print("Response issue.")
```

Get last response:
```python
chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")
response = chat_bot.return_last_response()
```

Switch models:
```python
chat_bot.switch_model(4)
```

Login check:
```python
if chat_bot.check_login_page():
    chat_bot.login()
```

## Requirements
- Python 3.8+
- Selenium==4.9.0
- See `requirements.txt` for more.

## License
MIT License - see [LICENCE.md](LICENCE.md).

## Contact
Seyed Ali Hosseini 🧑‍💻 - iamseyedalipro@gmail.com 📧.

## Acknowledgements
- Thanks to OpenAI and Selenium. 🙏👨‍💻