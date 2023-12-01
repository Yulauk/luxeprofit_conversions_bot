# Luxeprofit API Bot
### This Telegram bot will help you quickly see the conversion results from your personal account in the Luxeprofit affiliate network

1. **What the project does?**
   - It helps receive conversions notifications.
   - Now this bot can show your daily conversions with details about country, offer, time, and count of conversions.
   - It shows your hold and available balance.
   - When the conversion status is 'deposit,' the bot shows how much money you have.

2. **Why the project is useful?**
   - The bot helps you spend less time getting useful information about the number of conversions, as well as information about offers and the total account balance.

3. **How users can get started with the project?**
   - In the current version of the bot, follow these steps to set it up:
     1. Create a new Telegram bot in your personal Telegram account through the BotFather. Copy the token provided for the newly created bot.
     2. Open the `config.py` file in the bot's codebase and assign the copied Telegram token to the `telegram_token` variable.
     3. Next, navigate to your LuxeProfit personal account and access the API key from the Security settings.
     4. In the `config.py` file, assign the API key to the `luxeprofit_api_key` variable.
   
   By completing these steps, you'll have configured both the Telegram bot and LuxeProfit API key for optimal functionality.
