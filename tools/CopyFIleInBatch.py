import os
import shutil

path = "/Users/xujintao/Downloads/1-30/"
target = "/Users/xujintao/Downloads/1-30/all"
dir_name = []
sub_dir_items = []
pb_sub_dir = []
count = 1
all_list = os.listdir(path)

# 获取每个文件夹的路径 dir_name:/Users/xujintao/Downloads/1-30/00xx
for i in range(len(all_list) - 2):
    if count < 10:
        source_name = path + "000%d" % count
        dir_name.append(source_name)
        count += 1
    else:
        source_name = path + "00%d" % count
        dir_name.append(source_name)
        count += 1

# 获取每一个文件名:englishpod_X00xxpb.mp3
for i in range(count - 2):
    sub_dir_items = os.listdir(dir_name[i])
    for i in sub_dir_items:
        if "pb" in i:
            pb_sub_dir.append(i)

for i in range(len(pb_sub_dir)):
    pass

for i in range(len(all_list) - 3):
    res_path = dir_name[i] + "/" + pb_sub_dir[i]
    print("复制成功: " + res_path)
    shutil.copy(res_path, target)
