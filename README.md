# Installing Software for code1.py and code2.py

# Installing Transformers

If you haven't already, you have to install transformers into your conda enviornment. Create a new enviornment with the parameters given in the requirments.yaml that I have provided. Should you need to, you can use this call to install the transformer library by prompting the terminal:
    ```python
            conda install -c conda-forge transformers huggingface_hub
    ```
This should ensure you have the libraries needed for the program.

# Installing PyTorch

You will also have to install pytorch so the program can run off your CPU and/or GPU. The installation process for this is similar to how you installed tranformers. You are going to put another prompt into your terminal that looks like:
    ```python
            conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    ```python
This call downloads pytorch to run off of your GPU with CUDA. If you want to run it off your CPU you will have to change the call to look like:
    ```python
            conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```python
Either will work for this program, but using your GPU may lead to faster compiling.

## Possible Login to use the LLMs

You may have to get access to the LLMs through the Hugging Face website. If you get an access error after trying to compile the program, you will have to create an account to get access. In order to compile the program for the first time, you will need to login to your Hugging Face account through your code. You can do this by creating a new access token on the website.

Once on the [Hugging Face](https://huggingface.co/) website, register or sign in. Click settings in top right corner, then access tokens on the left side panel, and then you will be prompted to input your password. Once you have authenitcated, you arrive on a page that says "Create new Token" on the right side. Click that. When prompted, input a name that indicates what the token is being used for(example: P1Test1). Select all Repositories and Repository Permissions, then click create token.

You now should have a token you can copy. In both code1.py and code2.py you will find a commented segment for logging in at the very top:
    ```python
         from huggingface_hub import login
         # Authenticate using the Hugging Face token
         access_token = "your_hugging_face_access_token"
         login(token=access_token)
    ```
Replace *your_hugging_face_access_token* with your copied token. Make sure to keep the quotations, an uncomment that whole segment. Then you should be able to use TinyLlama and LaMini.

***You only have to login once, so you can comment it out after the first successful run.***

# First Compile

Your first compilation is going to take a while since it has to download all of the files for the LLms as well as the transformer and pytorch library if you have never used them before. Depending on your device, it could take several minutes, so try to have as little other applications running as you can, and be patient. 

After the first compilation, it should output much faster!

# After the First Compile

Depending on your device, compilationcan be really slow since it is running off you CPU and GPU. Do not fret if it hase been five minutes. Just make sure you have as few applications closed, and it will output to end.txt in due time.
