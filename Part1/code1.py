# Jordan Staggs CS 325
# Built: 2-27-25
# This program prompts TinyLlama with all prompts in the prompt.txt file and out puts 
# the resulting text into the end.txt file
########################################################################################


# from huggingface_hub import login
# # Authenticate using the Hugging Face token
# access_token = "your_hugging_face_access_token"
# login(token=access_token)

from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
tokenizer= AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Open the file for reading
prompts = open('prompts.txt', 'r')
input_text = prompts.readline()
# Loop for reading all of the prompt.txt file
while input_text:
    # Tokenize input for the model
    input = tokenizer(input_text, return_tensors="pt")
    # Generate text through TinyLlama
    outputs1 = model.generate(
    input["input_ids"], # run the tokenized IDs through
    num_return_sequences=1, # number of sequences to be returned
    no_repeat_ngram_size=2, # low number prevents looping(consecutive tokens)
    top_p=1.0, # disabled nucleus sampling
    do_sample=False, # provides more focused outputs
    pad_token_id=tokenizer.eos_token_id, # stops the generating
    attention_mask=input.get("attention_mask", None)  # Include attention mask if available
    )
    # Decode the outputs
    gText = tokenizer.decode(outputs1[0], skip_special_tokens=True)
    #Write the output to end.txt
    with open('end.txt', 'a') as end:
        end.write("Prompt\n")
        end.write(gText)
        end.write("\n")
    input_text = prompts.readline()