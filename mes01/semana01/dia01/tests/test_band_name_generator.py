import pytest

from mes01.semana01.dia01.band_name_generator import band_name_generator

def test_band_name_generator():
    city = 'Botucatu'
    pet_name = 'Lili'
    result = band_name_generator(city, pet_name)
    assert result == 'Botucatu Lili'
