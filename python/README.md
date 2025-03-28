# Extract chat history from ChatGPT

## Prerequisites

* [Selenium Webdriver](#downloading-selenium-webdriver) - Selenium will be used to extract chat history from the ChatGPT web UI.

* [Google Chrome](#downloading-google-chrome) - ChatGPT will run on Google Chrome.

* [BeautifulSoup4](#downloading-beautifulsoup4) - BeautifulSoup will be used to parse HTML and save the chat into a file.


---

# Installation

## Downloading python venv
```
sudo apt install python3.12-venv
```
Let's install python on your machine.


## Activating virtual environment
```py
python3 -m venv myenv
source myenv/bin/activate
```

## Downloading selenium webdriver
```py
pip install selenium webdriver-manager
```

## Checking if selenium is running
```py
pip list
```

## Downloading Google Chrome
```
sudo apt update
sudo apt install google-chrome-stable
```

### or alternatively,
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
```

## Checking Google Chrome version
```
google-chrome --version
```

## Downloading Beautifulsoup4
```
python -m pip install beautifulsoup4
```
