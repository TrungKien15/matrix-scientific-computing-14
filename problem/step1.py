from manim import *

def step1(scene):
    title = VGroup(
        Text("Step 1. ", weight=BOLD),
        Text("Find the eigenvalues of A")
    ).arrange(RIGHT).scale_to_fit_width(config.frame_width - 1)

    matrices = [
        MathTex(
            "A", "=",
            r"\begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 1 & 3 \end{bmatrix}"
        ),

        MathTex(
            "A", "-", r"\lambda I", "=",
            r"\begin{bmatrix} 2 - \lambda & 0 & 0 \\ 0 & 3 - \lambda & 1 \\ 0 & 1 & 3 - \lambda \end{bmatrix}"
        ),

        MathTex(
            r"\det(", "A", "-", r"\lambda I", ")", "=",
            r"\begin{vmatrix} 2 - \lambda & 0 & 0 \\ 0 & 3 - \lambda & 1 \\ 0 & 1 & 3 - \lambda \end{vmatrix}"
        ),

        MathTex(
            r"\det(A - \lambda I)", "=",
            r"(2 - \lambda)",
            r"\begin{vmatrix} 3 - \lambda & 1 \\ 1 & 3 - \lambda \end{vmatrix}"
        ),

        MathTex(
            r"\det(A - \lambda I)", "=",
            r"(2 - \lambda)",
            r"((3 - \lambda)^2 - 1)"
        ),

        MathTex(
            r"\det(A - \lambda I)", "=",
            r"(2 - \lambda)",
            r"(\lambda^2 - 6\lambda + 8)"
        ),

        MathTex(
            r"\det(A - \lambda I)", "=",
            r"(2 - \lambda)",
            r"(\lambda - 2)",
            r"(\lambda - 4)"
        )
    ]

    text = MathTex("=", "0").next_to(matrices[-1], RIGHT)
    result = MathTex(r"\Rightarrow \lambda = 2, 2, 4").next_to(matrices[-1], DOWN)

    # Animation
    scene.play(Write(title))
    scene.play(title.animate.to_edge(UP + LEFT))

    scene.play(Write(matrices[0]))

    for i in range(len(matrices) - 1):
        scene.play(
            TransformMatchingTex(matrices[i], matrices[i + 1]),
            run_time=1.5
        )
        scene.wait(0.5)

    scene.play(FadeIn(text))
    scene.wait(0.5)

    scene.play(Write(result))
    scene.wait(1)

    scene.clear()