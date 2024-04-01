# weather-bot-slacky
****


Weather Bot for Slack

This Slack bot provides weather data for a given city using the OpenWeatherMap API. Users can retrive the current temp by typing a slash command followed by the desired city name.

Pre-Reqs

Before setting up and running the Weather Bot, ensure you have the following prerequisites installed:

    Python latest version
    Flask
    requests
    ngrok

Setup Instructions

Follow these steps to set up and run the Weather Bot in your Slack workspace
1. Create a Slack App

    Go to the Slack API website.
    Click on "Create New App".
    Name your app (e.g., "Weather Bot") and select your workspace.
    Under "Features", click on "Slash Commands"
    Click on "Create New Command"
    Set the following:
        Command: /jumo_weather
        Request URL: We'll set this up later after creating the Python Flask application
    Save the changes

2. Obtain an API Key from OpenWeatherMap

    Sign up for an account on OpenWeatherMap.
    Once logged in, navigate to the API keys section and generate a new API key.

3. Set up the Flask Application

    Clone this repository to your local machine.
    Install the required dependencies by running pip install Flask requests.
    Open flashy-app.py and Set the OpenWeatherMap API key as an enviroment variable on your system
    Start the Flask application by running python flashy-app.py

4. Expose Flask Application using ngrok

    Download and install ngrok from ngrok website.
    Run ngrok from the command line: ngrok http 5000.
    Note the ngrok forwarding URL for example( https://3fb6-x-x-x.ngrok.io)  this will be used in our Slack app configuration.

5. Configure Slack App

    Go back to your Slack App configuration.
    Under "Slash Commands", edit the /jumo_weather command.
    Set the Request URL to your ngrok forwarding URL followed by /weather
    Save the changes.

6. Test the Weather Bot in Slack

    Open the Slack desktop app or use Slack in your web browser.
    In any channel or direct message, type /jumo_weather [city] (e.g., /jumo_weather Berlin).
    Send the message.
    You should receive a response with the current temperature in the specified city.

Contributors

    Rachel K

License

This project is licensed under the MIT License.
