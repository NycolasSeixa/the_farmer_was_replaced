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

ei_pad = 10
def ei_log(plant_dict):
	quick_print(pad(['ENTITY','ITEM','UNLOCKS','AMMOUNT','COST'], ei_pad))
	for i in plant_dict:
		atr = []
		for j in plant_dict[i]:
			atr.append(plant_dict[i][j])
		quick_print(pad(atr, ei_pad))
		
un_pad = 21
def un_log(unlock_dict):
	quick_print(pad(['UNLOCK','COST','CAN_UNLOCK'], un_pad))
	for i in unlock_dict:
		atr = []
		for j in unlock_dict[i]:
			atr.append(unlock_dict[i][j])
		quick_print(pad(atr, un_pad))
	
def is_even(num):
		return num % 2 == 0
		
def can_unlock(unlock):
	cost = get_cost(unlock)
	for item in cost:
		return num_items(item) > cost[item]
		
def cost(entity):
	result = ''
	all_cost = get_cost(entity)
	first = True
	for item in all_cost:
		if not first:
			result += ', '
		first = False
		value = all_cost[item]
		result += str(value) + ' ' + str(item)[6:]
	return result
	
def pos_check(pos):
	return [get_pos_x(), get_pos_y()] == pos
	
def x_check(pos):
	return get_pos_x() == pos
	
def y_check(pos):
	return get_pos_y() == pos