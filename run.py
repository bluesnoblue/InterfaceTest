import sys
import getopt
from unittest import defaultTestLoader, TextTestRunner


def build_config(env):
    with open('CONFIG_raw.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    with open('CONFIG.py', 'w', encoding='utf-8') as f:
        f.write(f"ENV = '{env}'\n")
        f.write('\n')
        f.write(content)


def main(argv):
    pattern = 'test_*.py'
    env = 'test'
    try:
        opts, args = getopt.getopt(argv, 'hp:e:')
        for opt, arg in opts:
            if opt == '-h':
                print('run.py -p <pattern>')
                sys.exit()
            if opt == '-e':
                env = arg.lower()
            if opt == '-p':
                pattern = f'{arg}*.py'

        build_config(env)  # 构建CONFIG文件
    except getopt.GetoptError as e:
        print(e)
        sys.exit()

    cases = defaultTestLoader.discover('./case/', pattern=pattern)
    runner = TextTestRunner()
    runner.run(cases)


if __name__ == '__main__':
    main(sys.argv[1:])

