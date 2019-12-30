#サイコロの機能を持つDice型を作り、モジュール化する
#モジュール名は dice

import random

class Dice:
    #面の数
    face_num = 6
    
    #サイコロを振る動作を再現したメソッド
    ##メソッドを書くときは常に引数を1つ書かなければらなず、それをselfにするのが決まりごと
    def shoot(self):
        return random.randint(1,6)