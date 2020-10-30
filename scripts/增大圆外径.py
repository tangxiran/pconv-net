def data_select(data_dir):  #
    import  glob
    file_list = list(glob.glob(data_dir + '/*.png')) + list(glob.glob(data_dir + '/*.jpg'))   # get name list of all .png files
    data = []
    print(file_list) # 得到文件的路径列表
    return file_list

def copyfile(origin_filename, targetFile):
    import shutil
    shutil.copy(origin_filename, targetFile)
def bigerpic(img,num_point):
    for i in range(num_point):
        import cv2

        mask = img
        print(mask)
        height, width = mask.shape
        mask_copy = mask.copy()
        for i in range(height - 1):
            for j in range(width - 1):
                if mask[i, j] == 0:
                    if (mask[i - 1, j - 1] == 255 or mask[i - 1, j - 0] == 255 or mask[i - 1, j + 1] == 255 or mask[
                        i - 0, j - 1] == 255 or mask[i - 0, j + 1] == 255 or mask[i + 1, j - 1] == 255 or mask[
                        i + 1, j + 0] == 255 or mask[i + 1, j + 1] == 255):
                        mask_copy[i, j] = 255
        mask_copy = mask_copy
        return mask_copy

if __name__ == '__main__':
    # 扩大轮廓的外边缘几个像素
    filelist  =data_select('../masks')
    num_point = 1
    file_to_copy = '../masks/origin/0000_00_0.png'
    for file in filelist:

        # 扩大轮廓的外边缘几个像素
        file_mask  = file
        file_to_paste = file_mask.replace('masks','masks/thin')
        copyfile(file_to_copy,file_to_paste)