# Events-assistant
<hr/>

[![GitHub issues](https://img.shields.io/github/issues/PraveenKumarSridhar/Events-assistant?style=for-the-badge)](https://github.com/PraveenKumarSridhar/Events-assistant/issues)
[![GitHub forks](https://img.shields.io/github/forks/PraveenKumarSridhar/Events-assistant?style=for-the-badge)](https://github.com/PraveenKumarSridhar/Events-assistant/network)
[![GitHub stars](https://img.shields.io/github/stars/PraveenKumarSridhar/Events-assistant?style=for-the-badge)](https://github.com/PraveenKumarSridhar/Events-assistant/stargazers)
[![GitHub license](https://img.shields.io/github/license/PraveenKumarSridhar/Events-assistant?style=for-the-badge)](https://github.com/PraveenKumarSridhar/Events-assistant/blob/main/LICENSE)

<img align="center" alt="robo assistant" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Events-assistant/main/assets/robo-assistant.png" />

## Introduction 
An assistant that will read out the scheduled events in your google calender at a specified time during the day.

## Packages required
```
pip install APScheduler
pip install  gTTS
pip install pyttsx3
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Steps to setup
### Step 1: Create and save the credentials for your google calender API:
Go to this link:
https://developers.google.com/calendar/quickstart/python
and click on `Enable the Google calender API`

<img align="center" alt="enable api" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Events-assistant/main/assets/enable_google_calender.PNG" />

<br/>

Then save the `credentials.json` in the following path `./src/`

### Step 2: Configure you assistant:

Go to `src\global_variable.py` and change the `ALERT_TIME` to when you want the assistant to read out your events for the day.

### Step 3: Start the assistant:

You can start the assistant by running the following command:
```
python morning_task.py
```

With this the setup for your very own personal assistant is done.
