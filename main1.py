from turtle import Turtle ,Screen
import time
from food import Food
from snake import Snake
from scoar_board import Scoreboard
my_screen = Screen()
my_screen.setup(width = 600,height = 600)
my_screen.bgcolor("black")
my_screen.title("My sanke game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.Up,'Up')
my_screen.onkey(snake.down,'Down')
my_screen.onkey(snake.left,'Left')
my_screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


my_screen.exitonclick()