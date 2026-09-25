import os
from PIL import Image, ImageDraw, ImageFont

def generate_logo():
    # Create white canvas
    size = (400, 400)
    img = Image.new('RGBA', size, (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer circle border (green & blue)
    bbox = [40, 40, 360, 360]
    draw.arc(bbox, start=270, end=140, fill="#0d9488", width=12) # Teal/green
    draw.arc(bbox, start=140, end=270, fill="#2563eb", width=12) # Blue
    
    # Draw elements inside:
    # 1. Graduation Cap (Top center)
    diamond = [(200, 80), (250, 100), (200, 120), (150, 100)]
    draw.polygon(diamond, fill="#1e3a8a")
    base = [(175, 110), (225, 110), (225, 130), (175, 130)]
    draw.polygon(base, fill="#1e40af")
    draw.line([(240, 104), (255, 125), (255, 140)], fill="#2563eb", width=4)
    draw.ellipse([251, 138, 259, 146], fill="#2563eb")
    
    # 2. Magnifying glass (Left)
    draw.ellipse([110, 140, 170, 200], outline="#1e3a8a", width=7)
    draw.line([(125, 185), (95, 215)], fill="#1e3a8a", width=9)
    
    # 3. Bar Chart with arrow (Right)
    draw.rectangle([230, 180, 246, 220], fill="#0284c7")
    draw.rectangle([254, 160, 270, 220], fill="#0d9488")
    draw.rectangle([278, 135, 294, 220], fill="#16a34a")
    draw.line([(225, 175), (300, 125)], fill="#16a34a", width=6)
    draw.polygon([(300, 115), (308, 132), (290, 132)], fill="#16a34a")
    
    # Student figure / Open book in middle
    draw.polygon([(160, 220), (200, 230), (240, 220), (240, 235), (200, 245), (160, 235)], fill="#1e3a8a")
    draw.ellipse([190, 150, 210, 170], fill="#1e3a8a") # Head
    draw.polygon([(200, 175), (170, 205), (180, 212), (200, 195), (220, 212), (230, 205)], fill="#1e3a8a") # Arms
    
    # Text: STUDENT SKILL GAP ANALYTICS
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_sub = ImageFont.truetype("arial.ttf", 14)
        font_motto = ImageFont.truetype("arial.ttf", 11)
    except:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_motto = font_title

    draw.text((200, 260), "STUDENT", fill="#1e3a8a", font=font_title, anchor="mm")
    draw.text((200, 288), "SKILL GAP", fill="#2563eb", font=font_sub, anchor="mm")
    draw.text((200, 308), "- ANALYTICS -", fill="#0d9488", font=font_motto, anchor="mm")
    draw.text((200, 335), "Analyze • Improve • Succeed", fill="#475569", font=font_motto, anchor="mm")
    
    os.makedirs("assets", exist_ok=True)
    img.save("assets/logo.png")
    print("Logo generated successfully!")

if __name__ == "__main__":
    generate_logo()
