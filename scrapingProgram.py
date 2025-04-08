# Jordan Staggs CS 325
# Built: 4-1-25
########################################################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup

articles = open('newsSites.txt', 'r')

#START OF SITE 1 SCRAPPING************************************

# URL of the news site to scrape
url_to_scrape = articles.readline()

# Try statement to catch errors
try:
    # Open the URL
    request_page = urlopen(url_to_scrape)
    
    # Read the page content
    page_html = request_page.read()
    
    # Close the connection
    request_page.close()
    
    # Parse the HTML with BeautifulSoup
    html_soup = BeautifulSoup(page_html, 'html.parser')
    
    # Find all headlines using the appropriate tag and class
    headlines = html_soup.find_all('h3', class_='ListItem-title')

    # Write to the output file
    with open('articleOutput.txt', 'a') as site:
        site.write("Site************************\n")
        for headline in headlines:
            # Write each headline, cleaned up with .strip()
            site.write(headline.get_text().strip())
            site.write("\n")

except Exception as e:
    # Print error for site 1
    print(f"An error occurred with site 1: {e}")

#START OF SITE 2 SCRAPPING************************************
     
# URL of the news site to scrape
url_to_scrape = articles.readline()

# Try statement to catch errors
try:
    # Open the URL
    request_page = urlopen(url_to_scrape)
    
    # Read the page content
    page_html = request_page.read()
    
    # Close the connection
    request_page.close()
    
    # Parse the HTML with BeautifulSoup
    html_soup = BeautifulSoup(page_html, 'html.parser')
    
    # Find all headlines using the appropriate tag
    headlines = html_soup.find_all('h6')

    # Write to the output file
    with open('articleOutput.txt', 'a') as site:
        site.write("Site************************\n")
        for headline in headlines:
            # Write each headline, cleaned up with .strip()
            site.write(headline.get_text().strip())
            site.write("\n")

except Exception as e:
    # Print error for site 2
    print(f"An error occurred with site 2: {e}")
