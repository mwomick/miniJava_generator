import os
from generator import makeProgram

OUT_DIR = os.getenv('OUT_DIR', './')
FILE_EXT = os.getenv('FILE_EXT', 'mjava')
GEN_NUM = int(os.getenv('GEN_NUM', 10))

def main():
    for i in range(GEN_NUM):
        with open(os.path.join(OUT_DIR, f'Test{i:03d}.{FILE_EXT}'), 'w') as f:
            f.write(makeProgram())


if __name__ == "__main__":
    main()
