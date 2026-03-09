def pad(text_list, padding):
	result = ""

	for i in range(len(text_list)):
		text = str(text_list[i])
		
		while len(text) < padding:
			text += " "
			
		if i == len(text_list) - 1:
			result += text
		else:
			result += text + "| "
		
	return result
	