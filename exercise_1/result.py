from __future__ import print_function
import itertools
l = [["name", "dinner"], ["Abraham", "Avi"], ["Hello", "Tree", "Door"], ["Name",
"Glass", "Two", "am"]]

l_chain = list(itertools.chain.from_iterable(l))
l_without_duplicates=list(set(l_chain))
filtered_list=list(filter(lambda s: len(s) >=5, l_without_duplicates))
print('\n' .join(filtered_list))



