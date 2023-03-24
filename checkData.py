import os


def checkData(target):
    os.chdir(init + '/LogoRec')
    try:
        os.chdir('images/' + target)
    except:
        print('경로가 없어용 ~')
    
    imgDir = os.getcwd()
    img = os.listdir()
    
    labDir = imgDir.replace('images', 'labels')
    lab = os.listdir()

    tmpi = []
    for i in img:
        tmpi.append(i[:-4])

    tmpj = []
    for i in lab:
        tmpj.append(i[:-4])

    for i in tmpi:
        if not i in tmpj and not 'ipynb' in i:
            print('NG: ', i)

    for i in tmpj:
        if not i in tmpi and not 'ipynb' in i:
            print('NG: ', i)

    print('='*20, target, '='*20)
    print('Images: ', len(img))
    print('Ground Truth: ', len(lab))
    print('='*20, target, '='*20)

if __name__ == "__main__":
    os.chdir('..')
    init = os.getcwd()
    try:
        os.chdir(init + '/LogoRec')
    except:
        print('경로가 없어용 ~')

    checkData('train')
    checkData('val')
    checkData('test')