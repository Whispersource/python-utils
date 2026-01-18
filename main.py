from utils import add, count_words, to_uppercase


def main():
    print("Calculator demo:")
    print("2 + 3 =", add(2, 3))

    text = "Learning Python is fun"
    print("\nText tools demo:")
    print("Word count:", count_words(text))
    print("Uppercase:", to_uppercase(text))


if __name__ == "__main__":
    main()
