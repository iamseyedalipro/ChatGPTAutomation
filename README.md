
# ChatGPTAutomation 🤖💻🧠

## Description
ChatGPTAutomation is a Python package that automates interactions with ChatGPT using Selenium, streamlining the process for developers and testers. 🚀

## Features
- Automated messaging to ChatGPT. 📩
- File upload support. 📁
- ChatGPT conversation retrieval and storage. 🗂️
- Customizable WebDriver for browser management. 🌐
- Configurable delays for various operations. ⏲️

## Installation
Install with:
```bash
pip install ChatGPTAutomation
```

## Usage

### Chrome WebDriver Download

- **Latest Chrome Version**: Download [here](https://googlechromelabs.github.io/chrome-for-testing/).
- **Older Chrome Versions**: Find compatible drivers [here](https://chromedriver.chromium.org/downloads).

### Setup

#### Automatic setup (without paths):
```python
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

chat_bot = ChatGPTAutomation(
    username="<your username here>", # Optional
    password="<your password here>"  # Optional
)
```

#### Manual setup (with paths):
```python
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

chat_bot = ChatGPTAutomation(
    chrome_path="path/to/chrome.exe", 
    chrome_driver_path="path/to/chromedriver.exe",
    username="<your username here>", # Optional
    password="<your password here>"  # Optional
)

# Send prompt
chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")

# Save conversation
chat_bot.save_conversation("conversation.txt")
```

### File upload
```python
chat_bot.upload_file_for_prompt("test_file.txt")
chat_bot.send_prompt_to_chatgpt("Explain this file?")
```

### Check response status
```python
if chat_bot.check_response_status():
    print("Response ready.")
else:
    print("Response issue.")
```

### Get last response
```python
chat_bot.send_prompt_to_chatgpt("Hello, ChatGPT!")
response = chat_bot.return_last_response()
```

### Switch models
```python
chat_bot.switch_model(4)
```

### Login check
```python
if chat_bot.check_login_page():
    chat_bot.login()
```

### Login with Gmail

The `gmail_login_setup` function in `ChatGPTAutomation` allows you to automate the process of logging into ChatGPT using a Gmail account.

#### Automatic Gmail Login
To automatically log in using Gmail credentials, you can use the `gmail_login_setup` method. This method requires the email and password to be set either as parameters or within the class instance.

```python
# Automatic login using stored credentials
chat_bot.gmail_login_setup()

# Alternatively, specify the credentials directly
chat_bot.gmail_login_setup(email="your.email@gmail.com", password="yourpassword")
```

#### Login with google
if you logged in to the google account but logged out from openai account can use this function for login with that gmail
```python
chat_bot.login_using_gamil("iamseyedalipro@gmail.com") #this is optional you can set the email first of setup on username field
```



---
## Delay Configurations

The `ChatGPTAutomation` class includes configurable delays for various operations, defined in the `DelayTimes` class:

- `CONSTRUCTOR_DELAY`: Time to wait for initialization.
- `SEND_PROMPT_DELAY`: Delay after sending a prompt to ChatGPT.
- `UPLOAD_FILE_DELAY`: Delay following a file upload.
- `RETURN_LAST_RESPONSE_DELAY`: Wait time to fetch the last response.
- `OPEN_NEW_CHAT_DELAY`: Delay in opening a new chat session.
- `DEL_CURRENT_CHAT_OPEN_MENU_DELAY`: Wait time before deleting current chat.
- `DEL_CURRENT_CHAT_AFTER_DELETE_DELAY`: Delay after deleting current chat.
- `DEL_CURRENT_CHAT_BEFORE_OPEN_NEW_CHAT_DELAY`: Wait time before opening new chat after deletion.
- `CHECK_RESPONSE_STATUS_DELAY`: Interval to check response status.

These delays are crucial for the stability and reliability of automated interactions with ChatGPT.


## Customizing Delay Times

The `ChatGPTAutomation` class comes with default delay settings for various operations, suitable for most use cases. However, you might find the need to adjust these delay times based on your network speed, system performance, or specific use case requirements. Here’s how you can customize these delay times.

### Accessing Delay Times

The delay settings are part of the `DelayTimes` inner class in `ChatGPTAutomation`. They are defined as class variables and can be accessed directly using the class name.

### Changing Delay Times

To change the delay times, access the respective variable in the `DelayTimes` class and set it to your desired value (in seconds). Here’s an example of how to do this:

```python
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

# Access and modify delay times
ChatGPTAutomation.DelayTimes.CONSTRUCTOR_DELAY = 10  # Set constructor delay to 10 seconds
ChatGPTAutomation.DelayTimes.SEND_PROMPT_DELAY = 25  # Set send prompt delay to 25 seconds
# ... similarly for other delay times

# Initialize ChatGPTAutomation with customized delay times
chat_bot = ChatGPTAutomation(
    username="<your username here>",
    password="<your password here>"
)

# The rest of your code...
```

### Recommended Practices

- **Testing**: When changing delay times, it's recommended to test the interaction with ChatGPT to ensure that the new settings work well in your environment.
- **Incremental Adjustments**: Make incremental adjustments and test each change rather than making large changes all at once.
- **Network Speed Consideration**: If you are working with a slow network connection, consider increasing the delay times to allow for longer response times from ChatGPT.

By following these steps and recommendations, you can fine-tune the behavior of the `ChatGPTAutomation` class to best fit your automation needs.

---

## Requirements
- Python 3.8+
- Selenium==4.9.0
- See `requirements.txt` for more.

## To-Do List

### Sign up:
- ✅ User login
- ⬜️ Sign up via email address

### Conversation Management:
- ✅ Create new conversation
- ✅ Get message list in a conversation
- ✅ Delete a conversation
- ⬜️ Edit Conversation Name
- ⬜️ Subscribe for realtime message
- ⬜️ Handle Random message such as popup, hints, and login attempts

### Advanced Features:
- ✅ Support for uploading files
- ⬜️ Support ChatGPT with internet
- ⬜️ Using GPTs
- ⬜️ API

### User Account Handling:
- ✅ Switch Between ChatGPT 3.5 and 4
- ⬜️ Fetch user detail like email and plan type
- ⬜️ Set custom instructions for more personalized conversations

### Browser:
- ⬜️ Headless Browser

## License
MIT License - see [LICENCE.md](LICENCE.md).

## Contact
Seyed Ali Hosseini 🧑‍💻 - iamseyedalipro@gmail.com 📧.

## Acknowledgements
- Thanks to OpenAI and Selenium. 🙏👨‍💻