from entity_item_log import *
import hay, wood

clear()

while True:
	if (num_items(Items.Hay) - 1000) > num_items(Items.Wood):
		wood.farm()
	else:
		hay.farm()
	
	