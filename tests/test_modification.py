from shadow.polyedr import Polyedr
from pytest import approx


def test_modification_1():
    polyedr = Polyedr("data/ccc_for_test.geom")
    assert polyedr.count_characteristic(True) == approx(9.0)


def test_modification_2():
    polyedr = Polyedr("data/box_for_test.geom")
    assert polyedr.count_characteristic(True) == approx(9.0)
