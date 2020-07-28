#### Automation of Stack overflow login

### Introduction
Here I have used Selenium to achieve this task. This has been written in Python 3.7. 

## `code_selenium.py` 

This python script has method `stackoverflow_Login` with parameter being `email_ID` and `password`
we are using chrome driver to access the chrome browser and pass the data to it. 
Firstly, I define landing page of the website  and maximize the window. Then we look for web element name called `email` in html and pass user's `email_ID`.
Similarly, we look for web element with name `password` and send the password keys using selenium's webdriver. 
Finally, we use selenium's webdriver again to click on the login button in the browser.
