from argparse import ArgumentParser
from timeit import timeit
from unittest import TextTestRunner

from fibonacci_funcs import fibonacci_logn, fibonacci_n

from fibonacci_tests import get_test_suite


def parse_args():
    args_parser = ArgumentParser(description="Calculates n-th Fibonacci number")

    group = args_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--test", dest="test", action="store_true",
                       help="runs only tests - other arguments, if specified, are ignored")
    group.add_argument("-n", dest="n", metavar="NTH_NUMBER",
                       type=int, help="n-th Fibonacci number")

    args_parser.add_argument("-a", dest="alg", metavar="ALGORITHM", choices=["N", "LogN"], default="N",
                             help="algorithm for calculation (N | LogN). Default: N")

    parsed = args_parser.parse_args()

    if (not parsed.test and parsed.n < 0):
        print("The -n parameter must be non-negative integer")
        raise SystemExit(22)  # invalid argument

    return parsed


def main():
    args = parse_args()

    if (args.test):
        TextTestRunner(verbosity=2).run(get_test_suite())
    else:
        func_to_use = fibonacci_logn if args.alg == "LogN" else fibonacci_n

        # use dict to save results of statement execution inside timeit()
        result = {
            "number": None,
            "time": None,
        }

        stmt = 'result["number"] = func_to_use(args.n)'
        result["time"] = timeit(stmt=stmt, globals=locals(), number=1)

        print(f'The {args.n} Fibonacci number: {result["number"]}')
        print(f'Execution time with algorithm {args.alg}: {result["time"]:.15f}')


if (__name__ == "__main__"):
    main()
