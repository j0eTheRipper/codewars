from main import rgb, separate_hex


def test_code_separator():
    assert separate_hex('#ffabdd') == ['ff', 'ab', 'dd']
