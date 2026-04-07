from manim import * 

def problem(scene):
    title = Text("Consider the Diagonalization of the following matrix").scale_to_fit_width(config.frame_width - 1)
    scene.play(Write(title))
    scene.play(title.animate.to_edge(UP))

    matrix = MathTex(
        r"""               
        A =
        \begin{bmatrix}
        2 & 0 & 0 \\
        0 & 3 & 1 \\
        0 & 1 & 3
        \end{bmatrix}
        """
    )
    scene.play(FadeIn(matrix, shift=UP), run_time=2)
    scene.play(matrix.animate.next_to(title, DOWN, buff=1))

    text = Text("That is, find an invertible matrix P and a diagonal matrix D such that").scale_to_fit_width(config.frame_width - 1).next_to(matrix, DOWN, buff=1)
    mathTex = MathTex("A = P D P^{-1}", font_size=100).next_to(text, DOWN)
    
    scene.play(FadeIn(text, shift=UP))
    scene.play(FadeIn(mathTex, shift=UP))
    scene.wait()
    scene.clear()
    