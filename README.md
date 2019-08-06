# Telegram Chat Sentinel
Backend python scripts that listen for trigger words as an indication to selectively forward messages from target(s) to destination.
* 'Trigger word(s)' can be an entire word, or part of a word. This is designed to be singular, or in a list.
* 'Target(s)' can be of any entity - users, chats or channels. This is designed to be singular, or in a list.
* 'Destination' can be of any entity - chats or channels. This is designed to be singular.

## Use cases
These scripts are meant to act as a filter - a solution that seeks to solve the two-part challenge of obtaining time-sensitive messages in 'noisy' entities.

#### Where notifications can become bothersome
1. In chats or channels, there might be thousands of messages exchanged in a day.
2. The user may only be interested in some of these messages (those that contain trigger words).
   Hence, it may be a bother to enable notifications for these chats or channels.

#### When messages need to be responded to quickly
3. The 'conventional' approach is for the user to disable notifications; and manually, periodically use Telegram's in-built 'search' function to search for messages with trigger words.
4. This is laborious and time-sensitive messages may not be responded to in time. Furthermore, there will always be a time-lag due to human limitations.

With these scripts, messages containing the trigger words in target(s) are selectively forwarded to a 'destination' almost instantaneously.
Users can then safely disable notifications for target(s) and enable them for the destination; and be timely notified of important messages. Note that the machine running the scripts needs to be kept 'alive' and running. 

## Disclosures
1. The author has personally tried-and-tested these methods but is not liable for any losses, including but not exhaustively telegram account(s) and data on these account(s). 
2. No data/ access is transferred/ disclosed to any third-parties through these methods. Exchanges are only carried out between telegram and the user, using a third-party library of python helper functions.

## Prerequisites
1. [Telegram](https://web.telegram.org/) up-and-running, on any device
2. [Python](https://www.python.org/downloads/), ver. 3.7 recommended
3. [pip](https://pypi.org/project/pip/)
4. [requests](https://pypi.org/project/requests/)

## How it works
The described behaviour is achieved by executing two seperate python scripts:
1. forward_msg - Does the forwarding of messages between entities
2. bot - Echos any messages (in this case, forwarded messages). These echos will be 'push-notified'.

The bot  is necessary because any messages forwarded without it would already be deemed 'user acknowledged' by Telegram, and hence no push-notifications would be triggered.
<br>The scripts were designed to be seperate because in some cases, only the features provided by the first script is desired.

## Preinstallation
#### Create your own bot
_Process to be done only once per account, per connection_
1. Create your very own bot using botfather. This can be done by following the instructions found [here.](https://core.telegram.org/bots#6-botfather)
#### Telegram
_Process to be done only once per account, per connection_

2. Login to Telegram core and obtain a telegram api_id.
   Instructions can be found [here](https://core.telegram.org/api/obtaining_api_id).</br>
   Fill up the form found at 'API development tools'.</br>
   For the 'URL' field, access your 'telegram' app > 'Settings' > 'Edit profile' > click on 'Username'.</br>
   Your URL looks something like: `https://t.me/kktann`</br>
   Fill up the rest of the form as desired.
#### Zip
3. Download and extract entire zipped repository
#### Setting up
4. Set-up config file.</br>
   Navigate to forward_msg > main > config.yml</br>
   Update lines with the comment header: `Information to be obtained from 'API development tools'`</br>
   The remaining lines have already been initialised for you in order to successfully carry out the tests further below.
5. Set-up bot file.</br>
   Navigate to bot > run_bot</br>
   Copy and paste your bot token from step 1 within the quotes for the line under the comment `copy and paste your bot token in the line below`</br>
   The remaining lines have already been initialised for you in order to successfully carry out the tests further below.

## Installing

Run command to install requirements:
```pip install -r requirements.txt```

## Running the tests

1. Create the following groups and add the bot in it (since there must be at least 2 entities in a group) on Telegram for testing:
   * tcs target 1
   * tcs target 2
2. Open a command prompt in the bot directory/ folder
3. Run command to execute script
   ```python run_bot.py```
4. Open a command prompt in the forward_msg directory/ folder
5. Run command to execute script
   ```python main.py config.yml```
6. In both **tcs target 1** and **tcs target 2** groups, send the following test messages:
   * *Hello there*
   * *Testing one, two, three*
7. The test messages broadcasted in target groups should be instaneously forwarded to your bot.
8. Your bot will then echo the messages it received (the messages you forwarded to it). Push-notifications would be triggered.
8. **Tests completed and successful!**

## Deployment
This process is done only once per account.
1. Set-up config file and bot file as desired, as shown above.
2. Requirements should already be installed if the instructions above were followed.
3. Run the commands to execute both scripts, as shown above.

Points to note:
* Machine running the script needs to be kept 'alive' and running.
* To skip the process of keying in your phone number and login code in future runs, retain the **SESSION** file that would be created in the same directory/ folder.

## Built With

* [Python](https://www.python.org/downloads/)
* [Telethon](https://arabic-telethon.readthedocs.io/en/stable/)

## Future work

This script, along with more recipes; will be updated as and when the author finds and decide to implement more features he find useful.
Feel free to collaborate and contribute to this project, or open an issue to suggest more useful features for implementation!

## Author

[Kelvin Tan Xuan De](https://github.com/kelvinxuande)

## Acknowledgments

- [voidbar](https://github.com/voidbar)
- [Gareth Dwyer](https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay)
