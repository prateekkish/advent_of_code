from common.parse_input import parse_input

def sum_distance(left_list, right_list):
  return sum([abs(left - right) for left, right in zip(left_list, right_list)])


if __name__ == '__main__':
  left_list, right_list = parse_input()
  sorted_left = sorted(left_list)
  sorted_right = sorted(right_list)
  print(sum_distance(sorted_left, sorted_right))
