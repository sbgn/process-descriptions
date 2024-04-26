#!/bin/python

import argparse

TOK_ESCAPE = "\\"

commentators = ["dogrusoz"]


def main():
    parser = argparse.ArgumentParser(
        description="Tool for removeing \\corr and \\add commands from a latex file"
    )
    parser.add_argument(
        "-i",
        "--in-place",
        default=False,
        const=None,
        nargs="?",
        help="Edit files in-place, saving backups with the specified extension",
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?")
    args = parser.parse_args()
    run(args)


def run(args):
    input_file = args.input_file
    with open(input_file) as f:
        source = []
        target = []
        braces = []
        for c in f.read():
            """
            0: \\corr[
            1: \\corr{ or \\corr[]{
            2: \\corr[]{}{ or \\corr{}{
            3: \\add[
            4: \\add{ or \\add[]{
            -1: [ or { outside of above
            """
            add(source, c)
            add_c = True
            if endswith(source, "\\corr["):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\corr["))
                braces.append(0)
                add_c = False
            elif endswith(source, "\\add["):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\add["))
                braces.append(3)
                add_c = False
            elif endswith(source, "[") and source[-2] != TOK_ESCAPE:
                braces.append(-1)
            elif endswith(source, "\\corr{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\corr{"))
                braces.append(1)
                add_c = False
            elif endswith(source, "\\add{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\add{"))
                braces.append(4)
                add_c = False
            elif endswith(source, "\\dogrusoz{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\dogrusoz{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\rougny{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\rougny{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\mazein{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\mazein{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\toure{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\toure{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\draeger{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\draeger{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\luna{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\luna{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\lenovere{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\lenovere{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\wu{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\wu{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\balaur{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\balaur{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\borlinghaus{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\borlinghaus{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "\\blinov{"):
                if 0 not in braces and 1 not in braces:
                    remove(target, len("\\blinov{"))
                braces.append(5)
                add_c = False
            elif endswith(source, "]{") and braces and braces[-1] == 0:
                braces.pop()
                braces.append(1)
                add_c = False
            elif endswith(source, "]{") and braces and braces[-1] == 3:
                braces.pop()
                braces.append(4)
                add_c = False
            elif endswith(source, "}{") and braces and braces[-1] == 1:
                braces.pop()
                braces.append(2)
                add_c = False
            elif endswith(source, "{") and source[-2] != TOK_ESCAPE:
                braces.append(-1)
            elif endswith(source, "}") and source[-2] != TOK_ESCAPE:
                if braces and braces[-1] == -1:
                    braces.pop()
                elif braces and (
                    braces[-1] == 2 or braces[-1] == 4 or braces[-1] == 5
                ):
                    braces.pop()
                    add_c = False
            elif (
                endswith(source, "]")
                and source[-1] != TOK_ESCAPE
                and braces
                and braces[-1] < 0
            ):
                braces.pop()
            if 0 in braces or 1 in braces or 3 in braces or 5 in braces:
                add_c = False
            if add_c:
                add(target, c)
    output_string = "".join(target)
    output_file = args.output_file
    if args.in_place is not False and args.in_place is not None:
        backup_file = f"{input_file}.{args.in_place}"
        with open(backup_file, "w") as f:
            input_string = "".join(source)
            f.write(input_string)
        output_file = input_file
    if output_file is not None:
        with open(output_file, "w") as f:
            f.write(output_string)
    else:
        print(output_string, end="")


def remove(l, n):
    for i in range(n - 1):
        del l[-1]


def add(l, s):
    for c in s:
        l.append(c)


def endswith(l, s):
    if len(s) > len(l):
        return False
    for i, c in enumerate(s[::-1]):
        if l[-i - 1] != c:
            return False
    return True


if __name__ == "__main__":
    main()
