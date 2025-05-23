import argparse
import sys


def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b
    """
    return a + b


def cli(inline_args: list[str] | None = None) -> int:
    """Command-line interface for the add function.

    Args:
        inline_args (Optional[list[str]]): list of command-line arguments for testing purposes.

    Returns:
        int: Exit code of the CLI operation.
    """
    parser = argparse.ArgumentParser(
        description="A simple calculator that adds two numbers."
    )
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")

    if inline_args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(inline_args)

    try:
        result = add(args.a, args.b)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(cli())
