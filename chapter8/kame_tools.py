#今いるところを中心に円を描く関数
#引数にturtle.Turtle型のインスタンスと半径の値をとる
#このままでは、半径の値も受け取る必要がある
#def center_circle(name, r):
#r = 100とすることで、100をデフォルトの値（初期値）にする
#引数が与えられなければ、この値を使って処理を進める
def center_circle(name, r = 100):
    #半径分移動して回転する
    name.penup()
    name.forward(r)
    name.left(90)
    name.pendown()
    
    #円を描く
    name.circle(r)
    
    #中心に戻る
    name.penup()
    name.left(90)
    name.forward(r)
    name.left(180)
    name.pendown()