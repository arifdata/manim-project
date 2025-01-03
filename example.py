from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

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

        self.play(Create(s))
        self.play(s.animate.rotate(PI / 4))
        self.play(Transform(s, c))
        self.play(
                s.animate.set_fill("#00FF00", opacity=1)
                )
