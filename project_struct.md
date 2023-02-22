mastercard/
├── clients/
│   ├── __init__.py
│   ├── asynchronous_checkout_client.py
│   ├── asynchronous_payment_gateway_client.py
│   ├── card_client.py
│   ├── charge_client.py
│   ├── checkout_client.py
│   ├── payment_gateway_client.py
│   ├── refund_client.py
│   └── tokenization_client.py
├── interfaces/
│   ├── __init__.py
│   ├── card_interface.py
│   ├── charge_interface.py
│   ├── checkout_interface.py
│   ├── payment_gateway_interface.py
│   └── refund_interface.py
├── models.py
└── __init__.py

Где:
    mastercard/clients/ - пакет с реализациями клиентов для API Mastercard
    mastercard/interfaces/ - пакет с интерфейсами для клиентов
    mastercard/models.py - файл с описанием моделей данных для API Mastercard
