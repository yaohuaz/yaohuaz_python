import numpy as np
import cv2
import sys
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-img',
                        help='input image path',
                        required=True,
                        type=str
                        )
    parser.add_argument('--output-filename',
                        help='output txt filename',
                        default='output.txt',
                        type=str
                        )
    parser.add_argument('--output-path',
                        help='output txt file path',
                        default=os.getcwd(),
                        type=str
                        )
    args, _ = parser.parse_known_args()
    

    if not os.path.exists(args.input_img):
        raise RuntimeError('File Not Found')
    img = cv2.imread(args.input_img)
    height, width = img.shape[:2]
    img = cv2.resize(img, 
                     (128, 96), 
                     interpolation=cv2.INTER_AREA
                     )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = []
    tmp_str = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. \")\"'`")
    tmp_len = len(tmp_str)
    for row in img:
        for col in row:
            # if col == 255:
            if col > 245:
                res.append(' ')
            else:
                res.append(tmp_str[col%tmp_len])
        res.append('\n')
    res = ''.join(res)
    output = os.path.join(args.output_path, args.output_filename)
    print(res)
    with open(output, 'w') as f:
        f.write(res)
