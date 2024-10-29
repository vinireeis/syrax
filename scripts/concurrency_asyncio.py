import asyncio
from time import sleep

import httpx

accounts_url = "http://localhost:8015/syrax-bank/accounts"
deposit_url = "http://localhost:8015/syrax-bank/accounts/{account_id}/deposit"
withdraw_url = "http://localhost:8015/syrax-bank/accounts/{account_id}/withdraw"
transfer_url = "http://localhost:8015/syrax-bank/accounts/{account_id}/transfer"
get_transactions_url = (
    "http://localhost:8015/syrax-bank/accounts/{account_id}/transactions"
)

account_id_123 = "46f793c8-78ad-48ce-98ab-1aa09b5cc0d2"  # 123
account_id_456 = "84123974-58c1-44b8-a69a-c9086d87e765"  # 456
account_id_789 = "4dd6889d-cf50-43a9-a0bd-bec0582f7483"  # 789


async def http_client_post_result(url, body) -> dict:
    async with httpx.AsyncClient() as async_client:
        response = await async_client.post(url, params=body)
        result = response.json()
        print(result)
        return result

async def http_client_get_result(url) -> dict:
    async with httpx.AsyncClient() as async_client:
        response = await async_client.get(url)
        result = response.json()
        return result


async def first_step(account_id_123: str):
    d_url = deposit_url.format(account_id=account_id_123)
    d_body = {"amount": 100}
    await http_client_post_result(url=d_url, body=d_body)


async def second_step(account_id_123: str):
    w_url = withdraw_url.format(account_id=account_id_123)
    w_body = {"amount": 50}
    await http_client_post_result(w_url, w_body)


async def third_step(account_id_123: str, account_id_456: str):
    t_url = transfer_url.format(account_id=account_id_123)
    t_body = {"amount": 30, "target_account_id": account_id_456}
    await http_client_post_result(t_url, t_body)


async def fourth_step(account_id_123: str):
    d_url = deposit_url.format(account_id=account_id_123)
    d_body = {"amount": 50}
    w_url = withdraw_url.format(account_id=account_id_123)
    w_body = {"amount": 30}

    tasks = asyncio.gather(
        http_client_post_result(url=d_url, body=d_body),
        http_client_post_result(url=w_url, body=w_body),
    )
    await tasks


async def fifth_step(account_id_123: str, account_id_456: str):
    d_url = deposit_url.format(account_id=account_id_123)
    d_body = {"amount": 100}
    t_url = transfer_url.format(account_id=account_id_123)
    t_body = {"amount": 50, "target_account_id": account_id_456}

    tasks = asyncio.gather(
        *[
            http_client_post_result(url=d_url, body=d_body),
            http_client_post_result(url=t_url, body=t_body),
        ]
    )
    await tasks


async def sixth_step(account_id_123: str, account_id_456: str, account_id_789: str):
    t_url = transfer_url.format(account_id=account_id_123)
    t_body = {"amount": 20, "target_account_id": account_id_456}

    second_transfer_url = transfer_url.format(account_id=account_id_456)
    second_transfer_body = {"amount": 10, "target_account_id": account_id_789}

    tasks = asyncio.gather(
        http_client_post_result(url=t_url, body=t_body),
        http_client_post_result(url=second_transfer_url, body=second_transfer_body),
    )
    await tasks

async def list_accounts():
    result = await http_client_get_result(url=accounts_url)
    for account in result["payload"]:
        print(account["account_id"], account["balance"])


async def main(account_id_123: str, account_id_456: str, account_id_789: str):
    await first_step(account_id_123=account_id_123)
    await list_accounts()
    sleep(0.5)
    await second_step(account_id_123=account_id_123)
    await list_accounts()
    sleep(0.5)
    await third_step(account_id_123=account_id_123, account_id_456=account_id_456)
    await list_accounts()
    sleep(0.5)
    await fourth_step(account_id_123=account_id_123)
    await list_accounts()
    sleep(0.5)
    await fifth_step(account_id_123=account_id_123, account_id_456=account_id_456)
    await list_accounts()
    sleep(0.5)
    await sixth_step(
        account_id_123=account_id_123,
        account_id_456=account_id_456,
        account_id_789=account_id_789,
    )
    sleep(0.3)
    await list_accounts()


if __name__ == "__main__":
    asyncio.run(main(account_id_123, account_id_456, account_id_789))
