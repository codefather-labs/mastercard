from abc import ABC, abstractmethod
from typing import Optional, List

from mastercard.models import Payment, Refund, PaymentSummary, RefundSummary


class PaymentGatewayInterface(ABC):
    @abstractmethod
    async def create_payment(self, payment: Payment) -> Payment:
        pass

    @abstractmethod
    async def get_payment(self, payment_id: str) -> Payment:
        pass

    @abstractmethod
    async def get_payment_summary(
            self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> PaymentSummary:
        pass

    @abstractmethod
    async def refund_payment(self, refund: Refund) -> Refund:
        pass

    @abstractmethod
    async def get_refund(self, refund_id: str) -> Refund:
        pass

    @abstractmethod
    async def get_refund_summary(
            self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> RefundSummary:
        pass
