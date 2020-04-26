def find_all_possible_positions(board):
    positions = []
    for index, frog in enumerate(board):
        if frog == '>':
            single_move = index + 1
            jump_move = index + 2
        elif frog == '<':
            single_move = index - 1
            jump_move = index - 2
        else:
            continue
        if not single_move < 0 and not single_move >= len(board):
            if board[single_move] == '_':
                new_list = board[:]
                new_list[index] = '_'
                new_list[single_move] = frog
                positions.append(new_list)
        if not jump_move < 0 and not jump_move >= len(board):
            if board[jump_move] == '_':
                new_list = board[:]
                new_list[index] = '_'
                new_list[jump_move] = frog
                positions.append(new_list)
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


def convert_list_of_lists_into_list_of_strings(list_of_lists):
    list_of_strings = []
    for elem in list_of_lists:
        new_string = ''.join(elem)
        list_of_strings.append(new_string)
    return list_of_strings


def print_solution_path(list):
    for elem in list:
        print(elem)


def solve():
    number_of_frogs = int(input("Enter the number of frogs you want: "))
    left_frogs = number_of_frogs * '>'
    right_frogs = number_of_frogs * '<'
    starting_frogs = left_frogs + '_' + right_frogs
    ending_frogs = right_frogs + '_' + left_frogs
    initial_state = list(starting_frogs)
    result = find_correct_solution([initial_state], list(ending_frogs))
    list_of_strings = convert_list_of_lists_into_list_of_strings(result)
    print_solution_path(list_of_strings)


def main():
    solve()


if __name__ == '__main__':
    main()
