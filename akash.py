from base64 import b64decode
import requests


def get_transactions(number_block):
    url = f'https://akash-api.w3coins.io/blocks/{number_block}'
    response = requests.get(url)
    data_list = response.json()['block']['data']['txs']

    if data_list is None:
        print(f"В блоке {number_block} транзакции не найдены")
        return

    for index, data in enumerate(data_list, start=1):
        decoded_data = b64decode(data)
        print(f"{index} транзакция в блоке {number_block}:")
        print(decoded_data)
        print("=" * 30)


get_transactions(11260637)
