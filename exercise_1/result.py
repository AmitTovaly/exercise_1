from __future__ import  print_function
import itertools
l = [["name", "dinner"], ["Abraham", "Avi"], ["Hello", "Tree", "Door"], ["Name",
"Glass", "Two", "am",]]
#in this section all the sub list unify to one bigger list.
l_chain =list(itertools.chain.from_iterable(l))
#in this section all the duplicate remove from the bigger list.
l_without_duplicate=list(set(l_chain))
#in this section its print all the strings that have more than two characters in the middle of them.
filtered_list=list(filter(lambda s: len(s) >=5, l_without_duplicate))
print("\n".join(filtered_list))


