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
        eq1 = MathTex(r"\left(\overline{X_1}+\overline{X_0}\right)\left(X_3+\overline{X_0}\right)\left(\overline{X_2}+\overline{X_1}+X_0\right)\left(\overline{X_3}+X_2+\overline{X_0}\right)\left(X_3+X_2+X_1\right)").scale(0.9)
        self.add(eq1)

class KarnaughGenerator(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        t4 = IntegerTable([(0,0,1,1),
                        (0,1,1,0),
                        (0,1,0,0),
                        (0,0,1,0)], 
                        col_labels=[MathTex("00"), MathTex("01"), MathTex("11"), MathTex("10")],
                        row_labels=[MathTex("00"), MathTex("01"), MathTex("11"), MathTex("10")],
                        include_outer_lines=True).scale(0.8)
        tcolor = GRAY_C
        t4.get_horizontal_lines().set_color(tcolor)
        t4.get_vertical_lines().set_color(tcolor)
        t4.get_horizontal_lines()[2].set_color(RED)
        t4.get_horizontal_lines()[2].z_index = 100
        t4.get_vertical_lines()[2].set_color(RED)
        l = Line(t4.get_left()+t4.get_top(), t4.get_left()+t4.get_top()+(LEFT+UP)*0.9, color=tcolor)
        label1 = MathTex(r"X_3X_2").next_to(l, DOWN).shift(LEFT*0.5+UP*0.3)
        label2 = MathTex(r"X_1X_0").next_to(l, RIGHT).shift(0.3*LEFT)
        self.add(t4, l, label1, label2)

class Mux(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        mux = VGroup(Tex("MUX", color=RED, fill_opacity=0.3), Rectangle(color=RED).rotate(PI/2))
        inputs = VGroup()
        for line in range(8):
            inputs.add(VGroup(MathTex(f"X_{line}").scale(0.6).shift(1.35*LEFT), Line(LEFT, RIGHT)))
        inputs.arrange_submobjects(DOWN, buff=0.25).next_to(mux, LEFT).shift(0.23*RIGHT)
        output = VGroup(MathTex(f"Z").scale(0.6).shift(3.3*RIGHT),Line(LEFT, RIGHT).next_to(mux, RIGHT).shift(0.225*LEFT))
        mux.z_index = 100
        sel = VGroup(Line(mux.get_bottom(), mux.get_bottom()+0.75*DOWN), Line(mux.get_bottom()+0.75*DOWN, mux.get_bottom()+0.75*DOWN+1.75*LEFT), MathTex("S").next_to(Line(mux.get_bottom()+0.75*DOWN, mux.get_bottom()+0.75*DOWN+1.75*LEFT), LEFT).shift(0.2*RIGHT).scale(0.6))
        self.add(mux, inputs, output, sel)
        
        selector = []
        nums = []
        for idx, line in enumerate(inputs):
            selector.append(Line(output[1].get_left(), inputs[idx][1].get_right(), color=RED))
            if idx < 2:
                nums.append(MathTex("00"+bin(idx)[2:] ).next_to(sel[0], RIGHT).scale(0.7).shift(0.2*LEFT))
            elif idx < 4:
                nums.append(MathTex("0"+bin(idx)[2:] ).next_to(sel[0], RIGHT).scale(0.7).shift(0.2*LEFT))
            else:
                nums.append(MathTex(bin(idx)[2:] ).next_to(sel[0], RIGHT).scale(0.7).shift(0.2*LEFT))
            if idx:
                self.play(ReplacementTransform(selector[idx-1], selector[idx]), ReplacementTransform(nums[idx-1], nums[idx]))
            else:
                self.play(Create(selector[idx]), Write(nums[idx]))
            self.wait()