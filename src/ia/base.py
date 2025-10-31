# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseIA(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        pass