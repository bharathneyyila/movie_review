def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total = sum([r["rating"] for r in reviews])
    return round(total / len(reviews), 2)
