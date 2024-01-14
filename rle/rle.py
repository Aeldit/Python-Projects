#!/bin/env python3

"""
@author : Aeldit
This programs are an implementation of the RLE compression algorithm (both the
compress and decompress functions).
It only works with the bases 8, 10 and 16
"""

import cProfile


def compress(string: str, base: int) -> str:
    """
    Compresses a string using the RLE method.
    Works with base 8, 10 and 16

    @param string: The string to compress
    @param base: The base used to compress

    @return An empty string if the string doesn't meet the requirements to be
            compressed | The compressed string otherwise
    """
    # Incorrect base
    if base not in [8, 10, 16]:
        return ""

    base_max = base - 1
    base_max_str = "F" if base == 16 else str(base - 1)
    # tmp holds the values of each string that will be added to the compressed
    # string
    tmp = []

    hex_vals = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    nb_chars = len(string)
    i = 0
    while i < nb_chars:
        nb_identical = 1
        current = string[i]
        i += 1

        while i < nb_chars and string[i] == current:
            nb_identical += 1
            i += 1

        rest = nb_identical % (base_max)
        nb_base_breaks = int((nb_identical - rest) / base_max)
        # Appends nb_base_breaks times the base and the letters
        # (ex: '7h' in base 8) + the rest and the letter (ex: '5h' in base 8 again)
        tmp.append(
            "%s%s"
            % (
                nb_base_breaks * ("%s%s" % (base_max_str, current)),
                "%s%s" % (hex_vals[rest - 1] if base == 16 else str(rest), current),
            )
        )
    return "".join(tmp)


def decompress(string: str, base: int) -> str:
    """
    Decompresses a string using the RLE method.
    Works with base 8, 10 and 16

    @param string: The string to decompress
    @param base: The base used to decompress

    @return An empty string if the string doesn't meet the requirements to be
            decompressed | The decompressed string otherwise
    """
    str_len = len(string)
    # Incorrect base or odd number of characters
    if base not in [8, 10, 16] or str_len % 2 != 0:
        return ""

    eight_vals = ["1", "2", "3", "4", "5", "6", "7"]

    ten_vals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    hex_vals = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    if base == 8:
        b_vals = eight_vals
    elif base == 10:
        b_vals = ten_vals
    else:
        b_vals = hex_vals

    decomp_str = ""
    i = 0
    letter = ""
    ctr = ""
    while i < str_len:
        # If we are on a number
        if i % 2 == 0:
            # If the number belongs to the base
            if string[i] in b_vals:
                if base == 16:
                    # Hex uses letters as values,
                    # so we use their index in the hex_vals list
                    ctr = hex_vals.index(string[i]) + 1
                else:
                    ctr = string[i]
            else:
                return ""
        else:
            letter = string[i]

        # If the number and the letter have been found
        if ctr != "" and letter != "":
            for _ in range(int(ctr)):
                decomp_str += letter
            ctr = letter = ""
        i += 1

    return decomp_str


# ==============================================================================
# Compress function tests
# ==============================================================================
# print(compress("AAAAAAAAAAAAAAAAAAAABBBBBBBBBBC", 8))
# print("7A7A6A7B3B1C\n")
# print(compress("AAAAAAAAAAAAAAAAAAAABBBBBBBBBBC", 10))
# print("9A9A2A9B1B1C\n")
# print(compress("AAAAAAAAAAAAAAAAAAAABBBBBBBBBBC", 16))
# print("FA5AAB1C")
# print(compress("AAAAAAAAAA", 16))
# print("AA")

with open("./text", "r") as rf:
    s = rf.read()
    cProfile.run("compress(s, 8)")

# ==============================================================================
# Decompress function tests
# ==============================================================================
# print(decompress("7A1A6B1C", 8))
# print("AAAAAAAABBBBBBC")
# print(decompress("9A1A6B1C", 10))
# print("AAAAAAAAAABBBBBBC")
# print(decompress("FA1A6B1C", 16))
# print("AAAAAAAAAAAAAAAABBBBBBC")
# print("t " + decompress("FA1A%B1C", 16))
# print("t " + decompress("FA1A%B1", 16))
