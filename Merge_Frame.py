from PIL import Image, ImageDraw
import os

headSize = 106

def crop_to_circle(image):
    # 创建一个空白的透明画布
    circle_mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(circle_mask)

    # 画一个直径为 image 宽度的圆
    draw.ellipse((0, 0, image.width, image.height), fill=255)

    # 将圆形画布作为遮罩，裁剪头像框
    result = Image.new("RGBA", image.size)
    result.paste(image, mask=circle_mask)
    return result


def composite_image(src_img_path, frame_img_path, dst_img_path, canvas_size):
    # Load the source image
    src_img = Image.open(src_img_path).convert('RGBA')
    src_img.thumbnail((canvas_size, canvas_size))

    # Load the frame image
    frame_img = Image.open(frame_img_path).convert('RGBA')
    frame_img.thumbnail((canvas_size, canvas_size))

    # Create a blank canvas
    canvas = Image.new('RGBA', (canvas_size, canvas_size), (255, 255, 255, 0))

    # Calculate the position to center the images
    x_offset = (canvas_size - src_img.width) // 2
    y_offset = (canvas_size - src_img.height) // 2

    src_img = crop_to_circle(src_img)
    # Paste the source image onto the canvas
    canvas.paste(src_img, (x_offset, y_offset), src_img)

    # Paste the frame image onto the canvas
    canvas.paste(frame_img, (0, 0), frame_img)

    # Save the composite image
    canvas.save(dst_img_path)

def process_images_in_directory(directory_path):
    # Create the destination directory if it doesn't exist
    dst_directory = os.path.join(directory_path, 'dstimage')
    os.makedirs(dst_directory, exist_ok=True)

    # Load the frame image
    frame_img_path = 'avatar_frame.png'

    # Process each image in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            src_img_path = os.path.join(directory_path, filename)
            dst_img_path = os.path.join(dst_directory, f'result_{filename}')

            composite_image(src_img_path, frame_img_path, dst_img_path, canvas_size=headSize)

if __name__ == '__main__':
    headimg_directory = 'headimg'
    process_images_in_directory(headimg_directory)
