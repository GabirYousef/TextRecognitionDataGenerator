import os
import string
import random
import cv2

def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

def write_line(line):
    with open("gt.txt", "a") as f:
        f.write(line + "\n")


imgs_dir = "/home/ec2-user/TextRecognitionDataGenerator/out"
new_imgs = "/home/ec2-user/TextRecognitionDataGenerator/out-new"

for line in os.listdir(imgs_dir):
    name = get_random_string(15)
    print(name)
   #  print("line: ", line)
    img = cv2.imread(os.path.join(imgs_dir, line))
    cv2.imwrite(os.path.join(new_imgs, name + ".jpg"), img)
            # os.rename(self.data_directory + line, self.output_dir + name + ".jpg")
            # file_name = line.split('_')[1][:-4]
    gt = line.split("_")[0][::-1]
    # print("gt: ", gt)
    # new_gt, new_char_lst = self.check_gt(gt, new_char_lst)
    # threshold = 120
    new_line = name + ".jpg" + " " + gt
    write_line(new_line)
    #break
