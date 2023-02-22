from abc import ABC, abstractmethod
from typing import Optional

from mastercard.models import RefundRequest, RefundSummary


class RefundInterface(ABC):
    @abstractmethod
    async def refund(self, refund_request: RefundRequest) -> Optional[RefundSummary]:
        pass
