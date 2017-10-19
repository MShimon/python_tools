#coding: utf-8
#pythonで描画するときに便利なツールたち
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##########
##2次元グラフのアニメーションの描画を行うclass
##########
class plotAnimation2D:
    #@brief:初期設定
    #@param:name    アニメーションを保存するファイル名
    #       interval    画像一枚あたりの表示時間 単位は[ms]
    def __init__(self,name,interval):
        self.fig = plt.figure()
        self.ims = []
        self.name_graph = name
        self.interval = interval

    #@brief:描画を行う関数
    #@param:x_list  描画を行う座標のxのnumpy配列
    #       y_list  描画を行う座標のyのnumpy配列
    #       label_list  matplotのラベルの文字列リスト
    #       color_list  matplotのカラーの文字列リスト
    #@return:True   正常に処理が終わった場合
    #        False  要素数が違った場合
    def plot(self,x_list,y_list,label_list,color_list):
        num = len(x_list)
        #x,yの要素数が異なればFalseを返す
        if not num == len(y_list):
            print("[error]plotAnimation2D:x&y has different length")
            return False
        #渡された要素の数だけplot
        flagFirst = True
        for x,y,l,c in zip(x_list,y_list,label_list,color_list):
            if flagFirst:
                im = plt.plot(x,y,label=l,color=c)
                flagFirst = False
            else:
                im += plt.plot(x,y,label=l,color=c)
        #最後に画像を追加する
        self.ims.append(im)
        #処理が正常に終わればTrueを返す
        return True

    #@brief:plotしたグラフをhtml形式で保存する
    def save(self):
        ani = animation.ArtistAnimation(self.fig, self.ims, interval=self.interval)#animationに変換
        ani.save(self.name_graph + ".html", writer="imagemagick")#html形式で表示