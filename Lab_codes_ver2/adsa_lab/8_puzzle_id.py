def is_goal(state):
    return state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def get_possible_moves(state, empty_pos):
    moves = []
    x, y = empty_pos
    if x > 0: 
        moves.append((x - 1, y))  # Move up
    if x < 2: 
        moves.append((x + 1, y))  # Move down
    if y > 0:
        moves.append((x, y - 1))  # Move left
    if y < 2: 
        moves.append((x, y + 1))  # Move right
    return moves

def move(state, empty_pos, new_empty_pos):
    x, y = empty_pos
    new_x, new_y = new_empty_pos
    new_state = state[:]
    new_state[x * 3 + y], new_state[new_x * 3 + new_y] = new_state[new_x * 3 + new_y], new_state[x * 3 + y]
    return new_state, new_empty_pos

def dls(state, empty_pos, limit, visited):

    print(state)

    if is_goal(state):
        return state, visited
    
    elif limit == 0:
        return None, visited
    
    visited.add(tuple(state))

    for move_pos in get_possible_moves(state, empty_pos):

        new_state, new_empty_pos = move(state, empty_pos, move_pos)

        if tuple(new_state) not in visited:

            result, visited = dls(new_state, new_empty_pos, limit - 1, visited)

            if result is not None:
                return result, visited
            
            
    visited.remove(tuple(state))
    return None, visited

def ids(initial_state, empty_pos):
    depth = 0
    while True:
        visited = set()
        result, visited = dls(initial_state, empty_pos, depth, visited)
        if result is not None:
            return result
        depth += 1


# Example usage
initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
empty_pos = (2, 0)  # Position of the empty space

solution = ids(initial_board, empty_pos)
print(solution)

