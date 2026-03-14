from functions import pos_check, x_check, y_check

comeback = []

def farm():
	start_plant()
	replant()
	harvest()
	do_a_flip()
	clear()
	
def start_plant():
	for i in range(get_world_size()):
		for j in range(get_world_size()):			
			if get_entity_type() != Entities.Pumpkin:
				comeback.append([get_pos_x(), get_pos_y()])
				
				till()
				plant(Entities.Pumpkin)
			move(East)
		move(North)
		
def replant():
	while comeback:
		for pos in comeback[:]:

			while not pos_check(pos):
				while get_pos_x() < pos[0]:
					move(East)
				while get_pos_x() > pos[0]:
					move(West)

				while get_pos_y() < pos[1]:
					move(North)
				while get_pos_y() > pos[1]:
					move(South)

			if get_entity_type() != Entities.Pumpkin:
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Pumpkin)
			else:
				comeback.remove(pos)
			