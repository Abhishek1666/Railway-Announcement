from sys import platform
from tkinter import*
from tkinter import font
from tkinter.font import BOLD
import pymysql
from tkinter import ttk, messagebox
from gtts import gTTS
import os
import random
import time
from playsound import playsound
import pygame
# from pythonFiles import normalTrainArriving
# from pythonFiles import normalTrainDeparting


# def clear(trainnumber, trainname,source1,destination1,upOrDown,platformNumber):
#     trainnumber.delete(0, END),
#     trainname.delete(0, END),
#     source1.delete(0, END),
#     destination1.delete(0, END)
#     upOrDown.delete(0, END)
#     platformNumber.delete(0, END)

pygame.mixer.init()
def plays(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)

def Intro():
    playsound('C:\\Users\Abhishek\\OneDrive\Desktop\\Railway Announcement\\Introduction.mp3')

    

def getvals(trainnumber,trainname, source1, destination1):
        if trainnumber == "" or trainname == "" or source1 == "" or destination1 == "":
            messagebox.showerror("error", "All Fields are blank")
        else:
            try:
            
                con = pymysql.connect(host="localhost", user="root",
                                  password="", database="train announcement system")
                cur = con.cursor()
                cur.execute("insert into train(train_no,train_name,source,destination) values(%s,%s,%s,%s)", (

                trainnumber,
                trainname,
                source1 ,
                destination1

            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Train Detail Saved Successfully")
                

            except Exception as e:
                messagebox.showerror(f"Error due to:{str(e)} ")
                print(f"Error due to:{str(e)} ")  
            # clear(train_number,train_names,source,destination,upOrDown,platformNumber)                   



def GenerateEnglishAnnounvement(SelectedLang, train_number, train_names, source, destination, upOrDown,platformNumber, categories):
    if(categories=="Arriving"):

           

        langCode='en-in'
        mainText="Please pay attaintion, Train number "+train_number+", "+upOrDown+","+source+","+destination+" ,"+train_names+", is arriving on  platform number "+platformNumber+"."
             
       
            
    else:
            langCode='en-in'
            mainText="Please pay attaintion, Train number "+train_number+", "+upOrDown+", "+train_names+", is departing from platform number "+platformNumber+"."
           
            
             
    output=gTTS(text=mainText,lang=langCode,slow=False)      
    path="C:\\Users\\Abhishek\OneDrive\\Desktop\\Railway Announcement\\sounds"
    output.save(path+"SecondPart.mp3")  
    # playsound('C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\soundsSecondPart.mp3') 
    plays('C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\soundsSecondPart.mp3')   
        
      
 
    con = pymysql.connect(host="localhost", user="root",
                                  password="", database="train announcement system")
    cur = con.cursor()
    cur.execute("truncate table train")
    con.commit()
    con.close()

def GenerateHindiAnnounvement(SelectedLang, train_number, train_names, source, destination, upOrDown,platformNumber, categories):
    if(categories=="Arriving"):


            
            
        langCode='hi'
           

            
        mainText="कृपया सुनिए, ट्रेन नंबर "+train_number+", "+ upOrDown +" "+train_names+ ", प्लेटफॉर्म नंबर " +platformNumber+" आ रही है।"    
       
            
    else:
            
            
            langCode='hi'
           

            
            mainText="कृपया सुनिए, ट्रेन नंबर "+train_number+", "+ upOrDown +" "+train_names+ ", प्लेटफॉर्म नंबर " +platformNumber+" आ रह है।"
          
       
        
    output=gTTS(text=mainText,lang=langCode,slow=False)
    path="C:\\Users\\Abhishek\OneDrive\\Desktop\\Railway Announcement\\sounds"
    output.save(path+"SecondPart2.mp3")  
    # playsound('C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\soundsSecondPart2.mp3')   
    plays('C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\soundsSecondPart2.mp3') 
 
    con = pymysql.connect(host="localhost", user="root",
                                  password="", database="train announcement system")
    cur = con.cursor()
    cur.execute("truncate table train")
    con.commit()
    con.close()

def GenerateMalayalamAnnounvement(SelectedLang, train_number, train_names, source, destination, upOrDown,platformNumber, categories):
    if(categories=="Arriving"):

           
        langCode='ml'
            

         
        mainText="യാത്രക്കാരുടെ   ശ്രദ്ധയ്ക്ക് , "+train_number+", "+source+", നിന്നും , "+destination+", വരെ പോകുന്ന , "+train_names+","+platformNumber+", നാമത്തെ പ്ലാറ്റഫോമിൽ എത്തുന്നു  "
            
    elif(categories=="Arrived") :
        langCode='ml'
            

         
        mainText="യാത്രക്കാരുടെ   ശ്രദ്ധയ്ക്ക് , "+train_number+", "+source+", നിന്നും , "+destination+", വരെ പോകുന്ന , "+train_names+"  ,  "+platformNumber+", നാമത്തെ  പ്ലാറ്റഫോമിൽ  എത്തിച്ചേർന്നിരിക്കുന്നു   "
         
            
    else:
            
            langCode='ml'
            

             
             
            mainText="യാത്രക്കാരുടെ   ശ്രദ്ധയ്ക്ക് , "+train_number+", "+source+", നിന്നും , "+destination+", വരെ പോകുന്ന , "+train_names+","+platformNumber+", നാമത്തെ പ്ലാറ്റഫോമിൽനിന്നും  പുറപ്പിടും    "
             
    output=gTTS(text=mainText,lang=langCode,slow=False)
    path="C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\sounds"
    output.save(path+"SecondPart1.mp3")  
    # playsound('C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\soundsSecondPart1.mp3')     
       
    
    plays('C:\\Users\\Abhishek\\OneDrive\\Desktop\\Railway Announcement\\soundsSecondPart1.mp3') 
            
          
       
        
      
 
    con = pymysql.connect(host="localhost", user="root",
                                  password="", database="train announcement system")
    cur = con.cursor()
    cur.execute("truncate table train")
    con.commit()
    con.close() 
    # clear()     
        

        

def main():

    root = Tk()
    root.geometry("1300x700")
    root.title("Indian Railway Announcement")
    Label(root, text="Train Detail", font=("times new Roman", "14", "bold")).pack()
    frame1 = LabelFrame(root, padx=10, pady=10)
    frame1.pack(padx=50, pady=25)
        # Label(frame1, text="Train Detail", font="comicsansms 14 bold").grid(row=0, column=3)
    train_no = Label(frame1, text="train_no")
    train_name = Label(frame1, text="train_name")
    train_source = Label(frame1, text="train_source")
    train_destination = Label(frame1, text="train_destination")
    upOrDown = Label(frame1, text="upOrDown")
    platform_number = Label(frame1, text="platform_number")

    train_no.grid(row=1, column=2)
    train_name.grid(row=2, column=2)
    train_source.grid(row=3, column=2)
    train_destination.grid(row=4, column=2)
    upOrDown.grid(row=5,column=2)
    platform_number.grid(row=6,column=2)

    train_no_value = IntVar()
    train_name_value = StringVar()
    train_source_value = StringVar()
    train_destination_value = StringVar()
    upOrDown_value = StringVar()
    platform_number = IntVar()

    trainnumberentry = Entry(frame1, textvariable=train_no_value)
    trainnameentry = Entry(frame1, textvariable=train_name_value)
    trainsourceentry = Entry(frame1, textvariable=train_source_value)
    traindestinationentry = Entry(frame1, textvariable=train_destination_value)
    upOrDownentry = Entry(frame1, textvariable=upOrDown_value)
    platformnumberentry = Entry(frame1,textvariable=platform_number)

    trainnumberentry.grid(row=1, column=3)
    trainnameentry.grid(row=2, column=3)
    trainsourceentry.grid(row=3, column=3)
    traindestinationentry.grid(row=4, column=3)
    upOrDownentry.grid(row=5,column=3)
    platformnumberentry.grid(row=6,column=3)
    Button(frame1, text="Submit",command=lambda:getvals(trainnumberentry.get(), trainnameentry.get(),trainsourceentry.get(),traindestinationentry.get())).grid(row=7, column=3)
   
    categoryDes = "Category Of The Train"
    label4 = Label(root, text=categoryDes)
    label4.pack(pady=(0, 5))

    categories = StringVar()
    categories.set("Departing")
    dropMenu = OptionMenu(root, categories, "Arriving", "Departing","Arrived")
    dropMenu.pack(pady=(0, 15))
    
    
    frame2 = LabelFrame(root, text="Select The Language", padx=10, pady=10)
    frame2.pack(padx=50, pady=25)
    l = IntVar()
    l.set("3")
    Radiobutton(frame2, text="Malayalam", variable=l, value=1).pack()
    Radiobutton(frame2, text="Hindi", variable=l, value=2).pack()
    Radiobutton(frame2, text="Indian-English", variable=l, value=3).pack()
    # frame3 = LabelFrame(root, padx=10, pady=10)
    Button(root, text="Generate English Announcement",
            command=lambda: GenerateEnglishAnnounvement(l.get(), trainnumberentry.get(), trainnameentry.get(), trainsourceentry.get(), traindestinationentry.get(),upOrDownentry.get(),platformnumberentry.get(),categories.get())).pack(padx=10,pady=20)
    Button(root, text="Generate Hindi Announcement",
            command=lambda: GenerateHindiAnnounvement(l.get(), trainnumberentry.get(), trainnameentry.get(), trainsourceentry.get(), traindestinationentry.get(),upOrDownentry.get(),platformnumberentry.get(),categories.get())).pack(padx=10,pady=20)        
    Button(root, text="Generate Malayalam Announcement",
            command=lambda: GenerateMalayalamAnnounvement(l.get(), trainnumberentry.get(), trainnameentry.get(), trainsourceentry.get(), traindestinationentry.get(),upOrDownentry.get(),platformnumberentry.get(),categories.get())).pack(padx=10,pady=20)
    Button(root,text="Intro",command=lambda:Intro()).pack()


    root.mainloop()
    

    # Button(root,text="Play",command=)

if __name__=="__main__":
    main()
