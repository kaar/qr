from .qr import decode_image


def test_decode_image():
    assert (
        decode_image("./data/image.png")
        == "WIFI:S:Alpaca Guest;T:WPA;P:tyhjuz-dypjy3-Ciskow;;"
    )
