from bs4 import BeautifulSoup
import requests
import csv

for i in range(5, 10):
    try:
        data = []

        # Send the request
        url = 'https://www.flipkart.com/search?q=mobile&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&page=' + str(i)
        response = requests.get(url, timeout=5)
        content = BeautifulSoup(response.content, 'html.parser')

        # Fetch the main content
        body = content.find_all('div', {'class': '_1HmYoV _35HD7C'})
        mobiles = body[1].find_all('div', {'class': 'bhgxx2 col-12-12'})
        # Fetch the individual mobiles
        for mobile in mobiles[:-2]:
            try:
                mobile_description = mobile.find('div', {'class': 'col col-7-12'})
                # Fetch name and ratings,
                name = mobile_description.find('div', {'class': '_3wU53n'}).text
                ratings = mobile_description.find('div', {'class': 'hGSR34'}).text
                reviews = mobile_description.find('span', {'class': '_38sUEc'}).text
                # Fetch the details/description
                mobile_details = mobile_description.find('div', {'class': '_3ULzGw'})
                details_list = mobile_details.find_all('li', {'class': 'tVe95H'})
                details = ""
                for detail in details_list:
                    details += detail.text + "\n"
                # Fetch the mobile price
                mobile_price = mobile.find('div', {'class': 'col col-5-12 _2o7WAb'})
                price = mobile_price.find('div', {'class': '_1vC4OE _2rQ-NK'}).text
                # Save the data into List
                data.append({'Name': name, 'Ratings': ratings, 'Reviews': reviews, 'Details': details, 'Price': price})
            except:
                print(name)
                continue

        # Save the List as CSV
        csv_file = "first_data/page" + str(i) + ".csv"
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Ratings', 'Reviews', 'Details', 'Price'])
                writer.writeheader()
                for d in data:
                    writer.writerow(d)
        except IOError:
            print("I/O error")

    except:
        print(i)
        continue
