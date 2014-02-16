# First-fit Algorithm
# Take the items in the order listed, place each item in the
# first bin that has room for it.
from bin import Bin

def first_fit(list_items, max_size):
	""" Returns list of bins with input items inside. """
	list_bins = []
	list_bins.append(Bin()) # Add first empty bin to list

	for item in list_items:
		# Go through bins and try to allocate
		alloc_flag = False

		print("item %d:" % item)

		for bin in list_bins:
			print("\tBin %r - Size %d - Space %d" % (bin, bin.sum(), max_size-bin.sum()))
			if bin.sum() + item <= max_size:
				bin.addItem(item)
				alloc_flag = True
				print("\tAdded to current bin")
				break
		
		# If item not allocated in bins in list, create new bin
		# and allocate it to it.
		if alloc_flag == False:
			newBin = Bin()
			newBin.addItem(item)
			list_bins.append(newBin)
			print("\tNew bin created.")

	# Turn bins into list of items and return
	list_items = []
	for bin in list_bins:
		list_items.append(bin.show())

	return(list_items)



