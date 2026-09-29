"""A tiny validation pipeline for tabular records."""


def clean_records(records: list[dict]) -> list[dict]:
    cleaned = []
    for record in records:
        name = str(record.get('name', '')).strip()
        score = record.get('score')
        if not name or not isinstance(score, (int, float)) or not 0 <= score <= 100:
            continue
        cleaned.append({'name': name, 'score': float(score)})
    return cleaned


def average_score(records: list[dict]) -> float | None:
    scores = [record['score'] for record in clean_records(records)]
    return round(sum(scores) / len(scores), 2) if scores else None


if __name__ == '__main__':
    rows = [{'name': ' A ', 'score': 82}, {'name': 'B', 'score': 104}, {'name': 'C', 'score': 91}]
    print(clean_records(rows))
    print('average:', average_score(rows))
