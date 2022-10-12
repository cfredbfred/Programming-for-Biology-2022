#!/usr/bin/env python3


# Fn = Fn-1 + Fn-2
# need a way to track the history of rabit population numbers
# trying a list to track history

months = 32
rabbit_litter_number = 4

#need to append this list with the updated population number
population_list = [1, 1]

previous_month = 0
this_month = 0

for i in range(2, (int(months))):
    this_month = (population_list[i-1]) + ((rabbit_litter_number) * (population_list[i-2]))
    population_list.append(this_month)

print(population_list)


