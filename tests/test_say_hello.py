# -*- coding: utf-8 -*-
import thaipackage


def test_say_hello():
    try:
        thaipackage.main.say_hello()
        assert True
    except Exception as e:
        print(e)
        assert False
