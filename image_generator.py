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


class Demux(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        demux = VGroup(Tex("DEMUX", color=RED, fill_opacity=0.3).scale(0.85), Rectangle(color=RED).rotate(PI/2))
        inputs = VGroup()
        for line in range(8):
            inputs.add(VGroup(MathTex(f"Z_{line}").scale(0.6).shift(1.35*RIGHT), Line(LEFT, RIGHT)))
        inputs.arrange_submobjects(DOWN, buff=0.25).next_to(demux, RIGHT).shift(0.23*LEFT)
        output = VGroup(MathTex(f"X").scale(0.6).shift(3.3*LEFT),Line(LEFT, RIGHT).next_to(demux, LEFT).shift(0.225*RIGHT))
        demux.z_index = 100
        sel = VGroup(Line(demux.get_bottom(), demux.get_bottom()+0.75*DOWN), Line(demux.get_bottom()+0.75*DOWN, demux.get_bottom()+0.75*DOWN+1.75*LEFT), MathTex("S").next_to(Line(demux.get_bottom()+0.75*DOWN, demux.get_bottom()+0.75*DOWN+1.75*LEFT), LEFT).shift(0.2*RIGHT).scale(0.6))
        self.add(demux, inputs, output, sel)
        
        selector = []
        nums = []
        for idx, line in enumerate(inputs):
            selector.append(Line(output[1].get_right(), inputs[idx][1].get_left(), color=RED))
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

class Codificador(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        codificador = VGroup(Tex("CODIFICADOR", color=RED, fill_opacity=0.3).scale(0.5), Rectangle(color=RED).rotate(PI/2))
        inputs = VGroup()
        for line in range(8):
            inputs.add(Line(LEFT, RIGHT))
        inputs.arrange_submobjects(DOWN, buff=0.5).next_to(codificador, LEFT).shift(0.25*RIGHT)
        outputs = VGroup()
        for line in range(3):
            outputs.add(Line(LEFT, RIGHT))
        outputs.arrange_submobjects(DOWN, buff=0.5).next_to(codificador, RIGHT).shift(0.25*LEFT)
        codificador.z_index = 100
        self.add(codificador, inputs, outputs)
    
        ins = []
        outs = []
        for idx, line in enumerate(inputs):
            if idx < 2:
                outs.append(MathTex("00"+bin(idx)[2:] ).next_to(outputs[0], RIGHT).scale(0.9).shift(0.2*LEFT))
            elif idx < 4:
                outs.append(MathTex("0"+bin(idx)[2:] ).next_to(outputs[0], RIGHT).scale(0.9).shift(0.2*LEFT))
            else:
                outs.append(MathTex(bin(idx)[2:] ).next_to(outputs[0], RIGHT).scale(0.9).shift(0.2*LEFT))

            outs[idx][0][0].next_to(outputs[0], RIGHT).scale(0.7).shift(0.2*LEFT)
            outs[idx][0][1].next_to(outputs[1], RIGHT).scale(0.7).shift(0.2*LEFT)
            outs[idx][0][2].next_to(outputs[2], RIGHT).scale(0.7).shift(0.2*LEFT)

            ins.append(MathTex("0","0","0","0","0","0","0","0"))
            string = ""
            for i in range(8):
                if i == idx:
                    string+="1"
                else:
                    string+="0"
            onehot = VGroup()
            for letter in string:
                onehot.add(MathTex(letter).scale(0.9))
            ins[idx] = onehot.arrange_submobjects(UP, buff=0.4).next_to(inputs, LEFT).scale(0.7).shift(0.15*RIGHT)
            if idx:
                self.play(ReplacementTransform(outs[idx-1], outs[idx]), ReplacementTransform(ins[idx-1], ins[idx]))
            else:
                self.play(Write(outs[idx][0]), Write(ins[idx]))
            self.wait()

class Decodificador(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        decodificador = VGroup(Tex("DECODIFICADOR", color=RED, fill_opacity=0.3).scale(0.4), Rectangle(color=RED).rotate(PI/2))
        inputs = VGroup()
        for line in range(8):
            inputs.add(Line(LEFT, RIGHT))
        inputs.arrange_submobjects(DOWN, buff=0.5).next_to(decodificador, RIGHT).shift(0.25*LEFT)
        outputs = VGroup()
        for line in range(3):
            outputs.add(Line(LEFT, RIGHT))
        outputs.arrange_submobjects(DOWN, buff=0.5).next_to(decodificador, LEFT).shift(0.25*RIGHT)
        decodificador.z_index = 100
        self.add(decodificador, inputs, outputs)
    
        ins = []
        outs = []
        for idx, line in enumerate(inputs):
            if idx < 2:
                outs.append(MathTex("00"+bin(idx)[2:] ).next_to(outputs[0], LEFT).scale(0.9).shift(0.2*LEFT))
            elif idx < 4:
                outs.append(MathTex("0"+bin(idx)[2:] ).next_to(outputs[0], LEFT).scale(0.9).shift(0.2*LEFT))
            else:
                outs.append(MathTex(bin(idx)[2:] ).next_to(outputs[0], LEFT).scale(0.9).shift(0.2*LEFT))

            outs[idx][0][0].next_to(outputs[0], LEFT).scale(0.7).shift(-0.1*LEFT)
            outs[idx][0][1].next_to(outputs[1], LEFT).scale(0.7).shift(-0.1*LEFT)
            outs[idx][0][2].next_to(outputs[2], LEFT).scale(0.7).shift(-0.1*LEFT)

            ins.append(MathTex("0","0","0","0","0","0","0","0"))
            string = ""
            for i in range(8):
                if i == idx:
                    string+="1"
                else:
                    string+="0"
            onehot = VGroup()
            for letter in string:
                onehot.add(MathTex(letter).scale(0.9))
            ins[idx] = onehot.arrange_submobjects(UP, buff=0.4).next_to(inputs, RIGHT).scale(0.7).shift(-0.15*RIGHT)
            if idx:
                self.play(ReplacementTransform(outs[idx-1], outs[idx]), ReplacementTransform(ins[idx-1], ins[idx]))
            else:
                self.play(Write(outs[idx][0]), Write(ins[idx]))
            self.wait()

class Comparador(Scene):
    def construct(self):
        self.camera.background_color = "#353537"
        comparador = VGroup(Tex("COMPARADOR", color=RED, fill_opacity=0.3).scale(0.45), Rectangle(color=RED).rotate(PI/2))
        inputs1 = VGroup()
        for line in range(4):
            inputs1.add(Line(LEFT, RIGHT))
        inputs2 = VGroup()
        for line in range(4):
            inputs2.add(Line(LEFT, RIGHT))
        inputs1.arrange_submobjects(DOWN, buff=0.5).next_to(comparador, LEFT).shift(0.25*RIGHT).shift(UP)
        inputs2.arrange_submobjects(DOWN, buff=0.5).next_to(comparador, LEFT).shift(0.25*RIGHT).shift(DOWN)
        outputs = VGroup()
        for line in range(3):
            outputs.add(Line(LEFT, RIGHT))
        outputs.arrange_submobjects(DOWN, buff=0.5).next_to(comparador, RIGHT).shift(0.25*LEFT)
        comparador.z_index = 100
        self.add(comparador, inputs1, inputs2, outputs)
    
        ins = []
        ins2 = []
        outs = []
        i = 0
        j = 0
        i_txt = []
        j_txt = []
        for idx in range(16):
            print(i,j)
            if i < 2:
                ins.append(MathTex("000"+bin(i)[2:], color=GREEN).next_to(inputs1[0], LEFT).scale(0.9).shift(0.2*LEFT))
            elif i < 4:
                ins.append(MathTex("00"+bin(i)[2:], color=GREEN).next_to(inputs1[0], LEFT).scale(0.9).shift(0.2*LEFT))
            elif i < 8:
                ins.append(MathTex("0"+bin(i)[2:], color=GREEN).next_to(inputs1[0], LEFT).scale(0.9).shift(0.2*LEFT))
            else:
                ins.append(MathTex(bin(i)[2:], color=GREEN).next_to(inputs1[0], LEFT).scale(0.9).shift(0.2*LEFT))

            if j < 2:
                ins2.append(MathTex("000"+bin(j)[2:], color=BLUE).next_to(inputs2[0], LEFT).scale(0.9).shift(0.2*LEFT))
            elif j < 4:
                ins2.append(MathTex("00"+bin(j)[2:], color=BLUE).next_to(inputs2[0], LEFT).scale(0.9).shift(0.2*LEFT))
            elif j < 8:
                ins2.append(MathTex("0"+bin(j)[2:], color=BLUE).next_to(inputs2[0], LEFT).scale(0.9).shift(0.2*LEFT))
            else:
                ins2.append(MathTex(bin(j)[2:], color=BLUE).next_to(inputs2[0], LEFT).scale(0.9).shift(0.2*LEFT))

            ins[idx][0][0].next_to(inputs1[0], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins[idx][0][1].next_to(inputs1[1], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins[idx][0][2].next_to(inputs1[2], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins[idx][0][3].next_to(inputs1[3], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins2[idx][0][0].next_to(inputs2[0], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins2[idx][0][1].next_to(inputs2[1], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins2[idx][0][2].next_to(inputs2[2], LEFT).scale(0.7).shift(-0.1*LEFT)
            ins2[idx][0][3].next_to(inputs2[3], LEFT).scale(0.7).shift(-0.1*LEFT)

            if i == j:
                outs.append(MathTex("010"))
                outs[idx][0][1].set_color(YELLOW)
            elif i < j:
                outs.append(MathTex("001"))
                outs[idx][0][2].set_color(YELLOW)
            else:
                outs.append(MathTex("100"))
                outs[idx][0][0].set_color(YELLOW)
            
            outs[idx][0][0].next_to(outputs[0], RIGHT).scale(0.7).shift(0.1*RIGHT)
            outs[idx][0][1].next_to(outputs[1], RIGHT).scale(0.7).shift(0.1*RIGHT)
            outs[idx][0][2].next_to(outputs[2], RIGHT).scale(0.7).shift(0.1*RIGHT)

            i_txt.append(MathTex(i, color=GREEN).next_to(inputs1, LEFT).shift(0.6*LEFT))
            j_txt.append(MathTex(j, color=BLUE).next_to(inputs2, LEFT).shift(0.6*LEFT))

            if idx:
                self.play(ReplacementTransform(ins[idx-1], ins[idx]), ReplacementTransform(ins2[idx-1], ins2[idx]), ReplacementTransform(i_txt[idx-1], i_txt[idx]), ReplacementTransform(j_txt[idx-1], j_txt[idx]), ReplacementTransform(outs[idx-1], outs[idx]))
            else:
                self.play(Write(ins[idx]), Write(ins2[idx]), Write(i_txt[idx]), Write(j_txt[idx]), Write(outs[idx]))
            self.wait()

            if idx == 5:
                i+=1
                j=j
            elif idx == 9 or j == 10 or j == 11:
                i=i
                j+=1
            else:
                j+=1
                i+=1

class ALU(Scene):
    def construct(self):
        alu = Polygon([-3, 1.5, 0], [-1, -1.5, 0], [1, -1.5, 0], [3, 1.5, 0], [1, 1.5, 0], [0.5, 0.5, 0], [-0.5, 0.5, 0], [-1, 1.5, 0], [-3, 1.5, 0], fill_opacity=0.6, color=BLUE)
        a = VGroup(*[Line(0.7*UP, 0.5*DOWN) for i in range(4)]).arrange_submobjects(RIGHT, buff=0.45).next_to(alu, UP).shift(2*LEFT+0.25*DOWN)
        b = a.copy().shift(4*RIGHT)
        c = VGroup(*[Line(0.7*UP, 0.5*DOWN) for i in range(8)]).arrange_submobjects(RIGHT, buff=0.25).next_to(alu, DOWN).shift(0.25*UP)
        t1 = Tex("A").next_to(a, UP)
        t2 = Tex("B").next_to(b, UP)
        t3 = Tex("C").next_to(c, DOWN)
        sel = VGroup(*[Line(alu.get_left()+RIGHT, alu.get_left()+LEFT) for i in range(4)]).arrange_submobjects(UP).shift(2.6*LEFT)
        t4 = Tex("Sel").next_to(sel, LEFT)
        alu2 = Polygon([-3, 1.5, 0], [-1, -1.5, 0], [1, -1.5, 0], [3, 1.5, 0], [1, 1.5, 0], [0.5, 0.5, 0], [-0.5, 0.5, 0], [-1, 1.5, 0], [-3, 1.5, 0], fill_opacity=1, color=BLACK)
        alu.z_index = 100
        self.add(alu, a, b, c, t1, t2, t3, t4, sel, alu2)