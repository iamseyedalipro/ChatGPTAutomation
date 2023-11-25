# ChatGPTAutomation

## Description
ChatGPTAutomation is a Python package designed to automate interactions with ChatGPT using Selenium. It simplifies the process of sending prompts, managing responses, and handling files in the ChatGPT interface, making it an ideal tool for developers and testers who require automated ChatGPT interactions.

## Features
- Automated sending of messages to ChatGPT.
- Support for file uploads to ChatGPT.
- Retrieval and storage of ChatGPT conversations.
- Customizable WebDriver settings for browser management.

## Installation
To install ChatGPTAutomation, simply run:
```bash
pip install ChatGPTAutomation
```

## Usage

Before using the `ChatGPTAutomation` package, it is essential to download the Chrome WebDriver. The version of the WebDriver must match the version of your Google Chrome browser. 

For downloading the Chrome WebDriver:

- **Latest Version of Chrome WebDriver**: 
  If you are using the latest version of Google Chrome, download the corresponding latest version of Chrome WebDriver from:
  [Chrome WebDriver - Latest Version](https://googlechromelabs.github.io/chrome-for-testing/)

- **Older Versions of Chrome WebDriver**: 
  If you are using an older version of Google Chrome, find and download the compatible version of Chrome WebDriver from:
  [Chrome WebDriver - Older Versions](https://chromedriver.chromium.org/downloads)

Ensure that the version of Chrome WebDriver you download matches the version of your Google Chrome browser to avoid compatibility issues. 
---
Import the package and use it in your Python scripts as follows:

```python
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

# Initialize with path to Chrome and ChromeDriver
chat_bot = ChatGPTAutomation(chrome_path="path/to/chrome.exe", chrome_driver_path="path/to/chromedriver.exe"
username="<your username here>", # Optional
password="<your password here>" # Optional
)

# Example: Sending a prompt
chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")

# Retrieve and save conversation
chat_bot.save_conversation("conversation.txt")
```

Send file with prompt:
```python
chat_bot.upload_file_for_prompt("test_file.txt")
chat_bot.send_prompt_to_chatgpt("Please explain to me what is in this file?")
```

check_response_status function:
```python
if chat_bot.check_response_status():
    print("Response is ready and complete.")
    # You can now proceed to retrieve or process the response.
else:
    print("There was an issue in generating the response.")
```

get the last response using return_last_response function:
```python
chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")
response = chat_bot.return_last_response()
```

switch between the chatgpt models: (In this example, we switched to version 4 you can use 3.5)
```python
chat_bot.switch_model(4)
```

check login page:
```python
if chat_bot.check_login_page():
    chat_bot.login()
```


## Requirements
- Python 3.8 or higher
- Selenium==4.9.0
- Other dependencies can be found in `requirements.txt`

## License
This project is licensed under the MIT License - see the [LICENCE.md](LICENCE.md) file for details.

## Contact
For questions or feedback, please contact Seyed Ali Hosseini at iamseyedalipro@gmail.com.

## Acknowledgements
- OpenAI for ChatGPT
- Selenium contributors
