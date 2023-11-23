## Project Overview

This project, named "ChatGPT Automation", leverages Selenium WebDriver to automate interactions with OpenAI's ChatGPT. It provides a comprehensive set of functionalities, including sending messages, uploading files, handling chat sessions, and managing browser instances. This tool is especially useful for automating tasks, testing, or data collection from ChatGPT.

## Features

- **Automated Chat Interaction**: Send prompts to ChatGPT and retrieve responses programmatically.
- **File Upload Capability**: Automate the process of uploading files to ChatGPT.
- **Conversation Management**: Save entire conversations, start new chats, and delete existing chats.
- **Error Handling**: Detect and handle errors during chat interactions.
- **Human Verification Support**: Pause automation for manual human verification steps.
- **Clipboard Integration**: Copy and retrieve ChatGPT responses via the clipboard.
- **Remote Browser Control**: Utilize remote debugging to control an existing Chrome browser session.
- **Logging**: Detailed logging for troubleshooting and analysis.

## Installation

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- Chromedriver (compatible with your Chrome version)

### Setup

1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```

2. Install required Python packages:
   ```bash
   pip install selenium
   pip install pyperclip
   ```

3. Ensure Chrome and Chromedriver are installed and compatible.

## Usage

1. **Initialization**: Create an instance of `ChatGPTAutomation` class.
   ```python
   from chatgpt_automation import ChatGPTAutomation

   automation = ChatGPTAutomation(chrome_path="path_to_chrome.exe",
                                  chrome_driver_path="path_to_chromedriver.exe")
   ```

2. **Sending Prompts**: Use `send_prompt_to_chatgpt` to send messages.
   ```python
   automation.send_prompt_to_chatgpt("Hello, ChatGPT!")
   ```

3. **Uploading Files**: Use `upload_file_for_prompt` to upload files.
   ```python
   automation.upload_file_for_prompt("example.txt")
   ```

4. **Managing Conversations**: Save, delete, or start new chats using respective methods.
   ```python
   automation.save_conversation("chat_log.txt")
   automation.del_current_chat()
   automation.open_new_chat()
   ```

5. **Closing Session**: Properly close the browser and WebDriver session.
   ```python
   automation.quit()
   ```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Support and Contact

If you encounter any issues or have questions, please [open an issue](https://github.com/your-repository/issues) on GitHub.

---

*Note: This project is not affiliated with OpenAI. It's a community-driven project intended for educational purposes.*