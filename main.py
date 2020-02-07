"""
Starting point of the execution
"""

import pprint

from search.aggregator import multi_search


if __name__ == '__main__':
    k = int(input("Enter number of search outputs:\n"))
    n = int(input("Enter N:\n"))

    search_strings = []
    for i in range(n):
        search_string = input("Enter search string: \n")
        search_strings.append(search_string)

    (results, count) = multi_search(search_strings, k)

    print("\n\nResults:\n")
    pprint.pprint(results)
    print("\n\nTotal Results: ", count, "/", k)
