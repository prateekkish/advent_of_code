def parse_input():
  left_list = []
  right_list = []

  with open('../data/day1_input.txt', 'r') as input_file:
    for line in input_file:
      left_val, right_val = line.strip().split()
      left_list.append(int(left_val))
      right_list.append(int(right_val))

  return left_list, right_list
