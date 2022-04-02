from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time



screen = Screen()
screen.setup(width=600, height=600)
screen.title("Hungry Snake")
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(key="Up", fun= snake.move_up)
screen.onkey(key="Down", fun= snake.move_down)
screen.onkey(key="Left", fun= snake.move_left)
screen.onkey(key="Right", fun= snake.move_right)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.random_food()
        snake.extent()
        scoreboard.increase()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for  snak in snake.snakes:
        if snak == snake.head:
            pass
        elif snake.head.distance(snak) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()