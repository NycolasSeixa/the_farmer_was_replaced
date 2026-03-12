def farm():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				move(East)
			else:
				do_a_flip()
		move(North)