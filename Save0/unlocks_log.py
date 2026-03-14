from functions import can_unlock, un_log, cost

unlock_dict = {}

for i in Unlocks:
	unlock_dict[i] = {
		'Unlock': str(i)[8:],
		'Cost': cost(i),
		'Can_unlock': can_unlock(i)
	}