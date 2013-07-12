
def quicksortOP(list):
	if list == []:
		return []
	else:
		pivot=list[0]
		lsr = quicksortOP([x for x in list[1:] if x < pivot])
		gtr = quicksortOP([x for x in list[1:] if x > pivot])
		return lsr + [pivot] + gtr