"""
В Python геттеры и сеттеры создаются с использованием декораторов @property и сеттер-декораторов. Этот подход позволяет
 инкапсулировать данные, контролируя доступ к атрибутам класса и возможность их изменения. Использование @property
 делает код более читаемым и позволяет сохранить интерфейс класса неизменным даже при изменении внутренней реализации.

Пример использования @property для создания геттера:
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Геттер для радиуса."""
        return self._radius

"""
В этом примере @property используется для создания геттера для атрибута radius. Атрибут _radius представляет собой
защищённый атрибут класса Circle, доступ к которому осуществляется через свойство radius.

Создание сеттера:
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Геттер для радиуса."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Сеттер для радиуса."""
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = value


"""
Добавление метода radius.setter позволяет определить сеттер для атрибута radius. Теперь при попытке установить радиус
 в отрицательное значение или ноль будет вызвано исключение ValueError.

Пример использования:
"""

c = Circle(5)
print(c.radius)  # 5

c.radius = 10    # Устанавливаем новое значение радиуса
print(c.radius)  # 10

# c.radius = -5  # Будет вызвано исключение ValueError

"""
Этот подход позволяет не только контролировать доступ к данным, но и валидировать их при изменении, обеспечивая тем 
самым безопасность и целостность данных объекта. Использование геттеров и сеттеров делает классы в Python более 
гибкими и мощными, приближая их к поведению классов в статически типизированных языках программирования.
"""