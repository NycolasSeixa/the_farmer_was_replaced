from functions import pad, ei_log, cost
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
	'Cost' : cost(entity)
	}

# ei_log(plant_dict)