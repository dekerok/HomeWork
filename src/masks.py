from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция маскирует номера банковской карты"""
    private_num = card_num[:6] + (len(card_num[6:-4]) * "*") + card_num[-4:]

    chunks, chunk_size = len(private_num), len(private_num) // 4
    return " ".join([private_num[i : i + chunk_size] for i in range(0, chunks, chunk_size)])


def get_mask_account(bank_account: Union[str]) -> Union[str]:
    """Функция маскирует номера банковского счета"""
    private_num = (len(bank_account[-6:-4]) * "*") + bank_account[-4:]
    return private_num
