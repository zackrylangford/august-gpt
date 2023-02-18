
#Save conversation between user and chatgpt to txt file

def append_chat_logs(file_name, prompt, response):
	file_in = open(file_name, 'a')
	user_input = (f"Zackry: {prompt}")
	august_input = (f"August: {response}")
	file_in.write(user_input+"\n\n"+august_input+"\n\n")
            
	file_in.close()




# Save August output
#def append_august_output(file_name, response):
	#file_in = open(file_name, 'a')
	#august_input = response
	#file_in.write(august_input+"\n")
            
	#file_in.close()


