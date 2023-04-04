import os
import shutil

import csv
import json

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
    os.chdir('..')
    os.mkdir('labels')
    os.chdir('labels')
    os.mkdir('train')
    os.mkdir('val')
    os.chdir(tmp)

def labelme2YOLOv5(target, relJson):
    targetDirImg = DataStoreDir + '/images/' + target
    targetDirLab = DataStoreDir + '/labels/' + target
    relImage = relJson.replace('.json', '.jpg')
    # Make Target Data: IMG
    shutil.copy(relImage, targetDirImg + '/' + relImage)
    # Make Target Data: Poly (GT)
    h, w, _ = cv2.imread(relImage).shape
    with open(relJson) as f:
        data = json.load(f)
    for i in range(len(data['shapes'])):
        tmp = data['shapes'][i]['points'] 
        tar = []
        cnt = 0
        for j in tmp:
            for k in j:
                if cnt % 2 == 0:
                    tar.append(k/w)
                else:
                    tar.append(k/h)
        with open(targetDirLab + '/' + relJson.replace('.json', '.txt'), 'a', encoding='utf-8') as f:
            wr = csv.writer(f, delimiter=' ')
            wr.writerow([0, *tar])

if __name__ == "__main__":
    DataStoreName = "labelme"
    os.chdir('..')
    initializeData(DataStoreName)

    datasets = os.getcwd()
    DataStoreDir = datasets + '/' + DataStoreName

    os.chdir('tmp')

    candidate = []
    for i in os.listdir():
        if '.json' in i:
            candidate.append(i)

    cnt = 0
    for c in tqdm(candidate):
        if cnt % 3 == 0:
            labelme2YOLOv5('val', c)
        else:
            labelme2YOLOv5('train', c)
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

    print('=' * 30)
    print('No. Total Image Data: ', tin + vin)
    print('No. Total GT Data: ', ttn + vtn)
    print('=' * 30)

    os.chdir(datasets + '/MakeData')