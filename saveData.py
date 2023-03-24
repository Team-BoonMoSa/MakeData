import os
import shutil

import csv
import numpy as np
import pandas as pd

from tqdm import tqdm
import cv2


def initializeData(DataStoreName):
    tmp = os.getcwd()
    if DataStoreName in os.listdir():
        shutil.rmtree(DataStoreName)
    os.mkdir(DataStoreName)
    os.chdir(DataStoreName)
    os.mkdir('images')
    os.chdir('images')
    os.mkdir('train')
    os.mkdir('val')
    os.mkdir('test')
    os.chdir('..')
    os.mkdir('labels')
    os.chdir('labels')
    os.mkdir('train')
    os.mkdir('val')
    os.mkdir('test')
    os.chdir(tmp)

def makePoly(relMask):
    tmp = cv2.imread(relMask)
    mh, mw, _ = tmp.shape
    tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(tmp, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    tmp = np.array(contours[0]/[mw, mh])
    poly = tmp.reshape(len(contours[0])*2)
    return poly
    
def saveData(target, relImg):
    targetDirImg = DataStoreDir + '/images/' + target
    targetDirLab = DataStoreDir + '/labels/' + target
    imgName = relImg[-13:]
    # Make Target Data: IMG
    shutil.copy(relImg, targetDirImg + '/' + imgName)
    # Make Target Data: Poly (GT)
    gt = relImg.replace('.png', '.gt_data.txt')
    gt = pd.read_csv(gt, sep=' ', header=None)
    with open(targetDirLab + '/' + imgName.replace('.png', '.txt'), 'a', encoding='utf-8') as f:
        wr = csv.writer(f, delimiter=' ')
        for i in range(len(gt)):
            mask = gt.iloc[i, 6]
            relMask = relImg.replace('.png', '.' + mask + '.png')
            poly = makePoly(relMask)
            wr.writerow([0, *poly])

if __name__ == "__main__":
    DataStoreName = "LogoRec"
    os.chdir('..')
    initializeData(DataStoreName)

    datasets = os.getcwd()
    DataStoreDir = datasets + '/' + DataStoreName

    candidate = []
    
    tmp = "train/filelist-logosonly"
    file = open("FlickrLogos_47/" + tmp + ".txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        candidate.append('./FlickrLogos_47/train' + line.strip()[1:])

    tmp = "test/filelist"
    file = open("FlickrLogos_47/" + tmp + ".txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        candidate.append('./FlickrLogos_47/test' + line.strip()[1:])

    cnt = 0
    for c in tqdm(candidate):
        if cnt % 12 == 0:
            saveData('val', c)
        elif cnt % 12 == 1:
            saveData('test', c)
        else:
            saveData('train', c)
        cnt += 1

    print('=' * 30)
    print('No. Total Data: ', cnt)
    print('=' * 30)

    os.chdir(DataStoreDir + '/images/train')
    tin = len(os.listdir())
    print('Training Data: No. Images', tin)

    os.chdir(DataStoreDir + '/labels/train')
    ttn = len(os.listdir())
    print('Training Data: No. GT', ttn)

    os.chdir(DataStoreDir + '/images/val')
    vin = len(os.listdir())
    print('Validation Data: No. Images', vin)

    os.chdir(DataStoreDir + '/labels/val')
    vtn = len(os.listdir())
    print('Validation Data: No. GT', vtn)

    os.chdir(DataStoreDir + '/images/test')
    ttin = len(os.listdir())
    print('Test Data: No. Images', ttin)

    os.chdir(DataStoreDir + '/labels/test')
    tttn = len(os.listdir())
    print('Test Data: No. GT', tttn)

    print('=' * 30)
    print('No. Total Image Data: ', tin + vin + ttin)
    print('No. Total GT Data: ', ttn + vtn + tttn)
    print('=' * 30)

    os.chdir(datasets + '/MakeData')