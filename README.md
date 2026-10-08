# 📸 Auto Screen Capture & Split-Window Showcase Tool

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6.svg?logo=windows&logoColor=white)](https://www.microsoft.com/)
[![Automation](https://img.shields.io/badge/Automation-PyAutoGUI%20%7C%20PyGetWindow-orange.svg)](#-technical-stack)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-license)

> **An automated GUI pipeline for processing HTML files, watermarking source code, side-by-side split screen window arrangement (Edge & Notepad), and high-resolution screenshot generation.**
>
> *เครื่องมืออัตโนมัติสำหรับจัดการไฟล์ HTML, ลายน้ำในโค้ด, จัดหน้าต่างแบบแบ่งครึ่งหน้าจอ (Edge & Notepad) และบันทึกภาพหน้าจออัตโนมัติ*

---

## 📑 Table of Contents / สารบัญ

- [English Documentation](#-english-documentation)
  - [Overview](#-overview)
  - [Key Features](#-key-features)
  - [Workflow Diagram](#-workflow-diagram)
  - [Prerequisites & System Requirements](#-prerequisites--system-requirements)
  - [Installation](#-installation)
  - [Step-by-Step Usage](#-step-by-step-usage)
  - [Technical Stack & Mechanics](#-technical-stack--mechanics)
  - [Configuration & Tips for Improvement](#-configuration--tips-for-improvement)
- [เอกสารภาษาไทย](#-เอกสารภาษาไทย)
  - [ภาพรวมโปรแกรม](#-ภาพรวมโปรแกรม)
  - [คุณสมบัติเด่น](#-คุณสมบัติเด่น)
  - [ไดอะแกรมขั้นตอนการทำงาน](#-ไดอะแกรมขั้นตอนการทำงาน)
  - [ความต้องการของระบบ](#-ความต้องการของระบบ)
  - [ขั้นตอนการติดตั้ง](#-ขั้นตอนการติดตั้ง)
  - [คู่มือการใช้งานทีละขั้นตอน](#-คู่มือการใช้งานทีละขั้นตอน)
  - [การทำงานเบื้องหลังของระบบ](#-การทำงานเบื้องหลังของระบบ)
  - [คำแนะนำการปรับแต่งและพัฒนาต่อยอด](#-คำแนะนำการปรับแต่งและพัฒนาต่อยอด)
- [📄 License](#-license)

---

# 🇬🇧 English Documentation

## 🌟 Overview

**Auto Screen Capture & Split-Window Showcase Tool** is a desktop automation script designed for developers, educators, and content creators who need to quickly showcase HTML projects alongside their raw source code.

The script prompts the user to select batch HTML files, modifies them to inject custom watermarks/credits, automatically positions **Microsoft Edge** (rendered view) and **Notepad** (code view) in a 50/50 split screen, and captures a clean desktop screenshot of each pair.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 📂 **Interactive File Pickers** | Built with Tkinter file dialogs for zero-CLI, user-friendly multi-file and folder selection. |
| 🏷️ **Batch Code Injection** | Automatically appends brand watermarks (`Newsoyes.online`) to comments within HTML source files. |
| 🪟 **Smart Window Snapping** | Uses `pygetwindow` to tile Microsoft Edge to the left half ($0 \le X < W/2$) and Notepad to the right half ($W/2 \le X \le W$). |
| 📸 **Full-Resolution Capture** | Employs `pyautogui` to capture flawless full-screen screenshots saved sequentially as `.png`. |
| ⚡ **Batch Processing** | Handles single or multiple files in sequence with configured pause timings to ensure UI readiness. |

---

## 🔄 Workflow Diagram

```text
[Start Script]
      │
      ▼
[Tkinter Dialogs] ──► Select HTML file(s), Output Folder & Screenshot Folder
      │
      ▼
┌───► [For Each HTML File]
│     ├── 1. Read & Inject Credit Watermark (// Newsoyes.online ...)
│     ├── 2. Save modified HTML to Output Folder
│     ├── 3. Open in Microsoft Edge (Shell)
│     ├── 4. Open in Notepad (Subprocess)
│     ├── 5. Resize & Snap Edge to Left (0, 0, Width/2, Height)
│     ├── 6. Resize & Snap Notepad to Right (Width/2, 0, Width/2, Height)
│     └── 7. Capture Full Desktop Screenshot -> screenshot_i.png
└─── Repeat until all files processed
      │
      ▼
[Completion Popup] -> Finish!
```

---

## 🖥️ Screen Layout Preview

```text
+-----------------------------------+-----------------------------------+
|  [ Microsoft Edge: Web View ]     |  [ Notepad: Source Code View ]    |
|                                   |                                   |
|  Rendered HTML Page               |  <!DOCTYPE html>                  |
|  (Preview Output)                 |  <html>                           |
|                                   |    // Newsoyes.online ...         |
|                                   |  </html>                          |
|                                   |                                   |
|  X: 0 -> (Screen Width / 2)       |  X: (Screen Width / 2) -> Width   |
|  Y: 0 -> Screen Height            |  Y: 0 -> Screen Height            |
+-----------------------------------+-----------------------------------+
|<---------------------- Captured Screenshot -------------------------->|
```

---

## 📦 Prerequisites & System Requirements

- **Operating System:** Windows 10 or Windows 11 *(required due to dependencies on `msedge`, `notepad`, and Windows API window management)*.
- **Python:** Python 3.8 or higher.
- **Pre-installed Applications:**
  - Microsoft Edge (`msedge`) accessible via Windows Run path.
  - Windows Notepad (`notepad.exe`).

---

## 🚀 Installation

1. **Clone or Download** the project repository:
   ```bash
   git clone https://github.com/your-username/auto-screen-newsoyes.git
   cd auto-screen-newsoyes
   ```

2. **Create and Activate a Virtual Environment** *(Optional but recommended)*:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Required Python Dependencies:**
   ```bash
   pip install pyautogui pygetwindow
   ```
   > *Note: `os`, `subprocess`, `time`, `shutil`, and `tkinter` are built into standard Python distributions on Windows.*

---

## 📖 Step-by-Step Usage

1. **Launch the Script:**
   ```bash
   python auto_screen_newsoyes.py
   ```
2. **Dialog 1: Select HTML Files**
   - A file picker window will appear. Select one or more `.html` files you wish to process.
3. **Dialog 2: Destination Folder for HTMLs**
   - Choose a target directory where the processed (watermarked) HTML files will be copied.
4. **Dialog 3: Destination Folder for Screenshots**
   - Choose an output folder where final PNG screenshots will be stored.
5. **Automation Running:**
   - **Do not touch the mouse or keyboard** while windows are being tiled and captured.
   - The script will launch Edge and Notepad, resize them side-by-side, wait for rendering, and snap screenshots sequentially (`screenshot_1.png`, `screenshot_2.png`, etc.).
6. **Completion:**
   - A success dialog pops up notifying: *"เสร็จสิ้นจ้าา - แคปหน้าจอเสร็จแล้วค้าบบบ-newsoyes.online 🎉"*.

---

## ⚙️ Technical Stack & Mechanics

```python
# Window positioning logic breakdown:
screen_width, screen_height = pyautogui.size()

# Left Screen (Edge):
edge_win.resizeTo(screen_width // 2, screen_height)
edge_win.moveTo(0, 0)

# Right Screen (Notepad):
note_win.resizeTo(screen_width // 2, screen_height)
note_win.moveTo(screen_width // 2, 0)
```

- **`tkinter.filedialog`**: Suppresses the base root window via `root.withdraw()` and provides native Windows OS file and folder selection prompts.
- **`subprocess.Popen`**: Non-blocking process invocation to simultaneously trigger Edge browser and Notepad editors.
- **`pygetwindow`**: Searches active window title bars for `"Edge"` and `"Notepad"`, restoring minimized windows and reassigning window bounds via $(X, Y, W, H)$.
- **`pyautogui`**: Reads display resolution $(W, H)$ and executes whole-viewport bitmap capture to file.

---

## 💡 Configuration & Tips for Improvement

### 1. Adjusting Sleep Delays
If your PC takes longer to load Edge or large HTML documents, adjust the delay values:
```python
# Increase from 3 to 5 seconds if web pages load slowly:
time.sleep(5)
```

### 2. Auto-Closing Windows After Capture
To prevent multiple windows from piling up on your desktop after processing several files, you can add window termination commands right after saving the screenshot:
```python
# Optional addition: Close windows after capture
if edge_win:
    edge_win.close()
if note_win:
    note_win.close()
```

### 3. Modifying Watermark Pattern
To change or customize the watermark injected into your files, update the string replacement call:
```python
# Custom watermark replacement:
modified_content = content.replace("//", "// [Your Custom Credit or Link Here]")
```

---

# 🇹🇭 เอกสารภาษาไทย

## 🌟 ภาพรวมโปรแกรม

**Auto Screen Capture & Split-Window Showcase Tool** (`auto_screen_newsoyes.py`) คือสคริปต์อัตโนมัติบนระบบปฏิบัติการ Windows ที่ช่วยประหยัดเวลาในการทำภาพพรีวิวผลงานหน้าเว็บ HTML ร่วมกับโค้ดต้นฉบับ 

โปรแกรมจะเปิดหน้าต่างให้เลือกไฟล์ HTML ต้นทาง จากนั้นจะแทรกข้อความเครดิตหรือลายน้ำ (`Newsoyes.online`) ลงในโค้ด เปิดไฟล์ขึ้นมาเปรียบเทียบกันแบบแบ่งครึ่งหน้าจออัตโนมัติ (ซ้าย: Microsoft Edge, ขวา: Notepad) และทำการบันทึกภาพหน้าจอ (Screenshot) บันทึกเก็บเป็นไฟล์รูปภาพให้อัตโนมัติทุกขั้นตอน

---

## ✨ คุณสมบัติเด่น

| คุณสมบัติ | รายละเอียดการทำงาน |
| :--- | :--- |
| 🖥️ **กล่องโต้ตอบแบบ GUI** | ใช้งานง่าย ไม่ต้องพิมพ์คำสั่งในหน้าต่างดำ ใช้ Tkinter เลือกไฟล์และโฟลเดอร์ได้โดยตรง |
| ✍️ **แทรกลายน้ำในโค้ดอัตโนมัติ** | ค้นหาคอมเมนต์ `//` ในไฟล์ HTML แล้วเติมข้อความเครดิตแบรนด์ลงไปให้อัตโนมัติ |
| 🪟 **จัดหน้าต่างแบ่งครึ่งหน้าจอ (Split Screen)** | สั่งย้ายหน้าต่าง Edge ไปไว้ครึ่งซ้าย และ Notepad ไปไว้ครึ่งขวาแบบพอดีขอบจอ 100% |
| 📸 **ถ่ายภาพหน้าจอความละเอียดสูง** | สั่งจับภาพหน้าจอเดสก์ท็อปแบบเต็มจอ (Full Screen) ผ่าน PyAutoGUI และตั้งชื่อเรียงลำดับ |
| 📂 **รองรับการประมวลผลเป็นชุด (Batch)** | เลือกครั้งเดียวหลายไฟล์ สคริปต์จะวนลูปทำให้ทีละไฟล์จนเสร็จทั้งหมด |

---

## 🔄 ไดอะแกรมขั้นตอนการทำงาน

```text
[เริ่มทำงาน]
    │
    ▼
[หน้าต่างเลือกไฟล์/โฟลเดอร์] ──► 1. เลือกไฟล์ HTML (เลือกได้หลายไฟล์)
                             ├── 2. เลือกโฟลเดอร์เก็บไฟล์ HTML ที่แก้ไข
                             └── 3. เลือกโฟลเดอร์เก็บภาพ Screenshot
    │
    ▼
┌───► [เริ่มวนลูปประมวลผลทีละไฟล์]
│     ├── อ่านโค้ด HTML เดิม และแทรกข้อความลายน้ำ Newsoyes.online
│     ├── บันทึกไฟล์ใหม่ลงโฟลเดอร์ปลายทาง
│     ├── สั่งเปิดไฟล์ด้วย Microsoft Edge (แสดงผลหน้าเว็บ)
│     ├── สั่งเปิดไฟล์ด้วย Notepad (แสดงโค้ด)
│     ├── คำนวณความกว้างหน้าจอ แล้วเลื่อน Edge ไปซ้าย (0 ถึง กว้าง/2)
│     ├── เลื่อน Notepad ไปขวา (กว้าง/2 ถึง ขวาสุด)
│     └── ถ่ายภาพหน้าจอ บันทึกเป็น screenshot_1.png, screenshot_2.png, ...
└─── วนทำจนครบทุกไฟล์
    │
    ▼
[แสดงกล่องข้อความแจ้งเตือน "เสร็จสิ้นจ้าา"] -> เสร็จสมบูรณ์!
```

---

## 💻 ภาพจำลองเลย์เอาต์หน้าจอขณะบันทึกภาพ

```text
+-----------------------------------+-----------------------------------+
|  [ Microsoft Edge: ฝั่งแสดงผลเว็บ ]|  [ Notepad: ฝั่งแสดงผลโค้ด ]      |
|                                   |                                   |
|  หน้าเว็บที่เรนเดอร์แล้ว          |  <!DOCTYPE html>                  |
|                                   |  <html>                           |
|                                   |    // Newsoyes.online ...         |
|                                   |  </html>                          |
|                                   |                                   |
|  พิกัด X: 0 ถึง ความกว้าง / 2     |  พิกัด X: ความกว้าง / 2 ถึง ขวาสุด |
|  ความสูง: เต็มหน้าจอ              |  ความสูง: เต็มหน้าจอ              |
+-----------------------------------+-----------------------------------+
|<----------------------- รูปภาพที่แคปได้ทั้งหมด ----------------------->|
```

---

## 📦 ความต้องการของระบบ

1. **ระบบปฏิบัติการ:** Windows 10 หรือ Windows 11 (เนื่องจากต้องใช้คำสั่งจัดการหน้าต่างและโปรแกรมเฉพาะของ Windows)
2. **เวอร์ชัน Python:** Python 3.8 ขึ้นไป
3. **โปรแกรมประจำเครื่อง:**
   - Microsoft Edge
   - Notepad (สมุดบันทึก)

---

## 🚀 ขั้นตอนการติดตั้ง

1. **ดาวน์โหลดหรือโคลนโปรเจกต์:**
   ```bash
   git clone https://github.com/your-username/auto-screen-newsoyes.git
   cd auto-screen-newsoyes
   ```

2. **ติดตั้งไลบรารีที่จำเป็นผ่าน Pip:**
   ```bash
   pip install pyautogui pygetwindow
   ```
   *(หมายเหตุ: โมดูล `os`, `subprocess`, `time`, `shutil` และ `tkinter` เป็นโมดูลมาตรฐานที่มาพร้อมกับ Python บน Windows อยู่แล้ว ไม่ต้องติดตั้งเพิ่ม)*

---

## 📖 คู่มือการใช้งานทีละขั้นตอน

1. **สั่งรันสคริปต์:**
   ```bash
   python auto_screen_newsoyes.py
   ```
2. **ขั้นตอนที่ 1: เลือกไฟล์ HTML**
   - ระบบจะเปิดหน้าต่าง File Explorer ขึ้นมา ให้เลือกไฟล์ `.html` ที่ต้องการ (สามารถกด `Ctrl + คลิก` หรือ `Ctrl + A` เพื่อเลือกหลายไฟล์พร้อมกันได้)
3. **ขั้นตอนที่ 2: เลือกโฟลเดอร์ปลายทางสำหรับไฟล์ HTML**
   - เลือกโฟลเดอร์สำหรับเก็บไฟล์ HTML ที่แทรกลายน้ำแล้ว (แนะนำให้สร้างโฟลเดอร์ว่างใหม่)
4. **ขั้นตอนที่ 3: เลือกโฟลเดอร์บันทึกภาพหน้าจอ**
   - เลือกโฟลเดอร์สำหรับเก็บรูปภาพ `.png` ที่แคปได้
5. **ขั้นตอนที่ 4: การทำงานอัตโนมัติ**
   - ในระหว่างที่โปรแกรมกำลังเปิดหน้าต่างและจัดตำแหน่ง **กรุณาอย่าขยับเมาส์หรือกดคีย์บอร์ด** เพื่อป้องกันไม่ให้โฟกัสหน้าต่างคลาดเคลื่อน
6. **ขั้นตอนที่ 5: การแจ้งเตือนเมื่อเสร็จสิ้น**
   - เมื่อบันทึกภาพครบทุกไฟล์ จะมีหน้าต่างแจ้งเตือนว่า *"เสร็จสิ้นจ้าา"* ปรากฏขึ้น เป็นอันเสร็จสิ้น

---

## ⚙️ การทำงานเบื้องหลังของระบบ

- **การตรวจจับและจัดหน้าจอ**:
  โปรแกรมใช้ `pyautogui.size()` ดึงขนาดความกว้างและสูงของจอภาพ เช่น $1920 \times 1080$ จากนั้นหารสองเพื่อกำหนดความกว้างให้แต่ละโปรแกรม ($960$ พิกเซล)
- **การควบคุมหน้าต่าง**:
  ใช้ `pygetwindow.getWindowsWithTitle()` ค้นหาหน้าต่างที่มีชื่อว่า `"Edge"` และ `"Notepad"` และเรียกใช้เมธอด `.restore()`, `.resizeTo()`, `.moveTo()` เพื่อจัดวางหน้าต่างให้อยู่ในตำแหน่งที่แม่นยำ
- **การแทรกลายน้ำ**:
  ใช้คำสั่งสตริงมาตรฐาน `.replace("//", "// Newsoyes.online Newsoyes.online Newsoyes.online")` เพื่อเขียนทับคอมเมนต์ในภาษา JavaScript/CSS ภายในไฟล์ HTML

---

## 💡 คำแนะนำการปรับแต่งและพัฒนาต่อยอด

### 1. ปรับเวลาหน่วงหน้าจอ (Delay Timing)
หากเครื่องคอมพิวเตอร์ของคุณเปิดโปรแกรมช้า หรือหน้าเว็บมีขนาดใหญ่จนเรนเดอร์ไม่ทัน 3 วินาที สามารถเพิ่มเวลาในคำสั่ง `time.sleep` ได้:
```python
# ปรับจาก 3 เป็น 4 หรือ 5 วินาที
time.sleep(5)
```

### 2. เพิ่มคำสั่งปิดหน้าต่างอัตโนมัติหลังแคปเสร็จ
หากเลือกไฟล์เป็นจำนวนมาก หน้าต่าง Edge และ Notepad อาจเปิดค้างไว้เต็มหน้าจอ สามารถเพิ่มคำสั่งสั่งปิดหน้าต่างหลังจากแคปภาพเสร็จในแต่ละรอบได้ดังนี้:
```python
# แทรกต่อท้ายหลังจาก pyautogui.screenshot(screenshot_path)
if edge_win:
    edge_win.close()
if note_win:
    note_win.close()
```

### 3. เปลี่ยนโปรแกรมแก้ไขข้อความ (Editor)
หากต้องการใช้โปรแกรมอื่นแทน Notepad เช่น VS Code สามารถแก้ไขคำสั่ง `subprocess` ได้ตามความต้องการ:
```python
# ตัวอย่าง: เปิดด้วย VS Code
subprocess.Popen(['code', dst_path])
```

---

## 📄 License

Project created and copyrighted by **newsoyes.online**.  
Distributed under the **MIT License**. You are free to use, modify, and distribute this software for personal or commercial projects.
