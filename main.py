import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#uzyskuje koordynaty stanu z blank_states_img
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv") #odczytuje stany z pliku 50_states
all_states = data.state.to_list() #wszystkie stany z 50_states w liste
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50. Name of the State",
                                    prompt="Type the name of the State: ").title()#okienko, w ktorym
#wpisuje odpowiedz
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:#jesli odpowiedz wpisana w okienku sie zgadza z ktoryms ze stanow, tworzymy turtle,
        # ktory idzie na koordynaty danego stanu aby wyswietlic jego nazwe
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        #t.write(state_data.state.item())


