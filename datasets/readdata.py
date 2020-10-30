def reversal_middle(originPic,):
    # trans gray pic : black to white ,or white to black
    pic = originPic
    print(pic.shape )
    pic_reversal  = pic.copy()
    height  , width = pic.shape
    for i in range(height):
        for j in range(width):
            pic_reversal[i,j] = 255-pic_reversal[i,j]

    return pic_reversal

def erode_demo(image):
    # 腐蚀算法
    print(image.shape)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # cv2.imshow("binary", binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.erode(binary, kernel)
    # cv2.imshow("erode", dst)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return dst


def Morphology_Dilate(img, Dil_time=1):
    # 膨胀算法
    import numpy as np

    H, W = img.shape


    # kernel
    MF = np.array(((0, 1, 0),
            (1, 0, 1),
           (0, 1, 0)), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Dil_time):

         tmp = np.pad(out, (1, 1), 'edge')
         for y in range(1, H):
             for x in range(1, W):
                 if np.sum(MF * tmp[y-1:y+2, x-1:x+2]) >= 255:
                     out[y, x] = 255

    return out


def gaussian_filter(img, K_size=3, sigma=1.3):
    import numpy as np
    if len(img.shape) == 3:

        H, W, C = img.shape

    else:

        img = np.expand_dims(img, axis=-1)

        H, W, C = img.shape

    ## Zero padding

    pad = K_size // 2

    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)

    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)

    ## prepare Kernel

    K = np.zeros((K_size, K_size), dtype=np.float)

    for x in range(-pad, -pad + K_size):

        for y in range(-pad, -pad + K_size):
            K[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))

    K /= (2 * np.pi * sigma * sigma)

    K /= K.sum()

    tmp = out.copy()

    # filtering

    for y in range(H):

        for x in range(W):

            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = np.clip(out, 0, 255)

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    h, w, c = out.shape
    gauss = np.resize(out, new_shape=(h, w))

    return gauss

if __name__ == '__main__':
    import  numpy as np
    import cv2
    filename = './0000_00_1.png'
    img = cv2.imread(filename=filename,flags=0)
    erode = erode_demo(img)
    # 腐蚀后的pic
    cv2.imshow('erode pic ',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(img)

    # 膨胀后的pic
    bigger = Morphology_Dilate(img)
    cv2.imshow('bigger pic ',bigger)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 膨胀的反转，就是细化
    smaller  =reversal_middle(bigger)
    cv2.imshow('smaller pic ', smaller)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # gauss operation
    gauss = gaussian_filter(img=smaller)
    gauss = reversal_middle(gauss)

    # h,w,c= gauss.shape
    # gauss = np.resize(gauss,new_shape=(h,w))
    cv2.imshow('gauss pic ', gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




