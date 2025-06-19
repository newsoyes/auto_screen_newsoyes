import os
import subprocess
import time
import pyautogui
import pygetwindow as gw
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# newsoyes.online newsoyes.online newsoyes.online
root = tk.Tk()
root.withdraw()

# newsoyes.online newsoyes.online newsoyes.online
messagebox.showinfo("เลือกไฟล์ HTML", "กรุณาเลือกไฟล์ HTML ที่คุณต้องการใช้งาน (เลือกหลายไฟล์ได้นะจ๊ะ)")
file_paths = filedialog.askopenfilenames(title="เลือกไฟล์ HTML", filetypes=[("HTML files", "*.html")])
if not file_paths:
    messagebox.showwarning("ไม่มีไฟล์", "คุณยังไม่ได้เลือกไฟล์ HTML ใด ๆ")
    exit()

# newsoyes.online newsoyes.online newsoyes.online
output_folder = filedialog.askdirectory(title="เลือกโฟลเดอร์ปลายทาง (สำหรับเก็บไฟล์ที่จะเปิด ควรสร้างเป็นโฟลเดอร์ใหม่)")
if not output_folder:
    messagebox.showwarning("ไม่ได้เลือก", "คุณยังไม่ได้เลือกโฟลเดอร์ปลายทาง")
    exit()

screenshot_folder = filedialog.askdirectory(title="เลือกโฟลเดอร์สำหรับบันทึกภาพหน้าจอ (สำหรับเก็บรูปที่แคป ควรสร้างแยกเป็นโฟลเดอร์ใหม่)")
if not screenshot_folder:
    messagebox.showwarning("ไม่ได้เลือก", "คุณยังไม่ได้เลือกโฟลเดอร์ภาพหน้าจอ")
    exit()

# newsoyes.online newsoyes.online newsoyes.online
os.makedirs(output_folder, exist_ok=True)
os.makedirs(screenshot_folder, exist_ok=True)

# newsoyes.online newsoyes.online newsoyes.online
for i, src_path in enumerate(file_paths, start=1):
    filename = os.path.basename(src_path)
    dst_path = os.path.join(output_folder, filename)

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified_content = content.replace("//", "// Newsoyes.online Newsoyes.online Newsoyes.online")

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(modified_content)

    subprocess.Popen(['start', 'msedge', dst_path], shell=True)
    time.sleep(3)

    subprocess.Popen(['notepad', dst_path])
    time.sleep(3)

    # newsoyes.online newsoyes.online newsoyes.online
    screen_width, screen_height = pyautogui.size()
    time.sleep(1)

    edge_windows = gw.getWindowsWithTitle("Edge")
    note_windows = gw.getWindowsWithTitle("Notepad")

    edge_win = edge_windows[0] if edge_windows else None
    note_win = note_windows[0] if note_windows else None

    if edge_win:
        try:
            edge_win.restore()
            edge_win.resizeTo(screen_width // 2, screen_height)
            edge_win.moveTo(0, 0)
        except Exception as e:
            print(f"⚠ ไม่สามารถจัดการ Edge ได้: {e}")

    if note_win:
        try:
            note_win.restore()
            note_win.resizeTo(screen_width // 2, screen_height)
            note_win.moveTo(screen_width // 2, 0)
        except Exception as e:
            print(f"⚠ ไม่สามารถจัดการ Notepad ได้: {e}")

    # newsoyes.online newsoyes.online newsoyes.online
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{i}.png")
    pyautogui.screenshot(screenshot_path)
    print(f"✅ บันทึกภาพ: {screenshot_path}")
    time.sleep(1)

# newsoyes.online newsoyes.online newsoyes.online
messagebox.showinfo("เสร็จสิ้นจ้าา", "แคปหน้าจอเสร็จแล้วค้าบบบ-newsoyes.online 🎉")
