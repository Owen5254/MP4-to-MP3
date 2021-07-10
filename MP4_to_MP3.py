import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *



def UploadAction():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    mp4_file_name = filename
    file_mp4 = filename.split("/")[-1]
    file_mp3 = file_mp4.split(".")[0] + ".mp3"
    mp3_file_name = file_mp3

    videoClip = VideoFileClip(mp4_file_name)
    audioclip = videoClip.audio

    audioclip.write_audiofile(mp3_file_name)

    audioclip.close()
    videoClip.close()


window = tk.Tk()
window.geometry('640x480')
window.resizable(False, False)
window.title('convert mp4 to mp3')

input_frame = tk.Frame(window, width = 640, height = 480)
input_frame.pack()

button = tk.Button(input_frame, text='打開mp4檔案', command= UploadAction, height = 10, width = 50, fg = 'black', bg = "pink")
button.place(relx = 0.5, rely = 0.5, anchor = 'center')

window.mainloop()
