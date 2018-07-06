
'''
    随着背景色从左到右不断加深,文字变得越来越难以识别,Tesseract 识别出的 每一行的最后几个字符都是错的。
    遇到这类问题,可以先用 Python 脚本对图片进行清理。利用 Pillow 库,我们可以创建一个 阈值过滤器来去掉渐变的背景色,只把文字留下来,从而让图片更加清晰,便于 Tesseract 读取:
'''

from PIL import Image
import subprocess


def clean_file(file_path, new_file_path):
    image = Image.open(file_path)

    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(new_file_path)

    subprocess.call(["tesseract", new_file_path, "output"])

    file = open("output.txt", 'r')
    print(file.read())
    file.close()

clean_file('tess2.jpg', 'text2clean.png')