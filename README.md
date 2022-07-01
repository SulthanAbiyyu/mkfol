# MKFOL

Module untuk membuat folder berdasarkan template

## Latar Belakang

Lelah membuat folder-folder yang sama berulang kali

## Installation

Via git clone

```bash
git clone https://github.com/SulthanAbiyyu/mkfol
```

Via pip

```bash
pip install mkfol
```

## Usage

**Make semester folder**

```bash
mkfol -s 3 "DAA,IMK,STAT"
```

The result will look something like this:

```
└──  semester 3
    ├── DAA
    │   ├── tugas
    │   ├── materi
    │   ├── quiz
    │   ├── UTS
    │   ├── UAS
    │   └── lain-lain
    ├── IMK
    │   ├── tugas
    │   ├── materi
    │   ├── quiz
    │   ├── UTS
    │   ├── UAS
    │   └── lain-lain
    └── STAT
        ├── tugas
        ├── materi
        ├── quiz
        ├── UTS
        ├── UAS
        └── lain-lain
```

## Project Plan

- [x] Semester folder
- [x] Data science / machine learning project folder

Any suggestion for more template folders? please open a new issue
