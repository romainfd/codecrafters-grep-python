import sys


# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == r"\d":
        return match_digit(input_line)
    elif pattern == r"\w":
        return match_alphanumeric(input_line)
    elif pattern.startswith('['):
        return match_positive_character_group(input_line, pattern[1:-1])
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def match_digit(input_line):
    # return any([str(d) in input_line for d in range(10)])
    return match_positive_character_group(input_line, range(10))


def match_alphanumeric(input_line):
    # return any([w in input_line for w in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'])
    return match_positive_character_group(input_line, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789')


def match_positive_character_group(input_line, character_group):
    # Ref.: https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#positive-character-group--
    return any([c in input_line for c in character_group])


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
