"""
@property: Этот декоратор используется для создания свойств в классе. Он позволяет функции класса быть доступной как
 атрибут, а не как метод. Это удобно, когда значение атрибута должно быть вычисляемым.
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Возвращает радиус круга."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Устанавливает радиус круга."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Радиус не может быть отрицательным")
