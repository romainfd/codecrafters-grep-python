import sys


# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    # Termination
    if len(pattern) == 0:
        return True
    if len(input_line) == 0:
        return False

    # Recurrence: tries to find 1st element of pattern
    # We build input_line_next and pattern_next that will be used for the next match_pattern call
    current_char, input_line_next, pattern_next = input_line[0], input_line[1:], pattern
    if pattern.startswith(r"\d") and match_digit(input_line[0]):
        pattern_next = pattern[2:]
    elif pattern.startswith(r"\w") and match_alphanumeric(input_line[0]):
        pattern_next = pattern[2:]
    elif pattern.startswith('['):
        closingBracketIndex = pattern.index(']')
        if (pattern[1] == '^' and match_negative_character_group(input_line, pattern[2:closingBracketIndex])) or \
                match_positive_character_group(input_line, pattern[1:closingBracketIndex]):
            pattern_next = pattern[closingBracketIndex + 1:]
    else:
        # We perform direct match
        if input_line[0] == pattern[0]:
            pattern_next = pattern[1:]
    # print(input_line_next, pattern_next)
    return match_pattern(input_line_next, pattern_next)


def match_digit(input_line):
    # return any([str(d) in input_line for d in range(10)])
    return match_positive_character_group(input_line, '0123456789')


def match_alphanumeric(input_line):
    # return any([w in input_line for w in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'])
    return match_positive_character_group(input_line, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789')


def match_positive_character_group(input_line, character_group):
    # Ref.: https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#positive-character-group--
    return any([c in character_group for c in input_line])


def match_negative_character_group(input_line, character_group):
    # Ref.: https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-classes-in-regular-expressions#negative-character-group-
    return any([c not in character_group for c in input_line])


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
