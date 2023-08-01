from PIL import Image, ImageDraw
import numpy as np
import random 

def draw_avatar_frame(width, num, r):
    # 创建一个空白的图像
    img = Image.new("RGBA", (width+r, width+r), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 绘制头像框轨迹
    draw.ellipse([(0+r/2, 0+r/2), (width+r/2, width+r/2)], outline="black", width=2)

    # 计算每个贴图之间的间隔角度
    angle_interval = 360 / 2 / num

    # # 在头像框轨迹上贴图
    for i in range(2*num):
        angle = i * angle_interval + 90 + angle_interval/2

        x = width/2 * (1-np.cos(np.radians(angle))) + r/2
        y = width/2 * (1-np.sin(np.radians(angle))) + r/2

        random_number = i
        # 贴图路径
        image_path = "image/image_" + str(random_number)  +  ".png"

        # 打开贴图图片
        avatar = Image.open(image_path)

        # 缩放贴图图片为指定半径大小
        avatar = avatar.resize((r * 2, r * 2))

        # 在指定位置贴图
        img.paste(avatar, (int(x - r), int(y - r)), avatar)

    # 保存头像框图片
    img.save("avatar_frame.png")

# 示例用法
width = 100  # 头像框总宽度
num = 8      # 头像框边贴图数量
r = 6      # 贴图半径

draw_avatar_frame(width, num, r)
