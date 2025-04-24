from transformers import AutoTokenizer, AutoModelForCausalLM
# Parent Class for tokenizer and model
# Defines the Model name with the value passed into it
class LLM_model:
    # Assignment Functions for model name
    def __init__(self, model_name):
        self.model_name = model_name

# Class for the token
class Tokenizer(LLM_model):
    # Returns the tokenizer to be used for LLM queries
    def set_token(self):
        try: 
            # References self.model_name as inherited from Parent class
            tokenizer= AutoTokenizer.from_pretrained(self.model_name)
            # Return tokenizer for LLM use
            return tokenizer
        except Exception as e:
            # Print error for creating the tokenizer
            print(f"An error occurred with creating the tokenizer{e}")

# Class for the model
class Model(LLM_model):
    # Returns the model to be used to query the LLM
    def set_model(self):
        try:
            # References self.model_name as inherited from Parent class
            model = AutoModelForCausalLM.from_pretrained(self.model_name)
            # Return the model for LLM use
            return model
        except Exception as e:
            # Print error for initializing the model
            print(f"An error occurred with initializing model{e}")


# Class for determining the sentiment of a prompt    
class SentimentFinder:
    # Assigns the tokenizer and model to the object
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    # Reads each line from a file as an input to be evaluated
    def get_prompts(self, input_filename):
        try:
            # Open the prompt file and attach each line to a list
            with open(input_filename, 'r') as file:
                headlines = file.readlines()
            # Return the list of headlines to be evaluated
            return headlines
        except Exception as e:
            # Print error for getting headlines
            print(f"An error occurred with getting the headlines{e}")

    
    # Takes in instruction and a headline to query the LLM with
    # Returns a single word answer for the sentiment of the headline
    def collect_response(self, instruction):
        # Tokenize the prompt
        inputs = self.tokenizer(instruction, return_tensors="pt")
        try:
            # Generate response from model
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=50,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                top_p=1.0,
                do_sample=False,
                pad_token_id=self.tokenizer.eos_token_id,
            )

            # Decode and extract the response
            full_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            response_only = full_output[len(instruction):].strip()

            # Get just the first word
            sentiment = response_only.split()[0] 

            return sentiment
        except Exception as e:
            # Print error for getting the ouput
            print(f"An error occurred with collecting response{e}")




