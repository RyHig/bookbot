def lines(fileName: str) -> list:
    with open(fileName) as f:
        lines = f.readlines()
    f.close()
    return lines


def count_words(lines: list) -> int:
    count = 0
    for line in lines:
        count += len(line.split())

    return count


def count_letters(lines: list) -> dict:
    letter_dict = {}
    for line in lines:
        for char in line.lower():
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
    return letter_dict


def sort_dict(dictionary: dict) -> list:
    return sorted(dictionary.items(), key=lambda item: item[1])


def build_report(fileName) -> None:
    lines_in_file = lines(fileName)
    word_count = count_words(lines_in_file)
    letter_dict = count_letters(lines_in_file)
    sorted_list = sort_dict(letter_dict)

    print(f"--- Begin report of {fileName} ---")
    print(f"{word_count} words found in the document\n")

    for k, v in sorted_list[::-1]:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")

    print(f"--- End report ---")


if __name__ == "__main__":
    build_report("books/frankenstein.txt")
