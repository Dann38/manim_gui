from manim import *

# class Animation(Scene):
#     def construct(self):
        
#         # numberplane = NumberPlane().add_coordinates()
#         numberplane = NumberPlane()
#         self.play(Create(numberplane), run_time=2)
        
        
#         self.wait()
#         self.play(numberplane.animate.shift(3*LEFT+3*DOWN))
#         self.play(ApplyMethod(numberplane.scale, 3))
#         self.wait()
config.frame_height = 42


class Animation(LinearTransformationScene, MovingCameraScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            background_plane_kwargs={
                "x_range": [-3, 3, 1],
                "y_range": [-5, 5, 1],
            },
            foreground_plane_kwargs={
                "x_range": [-15, 15, 1],
                "y_range": [-12, 12, 1],
            },
            show_coordinates=True,
            leave_ghost_vectors=True,
        )
        MovingCameraScene.__init__(self)

    def construct(self):
        self.camera.background_color = WHITE

        x_axis = self.background_plane.get_x_axis()
        x_axis.numbers.set_color(BLACK)
        y_axis = self.background_plane.get_y_axis()
        y_axis.numbers.set_color(BLACK)

        x_axis = self.plane.get_x_axis()
        x_axis.set_color(BLACK)
        y_axis = self.plane.get_y_axis()
        y_axis.set_color(BLACK)

        rect = Rectangle(color=RED, width=2, height=4).shift(1*RIGHT+2*UP)

        self.add(rect)
        self.camera.frame.move_to(rect).set(height=rect.height * 1.2)
        ds = 0.2
        c1 = 1
        c2 = 3
        dt_up = c2*ds
        dt_down = c1*ds
        matrix = [[ds, ds], [-dt_down, dt_up]]
        self.apply_matrix(matrix)
        # self.play(self.camera.frame.animate.move_to(rect).set(width=rect.width * 3))
        self.wait()
       