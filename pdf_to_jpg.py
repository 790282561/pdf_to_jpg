import fitz
import os


#  打开PDF文件，生成一个对象
#  file = fitz.open('1.pdf')


def pdf_to_jpg(file, name):
    for pg in range(file.pageCount):
        page = file[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG(name[: -4] + '.jpg')


for folders1 in os.listdir('导图'):
    for folders2 in os.listdir('./导图/'+folders1):
        for folders3 in os.listdir('./导图/'+folders1+'/'+ folders2):
            file_path = './导图/'+folders1 +'/'+folders2 +'/'+folders3
            file = fitz.open(file_path)
            pdf_to_jpg(file, file_path)
