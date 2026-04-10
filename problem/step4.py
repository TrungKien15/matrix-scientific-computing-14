from manim import *

def step4(scene):
    title = VGroup(
        Text("Step 4. ", weight=BOLD),
        Text("Construct D from the corresponding eigenvalues")
    ).arrange(RIGHT).scale_to_fit_width(config.frame_width - 1)
    scene.play(Write(title))
    scene.play(title.animate.to_edge(UP + LEFT))

    text1 = MathTex(r"""
        D =
        \begin{bmatrix}
        \lambda_1 & 0 & 0\\
        0 & \lambda_2 & 0\\
        0 & 0 & \lambda_3
        \end{bmatrix}
        """)
    scene.play(Write(text1))
    scene.play(text1.animate.shift(LEFT*2.5))
      
    text2 = MathTex(r"""
        = 
        \begin{bmatrix}
        2 & 0 & 0 \\
        0 & 2 & 0 \\
        0 & 0 & 4
        \end{bmatrix}
        """).next_to(text1, RIGHT)
    scene.play(FadeIn(text2, shift=UP))
    scene.wait()
    scene.clear()