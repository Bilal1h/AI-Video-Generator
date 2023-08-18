from tkinter import *
import random
from gtts import gTTS
from moviepy.editor import *
import os
import tkinter.ttk as ttk
import pyautogui as pg
import tkinter.messagebox as tmsg
from mutagen.mp3 import MP3

def generate():
    category_val = category.get()
    topic_val = topic.get()
    script_val = script.get(1.0,END)
    templates = ["f1.mp4","f2.mp4","f3.mp4","f4.mp4","f5.mp4","f6.mp4","f7.mp4","f8.mp4","f9.mp4","f10.mp4","f11.mp4"]
    random_temp = random.choice(templates)
    topic_split = topic_val.split()
    script_split = script_val.split(",")
    scripts = script_split[0].split()
    scriptss = script_split[1].split()
    scriptsss = script_split[2].split()
    scriptssss = script_split[3].split()
    clip_1_voice = gTTS(topic_val)
    clip_1_voice.save("Assests/Voices/clip_1_voice.mp3")
    clip_2_voice = gTTS(f"{script_split[0]}")
    clip_2_voice.save("Assests/Voices/clip_2_voice.mp3")
    clip_3_voice = gTTS(script_split[1])
    clip_3_voice.save("Assests/Voices/clip_3_voice.mp3")
    clip_4_voice = gTTS(script_split[2])
    clip_4_voice.save("Assests/Voices/clip_4_voice.mp3")
    clip_5_voice = gTTS(script_split[3])
    clip_5_voice.save("Assests/Voices/clip_5_voice.mp3")
    def audio_duration(length):
        hours = length // 3600  # calculate in hours
        length %= 3600
        mins = length // 60  # calculate in minutes
        length %= 60
        seconds = length  # calculate in seconds
    
        return hours, mins, seconds  # returns the duration
    

    audio = MP3("Assests/Voices/clip_1_voice.mp3")
    audio_info = audio.info
    length = int(audio_info.length)
    hours, mins, seconds = audio_duration(length)

    audio2 = MP3("Assests/Voices/clip_2_voice.mp3")
    audio2_info = audio2.info
    length2 = int(audio2_info.length)
    hours, mins, seconds2 = audio_duration(length2)

    audio3 = MP3("Assests/Voices/clip_3_voice.mp3")
    audio3_info = audio3.info
    length3 = int(audio3_info.length)
    hours, mins, seconds3 = audio_duration(length3)


    audio4 = MP3("Assests/Voices/clip_4_voice.mp3")
    audio4_info = audio4.info
    length4 = int(audio4_info.length)
    hours, mins, seconds4 = audio_duration(length4)

    audio5 = MP3("Assests/Voices/clip_5_voice.mp3")
    audio5_info = audio5.info
    length5 = int(audio5_info.length)
    hours, mins, seconds5 = audio_duration(length5)

    # print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
    def listToString(s):
    
        return ' '.join([str(elem) for i,elem in enumerate(s)])
    clip_1 = VideoFileClip(f"Assests/{category_val}/{random_temp}").subclip(00,seconds)
    clip_2 = VideoFileClip(f"Assests/{category_val}/{random_temp}").subclip(00,seconds2)
    clip_3 = VideoFileClip(f"Assests/{category_val}/{random_temp}").subclip(00,seconds3)
    clip_4 = VideoFileClip(f"Assests/{category_val}/{random_temp}").subclip(00,seconds4)
    clip_5 = VideoFileClip(f"Assests/{category_val}/{random_temp}").subclip(00,seconds5)

    clip_1voice= AudioFileClip("Assests/Voices/clip_1_voice.mp3")
    clip_1= clip_1.set_audio(clip_1voice)
    txt_clip_1 = TextClip(f"{listToString(topic_split[0:4])}\n{listToString(topic_split[5:])}",fontsize=30,color="white",bg_color="black")
    txt_clip_1 = txt_clip_1.set_position("center").set_duration(seconds)


    clip_2voice= AudioFileClip("Assests/Voices/clip_2_voice.mp3")
    clip_2= clip_2.set_audio(clip_2voice)
    txt_clip_2 = TextClip(f"{listToString(scripts[0:6])}\n{listToString(scripts[6:])}",fontsize=30,color="white",bg_color="black")
    txt_clip_2 = txt_clip_2.set_position("center").set_duration(seconds2)



    clip_3voice= AudioFileClip("Assests/Voices/clip_3_voice.mp3")
    clip_3= clip_3.set_audio(clip_3voice)
    txt_clip_3 = TextClip(f"{listToString(scriptss[0:6])}\n{listToString(scriptss[6:])}",fontsize=30,color="white",bg_color="black")
    txt_clip_3 = txt_clip_3.set_position("center").set_duration(seconds3)




    clip_4voice= AudioFileClip("Assests/Voices/clip_4_voice.mp3")
    clip_4= clip_4.set_audio(clip_4voice)

    txt_clip_4 = TextClip(f"{listToString(scriptsss[0:6])}\n{listToString(scriptsss[6:])}",fontsize=30,color="white",bg_color="black")
    txt_clip_4 = txt_clip_4.set_position("center").set_duration(seconds4)



    clip_5voice= AudioFileClip("Assests/Voices/clip_5_voice.mp3")
    clip_5= clip_5.set_audio(clip_5voice)

    txt_clip_5 = TextClip(f"{listToString(scriptssss[0:6])}\n{listToString(scriptssss[6:])}",fontsize=30,color="white",bg_color="black")
    txt_clip_5 = txt_clip_5.set_position("center").set_duration(seconds5)

    clip1 = CompositeVideoClip([clip_1,txt_clip_1])
    clip2 = CompositeVideoClip([clip_2,txt_clip_2])
    clip3 = CompositeVideoClip([clip_3,txt_clip_3])
    clip4 = CompositeVideoClip([clip_4,txt_clip_4])
    clip5 = CompositeVideoClip([clip_5,txt_clip_5])
    final_video = concatenate_videoclips([clip1,clip2,clip3,clip4,clip5])
    name = pg.prompt("Enter your video's name to save.")
    final_video.write_videofile(f"Outputs/{name}.mp4")
    tmsg.showinfo("Success","Your Video has been generated in the Ouputs folder")



