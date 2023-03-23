import os
import shutil

import csv
import numpy as np
import pandas as pd

from tqdm import tqdm
import cv2


def initializeData():
    tmp = os.getcwd()
    try:
        os.chdir('FlickrLogos-v2')
    except Exception as e:
        print('There is no FlickrLogos-v2')
        print(e)
        os.chdir(tmp)
        return
    try:
        shutil.rmtree('images')
    except:
        pass
    try:
        shutil.rmtree('labels')
    except:
        pass
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


def saveData(target, brand, img):
    targetDirImg = datasets + '/FlickrLogos-v2/images/' + target
    targetDirLab = datasets + '/FlickrLogos-v2/labels/' + target
    absDataDir = datasets + '/FlickrLogos-v2'
    # Make Target Data: IMG
    absImgDir = absDataDir + '/classes/jpg/' + brand + '/' + img
    shutil.copy(absImgDir, targetDirImg + '/' + img)
    # Make Target Data: Bbox (GT)
    absBboxDir = absDataDir + '/classes/masks/' + brand.lower() + '/' + img + '.bboxes.txt'
    mh, mw, _ = cv2.imread(absImgDir).shape
    bbox = pd.read_csv(absBboxDir, sep=' ')
    with open(targetDirLab + '/' + img[:-4] + '.txt', 'a', encoding='utf-8') as f:
        wr = csv.writer(f, delimiter=' ')
        for i in range(len(bbox)):
            x, y, width, height = bbox.iloc[i]
            wr.writerow([0, x / mw + mw // 2, y / mh + mh // 2, width / mw, height / mh])

if __name__ == "__main__":
    os.chdir('..')
    initializeData()

    datasets = os.getcwd()

    os.chdir(datasets + '/FlickrLogos-v2/classes/jpg')
    brands = os.listdir()

    cnt = 0
    for brand in tqdm(brands):
        if not '.' in brand and not brand == 'no-logo':
            os.chdir(datasets + '/FlickrLogos-v2/classes/jpg/' + brand)
            for img in os.listdir():
                if '.jpg' in img:
                    if cnt % 12 == 0:
                        saveData('val', brand, img)
                    elif cnt % 12 == 1:
                        saveData('test', brand, img)
                    else:
                        saveData('train', brand, img)
                    cnt += 1

    print('=' * 30)
    print('No. Total Data: ', cnt)
    print('=' * 30)

    os.chdir(datasets + '/FlickrLogos-v2/images/train')
    tin = len(os.listdir())
    print('Training Data: No. Images', tin)

    os.chdir(datasets + '/FlickrLogos-v2/labels/train')
    ttn = len(os.listdir())
    print('Training Data: No. GT', ttn)

    os.chdir(datasets + '/FlickrLogos-v2/images/val')
    vin = len(os.listdir())
    print('Validation Data: No. Images', vin)

    os.chdir(datasets + '/FlickrLogos-v2/labels/val')
    vtn = len(os.listdir())
    print('Validation Data: No. GT', vtn)

    os.chdir(datasets + '/FlickrLogos-v2/images/test')
    ttin = len(os.listdir())
    print('Test Data: No. Images', ttin)

    os.chdir(datasets + '/FlickrLogos-v2/labels/test')
    tttn = len(os.listdir())
    print('Test Data: No. GT', tttn)

    print('=' * 30)
    print('No. Total Image Data: ', tin + vin + ttin)
    print('No. Total GT Data: ', ttn + vtn + tttn)
    print('=' * 30)

    os.chdir(datasets + '/MakeData')