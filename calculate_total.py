def calculate_total(prices, *discounts, **options):
    tax = options.get('tax', 0)
    round_to = options.get('round_to', 2)

    total = float(sum(prices))

    for discount in discounts:
        total *= (1 - discount / 100.0)

    total *= (1 + tax / 100.0)

    if round_to is not None:
        total = round(total, round_to)

    return total
