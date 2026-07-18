"""
Croppa — split dual-page PDF spreads into sequential single pages.

Each page is cropped into a left half and a right half, then interleaved
into out.pdf (left, right, left, right, ...).
"""

import sys

import PyPDF2


def crop_left(input_path: str, output_path: str = "left.pdf") -> None:
    with open(input_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            page.mediabox.upper_right = (
                page.mediabox.right / 2,
                page.mediabox.top,
            )
            writer.add_page(page)

        with open(output_path, "wb") as left_file:
            writer.write(left_file)

    print(f"{output_path} created")


def crop_right(input_path: str, output_path: str = "right.pdf") -> None:
    with open(input_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            new_width = page.mediabox.width / 2
            page.mediabox.upper_left = (
                page.mediabox.left + new_width,
                page.mediabox.top,
            )
            writer.add_page(page)

        with open(output_path, "wb") as right_file:
            writer.write(right_file)

    print(f"{output_path} created")


def merge_halves(
    left_path: str = "left.pdf",
    right_path: str = "right.pdf",
    output_path: str = "out.pdf",
) -> None:
    with open(left_path, "rb") as left_file, open(right_path, "rb") as right_file:
        left_reader = PyPDF2.PdfReader(left_file)
        right_reader = PyPDF2.PdfReader(right_file)
        writer = PyPDF2.PdfWriter()

        page_count = min(len(left_reader.pages), len(right_reader.pages))
        for page_num in range(page_count):
            writer.add_page(left_reader.pages[page_num])
            writer.add_page(right_reader.pages[page_num])

        with open(output_path, "wb") as out_file:
            writer.write(out_file)

    print(f"{output_path} created")


def print_banner() -> None:
    print(" ██▓███ ▓█████▄  █████▒    ▄████▄  ██▀███  ▒█████  ██▓███  ██▓███  ▄▄▄      ")
    print("▓██░  ██▒██▀ ██▓██   ▒    ▒██▀ ▀█ ▓██ ▒ ██▒██▒  ██▒██░  ██▒██░  ██▒████▄    ")
    print("▓██░ ██▓░██   █▒████ ░    ▒▓█    ▄▓██ ░▄█ ▒██░  ██▒██░ ██▓▓██░ ██▓▒██  ▀█▄  ")
    print("▒██▄█▓▒ ░▓█▄   ░▓█▒  ░    ▒▓▓▄ ▄██▒██▀▀█▄ ▒██   ██▒██▄█▓▒ ▒██▄█▓▒ ░██▄▄▄▄██ ")
    print("▒██▒ ░  ░▒████▓░▒█░       ▒ ▓███▀ ░██▓ ▒██░ ████▓▒▒██▒ ░  ▒██▒ ░  ░▓█   ▓██▒")
    print("▒▓▒░ ░  ░▒▒▓  ▒ ▒ ░       ░ ░▒ ▒  ░ ▒▓ ░▒▓░ ▒░▒░▒░▒▓▒░ ░  ▒▓▒░ ░  ░▒▒   ▓▒█░")
    print("░▒ ░     ░ ▒  ▒ ░           ░  ▒    ░▒ ░ ▒░ ░ ▒ ▒░░▒ ░    ░▒ ░      ▒   ▒▒ ░")
    print("░░       ░ ░  ░ ░ ░       ░         ░░   ░░ ░ ░ ▒ ░░      ░░        ░   ▒   ")
    print("           ░              ░ ░        ░        ░ ░                       ░  ░")
    print("         ░                ░                                                 ")
    print("Croppa v1.0")
    print("By: Devcon324  https://github.com/Devcon324")
    print("****************************************************************************")
    print("This program splits a dual-page PDF into sequential single pages.")
    print('Output is written as "out.pdf" in the current directory.')
    print("****************************************************************************")


def main() -> None:
    print_banner()

    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        print("Provide the name of the PDF file you would like to split.")
        print("Include the path if the file is not in the current directory.")
        print("Include the .pdf extension.")
        input_path = input("Enter Input PDF filename: ").strip()

    if not input_path:
        print("No input file provided.")
        sys.exit(1)

    crop_left(input_path)
    crop_right(input_path)
    merge_halves()

    print("Done!")
    print('The output file is named "out.pdf" in the current directory.')


if __name__ == "__main__":
    main()
