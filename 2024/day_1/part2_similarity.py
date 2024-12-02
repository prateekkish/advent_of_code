from collections import Counter
from common.parse_input import parse_input

def sum_similarity(left_list, right_list):
  frequencies = Counter(right_list)
  return sum([left * frequencies[left] for left in set(left_list)])


if __name__ == '__main__':
  left_list, right_list = parse_input()
  print(sum_similarity(left_list, right_list))
