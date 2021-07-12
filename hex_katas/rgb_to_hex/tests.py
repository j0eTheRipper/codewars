from main import rgb


def test_zero_values(): assert rgb(0, 0, 0), "000000"


def test_near_zero_values(): assert rgb(1, 2, 3), "010203"


def test_max_values(): assert rgb(255, 255, 255), "FFFFFF"


def test_near_max(): assert rgb(254, 253, 252), "FEFDFC"


def test_out_of_range(): assert rgb(-20, 275, 125), "00FF7D"
