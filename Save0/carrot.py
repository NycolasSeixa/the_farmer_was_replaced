def farm():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			if get_entity_type() == Entities.Carrot and can_harvest():
				harvest()
			plant(Entities.Carrot)
			move(East)
		move(North)