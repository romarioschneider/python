from argparse import ArgumentParser
from subprocess import Popen, PIPE
from datetime import datetime
from sys import exit


def remaining_days(args):

    p = Popen(['/usr/bin/openssl', 'crl', '-in', args.filename, '-nextupdate', '-noout'], shell=False, stdout=PIPE)
    (output, err) = p.communicate()
    nextUpdate=output.replace('\n', '').split('=')[1]
    
    #"nextUpdate" looks like that "Feb  9 15:22:42 2018 GMT"
    #Creating datetime object from it using appropriate format spec
    nextUpdate_datetime = datetime.strptime(nextUpdate, '%b  %d %H:%M:%S %Y %Z')
    
    now_datetime = datetime.now()
    timedelta = nextUpdate_datetime - now_datetime
    
    remaining_days_count = int(timedelta.days)
    
    if args.critical_remaining_days < remaining_days_count <= args.warning_remaining_days:
        print('WARNING - days remaining: {days}'.format(days = remaining_days_count))
        exit(1)
    elif args.critical_remaining_days >= remaining_days_count:
        print('CRITICAL - days remaining: {days}'.format(days = remaining_days_count))
        exit(2)
    else:
        print('OK - days remaining: {days}'.format(days = remaining_days_count))


def parse_args():
    parser = ArgumentParser(description='Process argumants')
    parser.add_argument("-f", "--filename", type = str, dest = "filename", default = "crl.pem", help = "crl.pem filename")
    parser.add_argument("-w", "--warning", type = int, dest = "warning_remaining_days", default = 5, help = "Remainig days count which will lead to WARNING state")
    parser.add_argument("-c", "--critical", type = str, dest = "critical_remaining_days", default = 2, help = "Remainig days count which will lead to CRITICAL state")
    parser.set_defaults(func=remaining_days)
    
    return parser.parse_args()


def main():
	args = parse_args()
	args.func(args)


if __name__ == '__main__':
	main()