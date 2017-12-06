import cv2
highlights_add = highlights_sub = midtones_add = midtones_sub = shadows_add = shadows_sub = [0]*256
for i in range(256):
    highlights_add[i] = shadows_sub[255 - i] = (1.075 - 1/( i*1.0 / 16.0 + 1))
    midtones_add[i] = midtones_sub[i] = 0.667 * (1 - (( i*1.0 - 127.0) / 127.0)*(( i*1.0 - 127.0) / 127.0))
    shadows_add[i] = highlights_sub[i] = 0.667 * (1 - (( i*1.0 - 127.0) / 127.0)*(( i*1.0 - 127.0) / 127.0))
def FMax(X, Y):
    return Y if X < Y else X
def FMin(X, Y):
    return X if X < Y else Y
def BalanceColor(image,value):
    img = image
    r_lookup = g_lookup = b_lookup =[0]*256
    for i in range(256):
        red = i;green = i;blue = i
        red += (int)(0.0 * shadows_sub[red] + value * midtones_add[red] + 0.0 * highlights_sub[red])
        red = FMax(0, FMin(0xFF, red))
        green += (int)(0.0 * shadows_sub[green] + value * midtones_add[green] + 0.0 * highlights_sub[green])
        green = FMax(0, FMin(0xFF, green))
        blue += (int)(0.0 * shadows_sub[blue] + value * midtones_add[blue] + 0.0 * highlights_sub[blue])
        blue = FMax(0, FMin(0xFF, blue))
        r_lookup[i] = red
        g_lookup[i] = green
        b_lookup[i] = blue
    rows, cols, bows = img.shape
    for i in range(rows):
         for j in range(cols):
            img[i, j][0] = b_lookup[img[i, j][0]]
            img[i, j][1] = g_lookup[img[i, j][1]]
            img[i, j][2] = r_lookup[img[i, j][2]]
    return img