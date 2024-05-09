import os
from chatgpt_automation.chatgpt_automation import ChatGPTAutomation  # Import the ChatGPTAutomation class

class ChromeManager:
    def __init__(self, number_of_instances):
        self.chromes = {}
        self.setup_many_chrome(number_of_instances)

    def setup_many_chrome(self, count):
        base_path = self.get_base_path()
        for i in range(count):
            user_data_dir = os.path.join(base_path, f"chrome_user_data_{i}")
            os.makedirs(user_data_dir, exist_ok=True)
            automation = ChatGPTAutomation(user_data_dir=user_data_dir)  # Instantiate ChatGPTAutomation with the specific user data dir
            self.chromes[automation] = False  # False indicates that the Chrome is not busy

    def get_base_path(self):
        # Determine the base path for user data directories based on the operating system
        if os.name == 'nt':  # Windows
            return os.path.join(os.environ.get('LOCALAPPDATA', ''), 'ChatGPTAutomation')
        elif os.name == 'posix':
            return '/tmp/ChatGPTAutomation'

    def get_free_chrome(self) -> ChatGPTAutomation:
        while True:
            # Retrieve the first free (not busy) ChatGPTAutomation instance
            for automation, is_busy in self.chromes.items():
                if not is_busy:
                    self.chromes[automation] = True  # Mark as busy
                    return automation
            
            # If no free Chrome instances are available, wait for a short period before retrying
            time.sleep(1) 

    def release_chrome(self, automation):
        # Mark the ChatGPTAutomation instance as freex
        if automation in self.chromes:
            self.chromes[automation] = False
        else:
            raise ValueError("Invalid ChatGPTAutomation instance")
