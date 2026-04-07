from manim import *

def svd_theory(scene):
    title = Text("SVD - Singular Value Decomposition", weight=BOLD).set_color(YELLOW).to_edge(UP).scale_to_fit_width(config.frame_width - 2)
    text = Tex(r"For all matrices $A \in \mathbb{R}^{m \times n}$ with rank $r$, there always exists:", font_size=36).next_to(title, DOWN).align_to(title, LEFT)
    equation = MathTex(r"A = U \Sigma V^{T}").scale(2).shift(UP)
    U = Tex(r"$U \in \mathbb{R}^{m \times m}$: an orthogonal matrix", font_size=36).next_to(equation, DOWN).align_to(title, LEFT).shift(RIGHT + DOWN)
    sigma = Tex(r"$\Sigma \in \mathbb{R}^{m \times n}$: an diagonal matrix whose diagonal entries are non-negative", font_size=36).next_to(U, DOWN).align_to(title, LEFT).shift(RIGHT)
    V_inverse = Tex(r"$V^{T} \in \mathbb{R}^{n \times n}$: transpose of an orthogonal matrix", font_size=36).next_to(sigma, DOWN).align_to(title, LEFT).shift(RIGHT)

    scene.play(Write(title))
    scene.play(Write(text))
    scene.play(Write(equation))
    scene.play(AnimationGroup(
        FadeIn(U, shift=LEFT),
        FadeIn(sigma, shift=RIGHT),
        FadeIn(V_inverse, shift=LEFT)
    ))
    scene.clear()