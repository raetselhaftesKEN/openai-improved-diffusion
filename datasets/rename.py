import os

cat="agri"
targetdir="E:\\Git\\UploadFolder\\openai-improved-diffusion\\datasets\\Sentinel-1&2 Image Pairs (SAR & Optical)\\v_2\\"+cat+"\\s2\\"

# 获取目标文件夹中的所有文件名
file_list = os.listdir(targetdir)

index=0
# 遍历文件列表
for file_name in file_list:
    # 构建新的文件名，可以使用字符串的replace()函数或正则表达式替换
    new_file_name = cat+"_"+str(index)+".png"
    index+=1

    # 构建完整的文件路径
    old_file_path = os.path.join(targetdir, file_name)
    new_file_path = os.path.join(targetdir, new_file_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

print("Processed "+str(index)+" files")