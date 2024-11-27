# NASA BOT

## Overview

The **NASA BOT** is designed to fetch the latest speeds of Coronal Mass Ejections (CMEs) from the atmosphere and convey this data back to you in the form of an ethereal, whimsical poem. By transforming raw scientific data into poetic form, this bot helps you relate to the vast and sometimes overwhelming speeds of the atmosphere, offering a sense of connection and perspective.

## Features

- Retrieves the latest Coronal Mass Ejection (CME) speeds from NASA's API.
- Generates a whimsical poem that relates the speed of the CME to personal reflection, helping you feel grounded and less existential.
- A light-hearted and poetic way to engage with space weather data!

## Requirements

Before using the bot, ensure you have the following:

1. **OpenAI API Key**: This is required for generating the poetic responses.
2. **NASA API Key**: This is used to access data about the Coronal Mass Ejections (CME) and their speeds.

### Security Notes:

- Save your API keys in separate files.
- **Make sure these files are added to your `.gitignore` to prevent accidental sharing or exposure.**

## Setup Instructions

### 1. Install Dependencies

Make sure you have Python 3.x installed. Then, install the required Python libraries using:

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

You will need to store your **OpenAI** and **NASA** API keys in files that are excluded from version control:

- **OpenAI API Key**: Store this in a file named `openai_key.txt`.
- **NASA API Key**: Store this in a file named `nasa_key.txt`.

Make sure both files are listed in your `.gitignore` file to keep them safe and private.

### 3. Set Your Date

You will need to enter a specific date to customize the generated poem. This could be a special date such as your birthday. The bot will use this input to create a unique poetic experience for you!

### 4. Running the Bot

After you've configured your API keys and set your desired date, run the bot.

The bot will fetch the latest CME speeds and present them to you in a creatively generated poem that helps you connect with the atmosphere's immense power.

## Example Usage

If you input your birthday (for example, "January 1st"), the bot might respond with something like:

*"On this day of your birth, the sun did sigh,
 A CME soared, in the deep sky.
 At speeds untold, it raced away,
 Yet in your heart, the winds did play."*

