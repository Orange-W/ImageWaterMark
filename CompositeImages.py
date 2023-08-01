from PIL import Image, ImageDraw, ImageFont

# 图片目录和输出路径
image_directory = "image/"
output_path = "result.png"

# 图片大小和行列数
image_size = 100
rows = 8
cols = 8

# 创建一个空白大图
result_image = Image.new("RGB", (image_size * cols, image_size * (rows)))

# 循环加载图片并拼接到大图上
for i in range(rows):
    for j in range(cols):
        index = i * cols + j
        if index <= 64:
            img_path = f"{image_directory}image_{index}.png"
            img = Image.open(img_path)
            img = img.resize((image_size, image_size))
            result_image.paste(img, (j * image_size, i * image_size))

# 在每张小图中央绘制序号
draw = ImageDraw.Draw(result_image)
font_path = "/System/Library/Fonts/Arial.ttf"
font = ImageFont.truetype(font_path, 14)

for i in range(rows):
    for j in range(cols):
        index = i * cols + j
        if index <= 64:
            text = format(index, '02X') 
            text_bbox = font.getbbox(text)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            x = j * image_size + (image_size - text_width) // 2
            y = i * image_size + (image_size - text_height) // 2
            draw.text((x, y), text, fill="black", font=font)

# 保存结果图片
result_image.save(output_path)
