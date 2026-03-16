from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_parse_guess_rejects_decimal():
    ok, value, err = parse_guess("10.5")
    assert not ok
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_accepts_integer():
    ok, value, err = parse_guess("55")
    assert ok
    assert value == 55
    assert err is None

def test_range_for_hard_is_larger_than_normal():
    easy_range = get_range_for_difficulty("Easy")
    normal_range = get_range_for_difficulty("Normal")
    hard_range = get_range_for_difficulty("Hard")
    assert easy_range[1] < normal_range[1]
    assert normal_range[1] < hard_range[1]
