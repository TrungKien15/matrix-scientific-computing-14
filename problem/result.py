from manim import *

def result(scene):
    equation = MathTex(
            "A", "=", "P", "D", "P^{-1}"
    ).arrange(RIGHT)
    scene.play(Write(equation))
    scene.play(equation.animate.shift(UP*2))

    A = MathTex(
        r"""               
        \begin{bmatrix}
        2 & 0 & 0 \\
        0 & 3 & 1 \\
        0 & 1 & 3
        \end{bmatrix}
        """).shift(LEFT*4)
    
    P = MathTex(r"""
        \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1 & 1 \\
        0 & -1 & 1
        \end{bmatrix}
        """).next_to(A)

    D = MathTex(r"""
        = 
        \begin{bmatrix}
        2 & 0 & 0 \\
        0 & 2 & 0 \\
        0 & 0 & 4
        \end{bmatrix}
        """).next_to(P)
    
    P_inverse = MathTex(r"""
        \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1/2 & -1/2 \\
        0 & 1/2 & 1/2
        \end{bmatrix}
        """).next_to(D)
    
    scene.play(equation[0].animate.set_color(YELLOW).scale(2))
    scene.play(AnimationGroup(
        equation[0].animate.set_color(WHITE).scale(0.5),
        FadeIn(A)
        ))

    scene.play(equation[2].animate.set_color(YELLOW).scale(2))

    scene.play(AnimationGroup(
        equation[2].animate.set_color(WHITE).scale(0.5),
        FadeIn(P)
        ))
    
    scene.play(equation[3].animate.set_color(YELLOW).scale(2))
    scene.play(AnimationGroup(
        equation[3].animate.set_color(WHITE).scale(0.5),
        FadeIn(D)
        ))
    
    scene.play(equation[4].animate.set_color(YELLOW).scale(2))
    scene.play(AnimationGroup(
        equation[4].animate.set_color(WHITE).scale(0.5),
        FadeIn(P_inverse)
        ))
    
    box = SurroundingRectangle(
        A,
        color=RED,
        buff=0.2
    )

    label = Text("Square Matrix").set_color(YELLOW).scale(0.5).next_to(box, UP).shift(UP)

    arrow = Arrow(
            start=label.get_bottom(),
            end=box.get_top(),
            color=RED,
            buff=0.2
        )
    scene.play(Create(box))
    scene.play(AnimationGroup(
        GrowArrow(arrow),
        Write(label)
    ))
    scene.wait()

    text = Text("What if the matrix is not square?").shift(DOWN*2)
    scene.play(FadeIn(text, shift=UP))
    scene.wait()
    scene.clear()
