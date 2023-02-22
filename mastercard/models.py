from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, List


@dataclass
class Payment:
    id: str
    amount: Decimal
    currency: str
    description: str
    status: str


@dataclass
class Checkout:
    id: str
    status: str
    created_time: str
    updated_time: str
    amount: Decimal
    currency: str
    order_id: str
    merchant_id: str
    transaction_id: str
    transaction_status: str


@dataclass
class Charge:
    id: str
    amount: Decimal
    currency: str
    description: str
    status: str
    order_id: str
    transaction_id: str


@dataclass
class Refund:
    id: str
    amount: Decimal
    currency: str
    description: str
    status: str
    charge_id: str


@dataclass
class Card:
    id: str
    card_number: str
    expiration_month: str
    expiration_year: str
    cvv: str
    cardholder_name: str
    billing_address: str


@dataclass
class Token:
    id: str
    value: str
    card: Card


@dataclass
class ChargeRequest:
    id: str
    amount: int
    currency: str
    description: Optional[str] = None
    metadata: Optional[dict] = None


@dataclass
class Address:
    id: str
    first_name: str
    last_name: str
    address1: str
    address2: str
    city: str
    country_code: str
    postal_code: str


@dataclass
class CheckoutRequest:
    amount: int
    currency: str
    callback_url: str
    redirect_url: str
    locale: str
    region: str
    order: str
    customer: Address
    merchant: Address
    cart: List[dict]
    payment: Payment


@dataclass
class CheckoutSummary:
    id: str
    status: str
    updated_time: str


@dataclass
class Currency:
    code: str
    name: str
    symbol: str


@dataclass
class PaymentType:
    type: str
    name: str


@dataclass
class PaymentSummary:
    id: str
    amount: Decimal
    currency: str
    status: str
    created_at: str
    updated_at: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[dict] = None


@dataclass
class RefundSummary:
    id: str
    amount: Decimal
    currency: str
    status: str
    created_at: str
    updated_at: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[dict] = None
    payment_id: Optional[str] = None


@dataclass
class RefundRequest:
    """
    A class representing a refund request.

    Attributes:
        amount (Decimal): The amount to refund.
        payment_id (str): The ID of the payment to refund.
    """
    amount: Decimal
    payment_id: Payment
