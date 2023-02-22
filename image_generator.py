from manim import *

class ImageGenerator(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        c1 = WHITE
        c2 = WHITE
        c3 = WHITE
        t4 = IntegerTable(
            [(0, 0, 0),
             (0, 1, 0),
             (1, 0, 0),
             (1, 1, 1)],
            col_labels=[Tex("A", color=c1), Tex("B", color=c2), Tex("C", color=c3)],
            include_outer_lines=True, 
        )
        t4.get_columns()[0].set_color(c1)
        t4.get_columns()[1].set_color(c2)
        t4.get_columns()[2].set_color(c3)
        tcolor = GRAY_C
        t4.get_horizontal_lines().set_color(tcolor)
        t4.get_vertical_lines().set_color(tcolor)
        self.add(t4)