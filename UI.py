# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import tkinter as tk
import controller

class UIMaker(tk.Frame):
    def __init__(self, master=None, money=0):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x500+100+100")
        self.master.resizable(False,False)
        self.pack()
        self.money= money
        self.input = input
        self.render()
        

    def render(self):
        
        self.label = tk.Label(self)
        self.label.config(text="현재 금액 = "+str(self.money))
        self.label.pack(side = "top" )      
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        self.button = tk.Button(self)
        self.button["text"] = "입력"
        self.button["command"] = self.enterAmount
        self.button.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def enterAmount(self):
        self.input = int(self.entry.get())
        self.label.config(text="충전 금액 = "+str(self.input))
        controller.getBalanceRequest(input)

    def event(self):
        self.render(self)


root = tk.Tk()
InterfacePage = UIMaker(master=root)
InterfacePage.mainloop()