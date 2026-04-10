from manim import *
import numpy as np

def svd_geometry(scene):
    A = np.array([[2.0, 2.0],
                  [0.0, 1.0]])
    
    U, S_values, VT = np.linalg.svd(A)
    Sigma = np.diag(S_values)
    
    V = VT.T
    v1_coord = V[:, 0]
    v2_coord = V[:, 1]

    C_A = WHITE
    C_V = PURPLE
    C_SIG = YELLOW
    C_U = BLUE
    C_V1 = YELLOW 
    C_V2 = GREEN

    plane = NumberPlane(
        x_range=[-4, 4], 
        y_range=[-4, 4], 
        background_line_style={"stroke_opacity": 0.4}
    )
    
    circle = Circle(radius=1.0, color=C_U).set_fill(C_U, opacity=0.2)
    
    vec_v1 = Vector(v1_coord, color=C_V1)
    vec_v2 = Vector(v2_coord, color=C_V2)
    
    label_v1 = MathTex("v_1", color=C_V1)
    label_v1.add_updater(lambda m: m.move_to(vec_v1.get_end() + vec_v1.get_vector() * 0.3))
    
    label_v2 = MathTex("v_2", color=C_V2)
    label_v2.add_updater(lambda m: m.move_to(vec_v2.get_end() + vec_v2.get_vector() * 0.3))

    trace_v1 = TracedPath(vec_v1.get_end, stroke_color=C_SIG, stroke_opacity=[0, 1, 0], stroke_width=3, dissipating_time=1)
    trace_v2 = TracedPath(vec_v2.get_end, stroke_color=C_SIG, stroke_opacity=[0, 1, 0], stroke_width=3, dissipating_time=1)
    
    matrix_a = MathTex("A =", f"\\begin{{bmatrix}} {A[0,0]} & {A[0,1]} \\\\ {A[1,0]} & {A[1,1]} \\end{{bmatrix}}", font_size=32).to_corner(UL).shift(DOWN * 2)
    
    title = Text("Geometric visual representation of SVD").to_edge(UP)
    title.add_background_rectangle()

    scene.add(plane)
    scene.play(Write(title))
    scene.play(FadeIn(matrix_a, shift=LEFT))
    scene.play(Create(circle), GrowArrow(vec_v1), GrowArrow(vec_v2))
    scene.add(label_v1, label_v2, trace_v1, trace_v2)
    scene.wait(1)

    ghost_init = circle.copy().set_fill(opacity=0).set_stroke(color=WHITE, opacity=0.3, width=2)
    scene.add(ghost_init)

    title_1 = Tex(r"Rotate - $V^T$", font_size=32).set_color(C_V).next_to(matrix_a, DOWN)
    scene.play(Write(title_1))
    
    matrix_vt = MathTex("V^T =", f"\\begin{{bmatrix}} {VT[0,0]:.2f} & {VT[0,1]:.2f} \\\\ {VT[1,0]:.2f} & {VT[1,1]:.2f} \\end{{bmatrix}}", font_size=32, color=C_V).scale(0.9).to_corner(DR).shift(UP * 2)
    scene.play(Write(matrix_vt))
    
    scene.play(
        ApplyMatrix(VT, circle),
        ApplyMatrix(VT, vec_v1),
        ApplyMatrix(VT, vec_v2),
        run_time=2,
        rate_func=linear 
    )
    
    scene.wait(1)

    ghost_step1 = circle.copy().set_fill(opacity=0).set_stroke(color=C_V, opacity=0.4, width=2)
    scene.add(ghost_step1)
    
    scene.play(FadeOut(matrix_vt))

    title_2 = Tex("Scale - $\Sigma$", font_size=32).set_color(C_SIG).next_to(title_1, DOWN)
    scene.play(Write(title_2))
    
    matrix_sigma = MathTex("\\Sigma =", f"\\begin{{bmatrix}} {Sigma[0,0]:.2f} & 0 \\\\ 0 & {Sigma[1,1]:.2f} \\end{{bmatrix}}", font_size=32, color=C_SIG).to_corner(DR).shift(UP * 2)
    scene.play(Write(matrix_sigma))
    
    label_sig1 = MathTex("\\sigma_1 e_1", color=C_V1)
    label_sig1.add_updater(lambda m: m.move_to(vec_v1.get_end() + vec_v1.get_vector() * 0.2))
    
    label_sig2 = MathTex("\\sigma_2 e_2", color=C_V2)
    label_sig2.add_updater(lambda m: m.move_to(vec_v2.get_end() + vec_v2.get_vector() * 0.2))
    
    scene.remove(label_v1, label_v2)
    scene.add(label_sig1, label_sig2)

    scene.play(
        ApplyMatrix(Sigma, circle),
        ApplyMatrix(Sigma, vec_v1),
        ApplyMatrix(Sigma, vec_v2),
        run_time=2,
        rate_func=linear
    )
    
    scene.wait(1)

    ghost_step2 = circle.copy().set_fill(opacity=0).set_stroke(color=C_SIG, opacity=0.4, width=2)
    scene.add(ghost_step2)

    scene.play(FadeOut(matrix_sigma))

    title_3 = Tex("Rotate - $U$", font_size=32).set_color(C_U).next_to(title_2, DOWN)
    scene.play(Write(title_3))

    matrix_u = MathTex("U =", f"\\begin{{bmatrix}} {U[0,0]:.2f} & {U[0,1]:.2f} \\\\ {U[1,0]:.2f} & {U[1,1]:.2f} \\end{{bmatrix}}", font_size=32, color=C_U).to_corner(DR).shift(UP * 2)
    scene.play(Write(matrix_u))

    label_u1 = MathTex("\\sigma_1 u_1", color=C_V1)
    label_u1.add_updater(lambda m: m.move_to(vec_v1.get_end() + vec_v1.get_vector() * 0.2))
    
    label_u2 = MathTex("\\sigma_2 u_2", color=C_V2)
    label_u2.add_updater(lambda m: m.move_to(vec_v2.get_end() + vec_v2.get_vector() * 0.2))
    
    scene.remove(label_sig1, label_sig2)
    scene.add(label_u1, label_u2)

    scene.play(
        ApplyMatrix(U, circle),
        ApplyMatrix(U, vec_v1),
        ApplyMatrix(U, vec_v2),
        run_time=2,
        rate_func=linear
    )
    
    scene.wait(1)
    scene.play(FadeOut(matrix_u))
    
    final_formula = MathTex("A =", "U", "\\Sigma", "V^T").set_color_by_tex_to_color_map({
        "U": C_U, "\\Sigma": C_SIG, "V^T": C_V
    }).arrange(RIGHT, buff=0.1)
    
    final_formula.next_to(title, DOWN, buff=1)
    
    scene.play(Write(final_formula))
    box_final = SurroundingRectangle(final_formula, color=GREEN, buff=0.3)
    scene.play(Create(box_final))
    
    scene.play(FadeOut(trace_v1), FadeOut(trace_v2), run_time=1)
    
    scene.play(VGroup(final_formula, box_final).animate.scale(1.75).to_edge(DOWN))
    
    scene.wait(4)
    scene.clear()