import os
#import psycopg2
import openai
from functions import append_user_input, append_august_input

# OpenAI settings
openai.api_key = os.environ["OPENAI_API_KEY"]
model_engine = "text-davinci-003"


# My Settings
username = "Zackry"
ai_username = "August"

# Database Settings
#conn = psycopg2.connect(
#    database= "chatgptdb",
 #   user="august",
 #   password="robot",
#    host="localhost",
 #   port="5432"
 #   )



# Initial Prompt
prompt = input(f"\n{username}: ")

# Conversation Loop
while prompt != '--quit':


    if prompt != '-quit':
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


    response = completion.choices[0].text
    print(f"\n{ai_username}: {response.strip()}")
    
    # Add user input to database
    append_user_input("/home/zack/Desktop/GitHub/Private/august-gpt/august/user-logs.txt", prompt)

    #Add Marcus output to database
    append_august_input("/home/zack/Desktop/GitHub/Private/august-gpt/august/august-logs.txt", response.strip())

    prompt = input(f"\n{username}: ")



