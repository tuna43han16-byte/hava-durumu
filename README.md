# Command-Line Weather App (CLI)

A simple, lightweight, and clean command-line (CLI) weather application built in Python. It fetches real-time weather data and a 3-day forecast from the `wttr.in` JSON API and displays it directly in your terminal.

This project was created to demonstrate fundamental Python skills, including API integration (using `requests`), JSON data handling, and user input management (via `sys.argv` and `input()`).

---

## 📸 Demo

It's highly recommended to add a screenshot of your application's output here.

`![A screenshot of the app running in a terminal, showing the weather for a city like 'London'](demo.png)`

---

## 🚀 Features

* **Current Conditions:** Get the real-time temperature, "Feels Like" temperature, and weather description.
* **Detailed Info:** Fetches humidity percentage and wind speed (in Km/h).
* **Today's Forecast:** Displays the min and max temperature for the current day.
* **Hourly Forecast:** Shows a summary for morning (6:00), noon (12:00), and evening (18:00).
* **Flexible Input:** Accepts a city name as either:
    1.  A command-line argument.
    2.  A user prompt if no argument is provided.
* **Error Handling:** Includes basic checks for connection errors or if a city is not found.

## 🛠️ Tech Stack

* **Language:** Python 3
* **API:** [wttr.in JSON API](https://wttr.in)
* **Core Libraries:**
    * `requests`: For making HTTP requests to the API.
    * `sys`: For reading command-line arguments.

---

## ⚙️ Setup and Usage

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
