"""
Name: Angie Bui
face.py
Problem: Face class for changing facial expression.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        size = self.head.getRadius()
        center = self.head.getCenter()
        mouth_size = 0.8 * size
        m_off = size / 2.0
        p_3 = center.clone()
        p_3.move(0, m_off * 1.8)
        p_1 = center.clone()
        p_1.move(-mouth_size/2, m_off)
        p_2 = center.clone()
        p_2.move(mouth_size/2, m_off)
        left = Line(p_1, p_3)
        right = Line(p_2, p_3)
        right.draw(self.window)
        left.draw(self.window)


    def shock(self):
        size = self.head.getRadius()
        mouth_size = 0.20 * size
        m_center = self.mouth.getCenter()
        shock = Circle(m_center, mouth_size)
        self.mouth.undraw()
        self.mouth = shock
        self.mouth.draw(self.window)


    def wink(self):
        center = self.head.getCenter()
        size = self.head.getRadius()
        eye = size / 3.0
        p_1 = center.clone()
        p_1.move(-eye / 1.6, -eye)
        p_2 = center.clone()
        p_2.move(eye/2, -eye)
        eye_line = Line(p_1, p_2)
        eye_line.move( -eye, 0)
        self.left_eye.undraw()
        self.left_eye = eye_line
        eye_line.draw(self.window)
        self.smile()

