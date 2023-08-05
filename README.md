# Pixela Interface App

This is a Python application that provides a user-friendly interface for interacting with the Pixela API. Pixela is a service that allows you to track and visualize various activities over time using graphs.

## Features


- Authentication: The app allows users to authenticate with the Pixela API using their username and token.
- In order to create user you need to make following call. Fill it with your own data

```
curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
```


You need to store your authentication data (username and token ) in .env file in the root of this project.

Here's example env file:
```
USUERNAME=someuser
TOKEN=sometoken
```
Fill it with your own data

## Getting Started

1. Clone this repository: `git clone https://github.com/Cloudy17g35/habbits-tracker.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the app: `python main.py`


## Dependencies

- Python 3.8

## Acknowledgements

- This app was inspired by the Pixela API documentation and the desire to create a more user-friendly interface.


