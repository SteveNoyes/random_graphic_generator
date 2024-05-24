from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)



    for i in range(N_CIRCLES):
        

        random_left_x = random.randint(0, CANVAS_HEIGHT)
        random_top_y = random.randint(0, CANVAS_WIDTH)
        random_right_x = random_left_x + CIRCLE_SIZE
        random_bottom_y = random_top_y + CIRCLE_SIZE
        random_color_this_round = str(random_color())




        pop = canvas.create_oval(random_left_x, random_top_y, random_right_x, random_bottom_y, random_color_this_round)






def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()