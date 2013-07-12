def quicksortIP(list):
	if list == []:
		return []
	else:
		pivot = list[0]
		lsr,eq,gtr = partition(list[1:], [], [pivot], [])
	return quicksortIP(lsr) + eq + quicksortIP(gtr)

def partition(list,lsr, eq, gtr):
	while list != []:
		head = list.pop(0)
		if head < eq:
			lsr = [head] + lsr
		if head > eq:
			gtr =  [head] + gtr
		else:
			eq =  [head] + eq
	return (lsr, eq, gtr)