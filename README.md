# Football---Stats---Scrapper

This code is a web scraper built using the Selenium library in Python. It retrieves soccer match data from the website "https://www.soccerstats.com/" for a specific league chosen by the user.

Prerequisites

Before running the code, make sure you have the following:

Python 3.x installed on your system
Selenium library installed (pip install selenium)
Chrome WebDriver installed and added to the system's PATH. You can use the Chrome WebDriver Manager (webdriver_manager.chrome) to automatically download and manage the WebDriver.

Setup

Replace the value of the PATH variable with the path to your Chrome WebDriver executable file (e.g., D:\Program files\chromedriver.exe).
Replace the value of the PATH_TO_EXTENSION variable with the path to the Chrome extension you want to load, if any.
Run the code using a Python interpreter.

Usage

When prompted, enter the league you want to retrieve data for.
The code will open the "https://www.soccerstats.com/" website using Chrome WebDriver.
It will close any privacy policy alert if present.
It will navigate to the chosen league's page.
It will close any additional alerts that appear.
It will navigate to the "All Matches" page for the chosen league.
It will retrieve the match data from the web table on the page.
The retrieved data will be stored in a pandas DataFrame.
The DataFrame will be saved as a CSV file named "file_match.csv" on the desktop.

Limitations

The code assumes a specific website structure and CSS selectors, which may change over time. If the website structure is modified, the code may not work as expected. Regular maintenance and updates may be required.
The code does not handle all possible error scenarios, such as network issues or invalid user inputs. Additional error handling can be added to enhance the code's robustness.

Contributing

Contributions are welcome! If you find any issues or want to add new features to the code, feel free to open a pull request.
