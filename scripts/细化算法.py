

# hilditch thining
def hilditch(img_saveplace):
    import cv2
    import  numpy as np

    img = (cv2.imread(filename=img_saveplace)).astype(np.float32)

    # get shape
    H, W, C = img.shape


    # prepare out image
    out = np.zeros((H, W), dtype=np.int)
    out[img[..., 0] > 0] = 1

    # inverse pixel value
    tmp = out.copy()
    _tmp = 1 - tmp

    count = 1
    while count > 0:
        count = 0
        tmp = out.copy()
        _tmp = 1 - tmp

        tmp2 = out.copy()
        _tmp2 = 1 - tmp2

        # each pixel
        for y in range(H):
            for x in range(W):
                # skip black pixel
                if out[y, x] < 1:
                    continue

                judge = 0

                ## condition 1
                if (tmp[y, min(x + 1, W - 1)] * tmp[max(y - 1, 0), x] * tmp[y, max(x - 1, 0)] * tmp[
                    min(y + 1, H - 1), x]) == 0:
                    judge += 1

                ## condition 2
                c = 0
                c += (_tmp[y, min(x + 1, W - 1)] - _tmp[y, min(x + 1, W - 1)] * _tmp[max(y - 1, 0), min(x + 1, W - 1)] *
                      _tmp[max(y - 1, 0), x])
                c += (_tmp[max(y - 1, 0), x] - _tmp[max(y - 1, 0), x] * _tmp[max(y - 1, 0), max(x - 1, 0)] * _tmp[
                    y, max(x - 1, 0)])
                c += (_tmp[y, max(x - 1, 0)] - _tmp[y, max(x - 1, 0)] * _tmp[min(y + 1, H - 1), max(x - 1, 0)] * _tmp[
                    min(y + 1, H - 1), x])
                c += (_tmp[min(y + 1, H - 1), x] - _tmp[min(y + 1, H - 1), x] * _tmp[
                    min(y + 1, H - 1), min(x + 1, W - 1)] * _tmp[y, min(x + 1, W - 1)])
                if c == 1:
                    judge += 1

                ## condition 3
                if np.sum(tmp[max(y - 1, 0): min(y + 2, H), max(x - 1, 0): min(x + 2, W)]) >= 3:
                    judge += 1

                ## condition 4
                if np.sum(out[max(y - 1, 0): min(y + 2, H), max(x - 1, 0): min(x + 2, W)]) >= 2:
                    judge += 1

                ## condition 5
                _tmp2 = 1 - out

                c = 0
                c += (_tmp2[y, min(x + 1, W - 1)] - _tmp2[y, min(x + 1, W - 1)] * _tmp2[
                    max(y - 1, 0), min(x + 1, W - 1)] * _tmp2[max(y - 1, 0), x])
                c += (_tmp2[max(y - 1, 0), x] - _tmp2[max(y - 1, 0), x] * (1 - tmp[max(y - 1, 0), max(x - 1, 0)]) *
                      _tmp2[y, max(x - 1, 0)])
                c += (_tmp2[y, max(x - 1, 0)] - _tmp2[y, max(x - 1, 0)] * _tmp2[min(y + 1, H - 1), max(x - 1, 0)] *
                      _tmp2[min(y + 1, H - 1), x])
                c += (_tmp2[min(y + 1, H - 1), x] - _tmp2[min(y + 1, H - 1), x] * _tmp2[
                    min(y + 1, H - 1), min(x + 1, W - 1)] * _tmp2[y, min(x + 1, W - 1)])
                if c == 1 or (out[max(y - 1, 0), max(x - 1, 0)] != tmp[max(y - 1, 0), max(x - 1, 0)]):
                    judge += 1

                c = 0
                c += (_tmp2[y, min(x + 1, W - 1)] - _tmp2[y, min(x + 1, W - 1)] * _tmp2[
                    max(y - 1, 0), min(x + 1, W - 1)] * (1 - tmp[max(y - 1, 0), x]))
                c += ((1 - tmp[max(y - 1, 0), x]) - (1 - tmp[max(y - 1, 0), x]) * _tmp2[max(y - 1, 0), max(x - 1, 0)] *
                      _tmp2[y, max(x - 1, 0)])
                c += (_tmp2[y, max(x - 1, 0)] - _tmp2[y, max(x - 1, 0)] * _tmp2[min(y + 1, H - 1), max(x - 1, 0)] *
                      _tmp2[min(y + 1, H - 1), x])
                c += (_tmp2[min(y + 1, H - 1), x] - _tmp2[min(y + 1, H - 1), x] * _tmp2[
                    min(y + 1, H - 1), min(x + 1, W - 1)] * _tmp2[y, min(x + 1, W - 1)])
                if c == 1 or (out[max(y - 1, 0), x] != tmp[max(y - 1, 0), x]):
                    judge += 1

                c = 0
                c += (_tmp2[y, min(x + 1, W - 1)] - _tmp2[y, min(x + 1, W - 1)] * (
                            1 - tmp[max(y - 1, 0), min(x + 1, W - 1)]) * _tmp2[max(y - 1, 0), x])
                c += (_tmp2[max(y - 1, 0), x] - _tmp2[max(y - 1, 0), x] * _tmp2[max(y - 1, 0), max(x - 1, 0)] * _tmp2[
                    y, max(x - 1, 0)])
                c += (_tmp2[y, max(x - 1, 0)] - _tmp2[y, max(x - 1, 0)] * _tmp2[min(y + 1, H - 1), max(x - 1, 0)] *
                      _tmp2[min(y + 1, H - 1), x])
                c += (_tmp2[min(y + 1, H - 1), x] - _tmp2[min(y + 1, H - 1), x] * _tmp2[
                    min(y + 1, H - 1), min(x + 1, W - 1)] * _tmp2[y, min(x + 1, W - 1)])
                if c == 1 or (out[max(y - 1, 0), min(x + 1, W - 1)] != tmp[max(y - 1, 0), min(x + 1, W - 1)]):
                    judge += 1

                c = 0
                c += (_tmp2[y, min(x + 1, W - 1)] - _tmp2[y, min(x + 1, W - 1)] * _tmp2[
                    max(y - 1, 0), min(x + 1, W - 1)] * _tmp2[max(y - 1, 0), x])
                c += (_tmp2[max(y - 1, 0), x] - _tmp2[max(y - 1, 0), x] * _tmp2[max(y - 1, 0), max(x - 1, 0)] * (
                            1 - tmp[y, max(x - 1, 0)]))
                c += ((1 - tmp[y, max(x - 1, 0)]) - (1 - tmp[y, max(x - 1, 0)]) * _tmp2[
                    min(y + 1, H - 1), max(x - 1, 0)] * _tmp2[min(y + 1, H - 1), x])
                c += (_tmp2[min(y + 1, H - 1), x] - _tmp2[min(y + 1, H - 1), x] * _tmp2[
                    min(y + 1, H - 1), min(x + 1, W - 1)] * _tmp2[y, min(x + 1, W - 1)])
                if c == 1 or (out[y, max(x - 1, 0)] != tmp[y, max(x - 1, 0)]):
                    judge += 1

                if judge >= 8:
                    out[y, x] = 0
                    count += 1

    out = out.astype(np.uint8) * 255

    return out

# 特定的文件后缀保存
def data_select(data_dir):  #
    import  glob
    file_list = list(glob.glob(data_dir + '/*.png')) + list(glob.glob(data_dir + '/*.jpg')) +list(glob.glob(data_dir + '/*.JPG'))   # get name list of all .png files
    data = []
    # print(file_list) # 得到文件的路径列表
    return file_list
if __name__ == '__main__':
    import cv2
    import numpy as np
    dir = r'F:\all_datas\gray_mask'
    data = data_select(dir)
    # print(data_select(dir))
    # for i in range(len(data)):
    #     if i >1266:
    #         pic = data[i]
    #
    # #
    # #
    count = 0
    for pic in data:
        count = count +1
        print('is dealing No',count,'picture')
        print('origin pic place ;',pic)

        out_temp  = hilditch(img_saveplace=pic)
        out_saveplace = ((pic.replace('.png','.png'))).replace('gray_mask',r'gray_mask\thin')
        print('save at :',out_saveplace)
        cv2.imwrite(out_saveplace, out_temp)
        # 展示一下
        # cv2.imshow("result", out_temp)
        # cv2.waitKey(1)
        # cv2.destroyAllWindows()