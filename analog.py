import tkinter as tk
import time
import math

def draw_clock():
    # پاک کردن صفحه
    canvas.delete("all")
    
    # رسم دایره ساعت
    canvas.create_oval(50, 50, 350, 350, outline="black", width=2)

    # دریافت زمان جاری
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # محاسبه زاویه عقربه‌ها
    hour_angle = (hours + minutes / 60) * 30  # 360 / 12 = 30
    minute_angle = (minutes + seconds / 60) * 6  # 360 / 60 = 6
    second_angle = seconds * 6  # 360 / 60 = 6

    # محاسبه موقعیت عقربه‌ها
    hour_x = 200 + 70 * math.cos(math.radians(hour_angle - 90))
    hour_y = 200 + 70 * math.sin(math.radians(hour_angle - 90))
    minute_x = 200 + 100 * math.cos(math.radians(minute_angle - 90))
    minute_y = 200 + 100 * math.sin(math.radians(minute_angle - 90))
    second_x = 200 + 120 * math.cos(math.radians(second_angle - 90))
    second_y = 200 + 120 * math.sin(math.radians(second_angle - 90))

    # رسم عقربه‌ها
    canvas.create_line(200, 200, hour_x, hour_y, fill="black", width=6)
    canvas.create_line(200, 200, minute_x, minute_y, fill="blue", width=4)
    canvas.create_line(200, 200, second_x, second_y, fill="red", width=2)

    # به‌روزرسانی هر 1000 میلی‌ثانیه
    root.after(1000, draw_clock)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ساعت آنالوگ")

# ایجاد بوم برای رسم ساعت
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# شروع رسم ساعت
draw_clock()

# اجرای حلقه اصلی
root.mainloop()