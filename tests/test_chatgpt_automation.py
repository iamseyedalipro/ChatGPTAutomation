import unittest
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation

class TestChatGPTAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        CHROME_DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        cls.automation = ChatGPTAutomation(chrome_path=CHROME_PATH,
                                           chrome_driver_path=CHROME_DRIVER_PATH)
    def setUp(self):
        # Print the name of the test before it starts
        print(f"Starting {self._testMethodName}")
        
    @classmethod
    def tearDownClass(cls):
        cls.automation.del_current_chat()
        cls.automation.quit()

    def test_01_send_prompt(self):
        test_prompt = "Hello, ChatGPT!"
        self.automation.send_prompt_to_chatgpt(test_prompt)
        # Add assertion to check if the prompt was sent correctly

    def test_02_save_conversation(self):
        self.automation.send_prompt_to_chatgpt("Test message for saving conversation")
        test_filename = "test_chat.txt"
        self.automation.save_conversation(test_filename)
        # Add assertion to check if the conversation was saved correctly

    def test_03_delete_current_chat(self):
        self.automation.send_prompt_to_chatgpt("Test message before deleting chat")
        self.automation.del_current_chat()
        # Add assertion to verify chat deletion

    def test_04_return_last_response(self):
        self.automation.send_prompt_to_chatgpt("Hello, ChatGPT again!")
        import time
        time.sleep(10)  # Adjust this based on expected response time
        last_response = self.automation.return_last_response()
        self.assertIsNotNone(last_response, "The last response should not be None.")
        self.assertNotEqual(last_response, "", "The last response should not be empty.")
        # Additional specific assertions can be added based on expected content

    def test_05_upload_file(self):
        test_file_name = "test_file.txt"
        self.automation.upload_file_for_prompt(test_file_name)
        # Add assertion to verify the file upload

    def test_06_check_response_status(self):
        # Send a prompt to ChatGPT to initiate a response
        self.automation.send_prompt_to_chatgpt("Hello, ChatGPT! Please write a long lorem ipsum")

        # Calling the check_response_status method
        response_status = self.automation.check_response_status()

        # Assert that the response status is as expected
        self.assertTrue(response_status, "Response status should be True indicating ready or no error.")


if __name__ == '__main__':
    unittest.main()
