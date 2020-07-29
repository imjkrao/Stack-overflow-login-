# Automation of Stack overflow login

## Introduction
This automation task is perfomed in two stages. One is script to login to web page using required credential.
This has been achieved by using Selenium package. 

To install selenium, open terminal in project location and use below command.

`pip install selenium`

Then run the script `code_selenium.py` to perform login task for one time. To run this script everyday, 
we can take help of task scheduler that is packed in windows or crontabs that comes with unix systems.  

## `code_selenium.py` 

This python script has method `stackoverflow_Login` with parameter being `email_ID` and `password`
we are using chrome driver to access the chrome browser and pass the data to it. 
Firstly, I define landing page of the website  and maximize the window. Then we look for web element name called `email`
in html and pass user's `email_ID`.Similarly, we look for web element with name `password` and send the password keys 
using selenium's web driver. Finally, we use selenium's web driver again to click on the login button in the browser.

## Run this script everyday
As i'm using windows platform, To run this script everyday, we can utilise the feature of windows 
called **"Task scheduler"**. 

Click on below link to learn to open up `task scheduler`

https://www.isunshare.com/windows-8/open-windows-8-8.1-task-scheduler.html

Once you open task scheduler, Click on **Task Scheduler Library** and press option *Create Basic Task* to create 
task of running python script everyday. Or you can import the task `**stackoverflow_login_schedulerTask**`  from the github to your local task scheduler library.

Click on the below link to create your own basic task. 

https://www.weirdgeek.com/2019/04/automating-python-script-to-run-at-specific-time-every-day/


