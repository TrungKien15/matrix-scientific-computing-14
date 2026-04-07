from manim import *

def case1(scene, title):
    case1 = MathTex(r"1.\ \lambda = 2").next_to(title, DOWN).align_to(title, LEFT).shift(RIGHT)
    scene.play(Write(case1))

    text1 = MathTex("(", "A", "-", "2I", ")", "v", "=", "0")
    scene.play(Write(text1))
    scene.wait()

    text2 = MathTex(
        r"\begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{bmatrix}",
        r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}",
        "=",
        "0"
    )
    scene.play(TransformMatchingTex(text1, text2))
    scene.wait()

    text3 = MathTex(r"\Rightarrow", "y", "+", "z", "=", "0")
    scene.play(TransformMatchingTex(text2, text3))
    scene.play(text3.animate.shift(LEFT * 3))

    text4 = MathTex(r"\Rightarrow", "y", "=", "-z").next_to(text3, RIGHT)
    scene.play(TransformMatchingTex(text3.copy(), text4))

    text5 = MathTex(r"\Rightarrow").next_to(text4, RIGHT)

    v1 = MathTex(
        r"v_1 =",
        r"\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}"
    ).next_to(text5, RIGHT).shift(UP)

    v2 = MathTex(
        r"v_2 =",
        r"\begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}"
    ).next_to(text5, RIGHT).shift(DOWN)

    scene.play(AnimationGroup(
        FadeIn(text5, shift=LEFT),
        FadeIn(v1, shift=LEFT),
        FadeIn(v2, shift=LEFT)
    ))
    scene.play(Circumscribe(v1, color=YELLOW),Circumscribe(v2, color=YELLOW))
    scene.wait()

    scene.clear()


def case2(scene, title):
    scene.add(title)

    case2 = MathTex(r"2.\ \lambda = 4").next_to(title, DOWN).align_to(title, LEFT).shift(RIGHT)
    scene.play(Write(case2))

    text1 = MathTex("(", "A", "-", "4I", ")", "v", "=", "0")
    scene.play(Write(text1))
    scene.wait()

    text2 = MathTex(
        r"\begin{bmatrix} -2 & 0 & 0 \\ 0 & -1 & 1 \\ 0 & 1 & -1 \end{bmatrix}",
        r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}",
        "=",
        "0"
    )
    scene.play(TransformMatchingTex(text1, text2))
    scene.wait()

    text3 = MathTex(r"\Rightarrow", "x", "=", "0,", "y", "=", "z")
    scene.play(TransformMatchingTex(text2, text3))
    scene.play(text3.animate.shift(LEFT * 2))

    v3 = MathTex(
        r"\Rightarrow",
        r"v_3 =",
        r"\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}"
    ).next_to(text3, RIGHT)

    scene.play(FadeIn(v3, shift=LEFT))

    scene.play(Circumscribe(v3, color=BLUE))
    scene.wait()

    scene.clear()


def step2(scene):
    title = VGroup(
        Text("Step 2. ", weight=BOLD),
        Text("Find three linearly independent eigenvectors of matrix A")
    ).arrange(RIGHT).scale_to_fit_width(config.frame_width - 1)

    scene.play(Write(title))
    scene.play(title.animate.to_edge(UP + LEFT))

    case1(scene, title)
    case2(scene, title)