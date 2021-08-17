def descendants(family_tree, name, distance):
	final = []
	empty = []
	if distance == 0:
		empty.append(name)
		return empty
# base case
	else:
		for x in family_tree[name]:
# x is the person
			if x in family_tree or distance == 1:
				final.extend(descendants(family_tree,x,distance-1))
# recursive function to run until distance is 0
		return final
