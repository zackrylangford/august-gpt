#import os
#import psycopg2
import openai
from functions import append_chat_logs
# OpenAI settings
openai.api_key = "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"
model_engine = "text-davinci-003"


# My Settings
username = "Zackry"
ai_username = "August"


# Initial Prompt
prompt = input(f"\n{username}: ")


# Conversation Loop
while prompt != '--quit':

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,

            #max length of response
            max_tokens=1024,

            # number of responses
            n=1,

            # Special stopping circumstances
            stop=None,

            #Randomness/creativity setting - higher = more random and open (up to .09)
            temperature=0.8
        )
        # ChatGPT's response
        response = completion.choices[0].text

        # Print the response from ChatGPT in the terminal
        print(f"\n{ai_username}: {response.strip()}")
    
        # Add conversation to txt logs
        append_chat_logs("/home/zack/Desktop/GitHub/Private/august-gpt/documents/chat-logs.txt", prompt, response.strip())


        # Restart the prompt
        prompt = input(f"\n{username}: ")



