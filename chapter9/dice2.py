#サイコロの機能を持つDice型を作り、モジュール化する
#モジュール名は dice

import random

class Dice:
    #面の数
    face_num = 6
    
    #初期化メソッド
    #これもメソッドなので、引数にselfを書く必要がある
    #これが呼ばれた時、画面にHello!と表示する
    def __init__(self):
        print('Hello!')
        
    #サイコロを振る動作を再現したメソッド
    ##メソッドを書くときは常に引数を1つ書かなければらなず、それをselfにするのが決まりごと
    def shoot(self):
        #上で定義されたface_numを使う
        #ただface_numと書いてもエラーが出る
        #イメージとしては、「class自身を指すselfの中のface_numを使うよ」という感じ
        return random.randint(1,self.face_num)