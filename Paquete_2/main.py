print("Resultados:")

from Shape import Point, Triangle, Square

def main():
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(0, 4)
    A = Triangle([p1, p2, p3])
    print("Área del triángulo:", A.compute_area())
    print("Perímetro del triángulo:", A.compute_perimeter())

    q1 = Point(0, 0)
    q2 = Point(0, 2)
    q3 = Point(2, 2)
    q4 = Point(2, 0)
    square = Square([q1, q2, q3, q4])
    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())

if __name__ == "__main__":
    main()