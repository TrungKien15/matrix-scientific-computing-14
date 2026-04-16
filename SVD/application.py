from manim import *
import numpy as np
from PIL import Image

def svd_application(scene):
    title = Text("Compressing images with SVD").set_color(PINK)
    scene.play(Write(title))
    scene.play(title.animate.to_edge(UP))

    image_name = "assets/image.png"

    try:
        img = Image.open(image_name).convert('RGB')
    except FileNotFoundError:
        img = Image.fromarray((np.random.rand(200, 200, 3) * 255).astype(np.uint8))

    image_mobject = ImageMobject(img)
    image_mobject.set_width(9)
    image_mobject.move_to(ORIGIN)

    scene.play(FadeIn(image_mobject))
    scene.wait(1)

    rows, cols = 9, 9
    pixel_grid = VGroup()
    np.random.seed(42)
    values = np.random.randint(0, 255, size=(rows, cols))

    for i in range(rows):
        for j in range(cols):
            val = values[i, j]
            color = rgb_to_color((val/255, val/255, val/255))

            pixel = Square(side_length=0.6)\
                .set_fill(color, opacity=1)\
                .set_stroke(WHITE, width=0.5)

            pixel.move_to(
                RIGHT * (j - cols/2 + 0.5) * 0.6 +
                DOWN * (i - rows/2 + 0.5) * 0.6
            )
            pixel_grid.add(pixel)

    pixel_grid.move_to(image_mobject.get_center())

    scene.play(
        FadeTransform(image_mobject, pixel_grid),
        run_time=2
    )
    scene.wait(1)

    note1 = Text("For computer: Image ~ Matrix of pixels").next_to(pixel_grid, DOWN)
    scene.play(Write(note1))
    scene.wait()
    scene.play(Unwrite(note1))

    number_grid = VGroup()
    for i in range(rows):
        for j in range(cols):
            val = values[i, j]
            pixel = pixel_grid[i * cols + j]
            num = Text(str(val), font_size=16).move_to(pixel.get_center())
            number_grid.add(num)

    left_bracket = MathTex("[").scale_to_fit_height(pixel_grid.height).next_to(pixel_grid, LEFT, buff=0.1)
    right_bracket = MathTex("]").scale_to_fit_height(pixel_grid.height).next_to(pixel_grid, RIGHT, buff=0.1)

    scene.play(
        Write(number_grid),
        pixel_grid.animate.set_fill(opacity=0.3)
    )
    note2 = Text("Each pixel ~ a number indicating brightness").next_to(pixel_grid, DOWN)
    scene.play(Write(note2))
    scene.wait()
    scene.play(Unwrite(note2))

    scene.play(
        pixel_grid.animate.set_fill(opacity=0),
        Write(left_bracket),
        Write(right_bracket)
    )
    scene.wait()

    scene.play(
        pixel_grid.animate.shift(LEFT),
        left_bracket.animate.shift(LEFT),
        right_bracket.animate.shift(LEFT),
        number_grid.animate.shift(LEFT)
    )
    scene.play(FadeIn(MathTex("= A").scale(2).next_to(right_bracket), shift=UP))
    scene.wait(2)
    scene.clear()
    scene.add(title)

    eq0 = MathTex(r"A = U \Sigma V^\top")
    scene.play(FadeIn(eq0, shift=LEFT))
    scene.wait(2)

    eq1 = MathTex(
        r"A =",
        r"\begin{pmatrix} | & & | \\ u_1 & \cdots & u_n \\ | & & | \end{pmatrix}",
        r"\begin{pmatrix} \sigma_1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \sigma_2 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \cdots & \vdots \\ 0 & 0 & \cdots & \sigma_r & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix}",
        r"\begin{pmatrix} - & v_1^\top & - \\ & \vdots & \\ - & v_n^\top & - \end{pmatrix}"
    ).scale(0.75)
    scene.play(ReplacementTransform(eq0, eq1))
    scene.wait(2)

    eq2 = MathTex(
        r"A = ",
        r"\sigma_1 \begin{pmatrix} | \\ u_1 \\ | \end{pmatrix} \begin{pmatrix} - & v_1^\top & - \end{pmatrix} + \cdots + \sigma_r \begin{pmatrix} | \\ u_r \\ | \end{pmatrix} \begin{pmatrix} - & v_r^\top & - \end{pmatrix} \\",
    ).scale(0.75)
    scene.play(ReplacementTransform(eq1, eq2))
    scene.wait(2)

    eq3 = MathTex(
        r"A = ",
        r"\sum_{i=1}^r \sigma_i \begin{pmatrix} | \\ u_i \\ | \end{pmatrix} \begin{pmatrix} - & v_i^\top & - \end{pmatrix}"
    )
    scene.play(ReplacementTransform(eq2, eq3))
    scene.wait(2)

    note3 = Text("=> An matrix ~ Sum of rank-1 matrices.", font_size=32).next_to(eq3, DOWN)
    scene.play(Write(note3))
    scene.wait(2)
    scene.clear()

    sigma = MathTex(r"\Sigma = \begin{pmatrix} \sigma_1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \sigma_2 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \cdots & \vdots \\ 0 & 0 & \cdots & \sigma_r & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix}")

    scene.play(Write(sigma))
    scene.wait()
    scene.play(FadeOut(sigma))

    axes = Axes(
        x_range=[0, 60, 10],
        y_range=[0, 100, 20],
        axis_config={"include_numbers": False, "color": WHITE},
        x_length=10,
        y_length=6
    )

    y_label = MathTex(r"\sigma_i").scale(1.5).next_to(axes.y_axis.get_top(), LEFT, buff=0.2)
    x_label = MathTex(r"Index \; (i)").scale(1.5).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
    
    scene.play(Create(axes), Write(y_label), Write(x_label))
    scene.wait(0.5)

    func = lambda x: 85 * np.exp(-0.15 * x) + 2
    
    graph = axes.plot(func, x_range=[0, 58], color=BLUE_C, stroke_width=4)
    
    scene.play(Create(graph), run_time=2)
    scene.wait(0.5)
    k = 20
    
    dashed_line = DashedLine(
        start=axes.c2p(k, 0),
        end=axes.c2p(k, 95), 
        color=WHITE,
        stroke_width=4
    )
    
    k_label = MathTex(r"k", font_size=36).next_to(dashed_line, DOWN, buff=0.5)
    
    scene.play(Create(dashed_line), Write(k_label))
    scene.wait(0.5)

    area_signal = axes.get_area(graph, x_range=[0, k], color=YELLOW, opacity=0.7)
    
    area_noise = axes.get_area(graph, x_range=[k, 58], color=GRAY, opacity=0.7)

    text_feature = Text("Feature\n(Keep)", color=YELLOW, font_size=32).next_to(dashed_line, RIGHT, buff=0.5).shift(UP * 1.5)
    text_noise = Text("Noise\n(Remove)", color=LIGHT_GREY, font_size=32).next_to(dashed_line, RIGHT, buff=2.5).shift(DOWN)

    scene.play(FadeIn(area_signal), Write(text_feature))
    scene.wait(1)
    scene.play(FadeIn(area_noise), Write(text_noise))
    scene.wait(2)
    scene.clear()
    scene.add(title)

    eq_final = MathTex(
        r"A \approx A_k := \sum_{i=1}^k \sigma_i \begin{pmatrix} | \\ u_i \\ | \end{pmatrix} \begin{pmatrix} - & v_i^\top & - \end{pmatrix}"
    )
    scene.play(Write(eq_final))

    note4 = Text("With this approximation idea we are now ready to implement image compression.").scale_to_fit_width(config.frame_width - 1).to_edge(DOWN).shift(UP)
    scene.play(eq_final.animate.scale(1.25))
    scene.play(
        Create(SurroundingRectangle(eq_final, color=RED, buff=0.2)),
        Write(note4)
    )
    scene.wait(2)
    scene.clear()
    scene.add(title)
    
    try:
        img = Image.open(image_name).convert('RGB')
        A = np.array(img) / 255.0 
    except FileNotFoundError:
        x, y = np.meshgrid(np.linspace(0, 4 * np.pi, 200), np.linspace(0, 4 * np.pi, 200))
        R = (np.sin(x) + 1) / 2
        G = (np.cos(y) + 1) / 2
        B = (np.sin(x*y) + 1) / 2
        A = np.dstack((R, G, B))

    R = A[:, :, 0]
    G = A[:, :, 1]
    B = A[:, :, 2]

    max_possible_rank = min(R.shape[0], R.shape[1])

    R_U, R_S, R_VT = np.linalg.svd(R, full_matrices=False)
    G_U, G_S, G_VT = np.linalg.svd(G, full_matrices=False)
    B_U, B_S, B_VT = np.linalg.svd(B, full_matrices=False)

    def read_as_compressed(U, S, VT, k):
        if k == 0:
            return np.zeros((U.shape[0], VT.shape[1]))
        return (U[:, :k] @ np.diag(S[:k])) @ VT[:k, :]

    def get_compressed_rgb(k):
        R_comp = read_as_compressed(R_U, R_S, R_VT, k)
        G_comp = read_as_compressed(G_U, G_S, G_VT, k)
        B_comp = read_as_compressed(B_U, B_S, B_VT, k)
        
        compressed_float = np.dstack((R_comp, G_comp, B_comp))
        compressed = (np.clip(compressed_float, 0.0, 1.0) * 255).astype(np.uint8)
        return compressed

    relative_ranks = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.0]
    
    first_rel_rank = relative_ranks[0]
    first_k = max(1, int(first_rel_rank * max_possible_rank))
    
    image_mob = ImageMobject(get_compressed_rgb(first_k))
    image_mob.height = 4.5
    
    info_text = Text(
        f"Relative Rank: {first_rel_rank*100:.0f}% | Rank (k): {first_k} / {max_possible_rank}", 
        font_size=28, color=YELLOW
    ).next_to(image_mob, DOWN, buff=0.3)
    
    scene.play(FadeIn(image_mob), Write(info_text))
    scene.wait(1.5)

    for rel_rank in relative_ranks[1:]:
        k = max(1, int(rel_rank * max_possible_rank))
        
        new_image_mob = ImageMobject(get_compressed_rgb(k))
        new_image_mob.height = 4.5
        new_image_mob.move_to(image_mob.get_center())
        
        new_info_text = Text(
            f"Relative Rank: {rel_rank*100:.0f}% | Rank (k): {k} / {max_possible_rank}", 
            font_size=28, color=YELLOW
        ).move_to(info_text.get_center())

        scene.play(
            image_mob.animate.become(new_image_mob),
            ReplacementTransform(info_text, new_info_text),
            run_time=1.5
        )
        info_text = new_info_text
        scene.wait(1.5)

    scene.wait(2)
    scene.clear()