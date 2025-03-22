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
