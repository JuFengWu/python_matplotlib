from matplotlib.font_manager import fontManager
import os

for font in fontManager.ttflist:
    print(font)

# find chinese

fonts = [font.name for font in fontManager.ttflist if 
         os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6] 
        # chinese font is very big , it should bigger than 1M
print("chinese word are")
for font in fonts:
    print(font)