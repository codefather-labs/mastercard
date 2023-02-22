from typing import List

from mastercard.models import Card


class CardClient:
    """
    Interface for interacting with the Mastercard Card API.
    """

    async def get_card(self, card_id: str) -> Card:
        """
        Retrieves a single card resource identified by the supplied `card_id`.

        :param card_id: A unique card identifier.
        :return: A card resource representing the card identified by `card_id`.
        """
        pass

    async def create_card(self, card: Card) -> Card:
        """
        Creates a new card resource.

        :param card: A new card resource to be created.
        :return: The created card resource.
        """
        pass

    async def update_card(self, card: Card) -> Card:
        """
        Updates an existing card resource.

        :param card: The card resource to be updated.
        :return: The updated card resource.
        """
        pass

    async def delete_card(self, card_id: str) -> bool:
        """
        Deletes an existing card resource identified by the supplied `card_id`.

        :param card_id: The unique identifier of the card to be deleted.
        :return: A boolean indicating whether the card was successfully deleted or not.
        """
        pass

    async def get_all_cards(self) -> List[Card]:
        """
        Retrieves all card resources.

        :return: A list of all card resources.
        """
        pass
