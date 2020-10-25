# -*- coding: utf-8 -*-
import thaipackage


def test_blank_package():
    my_str = "minhng.info"
    rev_str = thaipackage.reverse(my_str)
    assert rev_str == "ofni.gnhnim"
