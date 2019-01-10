#!python

"""
In data_aishell, the transcripts are put in a single file. While running 
deepspeech.pytorch (https://github.com/SeanNaren/deepspeech.pytorch.git), 
we need to specify the corresponding transcript file for each audio file. 
This python script is used to separate the single transcript file into 
multiple files.
"""

from __future__ import absolute_import, division, print_function

import argparse
import codecs
import os

parser = argparse.ArgumentParser(description='Processes transcripts in aishell data.')
parser.add_argument('--source-file', type=str,
                    default='transcript/aishell_transcript_v0.8.txt',
                    help='Source transcript file in aishell data (a single file)')
parser.add_argument('--target-dir', type=str,
                    default=None, help='Filepath for storing the target transcript files',
                    required=True)
args = parser.parse_args()

def main():
    print("---------------  Configuration Arguments ---------------")
    for arg, value in sorted(vars(args).iteritems()):
        print("%s: %s" % (arg, value))
    print("--------------------------------------------------------")
    transcript_dict = {}
    file_names = []
    for line in codecs.open(args.source_file, 'r', 'utf-8'):
        line = line.strip()
        if line == '': continue
        audio_id, text = line.split(' ', 1)
        text = text.strip()
        file_names.append(audio_id)
        transcript_dict[audio_id] = text
    if os.path.isdir(args.target_dir):
        print('Directory', args.target_dir, 'already exists.')
        print('Transcript files will be written to this directory.')
    else:
        print('Creating directory', args.target_dir)
        os.system('mkdir '+args.target_dir)
    print(transcript_dict[file_names[0]])
    for f1 in file_names:
        codecs.open(args.target_dir+'/'+f1+'.txt',
                   'w', 'utf-8').write(transcript_dict[f1])

if __name__ == '__main__':
    main()
