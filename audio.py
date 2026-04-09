import tkinter as tk
from tkinter import filedialog, messagebox
import pygame


pygame.mixer.init()


root = tk.Tk()
root.title("Audio Player")
root.geometry("350x250")
root.resizable(False, False)

song_path = ""


def browse_file():
    global song_path
    song_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav")]
    )
    if song_path:
        song_name.config(text=song_path.split("/")[-1])

def play_music():
    if song_path == "":
        messagebox.showwarning("Warning", "Please select a song first")
    else:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

title_label = tk.Label(root, text="Simple Audio Player", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


song_name = tk.Label(root, text="No song selected", font=("Arial", 10))
song_name.pack(pady=10)


browse_btn = tk.Button(root, text="Browse Song", width=20, command=browse_file)
browse_btn.pack(pady=5)

play_btn = tk.Button(root, text="Play", width=20, command=play_music)
play_btn.pack(pady=5)

pause_btn = tk.Button(root, text="Pause", width=20, command=pause_music)
pause_btn.pack(pady=5)

resume_btn = tk.Button(root, text="Resume", width=20, command=resume_music)
resume_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", width=20, command=stop_music)
stop_btn.pack(pady=5)

root.mainloop()