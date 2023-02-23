from manim import *

class TTGenerator(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        t4 = IntegerTable(
            [(0, 0, 0, 0, 0),
             (0, 0, 1, 0, 1),
             (0, 1, 0, 0, 1),
             (0, 1, 1, 1, 0),
             (1, 0, 0, 0, 1),
             (1, 0, 1, 1, 0),
             (1, 1, 0, 1, 0),
             (1, 1, 1, 1, 1)],
            col_labels=[MathTex("C_{in}"), Tex("X"), Tex("Y"), MathTex("C_{out}"), Tex("S")],
            include_outer_lines=True, 
        ).scale(0.7)
        tcolor = GRAY_C
        t4.get_horizontal_lines().set_color(tcolor)
        t4.get_vertical_lines().set_color(tcolor)
        self.add(t4)

class LatexGenerator(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        eq1 = MathTex(r"C_{i+1} = G_i+P_iC_{i}", color=BLUE).to_corner(UR)
        eq2 = MathTex(r"C_{i+2} = G_{i+1}+P_{i+1}C_{i+1}")
        eq3 = MathTex(r"C_{i+2} = G_{i+1}+P_{i+1}(G_{i}+P_{i}C_{i})")
        eq2[0][14:].set_color(BLUE)
        eq3[0][14:].set_color(BLUE)
        eqs = VGroup(eq2, eq3).arrange_submobjects(DOWN, buff=0.6)
        self.add(eqs, eq1)