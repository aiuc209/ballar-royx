import pytest

def normalize_scores(scores):
    return [score / 10 for score in scores]

@pytest.mark.parametrize("scores, expected", [
    ([100, 200, 300], [10, 20, 30]),
    ([0, 500, 1000], [0, 50, 100]),
    ([10, 20, 30], [1, 2, 3]),
])
def test_normalize_scores(scores, expected):
    assert normalize_scores(scores) == expected

def test_normalize_scores_empty_list():
    assert normalize_scores([]) == []

def test_normalize_scores_single_element():
    assert normalize_scores([100]) == [10]
