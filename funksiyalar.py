import random as r

def sontop(x):
    tasodifiy_son = r.randint(1, x)
    taxminlar = 0
    print(f"Men {x} gacha son o'yladim. Topa olasizmi?", end="")
    while True:
        taxminlar += 1
        tahmin = int(input(">>>"))
        if tahmin > tasodifiy_son:
            print("Kichikroq son o'ylang!", end="")
        elif tahmin < tasodifiy_son:
            print("Kattaroq son o'ylang!", end="")
        else:
            print("Topdingiz.")
            break
    print(f"Tabriklayman. Siz {taxminlar} ta tahmin bilan topdingiz")
    return taxminlar


def sontop_pc(x):
    input(f"1 dan {x} gacha istalgan son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi =1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            tahmin = r.randint(quyi, yuqori)
        else:
            tahmin = quyi
        javob = input(
            f"Siz {tahmin} sonini o'yladingiz. To'g'ri (t), "
            f"Men o'ylagan son bundan kattaroq (+) yoki kichikroq (-)".lower()
        )
        if javob == '+':
            quyi = tahmin + 1
        elif javob == '-':
            yuqori = tahmin - 1
        else:
            break
    print(f"Men {taxminlar} ta tahmin bilan topdim.")
    return taxminlar


def play(x):
    user_t = 0
    pc_t = 0
    tsikl = 0
    while True:
        tsikl += 1
        tahminlar_pc = sontop_pc(x)
        tahminlar_user = sontop(x)

        if tahminlar_pc > tahminlar_user:
            user_t += 1
            print(f"\nSiz {tahminlar_user} ta tahmin bilan meni yutdingiz. Tabriklayman.")
        elif tahminlar_pc < tahminlar_user:
            pc_t += 1
            print(f"\nMen {tahminlar_pc} ta tahmin bilan sizni yutdim. ")
        else:
            user_t += 1
            pc_t += 1
            print("Durrang. Do'stlik g'alaba qozondi.")
        yana = input("\nYana o'ynaymizmi? (yes/no)>>>").lower()
        if yana != 'yes':
            if user_t > pc_t:
                print(f"{tsikl} ta o'yin xulosasiga ko'ra, yakuniy natija {user_t}:{pc_t}"
                      f" Siz g'alaba qozondingiz.")
            
            elif user_t < pc_t:
                print(f"{tsikl} ta o'yin xulosasiga ko'ra, yakuniy natija {user_t}:{pc_t}"
                      f" Men g'alaba qildim.")
                
            else:
                print(f"{tsikl} ta o'yin xulosasiga ko'ra, yakuniy natija {user_t}:{pc_t}."
                      f" Durrang.")
            break
        else:
            print("O'yin davom etadi...")

x = int(input("Nechchigacha son topish o'ynaymiz???"))
play(x)

