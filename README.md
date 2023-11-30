# SNAKE BY DAN - CS50 Final Project
### Video Demo:  https://youtu.be/U_9CUF-2JOo

### BACKGROUND -
After the second-last lecture (on Object-Oriented Programming), I came up with the idea of recreating the beloved Nokia Snake game.

I spoke to my trustworthy friend (ChatGPT) for advice - asking if the project was too ambitious and looking for alternative ideas. I knew it would be quite a challenge, and was very tempted to take the easy way out and program a "Personal Finance Tracker" instead.

Despite this, I decided to give it a shot before I gave up, and so I started by focusing on grabbing the lowest hanging fruits.

### CODING -
ChatGPT recommended using a framework for the graphics, such as Pygame, Turtle or Arcade. Instead, I opted to run the entire game inside the terminal as I felt that this project should focus on the programming, rather than the fidelity and polish-ness of the final product.

Firstly, I coded the functions to render the board - following as closely as I could to the original snake game (20 wide by 9 high). Each "pixel" would be represented by 2 blank spaces "  ", the head of the snake with "::", the rest of the body with "[]", and the food with "<>". #keep-it-simple.

I then did a little bit of research and found the library "readchar", which allowed the program to take inputs from the user without having to press enter. I knew I needed a function like this for the game itself, and experimented using it for the main menu and help screen.

The Snake class was the part I was most unsure about. I did the easy bits first - self.move & self.direction. Then came the harder parts - running the game. My thinking was as follows: refresh the board at regular intervals (based on level). If the user gave an input, then the snake should respond. Otherwise, the snake should continue moving in the original direction. When I tried implementing this, the program would either:
1. Only refresh when user input was given
2. Keep refreshing but not accept any user input

Upon closer inspection, I found the issue. When using readchar.readkey function and an "if" statement, the program will not proceed with the code until the if (or else) statement is fulfilled. I tried many ways of circumventing this issue:
1. Multiple while loops didn't work - the program only runs one at a time
2. Using python's time library - by refreshing the board when the current time >= refresh time. This caused the board to constantly flicker and still, did not accept the user's input.

Ultimately, with ChatGPT's help, I (hesitantly) implemented a solution using the "threading" module. This allows different functions to run concurrently on different threads - 1 for refreshing the game, 1 to listen for the user's input. Surprisingly, this method worked.

Once I got the snake moving, the rest of the program was quite simple.
1. Death - by checking if the head of the snake is biting itself, or if the head was out-of-bounds.
2. Food - creating food randomly, check if it is inside the snake. If yes, create again.
3. Scoring - each time the head is inside the food, score += level, length += 1.
4. End menu - quitting (sys.exit) and restarting (re-initialising the snake with the default initial variables). I remember Al Sweigart talking about formatting text in his book, so I implemented the same technique to make the end-menu a little prettier.

### CONCLUSION -
This project was very challenging as I have never coded anything as interactive as this.

Learning lessons:
1. Don't be afraid to use libraries. Sometimes ChatGPT gives unnecessarily complex and convoluted solutions. Other times, like the use of threading, it seems to be the best method.
2. Start with the easy things and build momentum. I had no idea where to start, so I started with the things that I knew I knew how to code. As you progress, the items that fall inside the "I don't know | I don't know" quadrant slowly migrate to the "I know | I don't know" quadrant, and then its a matter of researching solutions online and consulting ChatGPT to come up with solutions.

### Next Steps -
There are some other features which would be nice-to-haves, but I felt were unnecessary for this proof-of-concept:

1. High-score - For persistent memory of high-score, I could write a txt file with the top 10 high scores and names, check if the current score is better than any and then write to file.
2. No-wall mode - in some versions of Nokia's snake, the snake could pass through walls and appear on the other side. I could check for this in the Snake.move function and transport the head to the other side of the play area.
3. I could improve the graphics by adding a directional head, right angle symbols when the snake turns etc.
4. Or better yet, as mentioned at the beginning, I could utilise a framework/library to pretty the game and add nicer graphics.
