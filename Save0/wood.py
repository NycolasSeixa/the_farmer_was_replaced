from functions import is_even

def farm():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest() and (get_entity_type() == Entities.Bush or get_entity_type() == Entities.Tree):
				harvest()
			if is_even(x+y):
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
			move(East)
			x = get_pos_x()
		move(North)
		y = get_pos_y()