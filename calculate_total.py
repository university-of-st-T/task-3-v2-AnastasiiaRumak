def calculate_total(prices, *discounts, **options):
    tax = options.get('tax', 0)
    round_to = options.get('round_to', 2)

    total = sum(prices)

    for discount in discounts:
        total *= (1 - discount / 100)

    total *= (1 + tax / 100)

    if round_to is not None:
        total = round(total, round_to)

    return total
