import pytest
from fetch_data import url_validator,check_save_images, count_images_url

def test_url_validator():
    assert url_validator('http://google.com') == True

def test_check_save_images():
    assert check_save_images('test_images') == 1

def test_count_images_url():
    images_url = ['https://www.cheatsheet.com/wp-content/uploads/2019/04/Planet-Earth-640x431.jpg','http://pragatiresorts.com/wp-content/uploads/2018/10/Nature-walk-1.jpg']
    assert count_images_url(images_url) == 2

