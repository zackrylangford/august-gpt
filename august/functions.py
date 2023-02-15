
#Save user input to database

def append_user_input(file_name, prompt):
	file_in = open(file_name, 'a')
	user_input = prompt
	file_in.write(user_input+"\n")
            
	file_in.close()


# Save August input to database

def append_august_input(file_name, response):
	file_in = open(file_name, 'a')
	august_input = response
	file_in.write(august_input+"\n")
            
	file_in.close()
