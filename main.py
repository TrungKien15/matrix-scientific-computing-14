from manim import *
from math import sqrt
from problem.problem import problem
from problem.step1 import step1
from problem.step2 import step2
from problem.step3 import step3
from problem.step4 import step4
from problem.result import result
from SVD.theory import svd_theory
from SVD.proof import svd_proof
from SVD.example import svd_example
from SVD.geometry import svd_geometry

class SVD(Scene):
    def intro(self):
        plane = NumberPlane()
        title = Text("SVD - Singular Value Decomposition").shift(UP)
        
        self.play(FadeIn(plane), Write(title))
        self.wait(2)
        self.play(FadeOut(plane), FadeOut(title))
        self.clear()

    def construct(self):
        
        self.intro()
        problem(self)
        step1(self)
        step2(self)
        step3(self)
        step4(self)
        result(self)
        svd_theory(self)
        svd_proof(self)
        svd_example(self)
        svd_geometry(self)