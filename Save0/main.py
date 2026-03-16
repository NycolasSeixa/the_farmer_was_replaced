from entity_item_log import *
from unlocks_log import *
import hay, wood, carrot, pumpkin

min_plant = 25000

clear()
ei_log(plant_dict)
un_log(unlock_dict)

while True:
	while(num_items(Items.Hay) < min_plant):
		hay.farm()
	while(num_items(Items.Wood) < min_plant):
		wood.farm()		
	while(num_items(Items.Carrot) < min_plant):
		carrot.farm()
	while(num_items(Items.Pumpkin) < min_plant):
		pumpkin.farm()
	do_a_flip()