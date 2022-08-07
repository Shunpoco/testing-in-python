import argparse


def main():
    parser = argparse.ArgumentParser(prog="cli")

    parser.add_argument("--foo", help="the foo option!")
    parser.parse_args()

if __name__ == "__main__":
    main()
