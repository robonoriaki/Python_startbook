#初期化メソッドにカメの形に変更する処理とサイズを大きくする処理をいれる
#しかし、単純に初期化メソッドを書くと、既に存在している初期化メソッドを上書きすることになり、エラーが出る
#よって、superを使う、これは自分の親クラスを返してくれる

import turtle

#継承するため、turtle.Turtleを指定する
class Kame(turtle.Turtle):
    #初期化メソッド
    def __init__(self):
        #親クラスであるturtle.Turtle型の初期化メソッドを呼び出す
        super(Kame, self).__init__()
        #その後、処理を加える
        self.shape('turtle')
        self.shapesize(2,2,3)