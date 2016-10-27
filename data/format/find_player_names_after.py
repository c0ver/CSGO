def get_unique_names():
	player_list = []
	with open('../raw_data.txt', 'r') as f:
		for line in f:
			words = line.split()
			if len(words) == 1:
				continue
			for i in range(1, 11):
				player_list.append(words[i * 7])

	f = open('../player_names.txt', 'w')
	player_list.sort()
	print >>f, len(set(player_list))
	print >>f, '\n'.join(set(player_list))
get_unique_names()