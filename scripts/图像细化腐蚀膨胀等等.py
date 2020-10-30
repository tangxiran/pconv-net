def reversal_Sharpe(originPic_file_savePlace,outoutPic_file_savePlace ):
    # trans gray pic : black to white ,or white to black
    import cv2
    pic = cv2.imread(originPic_file_savePlace,0)
    print(pic.shape )
    pic_reversal  = pic.copy()
    height  , width = pic.shape
    for i in range(height):
        for j in range(width):
            if not pic_reversal[i,j] ==0 :
                pic_reversal[i,j] =0
            else:
                pic_reversal[i,j] = 255
    print('origin pic is \n', pic)
    print('the pic after reverse  \n', pic_reversal)
    cv2.imwrite(outoutPic_file_savePlace, pic_reversal)
    cv2.imshow("origin", pic)
    cv2.imshow('now ', pic_reversal)
    cv2.waitKey(1
                )
    cv2.destroyAllWindows()

def reversal_middle(originPic_file_savePlace,outoutPic_file_savePlace ):
    # trans gray pic : black to white ,or white to black
    import cv2
    pic = cv2.imread(originPic_file_savePlace,0)
    print(pic.shape )
    pic_reversal  = pic.copy()
    height  , width = pic.shape
    for i in range(height):
        for j in range(width):
            pic_reversal[i,j] = 255-pic_reversal[i,j]
    print('origin pic is \n',pic  )
    print('the pic after reverse  \n',pic_reversal )
    cv2.imwrite(outoutPic_file_savePlace,pic_reversal)
    cv2.imshow("origin" , pic)
    cv2.imshow('now ' , pic_reversal )
    cv2.waitKey(1
                )
    cv2.destroyAllWindows()
    return pic_reversal

def makedir(dir):
    import os
    dir = dir.strip()
    isExist = os.path.exists(dir)
    if not isExist:
        os.makedirs(dir)
        return True
    else:
        return False

# 遍历得到某个文件夹下的所有文件名
def getFileName(dirName):
    import os
    fileList= []
    filePath = dirName
    for i, j, k in os.walk(filePath):
        # i是当前路径，j得到文件夹名字，k得到文件名字
        print(i, j, k)
        fileList.append(k)
    return fileList

if __name__ == '__main__':
    # - trans gray pic : black to white ,or white to black  ----

    # the pic in which dir u want to transform
    origin_dir =  r'F://wxt//PConv//testPic_200//test_origin//'
    # the pic in which dir u want to save
    output_dir =  'F://wxt//PConv//testPic_200//test_origin//good//'
    makedir(output_dir)
    filelist = getFileName(origin_dir)
    for file in filelist[0]:
        originPic_file_savePlace =  origin_dir + file
        outoutPic_file_savePlace = output_dir + file

        # 调用哪个函数？
        # reversal_Sharpe(originPic_file_savePlace,outoutPic_file_savePlace.replace('.png','')+'shape.png')
        reversal_middle(originPic_file_savePlace, outoutPic_file_savePlace)