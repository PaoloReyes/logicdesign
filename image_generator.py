from manim import *

class TTGenerator(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        t4 = IntegerTable(
            [(0, 0, 0, 0, 0),
             (0, 0, 0, 1, 0),
             (0, 0, 1, 0, 1),
             (0, 0, 1, 1, 1),
             (0, 1, 0, 0, 0),
             (0, 1, 0, 1, 1),
             (0, 1, 1, 0, 0),
             (0, 1, 1, 1, 1),
             (1, 0, 0, 0, 0),
             (1, 0, 0, 1, 0),
             (1, 0, 1, 0, 0),
             (1, 0, 1, 1, 1),
             (1, 1, 0, 0, 0),
             (1, 1, 0, 1, 1),
             (1, 1, 1, 0, 0),
             (1, 1, 1, 1, 0)],
            col_labels=[MathTex("X_3"), MathTex("X_2"), MathTex("X_1"), MathTex("X_0"), Tex("P")],
            include_outer_lines=True, 
        ).scale(0.4)
        tcolor = GRAY_C
        t4.get_horizontal_lines().set_color(tcolor)
        t4.get_vertical_lines().set_color(tcolor)
        self.add(t4)

class LatexGenerator(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        eq1 = MathTex(r"\left(\overline{X_3}+\overline{X_2}+\overline{X_1}\right)+\left(\overline{X_3}+X_0\right)+\left(\overline{X_2}+X_0\right)+\left(X_2+X_1\right)")
        self.add(eq1)