import numpy as np
from PIL import Image

file="E:\\学习\\UnityCity\\20231220\\sample\\samples_16x64x64x3.npz"
save="E:\\学习\\UnityCity\\20231220\\sample\\"

data = np.load(file)
images=data["arr_0"]

for i, image_data in enumerate(images):
    # 将数据转换为图像对象
    image = Image.fromarray(image_data)

    # 保存图像为图片文件（可以根据需要修改文件名格式）
    image.save(save+"output_image_"+str(i)+".png")

    print(i)