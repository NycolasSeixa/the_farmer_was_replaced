item_dict = {}

for i in Entities:
	item_dict[i] = {
	'Name' : i,
	'Unlock' : num_unlocked(i),
#	'Ammount' : num_items(i),
	'Cost' : get_cost(i)
	}

for i in item_dict:
	quick_print(item_dict[i])