import random

def guess_the_number():

    print("このゲームは入力された最小値ｎと最大値ｍからランダムに生成された数字を当てるゲームです！あなたの運を試そう！")

    n = int(input("最小値をnを入力してください。"))
    m = int(input("最大値をm入力してください。"))

    if n > m :
        print("nはm以下である必要があります。")
        return

    secret_number = random.randint(n,m)
    attempts = 0
    max_attempts = 5

    print(f'{n}から{m}の範囲で数字を入力して当ててください。最大試行回数は{max_attempts}回です。')

    while attempts < max_attempts:
        guess = int(input(f'※残り回数:{max_attempts - attempts} あなたの予想： '))
        attempts += 1

        if guess != secret_number and attempts < max_attempts:
            answer = input("ざんねん！ハズレ！ヒントを表示しますか？・\nはい または いいえ を入力してください。")
            if answer == "はい":
                if guess < secret_number:
                    print("もっと大きいです。")
                else: print("もっと小さいです。")
        else: 
            print(f'正解！すばらしい！今日はなにかとても良い事が起こるかも？')
            return
    print(f'残念！あなたは{max_attempts}回以内に当てられませんでした。\nでも落ち込まないで。時間はまだまだあります★')

guess_the_number()