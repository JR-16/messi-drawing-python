import tkinter as tk
from sketchpy import canvas

# 1 spanish >>>>>> primero instala:
#  1.1      pip install sketchpy

# Create main Tkinter window
root = tk.Tk()
root.withdraw()

# Create class object canvas.sketch  
Messi = canvas.sketch(x_offset=290, y_offset=320)

# Draw Messi
Messi.draw_fn("src/background1", co=(116,172,223), mode=0)
Messi.draw_fn("src/background2", co=(255, 255, 255), mode=0)
Messi.draw_fn("src/background3", co=(116,172,223), mode=0)

Messi.draw_fn("src/face_out", co=(233, 183, 151), mode=0)
Messi.draw_fn("src/beard_out", co=(30, 25, 31), mode=0)

Messi.draw_fn("src/chin1", co=(204, 139, 124), mode=0)
Messi.draw_fn("src/chin2", co=(204, 139, 124), mode=0)

Messi.draw_fn("src/lip_lower", co=(214, 125, 100), mode=0)
Messi.draw_fn("src/lip_upper", co=(186, 30, 21), mode=0)

Messi.draw_fn("src/nostril", co=(8, 15, 29), mode=0)
Messi.draw_fn("src/nose_curve", co=(128, 69, 56), mode=0)
Messi.draw_fn("src/right_eyebrow", co=(12, 16, 22), mode=0)
Messi.draw_fn("src/left_eyebrow", co=(12, 16, 22), mode=0)

Messi.draw_fn("src/noseline", co=(12, 16, 22), mode=0)

Messi.draw_fn("src/eyelid", co=(13, 15, 23), mode=0)
Messi.draw_fn("src/eye", co=(17, 12, 20), mode=0)
Messi.draw_fn("src/sclera", co=(230, 231, 229), mode=0)
Messi.draw_fn("src/eyeball", co=(15, 25, 15), mode=0)
Messi.draw_fn("src/eyeball_centre", co=(230, 231, 229), mode=0)

Messi.draw_fn("src/hair_outline", co=(12, 16, 25), mode=0)
Messi.draw_fn("src/hair_shade1", co=(12, 16, 25), mode=0)
Messi.draw_fn("src/hair_shade2", co=(61, 44, 52), mode=0)
Messi.draw_fn("src/hair_shade3", co=(119, 64, 75), mode=0)
Messi.draw_fn("src/hair_shade4", co=(119, 64, 75), mode=0)
Messi.draw_fn("src/hair_shade5", co=(61, 44, 52), mode=0)
Messi.draw_fn("src/hair_shade6", co=(119, 64, 75), mode=0)
Messi.draw_fn("src/hair_shade7", co=(61, 44, 52), mode=0)
Messi.draw_fn("src/hair_shade8", co=(61, 44, 52), mode=0)

Messi.draw_fn("src/throat", co=(245, 207, 171), mode=0)
Messi.draw_fn("src/throat_shade1", co=(236, 180, 153), mode=0)
Messi.draw_fn("src/throat_shade2", co=(236, 180, 153), mode=0)

Messi.draw_fn("src/ear_line1", co=(16, 10, 8), mode=0)
Messi.draw_fn("src/ear_line2", co=(16, 10, 8), mode=0)
Messi.draw_fn("src/ear_line3", co=(16, 10, 8), mode=0)
Messi.draw_fn("src/ear_shade1", co=(212, 138, 124), mode=0)
Messi.draw_fn("src/ear_shade2", co=(212, 138, 124), mode=0)
Messi.draw_fn("src/ear_shade3", co=(212, 134, 122), mode=0)

Messi.draw_fn("src/beard_shade1", co=(124, 77, 75), mode=0)
Messi.draw_fn("src/beard_shade2", co=(127, 76, 76), mode=0)

Messi.draw_fn("src/face_shade1", co=(209, 137, 122), mode=0)
Messi.draw_fn("src/face_shade2", co=(208, 138, 119), mode=0)

Messi.draw_fn("src/eye_shade1", co=(209, 143, 126), mode=0)
Messi.draw_fn("src/eye_shade2", co=(209, 143, 126), mode=0)

Messi.draw_fn("src/face_shade3", co=(245, 207, 171), mode=0)
Messi.draw_fn("src/face_shade4", co=(240, 208, 169), mode=0)

Messi.draw_fn("src/forhead_shade1", co=(202, 135, 119), mode=0)

Messi.draw_fn("src/tshirt", co=(255, 255, 255), mode=0)
Messi.draw_fn("src/tshirt_color1", co=(116,172,223), mode=0)
Messi.draw_fn("src/tshirt_color2", co=(255, 255, 255), mode=0)
Messi.draw_fn("src/tshirt_color3", co=(0, 0, 0), mode=0)

root.mainloop()