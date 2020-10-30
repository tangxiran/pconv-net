

def copyfile(origin_filename, targetFile):
    import shutil
    shutil.copy(origin_filename, targetFile)

def data_select(data_dir):  #
    import  glob
    file_list = list(glob.glob(data_dir + '/*.png')) + list(glob.glob(data_dir + '/*.jpg'))   # get name list of all .png files
    data = []
    print(file_list) # 得到文件的路径列表
    return file_list
if __name__ == '__main__':
    filelist = data_select('../masks')
    for file in filelist:
        mask = cv2.imread(filename=file_mask, flags=0)