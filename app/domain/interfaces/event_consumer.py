from abc import ABC, abstractmethod


class DomainEventConsumer(ABC):
    @abstractmethod
    def subscribe(self, callback):
        pass
