from manim import *

def svd_example(scene):
    title = Text("EXAMPLE", weight=BOLD, color=BLUE).to_edge(UP)
    scene.play(Write(title))

    task = Text("Construct a singular value decomposition of", font_size=28).next_to(title, DOWN)
    eq_A = MathTex(r"A = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}").scale(1.2)
    scene.play(FadeIn(task, shift=DOWN), FadeIn(eq_A, shift=DOWN))
    scene.wait()
    scene.play(FadeOut(task, shift=DOWN), FadeOut(eq_A, shift=DOWN))

    v_line = Line(DOWN*2, UP*2).set_color(BLUE).shift(LEFT * 3)
    scene.play(Create(v_line))

    # =========================================================
    # STEP 1.1
    # =========================================================
    step1_title = Tex("Step 1. Find an orthogonal diagonalization of $A^T A$", font_size=32, color=GREEN).next_to(title, DOWN)
    scene.play(Write(step1_title))

    eq_AtA = MathTex(
        r"A^T A", r"=", 
        r"\begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{bmatrix}", 
        r"\begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}", 
        r"=", 
        r"\begin{bmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}",
        r"A^T A = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}"
    ).next_to(step1_title, DOWN, buff=0.5).next_to(v_line, RIGHT)
    scene.play(Write(eq_AtA[0:1]))
    scene.play(Write(eq_AtA[1:4]))
    scene.play(Write(eq_AtA[4:6]))

    scene.play(Unwrite(eq_AtA[0:6]))
    eq_AtA[-1].scale(0.75).next_to(v_line, LEFT).shift(UP * 0.5)
    scene.play(FadeIn(eq_AtA[-1], shift=UP))

    # =========================================================
    # STEP 1.2
    # =========================================================
    text_find_eigen = Tex("Find Eigenvalues: $det(A^T A - \lambda I) = 0$", font_size=28, color=YELLOW).next_to(v_line, RIGHT, buff=1).align_to(v_line, UP)
    scene.play(Write(text_find_eigen))

    eq_det = MathTex(
        r"\det \begin{bmatrix} 2-\lambda & 1 & 1 \\ 1 & 1-\lambda & 0 \\ 1 & 0 & 1-\lambda \end{bmatrix} = 0"
    ).scale(0.8).next_to(text_find_eigen, DOWN, buff=0.3)
    scene.play(Write(eq_det))
    scene.wait()

    eq_poly = MathTex(
        r"\implies (1-\lambda)(\lambda^2 - 3\lambda) = 0"
    ).scale(0.8).next_to(eq_det, DOWN, buff=0.3)
    scene.play(Write(eq_poly))
    scene.wait(1)

    eq_roots = MathTex(
        r"\implies", r"\lambda_1 = 3, \quad \lambda_2 = 1, \quad \lambda_3 = 0"
    ).scale(0.8).set_color(YELLOW).next_to(eq_poly, DOWN, buff=0.3)
    scene.play(Write(eq_roots))
    
    box_roots = SurroundingRectangle(eq_roots, color=GREEN, buff=0.1)
    scene.play(Create(box_roots))
    scene.wait(2)
    scene.play(
        FadeOut(text_find_eigen), FadeOut(eq_det), FadeOut(eq_poly),
        FadeOut(eq_roots[0]),
        eq_roots[1].animate.scale(0.75).set_color(WHITE).next_to(eq_AtA[-1], DOWN, buff=0.5).align_to(eq_AtA[-1], RIGHT),
        FadeOut(box_roots)
    )

    
    # =========================================================
    # STEP 1.3
    # =========================================================
    text_find_vec = Tex("Find Normalized Eigenvectors: $(A^T A - \lambda_i I)x = 0$", font_size=28, color=YELLOW).next_to(v_line, RIGHT, buff=1).align_to(v_line, UP)
    scene.play(Write(text_find_vec))

    # v1
    eq_v1 = MathTex(
        r"\lambda_1 = 3:", r"\quad \begin{bmatrix} -1 & 1 & 1 \\ 1 & -2 & 0 \\ 1 & 0 & -2 \end{bmatrix} x = 0", 
        r"\implies x_1 = \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix}",
        r"\implies v_1 = \frac{x_1}{\|x_1\|} = \begin{bmatrix} \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \end{bmatrix}"
    ).scale(0.65).next_to(text_find_vec, DOWN, buff=0.3)
    
    scene.play(Write(eq_v1[0:2].align_to(text_find_vec, LEFT)))
    scene.play(Write(eq_v1[2:].next_to(eq_v1[0:2], DOWN).align_to(eq_v1[0:2], LEFT)))
    scene.wait(2)
    scene.play(FadeOut(eq_v1, shift=DOWN))

    # v2
    eq_v2 = MathTex(
        r"\lambda_2 = 1:", r"\quad \begin{bmatrix} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix} x = 0", 
        r"\implies x_2 = \begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}",
        r"\implies v_2 = \frac{x_2}{\|x_2\|} = \begin{bmatrix} 0 \\ -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}"
    ).scale(0.65).next_to(text_find_vec, DOWN, buff=0.3).align_to(eq_v1, LEFT)
    
    scene.play(Write(eq_v2[0:2].align_to(text_find_vec, LEFT)))
    scene.play(Write(eq_v2[2:].next_to(eq_v1[0:2], DOWN).align_to(eq_v1[0:2], LEFT)))
    scene.wait(2)
    scene.play(FadeOut(eq_v2, shift=DOWN))

    # v3
    eq_v3 = MathTex(
        r"\lambda_3 = 0:", r"\quad \begin{bmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix} x = 0", 
        r"\implies x_3 = \begin{bmatrix} 1 \\ -1 \\ -1 \end{bmatrix}",
        r"\implies v_3 = \frac{x_3}{\|x_3\|} = \begin{bmatrix} \frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{3}} \end{bmatrix}"
    ).scale(0.65).next_to(text_find_vec, DOWN, buff=0.3).align_to(eq_v1, LEFT)
    
    scene.play(Write(eq_v3[0:2].align_to(text_find_vec, LEFT)))
    scene.play(Write(eq_v3[2:].next_to(eq_v1[0:2], DOWN).align_to(eq_v1[0:2], LEFT)))
    scene.wait(2)
    scene.play(FadeOut(eq_v3, shift=DOWN))

    # eigenvectors
    eq_vec = MathTex(
        r"v_1 = \begin{bmatrix} \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \end{bmatrix}",
        r"v_2 = \begin{bmatrix} 0 \\ -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}",
        r"v_3 = \begin{bmatrix} \frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{3}} \end{bmatrix}"
    ).next_to(v_line, RIGHT)

    scene.play(Write(eq_vec))
    scene.wait(2)

    # =========================================================
    # STEP 2
    # =========================================================
    scene.clear()
    scene.add(title)

    step2_title = Tex("Step 2. Set up $V$ and $\Sigma$", font_size=32, color=GREEN).next_to(title, DOWN)
    scene.play(ReplacementTransform(step1_title, step2_title))

    eq_V = MathTex(
        r"V = \begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix} = \begin{bmatrix} \frac{2}{\sqrt{6}} & 0 & \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{3}} \end{bmatrix}"
    ).scale(0.8).next_to(step2_title, DOWN, buff=0.5)
    
    text_sigma = MathTex(r"\text{Singular values: } \sigma_i = \sqrt{\lambda_i} \implies \sigma_1 = \sqrt{3}, \sigma_2 = 1, \sigma_3 = 0", font_size=32).next_to(eq_V, DOWN, buff=0.5)
    
    eq_Sigma = MathTex(
        r"\Sigma = \begin{bmatrix} \sigma_1 & 0 & 0 \\ 0 & \sigma_2 & 0 \end{bmatrix} = \begin{bmatrix} \sqrt{3} & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}"
    ).scale(0.8).next_to(text_sigma, DOWN, buff=0.5)

    scene.play(Write(eq_V))
    scene.wait(1)
    scene.play(Write(text_sigma))
    scene.wait(1)
    scene.play(Write(eq_Sigma))
    scene.wait(2)
    scene.play(
        FadeOut(text_sigma),
        FadeOut(eq_V),
        FadeOut(eq_Sigma)
    )

    # =========================================================
    # STEP 3
    # =========================================================
    step3_title = Tex("Step 3. Construct $U$ from $u_i = (1/\sigma_i) A v_i$", font_size=32, color=GREEN).next_to(title, DOWN)
    scene.play(ReplacementTransform(step2_title, step3_title))

    eq_u = MathTex(r"u_i = \frac{1}{\sigma_i} A v_i").next_to(v_line, LEFT, buff=1)
    scene.play(Create(v_line), Write(eq_u))
    scene.wait()

    # u_1
    eq_u1_calc = MathTex(
        r"u_1", r"=", r"\frac{1}{\sqrt{3}}", r"\begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}", r"\begin{bmatrix} \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \end{bmatrix}",
        r"=", r"\frac{1}{\sqrt{3}}", r"\begin{bmatrix} \frac{3}{\sqrt{6}} \\ \frac{3}{\sqrt{6}} \end{bmatrix}",
        r"=", r"\begin{bmatrix} \frac{3}{\sqrt{18}} \\ \frac{3}{\sqrt{18}} \end{bmatrix}", r"=", r"\begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}"
    ).scale(0.65).next_to(v_line, RIGHT).align_to(v_line, UP)

    scene.play(Write(eq_u1_calc[0:5]))
    scene.wait(0.5)
    scene.play(Write(eq_u1_calc[5:8]))
    scene.wait(0.5)
    scene.play(Write(eq_u1_calc[8:]))
    scene.wait(1)

    # u_2
    eq_u2_calc = MathTex(
        r"u_2", r"=", r"\frac{1}{1}", r"\begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}", r"\begin{bmatrix} 0 \\ -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}",
        r"=", r"\begin{bmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{bmatrix}"
    ).scale(0.65).next_to(eq_u1_calc, DOWN, buff=0.5).align_to(eq_u1_calc, LEFT)

    scene.play(Write(eq_u2_calc[0:5]))
    scene.wait(0.5)
    scene.play(Write(eq_u2_calc[5:]))
    scene.wait(1)
    scene.play(FadeOut(eq_u1_calc), FadeOut(eq_u2_calc))

    eq_U = MathTex(
        r"\implies U = \begin{bmatrix} u_1 & u_2 \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}"
    ).next_to(v_line, RIGHT)
    scene.play(Write(eq_U))
    scene.wait(2)

    # =========================================================
    # FINAL
    # =========================================================
    scene.clear()
    scene.add(title)

    final_text = Tex("Final SVD: $A = U \Sigma V^T$", font_size=36, color=YELLOW).next_to(title, DOWN, buff=1)
    scene.play(Write(final_text))

    eq_final = MathTex(
        r"A = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}",
        r"= \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}",
        r"\begin{bmatrix} \sqrt{3} & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}",
        r"\begin{bmatrix} \frac{2}{\sqrt{6}} & \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{6}} \\ 0 & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{3}} \end{bmatrix}"
    ).scale(0.8).next_to(final_text, DOWN, buff=0.8)

    scene.play(FadeIn(eq_final[0], shift=UP))
    scene.wait(0.5)
    scene.play(FadeIn(eq_final[1], shift=UP))
    scene.wait(0.5)
    scene.play(FadeIn(eq_final[2], shift=UP))
    scene.wait(0.5)
    scene.play(FadeIn(eq_final[3], shift=UP))
    scene.wait(1)

    final_box = SurroundingRectangle(eq_final, color=RED, buff=0.2)
    scene.play(Create(final_box))
    scene.wait(4)
    scene.clear()