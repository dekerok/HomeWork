from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция маскирует номера банковской карты"""
    private_num = card_num[0:-12] + " " + card_num[-12:-10] + "** **** " + card_num[-4:]
    return private_num


def get_mask_account(bank_account: Union[str]) -> Union[str]:
    """Функция маскирует номера банковского счета"""
    private_account = bank_account[:4] + " " + "**" + bank_account[-4:]
    return private_account
