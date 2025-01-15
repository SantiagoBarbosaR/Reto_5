# Reto_5

shape es el paquete principal, y dentro de él se encuentran subpaquetes y módulos relacionados con la representación y manipulación de figuras geométricas.

Subpaquete: package_rectangle
Contiene clases específicas para trabajar con rectángulos y cuadrados:

class_rectangle : Defina la clase Rectángulo que hereda de Shape. Maneja propiedades y métodos específicos de rectángulos, como el cálculo del área y verificación de sus ángulos internos.
class_square : Defina la clase Cuadrado, una subclase de Rectángulo, que asegura que todos los lados sean iguales y representen un cuadrado.

Subpaquete: package_triangle
Contiene clases para trabajar con diferentes tipos de triángulos:

class_triangle : Define la clase base Triangle, que maneja la lógica genérica para triángulos, como el cálculo del área y ángulos interiores.
class_equilateral : Defina la clase Equilátero que representa triángulos equiláteros, asegurando que todos los lados y ángulos sean iguales.
class_isosceles : Define la clase Isósceles, para triángulos isósceles, verificando que al menos dos lados tengan la misma longitud.
class_scalene : Define la clase Scalene, para triángulos escalenos, donde todos los lados y ángulos son diferentes.
class_trirectangle : Defina la clase Trirectangleque representa triángulos rectángulos, verificando el Teorema de Pitágoras.

Otros módulos dentro de package_Shape
class_line : Define la clase Lineque representa líneas y proporciona métodos para calcular la longitud, pendiente y puntos de intersección con los ejes.
class_point : Define la clase Point, que representa puntos en un plano cartesiano y ofrece métodos como el cálculo de la distancia entre dos puntos.
class_shape : Define la clase base Shape, de la cual heredan todas las figuras geométricas. Proporciona métodos generales como el cálculo de perímetro y la verificación de regularidad.
