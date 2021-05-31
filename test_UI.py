# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:39:36 2021

@author: 정훈석
"""
from controller import *

def test_interface_input():
    data_put=["1000","123","0","2000","3000","12asd",""]
    data_in=[1000,123,0,2000,3000,0,0]
    
    controller = Controller(userID="a")
    controller.Page.test_flg=2
    controller.Page.start()
    
    print(controller.Page.input)
    for i in range(len(data_put)):
        money_before=controller.money.amount
        
        controller.Page.test(data_put[i])
        assert controller.Page.input==data_in[i]
        
        money_after=money_before+data_in[i]
        
        assert controller.money.amount==money_after
        