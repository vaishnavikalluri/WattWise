import os
import shutil

os.makedirs('static/images', exist_ok=True)
src = r'C:\Users\vaish\.gemini\antigravity\brain\f99a5bea-c964-4bf6-8221-48ee5d4caad8\electricity_bg_1773508163014.png'
dst = 'static/images/electricity.png'

shutil.copy(src, dst)
print("Image successfully copied.")
