input = """
2
2 3
4
1 2
10"""

import sys

num_tests = int(sys.stdin.readline())

while num_tests:
    series_string = sys.stdin.readline().split()
    series_num = [int(e) for e in series_string]
    term_index = int(sys.stdin.readline())
    common_diff = series_num[1] - series_num[0]
    nth_element = series_num[0] + (term_index-1) * common_diff
    print nth_element
    num_tests -=1

output = """
5
10"""
