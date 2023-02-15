import openai
from functions import append_user_input, append_august_input

# OpenAI settings
openai.api_key = "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"
model_engine = "text-davinci-003"


# My Settings
username = "Zackry"
ai_username = "August"

# Database Settings




# Initial Prompt
prompt = input(f"\n{username}: ")

# Conversation Loop
while prompt != '--quit':
    
    # Add user input to database
    append_user_input("user-data.txt", prompt)

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
    
    #Add Marcus output to database
    append_august_input("august-data.txt", response.strip())

    prompt = input(f"\n{username}: ")



