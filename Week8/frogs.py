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

result = find_all_possible_positions(['>','>','_','<','<'])
print(result)