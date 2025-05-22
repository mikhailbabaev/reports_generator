from abc import ABC, abstractmethod
from typing import List, Dict, Any


class Report(ABC):
    @abstractmethod
    def generate(self, data: List[Dict[str, Any]]) -> Any:
        pass

    @abstractmethod
    def render(self, report_data: Any) -> str:
        pass