def get_started():
    global category
    global topic
    global script

    home_frame.destroy()
    mode_frame=Frame(root,bg="#ffffff")
    mode_frame.pack()
    l1 = Label(mode_frame,text="Fill out these details",font=("Nexa",40,"bold"),bg="#ffffff",fg="#4A4A4A")
    l1.pack(pady=50)

    # category box
    # main work goes form here  
    category_label =  Label(mode_frame,text="Choose a category",font="Nexa 10",bg="#ffffff",fg="#4a4a4a")
    category_label.pack(padx=10,pady=5)
    category = ttk.Combobox(mode_frame,values=["Technology","Cooking","Travel","Enviroment","Arts"],font=("Nexa",15,"bold"),background="#ffffff",foreground="#4A4A4A") 
    category.pack(padx=10,pady=5)
    # topic content
    topic_label =  Label(mode_frame,text="Enter your video's topic",font="Nexa 10",bg="#ffffff",fg="#4a4a4a")
    topic_label.pack(padx=10,pady=5)
    topic = Entry(mode_frame,font=("Nexa",15,"bold"),bg="#ffffff",fg="#4A4A4A",highlightthickness=5,highlightcolor="#4a4a4a") 
    topic.pack(padx=10,pady=5)
    # script content
    script_label =  Label(mode_frame,text="Enter your video's script (Max 100 words) (seperate each line by using a comma)",font="Nexa 10",bg="#ffffff",fg="#4a4a4a")
    script_label.pack(padx=10,pady=5)
    script = Text(mode_frame,font=("Nexa",15,"bold"),bg="#ffffff",fg="#4A4A4A",highlightthickness=5,highlightcolor="#4a4a4a",width=50,height=10) 
    script.pack(padx=10,pady=5)

    generate_but = Button(mode_frame,text="Generate",font=("Nexa",30,"bold"),fg="#ffffff",bg="#151515",relief=FLAT,command=generate)
    generate_but.pack(padx=10,pady=10)


    

root=Tk()
root.state("zoomed")
root.title("ClipCraft - AI Video Generator")
root.resizable(0,0)
root.wm_iconbitmap("Assests/creative-commons.ico")
root.config(bg="#ffffff")
home_frame= Frame(root,bg="#ffffff")
home_frame.pack()
# Label(home_frame,text="Generate your own Video\nin under 2 minutes",font=("Nexa",40,"bold"),bg="#ffffff",fg="#4A4A4A").pack(pady=50)
# Label(home_frame,text="Free | Forever",font=("Nexa",40,"bold"),bg="#ffffff",fg="#000000").pack(pady=30)

# Label(home_frame,text="No Signup Required",font="Roboto 10",bg="#ffffff",fg="#A9A9A9").pack(pady=2)

path = os.getcwd()
img = PhotoImage(file=f"{path}/Assests/Home.png")

l1 = Label(home_frame,image=img)
l1.pack()
b1 = Button(home_frame,text="Get Started",font=("Nexa",40,"bold"),fg="#ffffff",bg="#151515",relief=FLAT,command=get_started)
b1.place(x=65,y=530)




root.mainloop()
