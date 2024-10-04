from abc import ABC, abstractmethod


class DomainEventPublisher(ABC):
    @abstractmethod
    def publish_event(self, event_data):
        pass

