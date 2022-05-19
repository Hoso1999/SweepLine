from ground.base import get_context
from planar import contour_self_intersects

context = get_context()
Contour, Point = context.contour_cls, context.point_cls
x = contour_self_intersects(Contour([Point(0, 0), Point(0, 200),Point(200, 200), Point(200, 0), Point(-100,0)]))
print(x)
