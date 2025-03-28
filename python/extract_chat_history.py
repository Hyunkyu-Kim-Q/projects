#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
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

# Generate a timestamp for the current date
timestamp = datetime.now().strftime("%d.%m.%Y")

# Initialize file counter
counter = 1
filename = f"chat_history.{timestamp}({counter}).txt"

# Check if file already exists, and increment counter if necessary
while os.path.exists(filename):
    counter += 1
    filename = f"chat_history.{timestamp}({counter}).txt"

# Process and save chat to a new file
chat_text = extract_chat_from_html(page_source)
with open(filename, "w", encoding="utf-8") as file:
    file.write(chat_text)

print(f"Chat history saved to '{filename}'!")

# Close browser
time.sleep(3)
driver.quit()
