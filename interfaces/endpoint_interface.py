from abc import ABC, abstractmethod


class EndpointInterface(ABC):

    @abstractmethod
    def register(
        self,
        endpoint,
    ):
        ...
