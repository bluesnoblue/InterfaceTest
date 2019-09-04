import sys
import getopt
from unittest import defaultTestLoader, TextTestRunner


def build_config(env):  # 构建CONFIG文件的方法
    with open('CONFIG_raw.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    with open('CONFIG.py', 'w', encoding='utf-8') as f:
        f.write(f"ENV = '{env}'\n")
        f.write('\n')
        f.write(content)


def main(argv):  # 主方法
    pattern = 'test_*.py'   # pattern默认搜集全部测试用例
    env = 'test'  # 默认在测试环境运行测试用例
    try:
        opts, args = getopt.getopt(argv, 'hp:e:')
        for opt, arg in opts:
            if opt == '-h':
                print('run.py -p <pattern> -e <environment>')
                sys.exit()
            if opt == '-e':
                env = arg.lower()
            if opt == '-p':
                pattern = f'{arg}*.py'

        build_config(env)  # 构建CONFIG文件
    except getopt.GetoptError as e:
        print(e)
        sys.exit()

    # 根据入参pattern，在case文件夹中收集测试用例，pattern默认搜集全部测试用例
    cases = defaultTestLoader.discover('./case/', pattern=pattern)

    # 实例化一个测试执行器并执行所有测试用例
    runner = TextTestRunner()
    runner.run(cases)


if __name__ == '__main__':
    main(sys.argv[1:])

