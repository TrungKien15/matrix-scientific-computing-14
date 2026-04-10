from manim import *

def svd_proof(scene):
    main_title = Text("PROOF OF THE SVD THEOREM", weight=BOLD, color=BLUE).to_edge(UP)
    scene.play(Write(main_title))

    # =========================================================
    # STEP 1: ORTHOGONAL BASIS
    # =========================================================
    step1_title = Text("1. Orthogonal Basis", font_size=36, color=GREEN).next_to(main_title, DOWN)
    scene.play(FadeIn(step1_title, shift=DOWN))
    scene.wait()

    eq_A_transpose_A = MathTex(r"A^T", r"A", r"?").scale(1.5)
    scene.play(Write(eq_A_transpose_A[1]))
    scene.play(FadeIn(eq_A_transpose_A[0]))
    scene.play(FadeIn(eq_A_transpose_A[2]))
    scene.play(eq_A_transpose_A.animate.to_edge(LEFT).shift(RIGHT * 0.5))

    derivation_square_matrix = VGroup(
        MathTex(r"A^{T}", r"{n \times m}").arrange(DOWN),
        MathTex(r"\times"),
        MathTex(r"A", r"{m \times n}").arrange(DOWN),
        MathTex(r"="),
        MathTex(r"A^{T}A", r"{n \times n}").arrange(DOWN),
        Tex(r"$\implies$ A square matrix", font_size=32),
        MathTex(r"A^{T} A v_{i} = \lambda_{i} v_{i}")
    ).arrange(RIGHT, buff=0.3).next_to(eq_A_transpose_A, RIGHT).shift(RIGHT * 0.5 + UP)

    derivation_symmetric_matrix = VGroup(
        MathTex(r"(A^{T} A)^{T}"),
        MathTex(r"= A^{T} (A^{T})^{T}"),
        MathTex(r"= A^{T} A"),
        Tex(r"$\implies$ A symmetric matrix", font_size=32),
        MathTex(r"""
            \begin{cases}
            v_{i}^{T} v_{j} = 0 \quad (i \ne j) \\
            \|v_{i}\| = 1 \implies v_{i}^{T} v_{i} = \|v_{i}\|^{2} = 1
            \end{cases}
        """)
    ).arrange(RIGHT, buff=0.3).next_to(eq_A_transpose_A, RIGHT).shift(RIGHT * 0.5 + DOWN)

    for i in range(len(derivation_square_matrix) - 1):
        scene.play(Write(derivation_square_matrix[i]))
    
    for i in range(len(derivation_symmetric_matrix) - 1):
        scene.play(Write(derivation_symmetric_matrix[i]))
    
    scene.wait()
    
    scene.clear()
    scene.add(main_title, step1_title, derivation_square_matrix[-2], derivation_symmetric_matrix[-2])

    scene.play(
        derivation_square_matrix[-2].animate.to_edge(LEFT).shift(RIGHT), 
        derivation_symmetric_matrix[-2].animate.to_edge(LEFT).shift(RIGHT)
    )
    derivation_square_matrix[-1].next_to(derivation_square_matrix[-2]).shift(RIGHT)
    derivation_symmetric_matrix[-1].next_to(derivation_symmetric_matrix[-2]).align_to(derivation_square_matrix[-1], LEFT)
    scene.play(Write(derivation_square_matrix[-1]), Write(derivation_symmetric_matrix[-1]))
    scene.wait()

    note_eigenvector = Tex(r"$v_i$ is eigenvector corresponding to eigenvalue $\lambda_i$", font_size=32).to_edge(DOWN).shift(UP) 
    
    eq_orthogonality = MathTex(r"v_{i}^{T} v_{j} = 0")
    eq_unit_length = MathTex(r"v_{i}^{T} v_{i} = 1").next_to(eq_orthogonality, DOWN)
    
    scene.play(Write(note_eigenvector))
    scene.wait()
    scene.play(ReplacementTransform(derivation_symmetric_matrix[-1], eq_orthogonality), Write(eq_unit_length))

    scene.clear()
    scene.add(main_title, step1_title, derivation_square_matrix[-1], eq_orthogonality, eq_unit_length)

    scene.play(derivation_square_matrix[-1].animate.scale(0.75).to_edge(LEFT).shift(UP))
    scene.play(eq_orthogonality.animate.scale(0.75).next_to(derivation_square_matrix[-1], DOWN).align_to(derivation_square_matrix[-1], LEFT))
    scene.play(eq_unit_length.animate.scale(0.75).next_to(eq_orthogonality, DOWN).align_to(eq_orthogonality, LEFT))
    
    eq_dot_product_proof = VGroup(
        MathTex(r"(Av_i)^T", r"(Av_j)"),
        MathTex(r"(Av_i)^T", r"(Av_j)", r"=", r"v_i^T", r"A^T", r"A", r"v_j"),
        MathTex(r"(Av_i)^T", r"(Av_j)", r"=", r"v_i^T", r"\lambda_j", r"v_j"),
        MathTex(r"(Av_i)^T", r"(Av_j)", r"=", r"\lambda_j", r"v_i^T", r"v_j"),
        MathTex(r"(Av_i)^T", r"(Av_j)", r"=", r"0")
    )

    scene.play(Write(eq_dot_product_proof[0]))
    scene.play(TransformMatchingTex(eq_dot_product_proof[0], eq_dot_product_proof[1]))
    scene.wait()

    part_At_A_vj = eq_dot_product_proof[1][4:]
    scene.play(
        derivation_square_matrix[-1].animate.scale(1.25).set_color(YELLOW),
        part_At_A_vj.animate.scale(1.25).set_color(YELLOW)
    )
    scene.play(
        derivation_square_matrix[-1].animate.scale(1/1.25).set_color(WHITE),
        part_At_A_vj.animate.scale(1/1.25).set_color(WHITE)
    )
    
    scene.play(TransformMatchingTex(eq_dot_product_proof[1], eq_dot_product_proof[2]))
    scene.play(TransformMatchingTex(eq_dot_product_proof[2], eq_dot_product_proof[3]))

    part_vi_vj = eq_dot_product_proof[3][4:]
    scene.play(
        eq_orthogonality.animate.scale(1.25).set_color(YELLOW),
        part_vi_vj.animate.scale(1.25).set_color(YELLOW)
    )
    scene.play(
        eq_orthogonality.animate.scale(1/1.25).set_color(WHITE),
        part_vi_vj.animate.scale(1/1.25).set_color(WHITE)
    )
    
    scene.play(TransformMatchingTex(eq_dot_product_proof[3], eq_dot_product_proof[4]))
    scene.play(eq_dot_product_proof[4].animate.scale(1.5))

    box_dot_product = SurroundingRectangle(eq_dot_product_proof[4], color=GREEN, buff=0.2)
    scene.play(Create(box_dot_product))
    scene.wait()

    text_orthogonal_basis = Tex(r"$\implies \{Av_1, \dots , Av_r\}$ is an orthogonal basis for Col A.").next_to(eq_dot_product_proof[4], DOWN).shift(DOWN)
    scene.play(Write(text_orthogonal_basis))
    scene.wait()

    scene.play(
        FadeOut(eq_dot_product_proof[4]), 
        FadeOut(box_dot_product),
        FadeOut(text_orthogonal_basis)
    )
    scene.wait()

    # =========================================================
    # STEP 2: NORMALIZATION
    # =========================================================
    step2_title = Text("2. Normalization", font_size=36, color=GREEN).next_to(main_title, DOWN)
    scene.play(ReplacementTransform(step1_title, step2_title))
    scene.wait()

    eq_norm_proof = VGroup(
        MathTex(r"\|A v_i\|"),
        MathTex(r"\|A v_i\|", r"=", r"\sqrt{", r"(A v_i)^T", r"(A v_i)", r"}"),
        MathTex(r"\|A v_i\|", r"=", r"\sqrt{", r"v_i^T", r"A^T", r"A", r"v_i", r"}"),
        MathTex(r"\|A v_i\|", r"=", r"\sqrt{", r"v_i^T", r"\lambda_i", r"v_i", r"}"),
        MathTex(r"\|A v_i\|", r"=", r"\sqrt{", r"\lambda_i", r"v_i^T", r"v_i", r"}"),
        MathTex(r"\|A v_i\|", r"=", r"\sqrt{", r"\lambda_i", r"}")
    )

    scene.play(Write(eq_norm_proof[0]))
    scene.wait()
    scene.play(TransformMatchingTex(eq_norm_proof[0], eq_norm_proof[1]))
    scene.wait()
    scene.play(TransformMatchingTex(eq_norm_proof[1], eq_norm_proof[2]))
    scene.wait()

    part_AtAvi = eq_norm_proof[2][4:7]
    scene.play(
        derivation_square_matrix[-1].animate.scale(1.25).set_color(YELLOW),
        part_AtAvi.animate.scale(1.25).set_color(YELLOW)
    )
    scene.play(
        derivation_square_matrix[-1].animate.scale(1/1.25).set_color(WHITE),
        part_AtAvi.animate.scale(1/1.25).set_color(WHITE)
    )
    
    scene.play(TransformMatchingTex(eq_norm_proof[2], eq_norm_proof[3]))
    scene.play(TransformMatchingTex(eq_norm_proof[3], eq_norm_proof[4]))

    part_vivi = eq_norm_proof[4][4:6]
    scene.play(
        eq_unit_length.animate.scale(1.25).set_color(YELLOW),
        part_vivi.animate.scale(1.25).set_color(YELLOW)
    )
    scene.play(
        eq_unit_length.animate.scale(1/1.25).set_color(WHITE),
        part_vivi.animate.scale(1/1.25).set_color(WHITE)
    )

    scene.play(TransformMatchingTex(eq_norm_proof[4], eq_norm_proof[5]))

    box_norm = SurroundingRectangle(eq_norm_proof[5], color=BLUE, buff=0.2)
    scene.play(Create(box_norm))
    
    eq_define_u_i = MathTex(r"\implies u_i = \frac{1}{\|Av_i\|} Av_i", r"= \frac{1}{\sigma_i} Av_i").next_to(eq_dot_product_proof[4], DOWN).shift(DOWN)
    scene.play(Write(eq_define_u_i))
    scene.wait()

    scene.clear()
    scene.add(main_title, step2_title, eq_define_u_i)
    scene.play(eq_define_u_i.animate.move_to(ORIGIN))

    # =========================================================
    # STEP 3: CORE TRANSFORMATION
    # =========================================================
    step3_title = Text("3. Core Transformation", font_size=36, color=GREEN).next_to(main_title, DOWN)
    scene.play(ReplacementTransform(step2_title, step3_title)) 
    scene.wait()

    eq_u_i_expanded = MathTex(r"u_i", r"=", r"\frac{1}{\sigma_i}", r"A", r"v_i")
    scene.play(ReplacementTransform(eq_define_u_i, eq_u_i_expanded))
    scene.wait()

    eq_core_transformation = MathTex(r"A", r"v_i", r"=", r"\sigma_i", r"u_i", r"\quad (1 \le i \le r)")
    scene.play(TransformMatchingTex(eq_u_i_expanded, eq_core_transformation))
    scene.wait()

    note_transformation_meaning = Tex(
        r"Matrix $A$ transforms $v_i$ into $u_i$ scaled by $\sigma_i$", 
        font_size=32, color=YELLOW
    ).next_to(eq_core_transformation, DOWN, buff=0.8)
    scene.play(Write(note_transformation_meaning))
    scene.wait(2)

    # =========================================================
    # STEP 4: MATRIX SYNTHESIS
    # =========================================================
    
    scene.play(
        FadeOut(note_transformation_meaning),
        eq_core_transformation.animate.scale(0.8).to_edge(LEFT).shift(UP * 1.5)
    )

    step4_title = Text("4. Matrix Synthesis", font_size=36, color=GREEN).next_to(main_title, DOWN)
    scene.play(ReplacementTransform(step3_title, step4_title))
    scene.wait()

    eq_matrix_synthesis_1 = MathTex(
        r"A", r"V", r"=", r"\Big[", r"\sigma_1", r"u_1", r"\dots", r"\sigma_r", r"u_r", 
        r"\quad", r"0", r"\dots", r"0", r"\Big]"
    )
    scene.play(Write(eq_matrix_synthesis_1))
    scene.wait()

    part_sigma_u_top = eq_core_transformation[3:5]
    part_sigma_u_bot_1 = eq_matrix_synthesis_1[4:6]
    part_sigma_u_bot_2 = eq_matrix_synthesis_1[7:9]

    scene.play(
        part_sigma_u_top.animate.scale(1.25).set_color(YELLOW),
        part_sigma_u_bot_1.animate.scale(1.25).set_color(YELLOW),
        part_sigma_u_bot_2.animate.scale(1.25).set_color(YELLOW)
    )
    scene.play(
        part_sigma_u_top.animate.scale(1/1.25).set_color(WHITE),
        part_sigma_u_bot_1.animate.scale(1/1.25).set_color(WHITE),
        part_sigma_u_bot_2.animate.scale(1/1.25).set_color(WHITE)
    )
    scene.wait()

    eq_matrix_synthesis_2 = MathTex(r"A", r"V", r"=", r"U", r"\Sigma")
    scene.play(TransformMatchingTex(eq_matrix_synthesis_1, eq_matrix_synthesis_2))
    scene.wait()

    note_v_orthogonal = Tex(r"Because $V$ is orthogonal: ", r"$V^T V = I$", font_size=32).to_edge(DOWN).shift(UP * 0.5)
    scene.play(Write(note_v_orthogonal))
    scene.wait()

    eq_matrix_synthesis_3 = MathTex(r"A", r"V", r"V^T", r"=", r"U", r"\Sigma", r"V^T")
    scene.play(TransformMatchingTex(eq_matrix_synthesis_2, eq_matrix_synthesis_3))
    scene.wait()

    part_vvt_eq = eq_matrix_synthesis_3[1:3]
    part_vvt_note = note_v_orthogonal[1]

    scene.play(
        part_vvt_eq.animate.scale(1.25).set_color(YELLOW),
        part_vvt_note.animate.scale(1.25).set_color(YELLOW)
    )
    scene.play(
        part_vvt_eq.animate.scale(1/1.25).set_color(WHITE),
        part_vvt_note.animate.scale(1/1.25).set_color(WHITE)
    )

    eq_final_svd = MathTex(r"A", r"=", r"U", r"\Sigma", r"V^T").scale(1.5)
    scene.play(
        FadeOut(note_v_orthogonal), 
        FadeOut(eq_core_transformation), 
        TransformMatchingTex(eq_matrix_synthesis_3, eq_final_svd)
    )
    scene.wait()

    final_svd_box = SurroundingRectangle(eq_final_svd, color=RED, buff=0.25)

    scene.play(Create(final_svd_box))
    scene.wait(2)
    scene.clear()