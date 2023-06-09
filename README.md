# How to use?

### labelme2YOLOv5.py

```shell
Parent
└── datasets
    ├── MakeData
    │   └─ labelme2YOLOv5.py
    └── tmp
        ├── data1.jpeg
        ├── data1.json
        ├── ...
```

```python
Parent/datasets/MakeData$ python labelme2YOLOv5.py
100%|█████████████████████████████████████████████| 5/5 [00:00<00:00,  9.03it/s]
==============================
No. Total Data:  5
==============================
Training Data: No. Images 3
Training Data: No. GT 3
Validation Data: No. Images 2
Validation Data: No. GT 2
==============================
No. Total Image Data:  5
No. Total GT Data:  5
==============================
```

> Result

```shell
labelme
├── images
│   ├── train
│   └── val
└── labels
    ├── train
    └── val
```

### saveData.py

```shell
Parent
└── datasets
    ├── FlickrLogos_47
    │   ├── scripts
    │   ├── test
    │   │   ├── 000000
    │   │   ├── 000001
    │   │   └── 000002
    │   └── train
    │       ├── 000000
    │       ├── 000001
    │       ├── 000002
    │       └── no-logo
    └── MakeData
        ├── checkData.py
        └── saveData.py
```

```shell
Parent/datasets/MakeData$ python saveData.py
100%|████████████████████████████████████████████████████████████████████████| 2235/2235 [00:45<00:00, 49.47it/s]
==============================
No. Total Data:  2235
==============================
Training Data: No. Images 1861
Training Data: No. GT 1861
Validation Data: No. Images 187
Validation Data: No. GT 187
Test Data: No. Images 187
Test Data: No. GT 187
==============================
No. Total Image Data:  2235
No. Total GT Data:  2235
==============================
```

> Result

```shell
LogoRec
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
Parent/datasets/MakeData$ python checkData.py
==================== train ====================
Images:  1861
Ground Truth:  1861
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