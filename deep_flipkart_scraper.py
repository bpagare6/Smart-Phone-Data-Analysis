from bs4 import BeautifulSoup
import requests
import csv
import os

number_of_phones_done = 0

for i in range(51):
    if number_of_phones_done % 100 == 0:
        print('Number of phones done:', number_of_phones_done)
    try:
        phone_data = []
        # Send the request
        url = 'https://www.flipkart.com/search?q=mobile&p[]=facets.type%255B%255D%3DSmartphones&page=' + str(i)
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, 'html.parser')
        # Fetch the main content
        body = content.find_all('div', {'class': '_1HmYoV _35HD7C'})
        mobiles = body[1].find_all('div', {'class': 'bhgxx2 col-12-12'})
        # Fetch the individual mobiles
        for mobile in mobiles[:-2]:
            try:
                phone_urls = mobile.find_all('a', {'class': '_31qSD5'})
                for phone_url in phone_urls:
                    # Sending request to each single phone url
                    phone_url = 'https://www.flipkart.com' + phone_url.get('href')
                    mobile_response = requests.get(phone_url, timeout=5)
                    # print(mobile_response)
                    mobile_content = BeautifulSoup(mobile_response.content, 'html.parser')
                    # Fetch Name
                    name = mobile_content.find('span', {'class': '_35KyD6'}).text.strip()
                    # Fetch Ratings and Reviews
                    stars = mobile_content.find('div', {'class': 'hGSR34'}).text.strip()
                    ratings_and_reviews = mobile_content.find('span', {'class': '_38sUEc'}).find('span').find_all('span')
                    ratings = ratings_and_reviews[0].text.strip()
                    reviews = ratings_and_reviews[2].text.strip()
                    # Fetch Price
                    price = mobile_content.find('div', {'class': '_1vC4OE _3qQ9m1'}).text[1:].strip().replace(',', '')
                    # Fetch Specs
                    full_specs = mobile_content.find_all('div', {'class': '_2RngUh'})
                    specifications = {}
                    for specs in full_specs:
                        specs_rows = specs.find('table').find('tbody').find_all('tr')
                        for spec in specs_rows:
                            data = spec.find_all('td')
                            key = data[0].text
                            value = data[1].text
                            specifications[key] = value
                    phone_data.append({'Name': name, 'Stars': stars, 'Ratings': ratings, 'Reviews': reviews, 'Specifications': specifications, 'Price': price})
                number_of_phones_done += 1
            except Exception as ex:
                print('Error:', ex)
                continue

        # Save the List as CSV
        csv_file = "data/page" + str(i) + ".csv"
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Stars', 'Ratings', 'Reviews', 'Specifications', 'Price'])
                writer.writeheader()
                for d in phone_data:
                    writer.writerow(d)
        except IOError:
            print("I/O error")

    except Exception as ex:
        print('Error:', ex)
        print('Happened at i =', i)
        continue

print('All done man !!')
os.system('echo ' + str(number_of_phones_done) + ' > phones_done.txt')
os.system('systemctl poweroff')
