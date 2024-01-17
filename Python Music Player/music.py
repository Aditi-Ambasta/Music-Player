from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        
import os

mixer.init()

root = Tk()
root.geometry('400x570')
root.title('MUSIC MINGLE!')
root.resizable(0, 0)

# Play, Stop, Load and Pause & Resume functions
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")


def load(listbox):
    directory = filedialog.askdirectory(title='Open a songs directory')
    os.chdir(directory)

    tracks = os.listdir()

    for track in tracks:
        if track.endswith(".mp3"):
            listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

# frames
song_frame = LabelFrame(root, text='Current Song', font=('MS Sans Serif',11,'bold'), bg='Black',fg='White', width=400, height=100)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons',bg='Black', fg='White',font=('MS Sans Serif',11,'bold'), width=400, height=140)
button_frame.place(x=0,y=100)

listbox_frame = LabelFrame(root, text='Playlist',  bg='Black',fg='White',font=('MS Sans Serif',11,'bold'))
listbox_frame.place(x=0, y=240, height=310, width=400)

# StringVar variables
current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Not Available>')

# Playlist ListBox
playlist = Listbox(listbox_frame, font=('MS Sans Serif',12,'bold'), selectbackground='Gold',selectforeground='Black',height=15, bg='black',fg='springgreen',cursor="heart")

Label(listbox_frame,text='SONG LIST: ',font=('MS Sans Serif',12,'bold'),bg='black',fg='springgreen',justify=LEFT).pack(side=TOP, fill=X)

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=10, pady=10)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', font=('MS Sans Serif',13,'bold'), bg='Black',fg='springgreen').place(x=10, y=25)

song_lbl = Label(song_frame, textvariable=current_song, font=('MS Sans Serif',12,'bold'), bg='Black',fg='White')
song_lbl.place(x=210, y=25)

# Buttons main screen
pause_btn = Button(button_frame, text='Pause', bg='springgreen', fg='black',font=('MS Sans Serif',12,'bold'), width=8, borderwidth=0,
                    command=lambda: pause_song(song_status))
pause_btn.place(x=20, y=15)

stop_btn = Button(button_frame, text='Stop', bg='springgreen', fg='black',font=('MS Sans Serif',12,'bold'), width=8, borderwidth=0,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=110, y=15)

play_btn = Button(button_frame, text='Play', bg='springgreen', fg='black',font=('MS Sans Serif',12,'bold'), width=8, borderwidth=0,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=200, y=15)

resume_btn = Button(button_frame, text='Resume', bg='springgreen', fg='black',font=('MS Sans Serif',12,'bold'), width=8, borderwidth=0,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=290, y=15)

load_btn = Button(button_frame, text='Load Directory', bg='springgreen', fg='black',font=('MS Sans Serif',12,'bold'), width=35, borderwidth=0, command=lambda: load(playlist))
load_btn.place(x=20, y=60)

# Label at the bottom 
Label(root, textvariable=song_status, bg='springgreen',fg='black',font=('MS Sans Serif',12,'bold'), justify=LEFT).pack(side=BOTTOM, fill=X)

root.update()
root.mainloop()