import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    # Використовує жадібний алгоритм для знаходження монет
    result = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    # Використовує алгоритм динамічного програмування для знаходження мінімальної кількості монет
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    last_coin = [None] * (amount + 1)

    for coin in COINS:
        for value in range(coin, amount + 1):
            if dp[value - coin] + 1 < dp[value]:
                dp[value] = dp[value - coin] + 1
                last_coin[value] = coin

    result = {}
    current = amount

    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


def benchmark():
    # Порівняння продуктивності двох алгоритмів
    amount = 113
    runs = 10_000

    greedy_time = timeit.timeit(
        stmt=lambda: find_coins_greedy(amount),
        number=runs,
    )

    dp_time = timeit.timeit(
        stmt=lambda: find_min_coins(amount),
        number=runs,
    )

    print("=== Результати алгоритмів ===")
    print("Жадібний:", find_coins_greedy(amount))
    print("Динамічне програмування:", find_min_coins(amount))

    print(f"\n=== Продуктивність ({runs:,} запусків) ===")
    print(f"Жадібний алгоритм: {greedy_time:.6f} сек")
    print(f"Динамічне програмування: {dp_time:.6f} сек")


if __name__ == "__main__":
    benchmark()
