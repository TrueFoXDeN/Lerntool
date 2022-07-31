import random


def random_hiragana(difficulty):
    easy = ["あ", "い", "う", "え", "お"]

    all = [("あ", "a"), ("か", "ka"), ("さ", "sa"), ("た", "ta"), ("な", "na"), ("は", "ha"), ("ま", "ma"), ("や", "ya"),
           ("ら", "ra"), ("わ", "wa"),
           ("い", "i"), ("き", "ki"), ("し", "shi"), ("ち", "chi"), ("に", "ni"), ("ひ", "hi"), ("み", "mi"), ("り", "ri"),
           ("う", "u"), ("く", "ku"), ("す", "su"), ("つ", "tsu"), ("ぬ", "nu"), ("ふ", "fu"), ("む", "mu"), ("ゆ", "yu"),
           ("る", "ru"),
           ("え", "e"), ("け", "ke"), ("せ", "se"), ("て", "te"), ("ね", "ne"), ("へ", "he"), ("め", "me"), ("れ", "re"),
           ("お", "o"), ("こ", "ko"), ("そ", "so"), ("と", "to"), ("の", "no"), ("ほ", "ho"), ("も", "mo"), ("よ", "yo"),
           ("ろ", "ro"), ("を", "wo"),
           ("ん", "n")
           ]

    if difficulty == "easy":
        return random.choice(easy)
    elif difficulty == "all":
        return random.choice(all)
    else:
        print("mode not supported :(")
        return None


def hiragana_loop(mode):
    while True:
        print("easy, medium, all, dakoun, combo:")
        difficulty = input()
        if difficulty == 'c':
            break
        print("count:")
        count = int(input())
        while True:
            chars_hiragana = ""
            chars_roman = ""
            for i in range(count):
                hir = random_hiragana(difficulty)
                chars_hiragana += hir[0]
                chars_roman += hir[1]

            if mode == 'hiragana':
                print(chars_hiragana, end="")
                if input() == 'c':
                    break
                print(chars_roman)

            elif mode == 'roman':
                print(chars_roman, end="")
                if input() == 'c':
                    break
                print(chars_hiragana)


if __name__ == '__main__':
    while True:
        print("press c to exit")
        print("hiragana, roman:")
        mode = input()

        if mode == 'c':
            break

        hiragana_loop(mode)
