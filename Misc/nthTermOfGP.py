input = """
2
84 87
3
1 2
1"""

import sys,math

num_tests = int(sys.stdin.readline())

while num_tests:
    series_string = sys.stdin.readline().split()
    series_num = [int(e) for e in series_string]
    term_index = int(sys.stdin.readline())
    assert(len(series_num) == 2)
    ratio = series_num[1]/series_num[0]
    nth_element = series_num[0] * pow(ratio,term_index-1)
    print nth_element
    num_tests -= 1

output = """
90
2"""
