import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from moviepy.editor import VideoFileClip, concatenate_videoclips
from threading import Thread


# -----------------------------
# Utility Functions
# -----------------------------

def time_str_to_seconds(time_str):
    """Convert time from HH:MM:SS format to seconds."""
    try:
        parts = time_str.strip().split(":")
        if len(parts) != 3:
            raise ValueError
        h, m, s = map(int, parts)
        return h * 3600 + m * 60 + s
    except:
        raise ValueError("Time format must be HH:MM:SS")


def load_video(file_path):
    return VideoFileClip(file_path)


def process_video(video, time_pairs):
    clips = []
    current_time = 0

    # Convert and validate intervals
    intervals = []
    for start_time, end_time in time_pairs:
        start_sec = time_str_to_seconds(start_time)
        end_sec = time_str_to_seconds(end_time)

        if start_sec >= end_sec:
            raise ValueError("Start time must be before end time")

        if end_sec > video.duration:
            raise ValueError("End time exceeds video duration")

        intervals.append((start_sec, end_sec))

    # Sort intervals
    intervals.sort()

    for start_sec, end_sec in intervals:
        if current_time < start_sec:
            clips.append(video.subclip(current_time, start_sec))
        current_time = end_sec

    if current_time < video.duration:
        clips.append(video.subclip(current_time, video.duration))

    if not clips:
        raise ValueError("No valid video segments remaining.")

    return concatenate_videoclips(clips)


# -----------------------------
# GUI Application
# -----------------------------

class VideoEditorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Simple Video Editor")
        self.root.geometry("750x450")
        self.cancelled = False

        # Variables
        self.input_video_path = tk.StringVar()
        self.output_video_path = tk.StringVar()
        self.time_intervals = []

        self.build_ui()

    # -----------------------------
    # UI Layout
    # -----------------------------

    def build_ui(self):

        # Input video
        tk.Label(self.root, text="Input Video:").grid(row=0, column=0, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.input_video_path, width=50).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_input).grid(row=0, column=2)

        # Intervals Frame
        self.intervals_frame = tk.LabelFrame(self.root, text="Intervals to Remove")
        self.intervals_frame.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky="ew")

        tk.Button(self.root, text="Add Interval", command=self.add_interval).grid(row=2, column=1, pady=5)

        # Output video
        tk.Label(self.root, text="Output Video:").grid(row=3, column=0, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.output_video_path, width=50).grid(row=3, column=1)
        tk.Button(self.root, text="Save As", command=self.save_output).grid(row=3, column=2)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", mode="indeterminate", length=400)
        self.progress.grid(row=4, column=1, pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=5, column=1)

        tk.Button(button_frame, text="Process Video", command=self.start_processing_video).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Quit", command=self.root.quit).grid(row=0, column=1, padx=5)

    # -----------------------------
    # File Selection
    # -----------------------------

    def browse_input(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
        )
        if file_path:
            self.input_video_path.set(file_path)

    def save_output(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4 files", "*.mp4")]
        )
        if file_path:
            self.output_video_path.set(file_path)

    # -----------------------------
    # Interval Management
    # -----------------------------

    def add_interval(self):
        row = len(self.time_intervals)

        start_var = tk.StringVar()
        end_var = tk.StringVar()

        tk.Label(self.intervals_frame, text=f"Start {row + 1} (HH:MM:SS):").grid(row=row, column=0, padx=5, pady=2)
        tk.Entry(self.intervals_frame, textvariable=start_var, width=12).grid(row=row, column=1)

        tk.Label(self.intervals_frame, text=f"End {row + 1} (HH:MM:SS):").grid(row=row, column=2, padx=5)
        tk.Entry(self.intervals_frame, textvariable=end_var, width=12).grid(row=row, column=3)

        self.time_intervals.append((start_var, end_var))

    # -----------------------------
    # Processing Logic
    # -----------------------------

    def start_processing_video(self):
        if not self.input_video_path.get() or not self.output_video_path.get():
            messagebox.showerror("Error", "Please select input and output files.")
            return

        if not self.time_intervals:
            messagebox.showerror("Error", "Please add at least one interval.")
            return

        self.progress.start()
        thread = Thread(target=self.process_video_thread)
        thread.start()

    def process_video_thread(self):
        try:
            time_pairs = []

            for start_var, end_var in self.time_intervals:
                start = start_var.get().strip()
                end = end_var.get().strip()

                if start and end:
                    time_pairs.append((start, end))

            video = load_video(self.input_video_path.get())
            edited_video = process_video(video, time_pairs)

            edited_video.write_videofile(
                self.output_video_path.get(),
                codec="libx264",
                audio_codec="aac"
            )

            video.close()
            edited_video.close()

            self.progress.stop()
            messagebox.showinfo("Success", "Video processed successfully!")

        except Exception as e:
            self.progress.stop()
            messagebox.showerror("Error", str(e))


# -----------------------------
# Main Entry
# -----------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()
