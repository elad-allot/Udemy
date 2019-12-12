import argparse


def pars_args():
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-u", "--username", help="Username.", type=str, default='username')
    parser.add_argument("-p", "--password", help="Password.", type=str, default='password')

    # Parse arguments
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = pars_args()
    print(args.username + ' ' + args.password)
