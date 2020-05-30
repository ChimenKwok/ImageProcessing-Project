import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram (pic):
    img = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img)
    n_k = np.zeros([256, 1])
    for pixel in V.flatten():
        n_k[pixel] += 1
    plt.plot(n_k)

def histogram_equalization(pic):
    img = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img)
    n_k = np.zeros([256, 1])
    for pixel in V.flatten():
        n_k[pixel] += 1
    p_r = n_k / V.size
    s_k = np.zeros([256, 1])

    for i in range(0, len(p_r)):
        p_sum_k = sum(p_r[0:i, :])
        s_k[i] = np.around(255 * p_sum_k)

    for i in range(0, len(V)):
        for j in range(0, len(V.T)):
            V[i][j] = s_k[V[i][j]]

    img = cv2.merge([H, S, V])
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img

def rotate(img):
    img = np.rot90(img,k=1,axes=(0,1))
    return img

def upsidedown(img):
    img = np.flipud(img)
    return img

def flipLeftToRight(img):
    img = np.fliplr(img)
    return img

def RGBToWhite(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img[:,:,1]=0
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img

def adjustS(img, n):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img[:,:,1]+=n
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    return img

def histogram_equalization_opti(pic):
    img = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img)
    n_k = np.zeros([256, 1])
    out_put_V = np.copy(V)

    for i in range(256):
        n_k[i] = np.sum(out_put_V == i)
    p_r = n_k / out_put_V.size
    s_k = np.zeros([256, 1])

    for i in range(256):
        p_sum_r = np.sum(p_r[0:i])
        s_k[i] = np.around(255 * p_sum_r)

    for i in range(256):
        out_put_V[np.where(V == i)] = s_k[i]

    V = out_put_V

    img = cv2.merge([H, S, V])
    #img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    return img

def histogram_opti(pic):
    img = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img)
    n_k = np.zeros([256, 1])
    for i in range(256):
        n_k[i] = np.sum(V==i)
    plt.plot(n_k)
