from manim import *
from manim_fonts import *
from manim_play_timeline import play_timeline

config.background_color = "#1A1A1D"

class CreateCircle(Scene):
    def construct(self):
        g = VGroup()
        g.add(Circle())
        g.add(Square())
        g.add(Star())
        g.add(Triangle())
        # print(len(g))
        for i in range(len(g)):
            if i == 0:
                pass
            else:
                g[i].next_to(g[i-1], RIGHT, buff=0.5)
        
        self.play(Create(g))
        self.wait(2)
        self.play(Uncreate(g))
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        # self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.8)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        c = Circle()
        c.set_fill(PINK, opacity=0.7)

        s = Square()
        s.set_fill(BLUE, opacity=0.8)

        s.next_to(c, RIGHT, buff=0.5)
        self.play(Create(c), Create(s))

class AnimateSquareToCircle(Scene):
    def construct(self):
        c = Circle()
        s = Square()
        with RegisterFont("Poppins") as fonts:
            t = Text("Coba objek text", font=fonts[0])

        self.play(Create(s))
        self.play(s.animate.rotate(PI / 4))
        self.play(Transform(s, c))
        self.play(
                s.animate.set_fill(PINK, opacity=1)
                )
        self.play(Uncreate(s))
        self.play(AddTextLetterByLetter(t))
        self.wait()
        self.play(Uncreate(t))

class DiffRotations(Scene):
    def construct(self):
        l_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        r_square = Square(color=GREEN, fill_opacity=0.7, side_length=3).shift(2 * RIGHT)
        self.play(Create(l_square), Create(r_square), run_time=2)
        self.play(l_square.animate.to_corner(UL), r_square.animate.to_corner(DR), run_time=2)
        self.play(l_square.animate.set_color("#FF0000").rotate(60), run_time=2)
        self.wait()

class CobaSVG(Scene):
    def construct(self):
        cheese = SVGMobject(file_name="./cheese.svg")
        self.play(GrowFromCenter(cheese))
        self.wait(3)

class Timeline(Scene):
    """Example showing how to use play_timeline."""
    def construct(self):
        n = NumberLine(include_numbers=True, x_range=[0,12]).to_edge(DOWN)
        self.add(n)
        progress_bar = Line(n.n2p(0), n.n2p(12)).set_stroke(color=YELLOW, opacity=0.5, width=20)

        # Create a timeline of animations. One of the animations is the progress bar itself
        # going from 0 to 12 in 12 seconds. It can be used as a reference to check that
        # the other animations are playing at the right time.
        timeline = {
            0: Create(progress_bar, run_time=12, rate_func=linear),
            1: Create(Square(), run_time=10),
            2: [Create(Circle(), run_time=4),
                Create(Triangle(), run_time=2)],
            9: Write(Text("It works!").next_to(progress_bar, UP, buff=1), 
                     run_time=3)
        }
        play_timeline(self, timeline)
        self.wait()       
