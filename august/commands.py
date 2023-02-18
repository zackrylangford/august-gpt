import os
import openai
from commands import *
# OpenAI settings
openai.api_key = ""
model_engine = "text-davinci-003"

def create_document():
        i = 1
        while os.path.exists("/home/zack/Documents/august/Document%s.odt" % i):
            i += 1
        file = open("/home/zack/Documents/august/Document%s.odt" % i, "w")
        file.close()
        print('Document created.')
    
def append_document(doc_prompt):
        answer = doc_prompt
        
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=answer,

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
        print(f"\nAugust: {response.strip()}")
        append_document_text("/home/zack/Documents/august/Document%s.odt", response) 
            
def append_document_text(file_name, response):
	file_in = open(file_name, 'a')
	august_input = response
	file_in.write(august_input+"\n")
            
	file_in.close()









## WOrking on document creation

        create_document()
        answer = input(f"\n{ai_username}: What would you like me to write?")
        doc_prompt = input 



        
        append_document(doc_prompt)
        prompt = input(f"\n{username}: ")







