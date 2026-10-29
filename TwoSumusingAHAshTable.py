
def two_sum(prices, target):
    seen = {}

    for i, price in enumerate(prices):
        needed = target - price

        if needed in seen:
            return [seen[needed], i]

        seen[price] = i

    return []


prices = [2, 7, 11, 15]
target = 9
print(two_sum(prices, target))
