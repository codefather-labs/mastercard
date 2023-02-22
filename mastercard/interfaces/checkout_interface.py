from abc import ABC, abstractmethod
from typing import List

from mastercard.models import (
    Address,
    CheckoutRequest,
    CheckoutSummary,
    Currency,
    Payment,
    PaymentType,
)


class CheckoutInterface(ABC):
    @abstractmethod
    async def create_checkout_session(self, request: CheckoutRequest) -> str:
        pass

    @abstractmethod
    async def get_checkout_summary(self, checkout_id: str) -> CheckoutSummary:
        pass

    @abstractmethod
    async def get_checkout_payment(self, checkout_id: str) -> Payment:
        pass

    @abstractmethod
    async def capture_payment(
            self,
            checkout_id: str,
            payment_id: str,
            amount: int,
            currency: Currency,
            payment_type: PaymentType,
            billing_address: Address,
    ) -> Payment:
        pass

    @abstractmethod
    async def void_payment(self, checkout_id: str, payment_id: str) -> Payment:
        pass

    @abstractmethod
    async def refund_payment(
            self, checkout_id: str, payment_id: str, amount: int, currency: Currency
    ) -> Payment:
        pass

    @abstractmethod
    async def get_payment(
            self, payment_id: str, payment_type: PaymentType
    ) -> Payment:
        pass

    @abstractmethod
    async def capture_authorization(
            self,
            checkout_id: str,
            payment_id: str,
            amount: int,
            currency: Currency,
            payment_type: PaymentType,
            billing_address: Address,
    ) -> Payment:
        pass

    @abstractmethod
    async def create_session_id(self) -> str:
        pass

    @abstractmethod
    async def get_payment_data(
            self, checkout_id: str, payment_id: str, payment_type: PaymentType
    ) -> List[Payment]:
        pass
