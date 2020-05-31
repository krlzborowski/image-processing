import argparse
from projectone import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('input', help='input image name', type=str)
    parser.add_argument('--rgb', action='store_true')
    parser.add_argument('--bin', action='store_true')
    parser.add_argument('--mono', action='store_true')
    args = parser.parse_args()
    app.run(args)
