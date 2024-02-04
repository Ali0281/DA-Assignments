def evaluate(configuration):
    for row in configuration:
        if len(set(row)) == 1 and row[0] != '.':
            return row[0]

    if configuration[0][0] == configuration[1][1] == configuration[2][2] and configuration[0][0] != '.':
        return configuration[0][0]

    if configuration[0][2] == configuration[1][1] == configuration[2][0] and configuration[0][2] != '.':
        return configuration[0][2]

    for col in range(3):
        if configuration[0][col] == configuration[1][col] == configuration[2][col] and configuration[0][col] != '.':
            return configuration[0][col]
    return None


def x_win(configuration):
    for row in configuration:
        if len(set(row)) == 1 and row[0] == 'X':
            return True

    if configuration[0][0] == configuration[1][1] == configuration[2][2] and configuration[0][0] == 'X':
        return True

    if configuration[0][2] == configuration[1][1] == configuration[2][0] and configuration[0][2] == 'X':
        return True

    for col in range(3):
        if configuration[0][col] == configuration[1][col] == configuration[2][col] and configuration[0][col] == 'X':
            return True
    return False


def o_win(configuration):
    for row in configuration:
        if len(set(row)) == 1 and row[0] == 'O':
            return True

    if configuration[0][0] == configuration[1][1] == configuration[2][2] and configuration[0][0] == 'O':
        return True

    if configuration[0][2] == configuration[1][1] == configuration[2][0] and configuration[0][2] == 'O':
        return True

    for col in range(3):
        if configuration[0][col] == configuration[1][col] == configuration[2][col] and configuration[0][col] == 'O':
            return True
    return False


def is_full(configuration):
    for row in configuration:
        if '.' in row:
            return False
    return True


def get_empty(configuration):
    empty = []
    for i in range(3):
        for j in range(3):
            if configuration[i][j] == '.': empty.append((i, j))
    return empty


def minimax(configuration, depth, X_turn):
    result = evaluate(configuration)
    if result: return {'score': 1} if result == 'X' else {'score': -1} if result == 'O' else {'score': 0}
    if is_full(configuration): return {'score': 0}
    if X_turn == False:
        best_score = {'score': float('inf')}
        for i, j in get_empty(configuration):
            configuration[i][j] = 'O'
            score = minimax(configuration, depth + 1, True)
            configuration[i][j] = '.'
            best_score = min(score, best_score, key=lambda x: x['score'])
        return best_score
    if X_turn == True:
        best_score = {'score': float('-inf')}
        for i, j in get_empty(configuration):
            configuration[i][j] = 'X'
            score = minimax(configuration, depth + 1, False)
            configuration[i][j] = '.'
            best_score = max(score, best_score, key=lambda x: x['score'])
        return best_score


def initial(configuration, param):
    ans = minimax(configuration, 0, param)
    if ans['score'] == 0: print("draw")
    if ans['score'] == 1: print("X wins")
    if ans['score'] == -1: print("O wins")


R1 = input()
R2 = input()
R3 = input()

str = R1 + R2 + R3
configuration = [list(R1), list(R2), list(R3)]

if not (str.count('X') == str.count("O") or str.count('X') == str.count("O") + 1):
    print("invalid configuration")
elif x_win(configuration) and o_win(configuration):
    print("invalid configuration")
elif str.count('X') == str.count("O"):
    initial(configuration, True)
else:
    initial(configuration, False)
