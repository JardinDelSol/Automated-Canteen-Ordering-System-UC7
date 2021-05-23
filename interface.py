# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import tkinter as tk


class InterfacePage(tk.Frame):
    def __init__(self,controller,money):
        self.root=tk.Tk()
        super().__init__(self.root)
        self.controller=controller
        self.input = 0
        self.money = money
        
        self.label = tk.Label(self)
        self.label.config(text="현재 금액 = " + str(self.money.amount))
        
        self.entry = tk.Entry(self)
        
        self.button = tk.Button(self)
        self.button["text"] = "입력"
        self.button["command"] = self.enterAmount
        
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        
        self.flg=1
         
    def enterAmount(self):
        self.input = int(self.entry.get())
        self.label.config(text="충전 금액 = " + str(self.input))
        self.flg=0
        self.controller.getReloadAmount(self.input)
    

    def display(self):
         while(self.flg):
             self.update_idletasks()
             self.update()
         self.flg=1
         print("OK")
         
    def event(self):
        self.display()
    
        
        

class UIMaker:
    def __init__(self, Page:InterfacePage):
        self.Page = Page
        self.setPage()
        
    def setPage(self):
        self.Page.root.geometry("300x500+100+100")
        self.Page.root.resizable(False, False)
        self.Page.pack()
        self.Page.label.pack(side="top")
        self.Page.entry.pack()
        self.Page.button.pack(side="top")
        self.Page.quit.pack(side="bottom")

    def render(self):
        self.Page.label.config(text="현재 금액 = " + str(self.Page.money.amount))
        
    def event(self):
        self.render()

