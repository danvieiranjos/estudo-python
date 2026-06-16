# Treinando Python
# Geek Bhereu

import arcade

# Open the window
arcade.open_window(600, 600, "Draw a parabola for Codingwithsagar ")

# set background
arcade.set_background_color(arcade.color.WHITE)

# start the render process.
arcade.start_render()

# function to draw a rainbow parabola
arcade.draw_parabola_filled(25, 80, 500, 300, arcade.color.RED ,0)
arcade.draw_parabola_filled(50, 70, 470, 280, arcade.color.ORANGE ,0)
arcade.draw_parabola_filled(75, 60, 440, 260, arcade.color.YELLOW ,0)
arcade.draw_parabola_filled(100, 50, 410, 240, arcade.color.GREEN ,0)
arcade.draw_parabola_filled(125, 40, 380, 220, arcade.color.SKY_BLUE ,0)
arcade.draw_parabola_filled(150, 30, 350, 200, arcade.color.VIOLET,0)
arcade.draw_parabola_filled(175, 20, 325, 180, arcade.color.INDIGO ,0)
arcade.draw_parabola_filled(200, 0, 295, 160, arcade.color.WHITE ,0)

# finish drawing
arcade.finish_render()

# to display everything
arcade.run()


#if __name__ == "__main__":
#    main()
