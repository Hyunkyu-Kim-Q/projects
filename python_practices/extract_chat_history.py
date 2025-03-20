#!/usr/bin/python3

"""

There were few prerequisites to be able to run this.

1. Selenium webdriver - Selenium will be used to extract chat history from the ChatGPT web UI.
2. Google Chrome - ChatGPT will run on Google Chrome.
3. BeautifulSoup4 - BeautifulSoup will be used to parse HTML and save the chat into a file.

When I was running this in Ubuntu Linux which was running into PEP 668, so I had to create a virtual environment to install selenium webdriver.

-Downloading python venv
sudo apt install python3.12-venv

-Activating virtual environment
python3 -m venv myenv
source myenv/bin/activate

-Downloading selenium webdriver
pip install selenium webdriver-manager

-Checking if selenium is running
pip list

-Downloading Google Chrome
sudo apt update
sudo apt install google-chrome-stable

or alternatively,
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install

-Checking Google Chrome version
google-chrome --version

-Downloading Beautifulsoup4
python -m pip install beautifulsoup4

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open ChatGPT
driver.get("https://chat.openai.com/")

# Wait for user to log in manually
input("Log in to ChatGPT, open your conversation, then press Enter...")

# Get full page source (entire HTML content)
page_source = driver.page_source

# Extract chat messages from the HTML
def extract_chat_from_html(html):
 from bs4 import BeautifulSoup # Install with pip install beautifulsoup4
 soup = BeautifulSoup(html, "html.parser")

 chat_history = []
 messages = soup.find_all("div", {"data-testid": "conversation-turn"}) # Adjust selector if needed

 for msg in messages:
  role = msg.find("span") # Find user/AI label
  text = msg.find("div") # Find message text

  if role and text:
   chat_history.append(f"{role.text.strip()}: {text.text.strip()}")

 return "\n\n".join(chat_history)

# Process and save chat

chat_text = extract_chat_from_html(page_source)
with open("chat_history.txt", "w", encoding="utf-8") as file:
 file.write(chat_text)

print("Chat history saved to 'chat_history.txt'!")

# Close browser
time.sleep(3)
driver.quit()