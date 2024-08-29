snake = [[1, 1]]
food = [[1, 4], [3, 1], [5, 5], [2, 1], [1, 3], [6, 6], [6, 1]]
print("This is a snake game")
print("Enter your choice : \n1. PLAY\n2. QUIT")

loop = True
while loop:
    choice = int(input())

    if choice == 1:
        while 7 > snake[-1][0] > 0 and 7 > snake[-1][1] > 0:
            for i in range(1, 7):
                for j in range(1, 7):
                    if [i, j] in snake:
                        print("0", end="")
                    elif [i, j] in food:
                        print("X", end="")
                    else:
                        print(".", end="")
                print()
            print("__________________")

            move = input()
            next_position = [snake[-1][0], snake[-1][1]]

            if move == 'W':
                next_position[0] -= 1
            elif move == 'S':
                next_position[0] += 1
            elif move == 'A':
                next_position[1] -= 1
            elif move == 'D':
                next_position[1] += 1
            elif move == 'E':
                print("You quit the game")
                break
            else:
                print("Invalid input")
                continue

            if not (1 <= next_position[0] < 7 and 1 <= next_position[1] < 7):
                print("You hit the wall. You lose the game")
                break

            if next_position in snake:
                print("The snake bit itself. You lose the game")
                break

            if next_position in food:
                food.remove(next_position)
                if len(food) == 0:
                    print("Congrats you've won the game!!!!")
                    break
            else:
                snake.pop(0)

            snake.append(next_position)

    elif choice == 2:
        print("BYE BYE :(")
        break

    else:
        print("Enter your choice : \n1. PLAY\n2. QUIT")
        print("Enter a valid choice : ")
