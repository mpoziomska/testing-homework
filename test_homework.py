# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 01:08:35 2021

@author: mpozi
"""

from homework import calculate, take_from_list

import pytest
from py.error import EEXIST

def test_take_from_list():
    li = list(range(10))
    assert take_from_list(li, []) == []
    assert take_from_list([], []) == []
    assert take_from_list(li, li) == li
    assert take_from_list(li, 5) == [li[5]]
    
    with pytest.raises(ValueError):
        take_from_list(li, [0.2])
        take_from_list(li, [0.2] + [1] * 5)
        
        
    with pytest.raises(IndexError):
        take_from_list(li, [11])
        take_from_list(li, [11] + [1] * 5)
    
def test_calculte(tmpdir):
    calculate('input.json', (tmpdir / 'test'))
    with pytest.raises(EEXIST):
        (tmpdir / "test").mkdir()

    