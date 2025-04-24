from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scraper:
    # Returns the URL it reads from a given file
    def get_URL(self,input_filename):
        try:
            # Open the file that holds the URL of the site to be scraped
            articles = open(input_filename, 'r')
            # Put the link into the url_to_scrape variable
            url_to_scrape = articles.readline()
            # return the URL
            return url_to_scrape
        except Exception as e:
            # Print error for getting the URL from the file
            print(f"An error occurred with reading URL{e}")

    # Opens the site associated with the URL it is given and returns the webpage content in the page_html variable
    def open_site(self, url_to_scrape):
        try:
            # Open the URL
            request_page = urlopen(url_to_scrape)
            # Read the page content
            page_html = request_page.read()
            # Close the connection
            request_page.close()
            # Return page content
            return page_html

        except Exception as e:
            # Print error for opening site
            print(f"An error occurred with opening site{e}")
    
    # Return the defined headlines from the page content passed through
    def get_headlines(self, page_html):
        try:
            # Parse the HTML with BeautifulSoup
            html_soup = BeautifulSoup(page_html, 'html.parser')
            # Find all headlines using the appropriate tag and class
            headlines = html_soup.find_all('h3', class_='ListItem-title')
            # Return the list of headlines
            return headlines
        
        except Exception as e:
            # Print error for getting headlines
            print(f"An error occurred with getting the headlines{e}")
    
    # Writes the list of headlines passed through it to the output file it is given
    def write_headlines(self, headlines, output_filename):
        try:
            # Write to the output file
            with open(output_filename, 'a') as site:
                for headline in headlines:
                    # Write each headline, cleaned up with .strip()
                    site.write(headline.get_text().strip())
                    site.write("\n")
        except Exception as e:
            # Print error for writing headlines
            print(f"An error occurred with writing the headlines{e}")
    

