def selenium_webdriver(self):
    driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    url = ('https://earthdata.nasa.gov/search?q={location}'.format(location=self.location))
    driver.get(url)
    time.sleep(15)

    # Driver scrolls down 25 times to load the table.
    for i in range(0, 30):
        driver.execute_script("window.scrollBy(0,6000)")
        time.sleep(10)

    # Fetch the webpage and store in a variable.
    webpage = driver.page_source

    # Parse the page using BeautifulSoup
    HTMLPage = BeautifulSoup(webpage, 'html.parser')

    titles = []
    descriptions = []
    links = []

    for result in HTMLPage.find_all(class_='result'):
        title_element = result.find('span', class_='result-title')
        description_element = result.find('p', class_='result-description')
        link_element = result.find('a', class_='result-text-link')

        if title_element and description_element and link_element:
            titles.append(title_element.text.strip())
            descriptions.append(description_element.text.strip())
            links.append(link_element['href'])

    # Create a DataFrame
    df = pd.DataFrame({'Title': titles, 'Description': descriptions, 'Link': links})

    # Display the DataFrame
    print(df)

    # Store to a CSV file
    df.to_csv('web_scraping_output.csv', index=False, encoding='utf-8')

    print('Web Scraping Successful!')

