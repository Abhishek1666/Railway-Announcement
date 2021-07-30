from tkinter import *
from tkinter import  messagebox
import sys
# sys.path.append("C:/Users/surde/OneDrive/Desktop/Indian Railway Announcement Project/FinalProject/")
from pythonFiles import goingToNormalTrainMainPage
from pythonFiles import announcement

def deleteAll(root):
    list=root.pack_slaves()
    for l in list:
        l.pack_forget()

def backButtonClicked(root,SelectedLang):
    goingToNormalTrainMainPage.main(root,SelectedLang)

def create(root,SelectedLang,train_number,train_names,upOrDown):
    
        announcement.arrivingTrain(SelectedLang,train_number,train_names,upOrDown)

def main(root,SelectedLang,train_number,train_names,upOrDown):
    deleteAll(root)
    root.title("Normal Train Sub-settings")
    backButton=Button(root,text='<< Back',command=lambda:backButtonClicked(root,SelectedLang))
    backButton.pack(pady=(15,100))

    global platformNo
    platformNo=Entry(root,borderwidth=5)
    platformNo.pack(pady=(0,10))
    des="Enter Platform Number Where The Train Is Going To Arrive"
    label0=Label(root,text=des)
    label0.pack(pady=(0,115))

    createButton=Button(root,text="Create The Announcement",command=lambda:create(root,SelectedLang,train_number,train_names,upOrDown,platformNo.get()))
    createButton.pack()

if __name__=="__main__":
    main(root,SelectedLang,train_number,train_names,upOrDown)