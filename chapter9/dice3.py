#サイコロの機能を持つDice型を作り、モジュール化する
#モジュール名は dice

import random

class Dice:
    #初期化メソッド
    #これもメソッドなので、引数にselfを書く必要がある
    #正多面体の面の数を受け取る（4、6、8、12、20）
    def __init__(self, val = 6):
        #エラーを発生させるにはraiseを使う
        #ここでは一般的な例外を示すExceptionを使う、これはエラーを示すデータ型
        #not in でその値がリストになければTrueを返す
        if val not in [4,6,8,12,20]:
            raise Exception('Not exist')
        
        #valをface_numに代入して面の数を保存する
        #クラス内で使うのでアトリビュートにする、そのためself.face_numとする
        self.face_num = val
        #確認用
        print(self.face_num)
        
    #サイコロを振る動作を再現したメソッド
    ##メソッドを書くときは常に引数を1つ書かなければらなず、それをselfにするのが決まりごと
    def shoot(self):
        #上で定義されたface_numを使う
        #ただface_numと書いてもエラーが出る
        #イメージとしては、「class自身を指すselfの中のface_numを使うよ」という感じ
        return random.randint(1,self.face_num)