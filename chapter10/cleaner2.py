#初期化メソッドにカメの形に変更する処理とサイズを大きくする処理をいれる
#しかし、単純に初期化メソッドを書くと、既に存在している初期化メソッドを上書きすることになり、エラーが出る
#よって、superを使う、これは自分の親クラスを返してくれる

import turtle
import random
import math

PI = math.pi

#継承するため、turtle.Turtleを指定する
class Kame(turtle.Turtle):
    #初期化メソッド
    def __init__(self):
        #親クラスであるturtle.Turtle型の初期化メソッドを呼び出す
        super(Kame, self).__init__()
        #その後、処理を加える
        self.shape('turtle')
        self.shapesize(2,2,3)
        #ウィンドウの幅と高さを得る
        #そこからx軸、y軸の最大値を得る
        xe = self.getscreen().window_width() / 2.0
        ye = self.getscreen().window_height() / 2.0
        
    #壁に当たってターンする動きをする 
    def hit_wall(self):
        #カメの角度、現在のx、y座標を渡す
        line = Line(self.heading(), self.xcor, self.ycor)
        rand_angle = random.random() * PI
        
        
        


#ウィンドウの幅と高さはすでにあるメソッドを使ってわかる、ウィンドウの中心が座標原点
#つまり、高さhなら、プラス方向の限界はh/2である

#現在の位置姿勢からウィンドウとの交点を計算する
#angleはz軸上向きを正としたときの、現在のx軸からの角度
#x0、y0は現在の座標

class Line:
    def __init__(self, angle, x0, y0):
        #引数をこのデータ型のアトリビュートに設定
        self.a = math.tan(float(angle))
        self.x0 = float(x0)
        self.y0 = float(y0)
        
    #直線の式
    #(y - y0) / (x - x0) = tan(theta) 
    #ウィンドウのx軸の限界（x）まで行ったときのy座標を計算する
    def get_y(self, x):
        endy = self.a * (x - self.x0) + self.y0
        return endy
    
    #ウィンドウのy軸の限界（y）まで行ったときのx座標を計算する
    def get_x(self, y):
        endx = self.x0 + (y - self.y0) / self.a
        return endx