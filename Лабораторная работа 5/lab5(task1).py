from pprint import pprint

new_list = [{'bin' : bin(x), 'dec' : x, 'hex' : hex(x), 'oct' : oct(x)} for x in range(16)]
pprint(new_list)

# TODO решить с помощью list comprehension и распечатать его
