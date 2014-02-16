# Examples
from first_fit import first_fit
from first_fit_dec import first_fit_dec

items = [8, 16, 12, 8, 45, 18, 30, 7, 10, 14, 9, 9, 52, 88]
bin_height = 60

# First-fit Algorithm
print(first_fit(items, bin_height))

# First-fit Decreasing Algorithm
print(first_fit_dec(items, bin_height))