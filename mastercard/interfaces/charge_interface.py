from abc import ABC, abstractmethod
from typing import List, Dict

from mastercard.models import Payment, Charge, ChargeRequest


class ChargeInterface(ABC):
    """
    The interface for charge clients.
    """

    @abstractmethod
    async def charge(self, payment: Payment, charge_request: ChargeRequest) -> Charge:
        """
        Creates a charge with the given payment and charge request.

        :param payment: The payment to charge.
        :type payment: Payment
        :param charge_request: The request containing the charge information.
        :type charge_request: ChargeRequest
        :return: The charge that was created.
        :rtype: Charge
        """
        pass

    @abstractmethod
    async def get_charge(self, charge_id: str) -> Charge:
        """
        Retrieves the charge with the given ID.

        :param charge_id: The ID of the charge to retrieve.
        :type charge_id: str
        :return: The charge that was retrieved.
        :rtype: Charge
        """
        pass

    @abstractmethod
    async def list_charges(self, params: Dict = None) -> List[Charge]:
        """
        Lists all charges.

        :param params: Additional query parameters to include in the request.
        :type params: Dict
        :return: The list of charges.
        :rtype: List[Charge]
        """
        pass

    @abstractmethod
    async def capture_charge(self, charge_id: str, amount: int = None) -> Charge:
        """
        Captures the charge with the given ID.

        :param charge_id: The ID of the charge to capture.
        :type charge_id: str
        :param amount: The amount to capture, in cents. If not specified, the full amount will be captured.
        :type amount: int
        :return: The charge that was captured.
        :rtype: Charge
        """
        pass

    @abstractmethod
    async def refund_charge(self, charge_id: str, amount: int = None) -> Charge:
        """
        Refunds the charge with the given ID.

        :param charge_id: The ID of the charge to refund.
        :type charge_id: str
        :param amount: The amount to refund, in cents. If not specified, the full amount will be refunded.
        :type amount: int
        :return: The charge that was refunded.
        :rtype: Charge
        """
        pass
