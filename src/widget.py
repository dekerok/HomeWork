from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_bank_input: Union[str]) -> Union[str]:
    """Функция принимает от пользователя информацию
    определяет номер или счет"""
    card_or_account = user_bank_input.split()[-1]
    if len(card_or_account) <= 16:
        return get_mask_card_number(user_bank_input)
    else:
        return get_mask_account(user_bank_input)


def get_date(date_info: Union[str]) -> Union[str]:
    '''Функция которая принимает на вход строку
         и отдает корректный результат в формате
    "ДД.ММ.ГГГГ"'''
    only_date = date_info.split("T")[0]
    year, month, day = only_date.split("-")
    return f"{day}.{month}.{year}"
