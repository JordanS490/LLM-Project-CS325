# ScrapingProgram Information

## What it does:

This program reads the two URLs located in the *newsSites.txt file.* It will only work with these sites. *** The software scrapes a website's source code and determines what items to return based on the specifications for what classes and types of elements to look for. Different sites will have different class names and header types, so they will not work with this program.

With the specifications it is given, the program will retrieve the titles of the news articles on these two sites. These titles are cleaned up and written into the *articleOutput.txt* file. 

## Beautiful Soup:

This program uses BeautifulSoup for it's web scrapping functionality. This software uses html parsers to scan a given URLs source code and return the content the program prompts it to retrieve. 

Clone the enviornment I provided in the *scrape_requirements.yaml* to aquire BeautifulSoup and the packages needed to use it. Should that fail, you can install it with the bash command bellow.

This call downloads BeautifulSoup:
    
    ```
            pip install beautifulsoup4

    ```
You may also need the parser package:

    ```
            pip install html5lib

    ```

## Compiling:

No work needs to be done for compiling. The resulting article titles will be present in the articleOutput.txt file.

Enjoy!
