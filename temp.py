from abc import ABC, abstractmethod, abstractproperty
from tkinter.messagebox import NO


class ABCTetrisObject(ABC):
    def __init__(self, origin: int) -> None:
        if origin < 0 or origin > 10:
            raise ValueError("Origin should be between 0 and 9")
        self.origin = origin
        self._position = None

    @abstractmethod
    def move_down(self) -> None:
        pass

    @property
    def position(self, ):
        return self


class ABCTetrisBoard(ABC):
    _hight: int
    _width: int
    _state: list[list[int]]

    @abstractproperty
    def hight(self):
        pass

    @abstractproperty
    def width(self):
        pass

    @abstractproperty
    def state(self):
        pass
    
    @abstractmethod
    def update_state(self) -> None:
        pass


class Q(TetrisObject):
    shape: list = [(0, 0), (0, 1), (1, 0), (1, 1)]


class L(TetrisObject):
    shape: list = [(0, 0), (1, 0),  (2, 0), (2, 1)]