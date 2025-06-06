import argparse
import sys
from src.interpreter import run_interpreter_from_file, InterpreterError


def main():
    parser = argparse.ArgumentParser(
        description="Интерпретатор для языка программирования Lang"
    )
    parser.add_argument("file", help="Путь к программному файлу Lang")
    args = parser.parse_args()

    try:
        output = run_interpreter_from_file(args.file)
        for line in output:
            print(line)
    except FileNotFoundError:
        print(f"Файл не найден: {args.file}", file=sys.stderr)
        sys.exit(1)
    except InterpreterError as e:
        print(f"Ошибка интерпретации: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
