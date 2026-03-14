def farm():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			while not can_harvest():
				pass
			harvest()
			move(East)
		move(North)