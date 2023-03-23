```shell
Parent
└── datasets
    ├── FlickrLogos-v2
    │   ├── classes
    │   │   ├── jpg
    │   │   ├── masks
    │   │   └── thumbnails
    │   └── scripts
    └── MakeData
        ├── checkData.py
        └── saveData.py
```

# How to use?

### saveData.py

```shell
Paraent/datasets/MakeData$ python saveData.py
100%|████████████████████████████████████████████████████████████████| 33/33 [00:26<00:00,  1.27it/s]
==============================
No. Total Data:  2240
==============================
Training Data: No. Images 1866
Training Data: No. GT 1866
Validation Data: No. Images 187
Validation Data: No. GT 187
Test Data: No. Images 187
Test Data: No. GT 187
==============================
No. Total Image Data:  2240
No. Total GT Data:  2240
==============================
```

> Result

```shell
FlickrLogos-v2
├── images
│   ├── test
│   ├── train
│   └── val
└── labels
    ├── test
    ├── train
    └── val
```

### checkData.py

```shell
Paraent/datasets/MakeData$ python checkData.py
==================== train ====================
Images:  1866
Ground Truth:  1866
==================== train ====================
==================== val ====================
Images:  187
Ground Truth:  187
==================== val ====================
==================== test ====================
Images:  187
Ground Truth:  187
==================== test ====================
```