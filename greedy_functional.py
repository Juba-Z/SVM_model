import random
import copy
import heapq

def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                real_val = value - 1
                goal_i = real_val // 3
                goal_j = real_val % 3
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def get_moves(board):
    moves = []
    x, y = find_zero(board)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = copy.deepcopy(board)
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            moves.append(new_board)
    
    return moves

# greedy search algorithm
def solve_puzzle(start):
    cnt = 0
    h = manhattan_distance(start)
    open_list = [(h, cnt, start, [start])]
    cnt += 1
    
    visited = set()
    expanded = 0
    
    while len(open_list) > 0:
        current_h, _, current, path = heapq.heappop(open_list)
        expanded += 1
        
        if is_goal(current):
            return path, expanded
        
        state = tuple(map(tuple, current))
        if state in visited:
            continue
        
        visited.add(state)
        
        for next_state in get_moves(current):
            state_tuple = tuple(map(tuple, next_state))
            if state_tuple not in visited:
                h_val = manhattan_distance(next_state)
                new_path = path + [next_state]
                heapq.heappush(open_list, (h_val, cnt, next_state, new_path))
                cnt += 1
    
    return None, expanded

def check_solvable(board):
    flat = []
    for row in board:
        for num in row:
            flat.append(num)
    
    inv = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if flat[i] != 0 and flat[j] != 0 and flat[i] > flat[j]:
                inv += 1
    
    return inv % 2 == 0

def show_board(board):
    print("\n+---+---+---+")
    for row in board:
        print("|", end="")
        for num in row:
            if num != 0:
                print(" " + str(num) + " |", end="")
            else:
                print("   |", end="")
        print("\n+---+---+---+")

def make_puzzle():
    nums = list(range(9))
    while True:
        random.shuffle(nums)
        board = [nums[0:3], nums[3:6], nums[6:9]]
        if check_solvable(board):
            return board

def get_direction(old, new):
    x1, y1 = find_zero(old)
    x2, y2 = find_zero(new)
    
    if x2 < x1:
        return "UP"
    elif x2 > x1:
        return "DOWN"
    elif y2 < y1:
        return "LEFT"
    else:
        return "RIGHT"

def play():
    print("=" * 45)
    print("     8-Puzzle Game - Manual Mode")
    print("=" * 45)
    
    board = make_puzzle()
    moves = 0
    
    while True:
        if is_goal(board):
            break
            
        print("\n" + "-" * 45)
        print(f"Move: {moves}")
        show_board(board)
        h = manhattan_distance(board)
        print(f"\nManhattan Distance: {h}")
        
        possible = get_moves(board)
        print("\nPossible moves:")
        for i in range(len(possible)):
            d = get_direction(board, possible[i])
            print(f"  {i+1}. {d}")
        
        print("\nOptiens: enter move number, 'h' for hint, 's' to solve, 'q' to quit")
        choice = input("Your choice: ").strip()
        
        if choice == 'q':
            print("Exiting...")
            break
        elif choice == 'h':
            # give hint
            print("Calculating hint...")
            solution, _ = solve_puzzle(board)
            if solution and len(solution) > 1:
                next_move = solution[1]
                d = get_direction(board, next_move)
                print(f"Hint: Try {d}")
                board = next_move
                moves += 1
            else:
                print("No hint available")
        elif choice == 's':
            print("Solving puzzle...")
            solution, exp = solve_puzzle(board)
            if solution:
                print(f"Found solution in {len(solution)-1} steps")
                print(f"Nodes expanded: {exp}")
                
                ans = input("Show steps? (y/n): ")
                if ans.lower() == 'y':
                    for i in range(1, len(solution)):
                        print(f"\nStep {moves + i}:")
                        show_board(solution[i])
                        if i < len(solution) - 1:
                            input("Press Enter...")
                
                board = solution[-1]
                moves += len(solution) - 1
            else:
                print("No solution found")
        else:
            # manual move
            try:
                num = int(choice)
                if 1 <= num <= len(possible):
                    board = possible[num - 1]
                    moves += 1
                else:
                    print("Invalid move number")
            except:
                print("Invalid input")
    
    if is_goal(board):
        print("\n" + "=" * 45)
        print("      CONGRATULATIONS! YOU WON!")
        print("=" * 45)
        show_board(board)
        print(f"\nTotal moves: {moves}")

def auto_solve():
    print("=" * 45)
    print("     8-Puzzle Game - Auto Solve")
    print("=" * 45)
    
    board = make_puzzle()
    print("\nInitial state:")
    show_board(board)
    
    h = manhattan_distance(board)
    print(f"\nManhatan Distance: {h}")
    
    print("\nSolving...")
    solution, exp = solve_puzzle(board)
    
    if solution:
        print(f"\nSolution found!")
        print(f"Steps: {len(solution) - 1}")
        print(f"Nodes expanded: {exp}")
        
        ans = input("\nShow solution? (y/n): ")
        if ans.lower() == 'y':
            for i, state in enumerate(solution):
                print(f"\nStep {i}:")
                show_board(state)
                h = manhattan_distance(state)
                print(f"Manhattan Distance: {h}")
                if i < len(solution) - 1:
                    cont = input("Press Enter (or 'a' for all)... ")
                    if cont.lower() == 'a':
                        # show all remaining
                        for j in range(i+1, len(solution)):
                            print(f"\nStep {j}:")
                            show_board(solution[j])
                        break
            print("\nPuzzle solved!")
    else:
        print("No solution found!")

print("\n" + "=" * 45)
print("          8-PUZZLE GAME")
print("=" * 45)

while True:
    print("\n1. Play manually")
    print("2. Auto solve")
    print("3. Exit")
    
    choice = input("\nChoose option (1-3): ").strip()
    
    if choice == '1':
        play()
    elif choice == '2':
        auto_solve()
    elif choice == '3':
        print("Godbye!")
        break
    else:
        print("Involid choice")