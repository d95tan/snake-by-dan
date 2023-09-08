from readchar import readkey, key
import os
import sys
import time
import threading
import random


class Snake:
    def __init__(self, level, head = [5,11], body = [[5,9],[5,10]], direction = "r", length = 3):
        #initialise Snake, define variables
        self._head = head
        self._body = body
        self._direction = direction
        self._length = length
        self._level = level
        self._food = None
        self.create_food()
        self._score = 0
        self.running = True
        self.lock = threading.Lock()


    def start_game(self):
        #initialises 2 threads: game_loop and listener
        game_thread = threading.Thread(target = self.game_loop)         #learning lesson - how to use multi-threading: 1 thread to run the game, 1 thread to listen for input from user.
        input_thread = threading.Thread(target = self.listener)

        game_thread.start()
        input_thread.start()

        game_thread.join()
        input_thread.join()


    def game_loop(self):
        #runs a loops that refreshes based on level chosen - 1st thread
        sleeptime = 0.5 / self._level

        while self.running:
            os.system("clear")
            renderBoard(self._head, self._body, self._food, self._score)
            self.move()
            if self._head == self._food:
                self._score += self._level
                self._length += 1
                self.create_food()
            time.sleep(sleeptime)

            if self.running == False:
                break


    def listener(self):
        #listens for user input - 2nd thread
        up = ["w","W",key.UP]
        down = ["s","S",key.DOWN]
        left = ["a","A",key.LEFT]
        right = ["d","d",key.RIGHT]

        while self.running:
            h = readkey()
            if h in up and self._direction != "d":
                self.direction("u")
            elif h in down and self._direction != "u":
                self.direction ("d")
            elif h in left and self._direction != "r":
                self.direction("l")
            elif h in right and self._direction != "l":
                self.direction("r")
            elif h == key.BACKSPACE:
                self.running = False
                break
            elif h == key.ENTER:
                self.restartGame(self._level)

    def create_food(self):
        #function to create food (ensures that food doesn't spawn inside snake)
        foodpos = [random.randint(1,9), random.randint(1,20)]
        while foodpos in [self._head] + self._body:
            foodpos = [random.randint(1,9), random.randint(1,20)]
        self._food = foodpos


    def move(self):
        #function to move snake (body absorbs head, head moves forward, body[0] is deleted if length doesn't increase (i.e food isn't eaten))
        self._body.append(list(self._head))         #add the old head to the body

        if self._direction == "r":                  #head[y][x] based on grid below (refer to renderBoard)
            self._head[1] += 1                      #move head to direction (x+1)
        elif self._direction == "l":
            self._head[1] -= 1
        elif self._direction == "u":
            self._head[0] -= 1
        elif self._direction == "d":
            self._head[0] += 1

        if len(self._body) >= self._length:
            del self._body[0]

        if self._head in self._body or self._head[0] == 0 or self._head[0] == 10 or self._head[1] == 0 or self._head[1] == 21:  #snake dead if head is inside body or head is outside play area
            self.game_over(self._score)
            self.running = False


    def direction(self, new_direction):
        #change direction if user input
        self._direction = new_direction


    def game_over(self,score):
        #game over function
        self.running = False
        os.system('clear')
        game_over_text = ["\n", "\n", "-----------------------", "GAME OVER", f"SCORE: {score}", "-----------------------", "", "Press <BACKSPACE> to QUIT", "Press <RETURN> to RESTART", "\n", "\n"]
        for line in game_over_text:
            print(line.center(44, " "))


    def restartGame(self, lvl):
        #re-initialise Snake if user decides to restart game
        self.__init__(level = lvl, head = [5,11], body = [[5,9],[5,10]], direction = "r", length = 3)
        self.start_game()


def main():
    snake = None
    printStart()                                                                    #prints main menu

    while True:                                                                     #wait for user input
        k = readkey()

        if k == "h":
            printHelp()
            continue

        if k == key.BACKSPACE:
            os.system('clear')
            sys.exit("BYE")

        if k == key.ENTER:
            os.system('clear')

            while True:

                try:
                    #asks for level (determines how often/frequent the board refreshes)
                    lvl = int(input("Input level (1-5): "))
                    if not 0 < lvl < 6:
                        os.system('clear')
                        print("Integer between 1-5 only")
                        continue
                except ValueError:
                    os.system('clear')
                    print("Integer between 1-5 only")
                    continue
                else:
                    os.system("clear")
                    snake = Snake(level = lvl)
                    snake.start_game()
                    break
            break
        sys.exit()


def renderBoard(head, body, food, score):
    #play area 20W x 9H
    board = [
        ["  ","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","  "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        ["  ","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","‾‾","  "],
        ]

    board[int(head[0])][int(head[1])] = "::"
    board[int(food[0])][int(food[1])] = "<>"
    for position in body:
        board[int(position[0])][int(position[1])] = "[]"

    for row in board:
        for column in row:
            print(column, end="")
        print()
    print(f"Score: {score}")

    return board


def printHelp():
    print("Control your snake's movements - Don't hit the walls, and don't bite yourself!",
          "Controls:",
          "<w> for UP",
          "<s> for DOWN",
          "<a> for LEFT",
          "<d> for RIGHT",
          "<BACKSPACE> to EXIT",
          "<RETURN> to START",
          sep="\n")


def printStart():
    os.system('clear')
    print("Welcome to Snake by Dan.",
            "Press <RETURN> to start",
            "Press <H> for help", sep="\n"
            )


if __name__ == "__main__":
    main()