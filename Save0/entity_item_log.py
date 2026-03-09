from functions import pad

padding = 13
plant_dict = {}

entity_to_item = {
	Entities.Grass: Items.Hay,
	Entities.Bush: Items.Wood,
	Entities.Tree: Items.Wood,	
	Entities.Carrot: Items.Carrot,
	Entities.Pumpkin: Items.Pumpkin,
	Entities.Cactus: Items.Cactus,
	Entities.Sunflower: Items.Power
}


for entity in entity_to_item:
	item = entity_to_item[entity]

	plant_dict[entity] = {
	'Entity' : str(entity)[9:],
	'Item' : str(item)[6:],
	'Unlock' : num_unlocked(entity),
	'Ammount' : num_items(item),
	'Cost' : get_cost(entity)
	}


def ei_log():
	quick_print(pad(['ENTITY','ITEM','UNLOCKS','AMMOUNT','COST'], padding))
	for i in plant_dict:
		atr = []
		for j in plant_dict[i]:
			atr.append(plant_dict[i][j])
		quick_print(pad(atr,padding))

ei_log()