# Web Scraper Project

This project contains a web scraper that retrieves news articles and data from a website.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project implements a web scraper to extract news articles and data from various sources. It consists of two main components: the `Weather_API` class for fetching news articles using the News API, and the `Web_Scraping` class for scraping data from a website.

## Features

- Retrieve news articles using the News API.
- Scrape data from a website using Selenium and BeautifulSoup.
- Organize and store data in a structured format.
- Print and display data for analysis.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git

2. Install the required dependencies using pip:
3. Download and place the ChromeDriver executable in the project directory or update the webdriver.Chrome() path in the code to the appropriate location.

## Usage 
1. Run the main.py script
2. Follow the prompts to enter the keyword for news articles and the location for web scraping.
3. The script will fetch news articles, display JSON output, and create a DataFrame for news articles. It will also perform web scraping, display the scraped data, and save it to a CSV file

## Technologies Used
* Python
* Requests
* Selenium
* BeautifulSoup
* Pandas
  
## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

## Fork the repository.
* Create a new branch for your feature or bug fix.
* Make your changes and commit them.
* Push your changes to your forked repository.
* Submit a pull request.
## License
This project is licensed under the MIT License.
