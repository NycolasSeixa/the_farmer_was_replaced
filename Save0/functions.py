padding = 13
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

def ei_log(plant_dict):
	quick_print(pad(['ENTITY','ITEM','UNLOCKS','AMMOUNT','COST'], padding))
	for i in plant_dict:
		atr = []
		for j in plant_dict[i]:
			atr.append(plant_dict[i][j])
		quick_print(pad(atr,padding))
		
def is_even(num):
		return num % 2 == 0