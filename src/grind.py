#Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100
import cv2

def mopi(img):
    value1=3
    value2=1#磨皮程度与细节程度的确定
    dx=value1*5#双边滤波参数之一
    fc=value1*12.5#双边滤波参数之一
    p=0.1#透明度
    temp1=cv2.bilateralFilter(img,dx,fc,fc)
    temp2 = (temp1 - img + 128)
    temp3=cv2.GaussianBlur(temp2,(2*value2-1,2*value2-1),0,0)
    temp4 = img + 2 * temp3 - 255
    dst = (img * (100 - p) + temp4 * p) / 100
    dst=cv2.addWeighted(img, p, temp4, 1 - p, 0.0)
    return dst

