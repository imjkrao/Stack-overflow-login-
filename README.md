#Automation of Stack overflow login

## Introduction
This automation task is perfomed in two stages. One is script to login to web page using required credential.
This has been achieved by using Selenium package. 

To install selenium, open terminal in project location and use below command.

`pip install selenium`
Then run the script `code_selenium.py` perform login task for one time. 
  

### `code_selenium.py` 

This python script has method `stackoverflow_Login` with parameter being `email_ID` and `password`
we are using chrome driver to access the chrome browser and pass the data to it. 
Firstly, I define landing page of the website  and maximize the window. Then we look for web element name called `email` in html and pass user's `email_ID`.
Similarly, we look for web element with name `password` and send the password keys using selenium's web driver. 
Finally, we use selenium's web driver again to click on the login button in the browser.

### Run this script everyday

To run this script everyday, we can utilise the feature of windows called **"Task scheduler"**.