import argparse
import os


def convert(dataset_path):
    converted_dataset_path = os.path.splitext(dataset_path)[0] + '.txt'

    with open(converted_dataset_path, 'w') as out_fh:

        for id, line in enumerate(open(dataset_path, 'r', encoding='utf-8')):
            context, rephrase, sentiment, form = line.split('\t')
            sample_text = context + ' -> ' + rephrase
            out_fh.write(sample_text + '\n')

    print('Saved converted dataset to {}'.format(converted_dataset_path))


def parse_args():
    argparser = argparse.ArgumentParser()

    argparser.add_argument('--dataset', metavar='PATH', type=str, required=True,
                        help='Input file, directory, or glob pattern (utf-8 text, or preencoded .npz files).')

    return argparser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    convert(args.dataset)
