from abc import ABC, abstractmethod

class Page(ABC):
    @abstractmethod
    def run(self):
        pass
