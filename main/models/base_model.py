from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def set_surface(self):
        pass

    @abstractmethod
    def set_display_surface(self):
        pass

    @abstractmethod
    def run(self):
        pass


if __name__ == '__main__':
    pass
