import tkinter as tk
# マップ表示のクラス
import Hexagon as Hexa
# プレイヤー表示のクラス　未完
import Player

CANVAS_WIDTH =  969
CANVAS_HEIGHT = 732

# 六角形の表示数値(px)
h_w = 45
h_w1_4 = 11.25
h_w1_2 = 22.5
h_w3_4 = 33.75

# 色の設定
BOARD_COLOR = 'gray'        # 盤面全体（見えない位置）
VISIBLE_COLOR = 'white'     # ユニットから見える範囲（カラー）
DEAD_COLOR = 'red'          # 侵入不可エリア
OUT_LINE_COLOR = 'black'    # 枠線の色
YOUR_COLOR = 'blue' # あなたのユニットの色
COM_COLOR = 'red' # 相手のユニットの色


class GameDrow:
    def __init__(self, master):
        '''コンストラクタ'''

        self.master = master    #   親ウィジェット
        self.createWidgets()
        self.hexa = Hexa.Hexagon(self.master)

        self.characters = []
        self.player = Player.Player(self.master)
#        for p_char in range(len(self.player.p_xy)):
#            self.characters.append([])

        print(self.player.p_xy)
        
        # マップの描画
        self.createMap(self.hexa)
        # プレイヤーの描画
        self.createPlayer(self.player)


    def createWidgets(self):
        '''ウィジェットを作成・配置する'''
    
        #   キャンバスの作成
        self.canvas = tk.Canvas(
            self.master,
            bg = BOARD_COLOR,
            width   = CANVAS_WIDTH,     # +1は枠線描画のため
            height  = CANVAS_HEIGHT, # +1は枠線描画のため
            highlightthickness = 0
        )
        self.canvas.pack(padx = 120, pady = 50)

    def createMap(self, hexa):
        #---６点指定 六角形
        for num in range(484):
            #canvas.create_polygon( (450, 60), (425, 17), (375, 17), (350, 60), (375, 103), (425, 103))
            if hexa.m_xy[num][1] == 0 or hexa.m_xy[num][1] == 21 or hexa.m_xy[num][0] == 0 or hexa.m_xy[num][0] == 21:
                self.canvas.create_polygon(hexa.m_xy[num][2], hexa.m_xy[num][3], hexa.m_xy[num][4], hexa.m_xy[num][5], hexa.m_xy[num][6], hexa.m_xy[num][7], hexa.m_xy[num][8], hexa.m_xy[num][9], hexa.m_xy[num][10], hexa.m_xy[num][11], hexa.m_xy[num][12], hexa.m_xy[num][13], fill=DEAD_COLOR, outline=OUT_LINE_COLOR)
            else:
                self.canvas.create_polygon(hexa.m_xy[num][2], hexa.m_xy[num][3], hexa.m_xy[num][4], hexa.m_xy[num][5], hexa.m_xy[num][6], hexa.m_xy[num][7], hexa.m_xy[num][8], hexa.m_xy[num][9], hexa.m_xy[num][10], hexa.m_xy[num][11], hexa.m_xy[num][12], hexa.m_xy[num][13], fill=BOARD_COLOR, outline=OUT_LINE_COLOR)

    def createPlayer(self, player):
        for num in range(6):
            #[num, self.xl[num], self.yl[num], xns, yn, xne, yw, tagname]
            self.canvas.create_oval(player.p_xy[num][3], player.p_xy[num][4], player.p_xy[num][5], player.p_xy[num][6], fill=YOUR_COLOR)
            tag_length = len(player.p_xy[num][7])
            if tag_length == 6:
                self.canvas.create_text( player.p_xy[num][3] + 4, player.p_xy[num][4] + 10, text=player.p_xy[num][7], anchor=tk.NW)
            elif tag_length == 7:
                self.canvas.create_text( player.p_xy[num][3] + 2, player.p_xy[num][4] + 10, text=player.p_xy[num][7], anchor=tk.NW)

    #def update(self, player_infos):
    #    for x, y in player_infos:
    #        self.canvas.create_oval(
    #            xs, ys,
    #            xe, ye,
    #            fill=YOUR_COLOR
    #        )

    #def update(self, player_infos):
    #    ''' キャラクターの生成・更新 '''
        #for x, y in player_infos:
            #self.canvas.create_oval(
            #    xs, ys,
            #    xe, ye,
            #    fill=YOUR_COLOR
            #)


app = tk.Tk()
app.geometry("1280x960")
app.title('world trigger')
game = GameDrow(app)
#player = Player.Player(app)
app.mainloop()