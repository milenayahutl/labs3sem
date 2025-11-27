class FigureColor:
    def __init__(self):
        self._color = None

    @property
    def colorproperty(self):  #читаем цвет как поле
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        self._color = value