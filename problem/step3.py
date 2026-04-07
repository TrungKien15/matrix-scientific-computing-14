from manim import *

def step3(scene):
    title = VGroup(
        Text("Step 3. ", weight=BOLD),
        Text("Construct P from the vectors in step 2")
    ).arrange(RIGHT).scale_to_fit_width(config.frame_width - 1)
    scene.play(Write(title))
    scene.play(title.animate.to_edge(UP + LEFT))

    text1 = MathTex(r"""
        D =
        \begin{bmatrix}
        v_1 & v_2 & v_3
        \end{bmatrix}
        """)
    scene.play(Write(text1))
    scene.play(text1.animate.shift(LEFT*2))
      
    text2 = MathTex(r"""
        = 
        \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1 & -1 \\
        0 & 1 & 1
        \end{bmatrix}
        """).next_to(text1, RIGHT)
    scene.play(FadeIn(text2, shift=UP))
    scene.wait()
    scene.clear()