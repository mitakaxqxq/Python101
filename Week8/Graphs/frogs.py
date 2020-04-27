def move_frog_to_lilly(lake, index, move, positions, frog):
    if not move < 0 and not move >= len(lake):
        if lake[move] == '_':
            new_list = lake[:]
            new_list[index] = '_'
            new_list[move] = frog
            positions.append(new_list)


def find_all_possible_positions(lake):
    positions = []
    for index, frog in enumerate(lake):
        if frog == '>':
            single_move = index + 1
            jump_move = index + 2
        elif frog == '<':
            single_move = index - 1
            jump_move = index - 2
        else:
            continue
        move_frog_to_lilly(lake, index, single_move, positions, frog)
        move_frog_to_lilly(lake, index, jump_move, positions, frog)
    return positions


def find_correct_solution(current_path, ending_state):
    current_state = current_path[-1]
    result_paths = find_all_possible_positions(current_state)
    for elem in result_paths:
        current_path.append(elem)
        if elem == ending_state:
            return current_path
        if find_correct_solution(current_path, ending_state):
            return current_path
        current_path.remove(elem)
    return False


def print_solution_path(list):
    for elem in list:
        print(elem)


def solve():
    number_of_frogs = int(input("Enter the number of frogs you want: "))
    if number_of_frogs % 2 == 1:
        raise ValueError('Wrong value - you must enter an even number greater than 2!')
    left_frogs = number_of_frogs // 2 * '>'
    right_frogs = number_of_frogs // 2 * '<'
    starting_frogs = left_frogs + '_' + right_frogs
    ending_frogs = right_frogs + '_' + left_frogs
    initial_state = list(starting_frogs)
    result = find_correct_solution([initial_state], list(ending_frogs))
    list_of_strings = [''.join(elem) for elem in result]
    return list_of_strings


def main():
    final_steps = solve()
    print_solution_path(final_steps)


if __name__ == '__main__':
    main()
