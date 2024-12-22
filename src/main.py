from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":

    """вызов функций по домашке 9.1"""
    user_card_number = input("Введите номер карты: ")
    print(get_mask_card_number(user_card_number))

    user_account_number = input("Введите номер счета: ")
    print(get_mask_account(user_account_number))

    """вызов функций по домашке 9.2"""
    user_bank_input = input("Введите номер счета или карты: ")
    print(mask_account_card(user_bank_input))

    print(get_date("2024-03-11T02:26:18.671407"))

# изменения
