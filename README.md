# Program Overview
## General Functionality
The function of the code is to read a URL, find the headlines from the associated financial news webpage, and write a list with "Postive", "Negative", or "Neutral" as it relates to the sentiment of each headline. 

It is broken in to parts of functionality: Scraping and Sentiment Finding.
The whole program compiles with *main.py* but it refers to *scraper.py* for the classes relating to scraping and *LLMModel.py* for the classes that relate to query an LLM to get the sentiment. The file *newsSites.txt* contains the url for the website, *prompts.txt* recieves the list of headlines from the web page, and *end.txt* recieves the final sentiment of the headlines.

## Requirements
Please clone the environment provided in the *requirments.yml* file. If that is an issue, the packages needed are:
    <ol>
        <li>beautifulsoup4 - FOR SCRAPING</li>
        <li>html5lib - FOR SCRAPING</li>
        <li>transformers - FOR FINDING SENTIMENT</li>
        <li>pytorch - FOR FINDING SENTIMENT</li>
   </ol>
Instructions on how to install the packages using bash are found in the relating two sections(Scraping and Sentiment Finding)

# Scraping Section Information
## What it does:
This section will read the URL found in the *newsSites.txt* and scrape the relating webpage to return the headlines of the articles present on said webpage. **This is specfiic to this webpage. If another site is to be scrapped the class and tag specifications found in the Scraper class' module *get_headlines(page_html) will need to be changed to fit that webpage.**
Thes headlines are stripped and written to the *prompts.tx* file for later use. **See Sentiment Finding Section**.
## Beautiful Soup:

This program uses BeautifulSoup for it's web scrapping functionality. This software uses html parsers to scan the given URLs source code and return the content the program prompts it to retrieve. 

Should you not be able to clone the enviornment in the *requirements.yml*, you can install it with the bash command bellow:
    ```
            pip install beautifulsoup4
    ```
You may also need the parser package:
    ```
            pip install html5lib
    ```
## Output of the Scraper
You should be able to run this portion of the program once you have these packages!
The output will be in the *prompts.txt* file. It will be a list of the headlines that were scraped from the website(around 30 lines).

# Sentiment Finding Section
## What it does:
This section will take the lines from *prompts.txt* and find the sentiment(Positive, Negative, or Neutral) of each headline and put the result in the *end.txt* file.
## Installing Transformers

If you haven't already, you have to install transformers into your conda enviornment. If you have not already, create a new enviornment with the parameters given in the *requirments.yml* that I have provided. Should you need to, you can use this call to install the transformer library by prompting the terminal:

    ```
            conda install -c conda-forge transformers huggingface_hub
    ```

This should ensure you have the libraries needed for the program.

## Installing PyTorch

You will also have to install pytorch so the program can run off your CPU and/or GPU. The installation process for this is similar to how you installed tranformers. You are going to put another prompt into your terminal that looks like:


    ```
            conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    ```

This call downloads pytorch to run off of your GPU with CUDA. If you want to run it off your CPU you will have to change the call to look like this:
    
    ```
            conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```

Either will work for this program, but using your GPU may lead to faster compiling.

## Possible Login to use the LLM

You may have to get access to the La-Mini through the Hugging Face website. If you get an access error after trying to compile the program, you will have to create an account to get access. In order to compile the program for the first time, you will need to login to your Hugging Face account through your code. You can do this by creating a new access token on the website.

Once on the [Hugging Face](https://huggingface.co/) website, register or sign in. Click settings in top right corner, then access tokens on the left side panel, and then you will be prompted to input your password. Once you have authenitcated, you arrive on a page that says "Create new Token" on the right side. Click that. When prompted, input a name that indicates what the token is being used for(example: P1Test1). Select all Repositories and Repository Permissions, then click create token.

You now should have a token you can copy. At the top of main.py you will find a commented segment for logging in at the very top:
    
    ```
         from huggingface_hub import login

         # Authenticate using the Hugging Face token

         access_token = "your_hugging_face_access_token"
         
         login(token=access_token)
    ```

Replace *your_hugging_face_access_token* with your copied token. Make sure to keep the quotations, and uncomment that whole segment. Then you should be able to use LaMini.

***You only have to login once, so you can comment it out after the first successful run.***

## First Compile

Your first compilation is going to take a while since it has to download all of the files for the LLms as well as the transformer and pytorch library if you have never used them before. Depending on your device, it could take several minutes, so try to have as little other applications running as you can, and be patient. 

After the first compilation, it should output much faster!

## After the First Compile

Depending on your device, compilation can be really slow since it is running off you CPU and GPU. Do not fret if it hase been five minutes. Just make sure you have as few applications opened as possible, and it will output to end.txt in due time.

## Output of Sentiment Finding
The output will be in the *end.txt* file. It will be a list of "Positive", "Negative", and "Neutral". These are the sentiments of the article headlines recieved from the *prompts.txt* file.

# Testing with Pytest
The pytest package is included in the *requirements.yml* file, but if you need to download it, execute this in the terminal:

    ```
            pip install pytest
    ```
Once installed, you can run the tests on *testScraper.py* by bashing this in the terminal:
    ```
            pytest testScraper
    ```
This should come back with 2 tests passed!

# Final Remarks
This program has a very specific use, but it is also made to be very easy to use. Please reach out with any issues.

Enjoy!
