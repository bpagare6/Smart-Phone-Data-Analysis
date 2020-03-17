# Smart Phone Data Analysis

It's just start of the year 2020 and already 1560.85 million smartphones are sold.
Considering this huge number of Smartphone buyers and their confusions while buying
a new phone, we should build a full pipeline which can help user to check the latest
trends in the mobile phones and value for money of any smartphone. This is main
motivation behind doing this project.

## To get started with the project
1. `git clone https://github.com/bpagare6/Smart-Phone-Data-Analysis.git`
2. `pip install -r requirements.txt`
3. Scrape the data from start if needed, `python deep_flipkart_scraper.py`. I have already put the scrped data into data folder.
4. For preprocessing the scraped data, `python preprocessing_flipkart_data.py`. I have already done the preprocessing and you can find that data too in data folder.
5. Use the data for your work :)

### Work Done till now
- Scraped the data of smartphones from Flipkart.
- Preprocessed the data and organized it in a final CSV file.

Note: There are two scripts for scraping, `flipkart_scraper.py` and `deep_flipkart_scraper.py`.
`flipkart_scraper.py` scrapes all the data just by visiting the main page of flipkart mobile url.
`deep_flipkart_scraper.py` scrapers all the data by going to the url of individual phone and fetches all details specifications from each page


