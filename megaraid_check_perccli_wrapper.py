from argparse import ArgumentParser
from subprocess import Popen, PIPE
from sys import exit


def check_call(args):
    results = {}
    p = Popen([args.perccli_binary, '-LDInfo', '-Lall', '-aALL'], shell=False, stdout=PIPE)
    (out, err) = p.communicate()

    output_lines = out.split('\n')

    for line in output_lines:
        if 'Mirror Data' in line:
            results["MirrorData"] = line.split(':')[1].strip()
        elif 'State' in line:
            results["State"] = line.split(':')[1].strip()

    if results["State"] != 'Optimal':
         print('CRITICAL - ' + str(results))
         exit(2)
    else:
        print('OK - ' + str(results))
        exit(0)


def parse_args():
    parser = ArgumentParser(description='Process argumants')
    parser.add_argument("-c", "--perccli-bin", type=str, dest="perccli_binary", default="/usr/local/bin/perccli64", help="MegaRAID/perccli/perccli64 binary file path")
    parser.set_defaults(func=check_call)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()