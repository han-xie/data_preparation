#!/usr/bin/env python
# coding=utf-8

"""
Prepare Aishell mandarin dataset
Create manifest files.
Manifest file is a file with each line containing the
meta data (i.e. audio filepath and transcript filepath)
of each audio file in the data set.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

DATA_HOME = "/root/speech_data/data_aishell/"
data_types = ['train', 'dev', 'test']
for dt1 in data_types:
    path_lines = []
    audio_dir = os.path.join(DATA_HOME, 'wav', dt1)
    fout = open('aishell_'+dt1+'_manifest.csv', 'w')
    for subfolder, _, filelist in sorted(os.walk(audio_dir)):
        for fname in filelist:
            audio_path = os.path.join(subfolder, fname)
            audio_id = fname[:-4]
            txt_path = os.path.join(DATA_HOME, 'txt_han', audio_id+'.txt')
            if not os.path.exists(txt_path): continue
            fout.write(audio_path+','+txt_path+'\n')
    fout.close()
