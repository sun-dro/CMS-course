lives = 3
apple_lives = 10
score = 0
grid = ['  .  ']
apple = 'A0'
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7']

print(f"Lives : {lives} _ Apple_Lives : {apple_lives} _ Score : {score}")
print("_________________________________")


def is_apple(row, column):
    apple_row = apple[0]
    apple_column = apple[1]
    if row == apple_row and column == apple_column:
        return True
    else:
        return False


def print_game_board():
    iterletters = iter(letters)
    for i in range(8):
        global grid
        a = '     '
        print(next(iterletters), ""+"|", a.join(grid) * 8, ""+"|")
    #print("________________________")
    #print('        '+ a.join(numbers))
    print(grid)
    if is_apple('A', '0'):
        for line in a:
            print(line)




print_game_board()

