from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import socket
import threading
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import logging
import pyperclip
# Configure logging
logging.basicConfig(filename='chatgpt_automation.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class ChatGPTXpath:
    MSG_BOX_INPUT = (By.CSS_SELECTOR, 'textarea#prompt-textarea')
    SEND_MSG_BTN = (By.CSS_SELECTOR, 'button[data-testid="send-button"]')
    GPT4_HOVER_BTN = (By.CSS_SELECTOR, 'button[id="radix-:rm:"]')
    GPT4_TPYE_FILE_BTN = (
        By.XPATH, 'div[role="menuitemradio"][aria-checked="false"] > span[title="Advanced Data Analysis"]')
    GPT4_FILE_INPUT = (By.CSS_SELECTOR, 'input.hidden')
    GPT4_FILE_INPUT2 = (By.XPATH, '<input multiple="" type="file" tabindex="-1" class="hidden" style="display: none;">')
    CHAT_GPT_CONVERSION = (By.CSS_SELECTOR, 'div.text-base')
    REGENERATE_BTN = (By.CSS_SELECTOR, 'button[as="button"]')

    FIRST_DELETE_BTN = (By.CSS_SELECTOR, 'button[data-state="closed"]')
    SECOND_DELETE_BTN = (By.CSS_SELECTOR, 'div[role="menuitem"].text-red-500')
    THIRD_DELETE_BTN = (By.CSS_SELECTOR, 'button.btn.btn-danger[as="button"]')

    RECYCLE_BTN = (By.CSS_SELECTOR, 'button.p-1.hover\:text-token-text-primary:nth-child(2)')
    DELETE_CONFIRM_BTN = (By.CSS_SELECTOR, 'button.btn.relative.btn-danger')

    NEW_CHAT_BTN = (By.CSS_SELECTOR, 'button.text-token-text-primary')


class ChatGPTAutomation:

    def __init__(self, chrome_path, chrome_driver_path):
        """
        This constructor automates the following steps:
        1. Open a Chrome browser with remote debugging enabled at a specified URL.
        2. Prompt the user to complete the log-in/registration/human verification, if required.
        3. Connect a Selenium WebDriver to the browser instance after human verification is completed.

        :param chrome_path: file path to chrome.exe (ex. C:\\Users\\User\\...\\chromedriver.exe)
        :param chrome_driver_path: file path to chrome.exe (ex. C:\\Users\\User\\...\\chromedriver.exe)
        """
        self.lock = threading.Lock()
        user_data_dir = r'--user-data-dir=C:\path\to\custom\user\data\directory'
        chrome_path = f'"{chrome_path}" {user_data_dir}'
        self.chrome_path = chrome_path
        self.chrome_driver_path = chrome_driver_path

        self.url = r"https://chat.openai.com"
        free_port = self.find_available_port()
        self.launch_chrome_with_remote_debugging(free_port, self.url)
        self.wait_for_human_verification()
        self.driver = self.setup_webdriver(free_port)
        time.sleep(4)

    def find_available_port(self):
        """
        Finds and returns an available port number on the local machine.
        It does this by creating a temporary socket, binding it to an ephemeral port,
        and then closing the socket to free the port for use.

        Returns:
            available_port (int): The available port number found.

        Raises:
            Exception: If the function fails to find an available port due to a socket error.
        """
        try:
            # Create a socket object using IPv4 addressing and TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Bind the socket to any available address on the machine ('') and port 0
                # The OS will then automatically assign an available ephemeral port
                s.bind(('', 0))

                # Set socket options - SO_REUSEADDR allows the socket to be bound to an address
                # that is already in use, which is useful for avoiding socket errors
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # Retrieve the port number assigned by the OS
                available_port = s.getsockname()[1]

                # Log the found available port
                logging.info(f"Available port found: {available_port}")

                # Return the found port
                return available_port

        except socket.error as e:
            # Log the error in case of a socket exception
            logging.error(f"Failed to find an available port: {e}")

            # Raise a new exception for the calling code to handle
            raise Exception("Failed to find an available port") from e

    def launch_chrome_with_remote_debugging(self, port, url):
        """
        Launches a new Chrome browser instance with remote debugging enabled. This method allows for
        Selenium WebDriver to connect to a pre-existing Chrome session.

        Args:
            port (int): The port number to use for remote debugging.
            url (str): The URL to navigate to when the browser opens.

        Raises:
            RuntimeError: If there is an error in launching the Chrome browser.
        """

        def open_chrome():
            try:
                # Construct the command to launch Chrome with specified debugging port and URL
                chrome_cmd = f"{self.chrome_path} --remote-debugging-port={port} --user-data-dir=remote-profile {url}"
                # Execute the command in the system shell
                os.system(chrome_cmd)
            except Exception as e:
                # Log and raise an exception if there's an error in launching Chrome
                logging.error(f"Failed to launch Chrome: {e}")
                raise RuntimeError(f"Failed to launch Chrome with remote debugging: {e}")

        try:
            # Create a new thread to run the Chrome launch command
            chrome_thread = threading.Thread(target=open_chrome)
            # Start the thread
            chrome_thread.start()
        except Exception as e:
            # Log and raise an exception if there's an error in starting the thread
            logging.error(f"Failed to start Chrome launch thread: {e}")
            raise RuntimeError(f"Failed to start thread for launching Chrome: {e}")

    def setup_webdriver(self, port):
        """
        Initializes and returns a Selenium WebDriver instance that is connected to an existing
        Chrome browser with remote debugging enabled. This method is crucial for controlling
        an already opened browser instance.

        Args:
            port (int): The port number on which the remote debugging of the Chrome browser is enabled.

        Returns:
            webdriver.Chrome: An instance of Chrome WebDriver connected to the existing browser session.

        Raises:
            WebDriverException: If there is an issue initializing the WebDriver.
        """

        try:
            # Setting up Chrome options for WebDriver
            chrome_options = webdriver.ChromeOptions()
            # Specifying the address for the remote debugging
            chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")

            # Initializing the Chrome WebDriver with the specified options
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=chrome_options)
            return driver
        except Exception as e:
            # Log the exception if WebDriver initialization fails
            logging.error(f"Failed to initialize WebDriver: {e}")
            # Raising a WebDriverException to indicate failure in WebDriver setup
            raise webdriver.WebDriverException(f"Error initializing WebDriver: {e}")

    def send_prompt_to_chatgpt(self, prompt):
        """
        Sends a message to ChatGPT via the web interface and waits for a response. This function
        automates the process of entering a prompt into the ChatGPT input box and triggering the send action.

        Args:
            prompt (str): The message or prompt to be sent to ChatGPT.

        Raises:
            WebDriverException: If there is an issue interacting with the web elements or sending the prompt.
        """

        try:
            # Locate the input box element on the webpage
            input_box = self.driver.find_element(*ChatGPTXpath.MSG_BOX_INPUT)
            # Use JavaScript to input the prompt into the input box
            self.driver.execute_script("arguments[0].value = arguments[1];", input_box, prompt)
            # Simulate the key press action to send the prompt
            input_box.send_keys(Keys.RETURN)
            # Locate and click the send button to submit the prompt
            send_button = self.driver.find_element(*ChatGPTXpath.SEND_MSG_BTN)
            send_button.click()
            # Wait for the response to be generated (20 seconds)
            time.sleep(20)
        except Exception as e:
            # Log the exception if any step in the process fails
            logging.error(f"Failed to send prompt to ChatGPT: {e}")
            # Raising a WebDriverException to indicate failure in sending the prompt
            raise webdriver.WebDriverException(f"Error sending prompt to ChatGPT: {e}")

    def upload_file_for_prompt(self, file_name):
        """
        Uploads a file to ChatGPT via the web interface. This function automates the process of
        selecting a file for upload through the ChatGPT's file input element.

        Args:
            file_name (str): The name of the file to be uploaded.

        Raises:
            FileNotFoundError: If the specified file does not exist in the current working directory.
            WebDriverException: If there is an issue interacting with the file upload element on the web page.
        """

        try:
            # Construct the full file path using the current working directory
            file_path = os.path.join(os.getcwd(), file_name)

            # Check if the file exists before attempting to upload
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file '{file_path}' does not exist.")

            # Locate the file input element on the webpage
            file_input = self.driver.find_element(*ChatGPTXpath.GPT4_FILE_INPUT)
            # Send the file path to the file input element, initiating the upload
            file_input.send_keys(file_path)
            # Wait for the upload process to complete (10 seconds)
            time.sleep(10)
        except FileNotFoundError as e:
            # Log the exception if the file is not found
            logging.error(f"File not found for upload: {e}")
            # Re-raise the exception to be handled by the calling code
            raise
        except Exception as e:
            # Log any other exception that occurs during the file upload process
            logging.error(f"Failed to upload file to ChatGPT: {e}")
            # Raising a WebDriverException to indicate failure in file upload
            raise WebDriverException(f"Error uploading file to ChatGPT: {e}")


    def return_chatgpt_conversation(self):
        """
        :return: returns a list of items, even items are the submitted questions (prompts) and odd items are chatgpt response
        """

        return self.driver.find_elements(by=By.CSS_SELECTOR, value='div.text-base')

    def save_conversation(self, file_name):
        """
        Saves the entire conversation from the ChatGPT interface into a text file. The conversation is formatted
        with prompts and responses, separated by a custom delimiter.

        Args:
            file_name (str): The name of the file where the conversation will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
            IndexError: If the conversation elements are not found or are in an unexpected format.
        """

        try:
            # Define the directory where conversations will be saved
            directory_name = "conversations"
            # Create the directory if it does not exist
            if not os.path.exists(directory_name):
                os.makedirs(directory_name)

            # Define a delimiter for separating conversation parts in the file
            delimiter = "----------------------------------------"
            # Retrieve the conversation elements from the ChatGPT interface
            chatgpt_conversation = self.return_chatgpt_conversation()

            del chatgpt_conversation[::2]

            # Open the file and append the conversation
            with open(os.path.join(directory_name, file_name), "a") as file:
                for i in range(0, len(chatgpt_conversation)):
                    file.write(
                        f"{chatgpt_conversation[i].text}\n\n{delimiter}\n\n")
        except IOError as e:
            # Log and raise an error if there is an issue writing to the file
            logging.error(f"Failed to write conversation to file: {e}")
            raise IOError(f"Error writing to file '{file_name}': {e}")
        except IndexError as e:
            # Log and raise an error if the conversation elements are not in the expected format
            logging.error(f"Error in conversation format: {e}")
            raise IndexError("Conversation elements are not in the expected format or not found.")

    def return_last_response(self):
        """
        Retrieves the text of the last ChatGPT response from a web interface using Selenium WebDriver.

        The function uses a specific CSS selector to locate the last ChatGPT response on the page. It then
        triggers a click action on a button within that container to copy the response text to the clipboard.
        The text is retrieved from the clipboard and returned. Error handling and logging are implemented
        to capture any issues during the execution of the function.

        :return: The text of the last ChatGPT response as a string, or an error message if an exception occurs.
        """

        try:
            # Find the elements that contain the ChatGPT responses using a CSS selector.
            response_elements = self.driver.find_elements(by=By.CSS_SELECTOR,
                                                          value='[your CSS selector here]')

            # Select the last element from the list of response elements.
            response_element = response_elements[-1]

            # Simulate a click action on the selected element.
            response_element.click()

            # Retrieve the copied text from the clipboard.
            response_text = pyperclip.paste()
            return response_text

        except NoSuchElementException:
            # Handle the case where the element is not found
            logging.error('Element not found in return_last_response')
            return "Element not found."
        except Exception as e:
            # Handle any other exceptions
            logging.error(f'Unexpected error in return_last_response: {str(e)}')
            return f"An unexpected error occurred: {str(e)}"
    def wait_for_human_verification(self):
        """
        Pauses the automation process and waits for the user to manually complete tasks such as log-in
        or human verification, which are not automatable. The function repeatedly prompts the user until
        they confirm the completion of the manual task.

        Returns:
            None

        Raises:
            SystemExit: If an unrecoverable input error occurs, indicating a problem with the system or environment.
        """
        with self.lock:
            print("You need to manually complete the log-in or the human verification if required.")

            while True:
                try:
                    user_input = input(
                        "Enter 'y' if you have completed the log-in or the human verification, or 'n' to check again: ").lower()
                except EOFError:
                    # Print error message and exit the program in case of an End-Of-File condition on input
                    print("Error reading input. Exiting the program.")
                    raise SystemExit("Failed to read user input.")  # Exiting the program due to input error

                # Check the user's input and act accordingly
                if user_input == 'y':
                    print("Continuing with the automation process...")
                    break  # Break the loop to continue with automation
                elif user_input == 'n':
                    print("Waiting for you to complete the human verification...")
                    time.sleep(5)  # Waiting for a specified time before asking again
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")  # Handle invalid input

    def write_last_answer_custom_file(self, filename):
        """
        Retrieves the latest response from ChatGPT and writes it to a specified file. The file is saved
        with UTF-8 encoding to support a wide range of characters.

        Parameters:
            filename (str): The name of the file (including path if necessary) where the last response will be saved.

        Returns:
            None: The function does not return any value.

        Raises:
            IOError: If there is an issue writing to the file.
        """

        try:
            # Retrieve the last response from ChatGPT
            answer = self.return_last_response()

            # Open the file for writing and use UTF-8 encoding
            with open(filename, "w", encoding="utf8") as file:
                # Write the answer to the file
                file.write(answer)

            # Print a confirmation message
            print(f"Last answer saved in the file: {filename}")

        except IOError as e:
            # Log and raise an error if there is an issue writing to the file
            logging.error(f"Failed to write the last answer to the file: {e}")
            raise IOError(f"Error writing to file '{filename}': {e}")

    def open_new_chat(self):
        """
        Navigates to the ChatGPT page using the WebDriver, effectively starting a new chat session. This function
        is useful for resetting the conversation or starting afresh.

        Raises:
            WebDriverException: If there is an issue navigating to the ChatGPT page.
        """
        try:
            # Navigate to the ChatGPT URL to start a new chat session
            self.driver.get(self.url + "/")
            # Print confirmation message
            print("New chat opened")
            # Wait for the page to load completely (10 seconds)
            time.sleep(10)
        except Exception as e:
            # Log the exception if navigation fails
            logging.error(f"Failed to open new chat: {e}")
            # Raising a WebDriverException to indicate failure in navigation
            raise webdriver.WebDriverException(f"Error opening new chat: {e}")

    def del_current_chat(self):
        """
        Deletes the current chat session in the ChatGPT interface. This function interacts with specific UI elements
        to trigger the deletion process of the active chat conversation.

        Handling:
            - If a timeout occurs (elements not found in time), it attempts to open a new chat session.
            - Any other exceptions trigger a retry by opening a new chat session.

        Raises:
            WebDriverException: If there are issues in deleting the chat or in navigating to start a new chat.
        """
        try:
            # Wait and click the first delete button
            del_chat_btn1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((ChatGPTXpath.FIRST_DELETE_BTN[0], ChatGPTXpath.FIRST_DELETE_BTN[1]))
            )
            del_chat_btn1.click()
            time.sleep(3)  # Wait for UI response

            # Wait and click the second delete button
            del_chat_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((ChatGPTXpath.SECOND_DELETE_BTN[0], ChatGPTXpath.SECOND_DELETE_BTN[1]))
            )
            del_chat_btn.click()

            # Wait and click the third delete button to confirm deletion
            del_chat_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((ChatGPTXpath.THIRD_DELETE_BTN[0], ChatGPTXpath.THIRD_DELETE_BTN[1]))
            )
            del_chat_btn.click()

            print("Current chat deleted")
            time.sleep(5)  # Wait for the chat to be completely deleted

        except TimeoutException:
            # Handle timeout exception when elements are not found within the specified time
            print("Timeout: Elements not found within the specified time.")
            try:
                self.open_new_chat()
            except Exception as e:
                logging.error(f"Failed to open new chat after timeout: {e}")
                raise webdriver.WebDriverException(f"Error navigating to start a new chat after timeout: {e}")

        except Exception as e:
            # Handle any other exceptions that might occur
            logging.error(f"Error encountered while deleting chat: {e}")
            try:
                time.sleep(5)
                self.open_new_chat()
            except Exception as e:
                logging.error(f"Failed to open new chat after error: {e}")
                raise webdriver.WebDriverException(f"Error navigating to start a new chat after deletion error: {e}")

    def check_error(self, regenerate=False):
        """
        Checks if there is an error message displayed on the webpage, indicating a problem with response generation.

        This method attempts to locate a specific error message element on the webpage using an XPath expression.
        If an error is found and the 'regenerate' flag is True, it triggers a response regeneration.
        Logs the occurrence of an error for debugging purposes.

        :param regenerate: A boolean flag indicating whether to regenerate the response if an error is found.
        :return: True if an error is detected, False otherwise.
        """
        try:
            # Locate the error message element using XPath
            error_element = self.driver.find_element(By.XPATH,
                                                     "//div[@class='mb-3 text-center text-xs' and text()='There was an error generating a response']")
            logging.info("Error detected: Responding error!")

            # Regenerate response if the flag is set
            if regenerate:
                self.regenerate()

            return True
        except NoSuchElementException:
            # Log that no error was found
            logging.info("No error detected.")
            return False
        except Exception as e:
            # Log any other exceptions that may occur
            logging.error(f"An unexpected error occurred: {e}")
            return False

    def check_response_status(self):
        """
        Continuously checks the status of the response on the webpage.

        This method loops indefinitely, checking for two conditions:
        1. If there is an error on the page, indicated by the check_error method.
        2. If the 'send' button is available, indicating that the response is ready to be sent.

        The method waits for a set interval before rechecking the conditions.

        :return: False if an error is detected, True if the response is ready to be sent.
        """
        while True:
            # Check for errors on the page
            if self.check_error(False):
                logging.info("Response Status: Error detected.")
                return False

            try:
                # Check if the 'send' button is available, indicating the response is ready
                self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="send-button"]')
                logging.info("Response Status: Ready to send.")
                return True
            except NoSuchElementException:
                # If 'send' button is not found, continue the loop
                pass

            # Log and wait before checking again
            logging.info("Responding...")
            time.sleep(7)

    def quit(self):
        """
        Closes the browser and terminates the WebDriver session.

        This method first attempts to close the current window of the browser using the `close` method.
        Then it calls the `quit` method to effectively end the entire WebDriver session.
        Error handling is implemented to catch any exceptions that might occur during this process.
        """
        try:
            # Attempt to close the current browser window
            print("Closing the browser...")
            self.driver.close()

            # Terminate the WebDriver session
            self.driver.quit()
            logging.info("Browser closed successfully and WebDriver session terminated.")
        except Exception as e:
            # Log any exceptions that occur during the quit process
            logging.error(f"An error occurred while closing the browser: {e}")
