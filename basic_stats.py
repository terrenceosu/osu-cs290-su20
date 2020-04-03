# Author: Terrence Dominguez-Smith
# Date: 4/1/2020
# Description: This program imports the statistics module and collects peoples name and ages which will create tuples
# of the mean, median, and mode of their ages.

import statistics as stats
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

def basic_stats(person_list):
    newage_list = []
    for i in range(len(person_list)):
        a_list = Person.get_age(person_list[i])

        newage_list.append(a_list)

    mean_1 = stats.mean(newage_list)
    median_1 = stats.median(newage_list)
    mode_1 = stats.mode(newage_list)

    tuple_mean_median_mode = (mean_1, median_1, mode_1)
    return tuple_mean_median_mode


#p1 = Person("Kyoungmin", 73)
#p2 = Person("Mercedes", 24)
#p3 = Person("Avanika", 48)
#p4 = Person("Marta", 24)

#person_list = [p1, p2, p3, p4]
#print(basic_stats(person_list))  # should print a tuple of three values
