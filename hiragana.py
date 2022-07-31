import random


def random_hiragana(difficulty):
    basic = [("あ", "a"), ("か", "ka"), ("さ", "sa"), ("た", "ta"), ("な", "na"), ("は", "ha"), ("ま", "ma"), ("や", "ya"),
             ("ら", "ra"), ("わ", "wa"), ("い", "i"), ("き", "ki"), ("し", "shi"), ("ち", "chi"), ("に", "ni"), ("ひ", "hi"),
             ("み", "mi"), ("り", "ri"), ("う", "u"), ("く", "ku"), ("す", "su"), ("つ", "tsu"), ("ぬ", "nu"), ("ふ", "fu"),
             ("む", "mu"), ("ゆ", "yu"), ("る", "ru"), ("え", "e"), ("け", "ke"), ("せ", "se"), ("て", "te"), ("ね", "ne"),
             ("へ", "he"), ("め", "me"), ("れ", "re"), ("お", "o"), ("こ", "ko"), ("そ", "so"), ("と", "to"), ("の", "no"),
             ("ほ", "ho"), ("も", "mo"), ("よ", "yo"), ("ろ", "ro"), ("を", "wo"), ("ん", "n")]

    dakoun = [("が", "ga"), ("ざ", "za"), ("だ", "da"), ("ば", "ba"), ("ぱ", "pa"), ("ぎ", "gi"), ("じ", "ji"), ("ぢ", "ji"),
              ("び", "bi"), ("ぴ", "pi"), ("ぐ", "gu"), ("ず", "zu"), ("づ", "zu"), ("ぶ", "bu"), ("ぷ", "pu"), ("げ", "ge"),
              ("ぜ", "ze"), ("で", "de"), ("べ", "be"), ("ぺ", "pe"), ("ご", "go"), ("ぞ", "zo"), ("ど", "do"), ("ぼ", "bo"),
              ("ぽ", "po")]

    combo = [("きゃ", "kya"), ("ぎゃ", "gya"), ("しゃ", "sha"), ("じゃ", "ja"), ("ちゃ", "cha"), ("にゃ", "nya"), ("ひゃ", "hya"),
             ("びゃ", "bya"), ("ぴゃ", "pya"), ("みゃ", "mya"), ("りゃ", "rya"), ("きゅ", "kyu"), ("ぎゅ", "gyu"), ("しゅ", "shu"),
             ("じゅ", "ju"), ("ちゅ", "chu"), ("にゅ", "nyu"), ("ひゅ", "hyu"), ("びゅ", "byu"), ("ぴゅ", "pyu"), ("みゅ", "myu"),
             ("りゅ", "ryu"), ("きょ", "kyo"), ("ぎょ", "gyo"), ("しょ", "sho"), ("じょ", "jo"), ("ちょ", "cho"), ("にょ", "nyo"),
             ("ひょ", "hyo"), ("びょ", "byo"), ("ぴょ", "pyo"), ("みょ", "myo"), ("りょ", "ryo")]

    if difficulty == "basic":
        return random.choice(basic)
    elif difficulty == "dakoun":
        return random.choice(dakoun)
    elif difficulty == "combo":
        return random.choice(combo)


def hiragana_loop(mode):
    while True:
        print("basic, dakoun, combo:")
        difficulty = input()
        if difficulty == 'c':
            break
        if difficulty not in ["basic", "dakoun", "combo"]:
            print("mode not supported :(")
            continue

        print("count:")
        count = int(input())
        print("---------------------")
        print()
        while True:
            chars_hiragana = ""
            chars_roman = ""
            for i in range(count):
                hir = random_hiragana(difficulty)
                chars_hiragana += hir[0] + " "
                chars_roman += hir[1] + " "

            if mode == 'hiragana':
                print(chars_hiragana, end="")
                if input() == 'c':
                    break
                print(chars_roman)
                print()

            elif mode == 'roman':
                print(chars_roman, end="")
                if input() == 'c':
                    break
                print(chars_hiragana)
                print()


if __name__ == '__main__':
    while True:
        print("press c to exit")
        print("hiragana, roman:")
        mode = input()

        if mode == 'c':
            break

        hiragana_loop(mode)
