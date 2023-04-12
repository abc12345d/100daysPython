import turtle
import pandas as pd

# setup US map as screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# setup pen for filling the state name
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# setup variable for game
state_data = pd.read_csv("50_states.csv")
all_state = state_data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    user_input = screen.textinput(title=f"{len(guessed_state)} / 50 correct", prompt="What's another state name?").title()

    if user_input == 'Exit':
        data_dict = {
            'state': [state for state in all_state if state not in guessed_state]
        }
        df_unguess_state = pd.DataFrame(data_dict)
        df_unguess_state.to_csv("unguessed_state.csv",index= False)
        break

    if user_input in guessed_state:
        continue

    if user_input in all_state:
        guessed_state.append(user_input)
        row = state_data[state_data.state == user_input]

        # fill state in map
        pen.goto(x= row.x.item(), y= row.y.item())
        pen.write(f"{row.state.item()}")
