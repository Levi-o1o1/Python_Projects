import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import threading
import os


# ---------------- Download Function ----------------
def download_playlist():
    url = url_entry.get()
    folder = folder_path.get()

    if not url or not folder:
        messagebox.showerror("Error", "Please enter playlist URL and choose folder")
        return

    ydl_opts = {
        'format': "bv*+ba/b", 
        '--merge-output-format': "mp4",
        'outtmpl': f'{folder}/%(playlist_title)s/%(title)s.%(ext)s', 
        'noplaylist': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Playlist Download Completed ✅")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- Thread Wrapper ----------------
def start_download():
    threading.Thread(target=download_playlist).start()

# ---------------- Folder Browser ----------------
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# ---------------- GUI ----------------
app = tk.Tk()
app.title("YouTube Playlist Downloader")
app.geometry("600x250")
app.resizable(False, False)

tk.Label(app, text="YouTube Playlist URL").pack(pady=5)
url_entry = tk.Entry(app, width=60)
url_entry.pack(pady=5)

tk.Label(app, text="Download Folder").pack(pady=10,padx=40)
folder_path = tk.StringVar()
folder_entry = tk.Entry(app, textvariable=folder_path, width=40)
folder_entry.pack(side="bottom", padx=20,pady=20)

browse_btn = tk.Button(app, text="Browse", command=browse_folder)
browse_btn.pack(side="bottom",padx=35,pady=5)

tk.Button(app, text="Download Playlist", command=start_download,
          bg="green", fg="white", height=-2, width=15).pack(padx=20)

def paste_from_clipboard(event=None):
    try:
        text = app.clipboard_get()
        url_entry.delete(0, tk.END)
        url_entry.insert(0, text)
    except:
        pass

url_entry.bind("<Button-3>",
paste_from_clipboard)

app.mainloop()