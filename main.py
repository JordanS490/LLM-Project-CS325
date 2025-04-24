# Jordan Staggs CS 325
# Built: 4-23-25
# This program scrapes the website associated with the link found in the newsSites.txt file, and collects all of the
# headlines for the articles on the web page.
# It then querys the LLM(LaMini-GPT) with all prompts in the prompts.txt file and writes the senitment(Positive, Negative, or Neutral)
# of the headlines into the end.txt file.
########################################################################################
# LOGINN WITH ACCESS TOKEN TO USE THE LLM HERE:
# 1. Uncomment the following three lines after this instruction section
# 2. Replace the "your_hugging_face_access_token" with the token you generated on Hugging Face
#    *** Refer to the "Possible Login to use the LLM" section of README.md for further instruction
# 3. Run the program with this section still uncommented out. It may take a second
# 4. You may comment out the 3 lines after the first successful compile
# END OF INSTRUCTIONS
########################################################################################
# START OF HUGGING FACE LOGIN SECTION(DO NOT uncomment this line)
# from huggingface_hub import login

# access_token = "your_hugging_face_access_token"
         
# login(token=access_token)

# END OF HUGGING FACE LOGIN SECTION(DO NOT uncomment this line)
########################################################################################

# Import scraper.py and LLMModel.py classes
# All libraries necessary are included on these files
from scraper import Scraper
from LLMModel import Tokenizer, Model, SentimentFinder

# Start of scraping the website*****************************************
#Initialize the scraper object
beauty_scraper = Scraper()
# Extract URL from the newsSites.txt file
url_to_scrape = beauty_scraper.get_URL("newsSites.txt")
# Get the web page content from the URL
page_html = beauty_scraper.open_site(url_to_scrape)
# Collect all of the stripped headlines from the webpage
headlines = beauty_scraper.get_headlines(page_html)
# Write all the headlines to the output file(prompts.txt)
beauty_scraper.write_headlines(headlines, "prompts.txt")


# Start of querying the LLM********************************************
model_name = "MBZUAI/LaMini-GPT-1.5B"

# Create instances
tokenizer_instance = Tokenizer(model_name)
model_instance = Model(model_name)

# Load tokenizer and model
tokenizer_loaded = tokenizer_instance.set_token()
model_loaded = model_instance.set_model()

# Create SentimentFinder
sentiment_finder = SentimentFinder(model_loaded, tokenizer_loaded)

# Identify output file to write the sentiments to
output_filename = "end.txt"
# Loop with new instructions based on each individual headline
# Print to the output file
with open(output_filename, 'a') as final:
    for headline in headlines:
        # Instruction to give to the SentimentFinder
        instruction = (
            "### Instruction:\n"
            f"Classify this headline as either Positive, Negative, or Neutral. Respond with a single word only: {headline}\n\n"
            "### Response:\n"
        )
        
        # Write each sentiment to the output file
        final.write(sentiment_finder.collect_response(instruction))
        final.write("\n")



