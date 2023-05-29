import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_video', type=str, default='VIDEO', help='path to the input video or folder', required=True)
parser.add_argument('-o', '--output_video', type=str, default='OUTPUT', help='path to the output folder')
parser.add_argument('-mp', '--model', type=str, default='t_be_decided', help='path to the model')
parser.add_argument('-ml', '--model_link', type=str, default='to_be_decided', help='path to the model')
parser.add_argument('--keep_frames', type=bool, default=False, help='keep frames folder after processing')
parser.add_argument('--use_gpu', type=bool, default=False, help='use gpu for processing')

args = parser.parse_args()
# print(args)

