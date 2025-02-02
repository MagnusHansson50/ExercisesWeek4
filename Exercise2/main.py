from multiprocessing.spawn import set_executable

import printouts
import loop
import list_functions
import average

printouts.greeting("Magnus")

printouts.eko("Hej", 3)

loop.loop()

last = [1, 2, 3]
result = list_functions.last(last)
print(result)

remove_first_last = [1, 2, 3, 4]
result = list_functions.cut_edges(remove_first_last)
print(result)

remove_first_last = [1, 2, 3, 4]
result = list_functions.cut_edges_second(remove_first_last)
print(result)

result = average.average(5, 6)
print(result)

printouts.pretty_print(["a", "b", 3.14])
printouts.pretty_print([])