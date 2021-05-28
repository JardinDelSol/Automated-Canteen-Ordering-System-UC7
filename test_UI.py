# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:39:36 2021

@author: 정훈석
"""
from controller import *

def test_interface_input():
    data=["1000","123","0","2000","3000"]
    
    controller = Controller(userID="a")
    controller.Page.test_flg=2
    controller.Page.start()
    controller.money
    print(controller.Page.input)
    for i in data:
        money_before=controller.money.amount
        controller.Page.test(i)
        assert controller.Page.input==int(i)
        money_after=money_before+int(i)
        assert controller.money.amount==money_after
        