import argparse
from projectone import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('input', help='input image name', type=str)
    parser.add_argument('--type', help='type of input image: bin | mono | rgb', type=str)
    args = parser.parse_args()
    app.run(args)
