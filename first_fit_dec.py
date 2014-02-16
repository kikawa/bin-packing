# First-fit Decreasing Algorithm
# Sort values into decreasing order.
# Then apply first-fit algorithm.
from bin import Bin
from first_fit import first_fit

def first_fit_dec(list_items, max_size):
	""" Returns list of bins with input items inside. """
	# Sort list in decreasing order
	list_items.sort(reverse=True)

	# Apply first-fit algorith
	return(first_fit(list_items, max_size))
