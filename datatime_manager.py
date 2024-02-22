from tkinter import Label
from datetime import datetime

class DateTimeManager:
    def __init__(self, master, x_hourtime, y_hourtime, x_daystime, y_daystime, x_datetime, y_datetime, size_hour):
        self.master = master
        self.current_datetime = datetime.now()

        # JAM
        self.label_hourtime = Label(
            self.master,
            text="",
            bg="#ffffff",
            fg="#68BE20",
            font=("Montserrat", size_hour * -1, "bold")
        )
        self.label_hourtime.place(x=x_hourtime, y=y_hourtime, anchor="nw")

        # DAYS
        self.label_daystime = Label(
            self.master,
            text="",
            bg="#ffffff",
            fg="#737373",
            font=("Montserrat", 20 * -1, "bold")
        )
        self.label_daystime.place(x=x_daystime, y=y_daystime, anchor="nw")

        # DATE
        self.label_datetime = Label(
            self.master,
            text="",
            bg="#ffffff",
            fg="#737373",
            font=("Montserrat", 20 * -1, "bold")
        )
        self.label_datetime.place(x=x_datetime, y=y_datetime, anchor="nw")

        # Atur agar fungsi update_datetime dipanggil setiap detik (1000 milidetik)
        self.master.after(1000, self.update_datetime)

    def update_datetime(self):
        # Dapatkan waktu dan tanggal saat ini
        self.current_datetime = datetime.now()
        # Format waktu, tanggal, dan hari sesuai kebutuhan
        formatted_hourtime = self.current_datetime.strftime("%H:%M:%S")
        formatted_daystime = self.current_datetime.strftime("%A")
        formatted_datetime = self.current_datetime.strftime("%Y-%m-%d")

        self.label_hourtime.config(text=formatted_hourtime)
        self.label_daystime.config(text=formatted_daystime)
        self.label_datetime.config(text=formatted_datetime)

        # Atur agar fungsi ini dipanggil setiap detik (1000 milidetik)
        self.update_id = self.master.after(1000, self.update_datetime)

    def stop_update(self):
        # Hentikan pemanggilan update setiap detik
        self.master.after_cancel(self.update_id)

