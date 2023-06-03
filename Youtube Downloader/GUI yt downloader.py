from tkinter import Tk, Label, Entry, Button, Radiobutton, OptionMenu, IntVar, messagebox
from pytube import YouTube, Playlist
import tkinter.scrolledtext as scrolledtext

def download_video():
    url = entry_url.get()
    try:
        yt = YouTube(url)
        task = quality_choice.get()
        if task == 1:
            title = yt.title
            messagebox.showinfo("Video Title", title)
        elif task == 2:
            show_thumbnail_url(yt.thumbnail_url)
        elif task == 3:
            video = yt.streams.all()
            audio = yt.streams.filter(only_audio=True)
            quality_list = [str(i) for i in range(len(video))]
            quality_choice.set('')
            quality_option['menu'].delete(0, 'end')  # Clear the existing menu
            for quality in quality_list:
                quality_option['menu'].add_command(label=quality, command=lambda q=quality: quality_choice.set(q))
            quality_label.pack()
            quality_option.pack()
            download_button.pack()
        else:
            messagebox.showinfo("Exit", "Exiting the program.")
            window.destroy()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_thumbnail_url(url):
    thumbnail_window = Tk()
    thumbnail_window.title("Thumbnail URL")
    thumbnail_window.geometry("400x200")

    def copy_thumbnail_url():
        thumbnail_window.clipboard_clear()
        thumbnail_window.clipboard_append(url)
        thumbnail_window.update()
        messagebox.showinfo("Copy Successful", "Thumbnail URL copied to clipboard.")

    thumbnail_label = Label(thumbnail_window, text="Thumbnail URL:")
    thumbnail_label.pack(pady=10)

    text_area = scrolledtext.ScrolledText(thumbnail_window, width=40, height=5)
    text_area.insert('1.0', url)
    text_area.pack(pady=10)

    copy_button = Button(thumbnail_window, text="Copy", command=copy_thumbnail_url)
    copy_button.pack()

    thumbnail_window.mainloop()

def download_selected_video():
    url = entry_url.get()
    yt = YouTube(url)
    video = yt.streams.all()
    selected_quality = int(quality_choice.get())
    video[selected_quality].download()
    messagebox.showinfo("Download Complete", "Video downloaded successfully.")

def download_playlist():
    url = entry_url.get()
    playlist = Playlist(url)
    messagebox.showinfo("Playlist Download", f"Downloading {playlist.title}")
    for video in playlist.videos:
        video.streams.first().download()
    messagebox.showinfo("Download Complete", "Playlist downloaded successfully.")

# Create the main window
window = Tk()
window.title("YouTube Downloader")

# Create and position the URL entry field
entry_url = Entry(window, width=50)
entry_url.pack(pady=10)

# Create and position the choice label
choice_label = Label(window, text="Select an option:")
choice_label.pack()

# Create and position the choice radio buttons
quality_choice = IntVar()
radio_video = Radiobutton(window, text="Download Video Title", variable=quality_choice, value=1)
radio_video.pack()
radio_thumbnail = Radiobutton(window, text="Download Thumbnail", variable=quality_choice, value=2, command=download_video)
radio_thumbnail.pack()
radio_download = Radiobutton(window, text="Download Video", variable=quality_choice, value=3, command=download_video)
radio_download.pack()

# Create and position the quality label and option menu
quality_label = Label(window, text="Select video quality:")
quality_option = OptionMenu(window, quality_choice, "")

# Create and position the download button
download_button = Button(window, text="Download", command=download_selected_video)

# Create and position the main download button
button_download = Button(window, text="Download", command=download_video)
button_download.pack(pady=5)

# Create and position the playlist download button
button_playlist = Button(window, text="Download Playlist", command=download_playlist)
button_playlist.pack(pady=5)

# Start the main window's event loop
window.mainloop()
