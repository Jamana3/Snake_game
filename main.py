import turtle
import time
from food import Food              ### if we only write import food then we would not able to use class Food so we need
from turtle import Screen          ### to import Food class also from food module                        
from snake import Snake
from scoreboad import Score

screen = turtle.Screen()

screen.tracer(0)            #### It lead to sleeping of screen, we can only see after we update it backs
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("Snake Game")

snake = Snake()
score = Score()

# screen.update()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


food = Food()


game_is_on = True
while game_is_on:
    snake.move()
    screen.update()                     ### whatever code is written, gonna see only after we update our screen.
    time.sleep(0.1)                     ###  the screen got sleep for 0.2 seconds.
    if snake.object[0].distance(food)<15:
        food.create()
        snake.add_object()
        score.update_score()
    if snake.object[0].xcor() < -280 or snake.object[0].xcor() > 280 or snake.object[0].ycor() < -255 or snake.object[0].ycor() > 255:
        game_is_on = False
        score.game_over()
    i = snake.object[1:len(snake.object)]
    for pos in i:
       if snake.object[0].distance(pos) < 15:
          game_is_on = False
          score.game_over()

screen.exitonclick()



