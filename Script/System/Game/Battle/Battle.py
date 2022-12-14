from enum import Enum
import pygame
from pygame.locals import *
from math import pi
import math
import sys, os

from ..Data.GameData import GameData
from Script.System.Util.Command import Command
from Script.System.Util.Command.MoveCommand import MoveCommand
# マップ表示のクラス
from .Map import Map
from .MoveMethod import MoveMethod
# プレイヤー表示のクラス
from .Character import CharacterManager
from .Player import Player
from .Enemy import Enemy
from .TextManager import TextManager
from .Weapon import Weapon
from .CountDownTimer import CountDownTimer as Timer
from ..GameSequenceBase import GameSequenceBase
from ...Util.PgLib import PgLib
from ...Util.Define import Define
from ...IO.InputKeyboard import InputKeyboard
from ...IO.InputMouse import InputMouse
from ...Util.Command.CommandUtil import CommandUtil
# カラーリスト
from ..Data.ColorList import ColorList

CANVAS_WIDTH =  1280
CANVAS_HEIGHT = 960

# 円タイマーの中央座標
TIMER_X = 1230
TIMER_Y = 50

MAX_COUNTER = 30
CIRCLE_WIDTH_OUT = 40
CIRCLE_WIDTH_IN = 35

PREPARE_TIME = 2

TURN_DISPLAY = 30
DATA_DISPLAY_WIDTH = 400
DATA_DISPLAY_HEIGHT = 300

FPS = 60

MINUS1 = (MAX_COUNTER * FPS) / 90

UNIT_NUM = 6
PLAYER_UNIT_NUM = 6
ENEMY_UNIT_NUM = 6

UNIT_X_START = 8
UNIT_X_END = 17
PLAYER_Y_START = 17
PLAYER_Y_END = 21
ENEMY_Y_START = 2
ENEMY_Y_END = 6

PLAYER = 0
ENEMY = 1

PREPARE_UNIT_WIDTH = 50

# 色の設定
BOARD_COLOR = ColorList.GRAY.value              # 盤面全体（見えない位置）
VISIBLE_COLOR = ColorList.WHITE.value           # ユニットから見える範囲（カラー）
CAN_MOVE_COLOR = ColorList.SKYBLUE.value        # ユニットの移動可能範囲（カラー）
DEAD_COLOR = ColorList.MAROON.value             # 侵入不可エリア
DEAD_OUT_LINE_COLOR = ColorList.BLACK.value     # 侵入不可エリア枠線
OUT_LINE_COLOR = ColorList.BLACK.value          # 枠線の色
YOUR_COLOR = ColorList.BLUE.value               # あなたのユニットの色
ENEMY_COLOR = ColorList.YELLOW.value            # 相手のユニットの色


class Battle(GameSequenceBase):
    class BattleState(Enum):
        Start = 0
        Prepare = 1
        Counter = 2
        Think = 3
        Stop = 4
        Move = 5
        Load = 6
        End = 10

    def __init__(self) -> None:
        '''コンストラクタ'''
        GameData.LoadData()
        
        self.screen = PgLib.GetScreen()             # スクリーンの設定 
        self.PrepareTime = PREPARE_TIME             # シーン「prepare」のユニットの装備の選択時間設定
        self.PrepareTimer = Timer(PREPARE_TIME, TIMER_X, TIMER_Y)
        self.weapon : list = []                     # Weaponリスト
        # 武器の初期設定
        for num in range(Weapon.IMAGE_NUM_MAX):
            if num == 0:
                self.weapon.append(None)
            else:
                self.weapon.append(Weapon(num))

        self.TurnCount = 1                          # ターンのカウント
        self.TurnDisplay = TURN_DISPLAY             # ターンの表示時間
        self.counter = MAX_COUNTER                  # シーン「Think」の時間設定
        self.map = Map()                            # Map管理
        self.Player_Characters = CharacterManager(UNIT_X_START, UNIT_X_END, PLAYER_Y_START, PLAYER_Y_END, PLAYER_UNIT_NUM)
        self.player : list = []                     # Playerユニット
        self.Enemy_Characters = CharacterManager(UNIT_X_START, UNIT_X_END, ENEMY_Y_START, ENEMY_Y_END, ENEMY_UNIT_NUM)
        self.enemy : list = []                      # Enemyユニット               
        self.state = self.BattleState.Start         # バトルのステイト
        self.click_flag_counter = 5                 # クリックのフラグが立っている間受付拒否時間
        self.click_flag = False                     # クリックした時のフラグ
        self.pushClick = None                       # クリックしたイベントの取得
        self.before_pushClick = None                # 1つ前のクリックイベントの取得
        self.isUnitselect = False                   # ユニットを選択しているかどうか
        self.text_player = TextManager()
        self.text_weapon = TextManager()
        self.text_enemy = TextManager()

        self.text_player_status = TextManager()
        self.text_enemy_status = TextManager()

        self.isWeaponselect1 = False                 # 武器1を選択しているかどうか
        self.isWeaponselect2 = False                 # 武器2を選択しているかどうか
        self.isWeaponhover = False                   # 武器の上にあるかどうか
        self.isArmorselect = False                   # 防具を選択しているかどうか
        self.player_flg = None


        # プレイヤーの初期設定
        for num in range(PLAYER_UNIT_NUM):
            self.player.append(Player(self.Player_Characters.xl[num], self.Player_Characters.yl[num], num))
            #self.player[num].SetSize(20, 20)

        # エネミーの初期設定
        for num in range(ENEMY_UNIT_NUM):
            self.enemy.append(Enemy(self.Enemy_Characters.xl[num], self.Enemy_Characters.yl[num], num, PLAYER_UNIT_NUM))
            #self.enemy[num].SetSize(20, 20)

        # 確認用（不要なら消してください）
        CommandUtil.AddMoveCommand(MoveCommand.MoveType.NormalToPosition, self.player[0], Define.Position(100, 100), startFrame=30, endFrame=60)
        CommandUtil.AddMoveCommand(MoveCommand.MoveType.NormalToPosition, self.player[1], Define.Position(900, 100), startFrame=60, endFrame=30) 

    def Update(self):
        if self.state == self.BattleState.Start:
            self.state = self.BattleState.Prepare
            return
        elif self.state == self.BattleState.Prepare:
            self.PrepareTimer.Update()
            # キー入力取得期間
            if self.click_flag == True:
                self.click_flag_counter -= 1
            if self.click_flag_counter == 0:
                self.click_flag = False
                self.click_flag_counter = 5

            if self.PrepareTimer.GetCounter() <= 0:
                self.isUnitSelect = False
                self.isWeaponselect1 = False
                self.isWeaponselect2 = False
                self.isWeaponhover = False
                for num in range(PLAYER_UNIT_NUM):
                    self.player[num].IsSelect == False
                self.BattleTimer = Timer(MAX_COUNTER, TIMER_X, TIMER_Y)
                self.state = self.BattleState.Counter
            return
        elif self.state == self.BattleState.Counter:
            self.TurnDisplay -= 1
            if self.TurnDisplay == 0:
                self.BattleTimer = Timer(MAX_COUNTER, TIMER_X, TIMER_Y)
                self.state = self.BattleState.Think
            else:
                self.state = self.BattleState.Counter
            return
        elif self.state == self.BattleState.Think:
            self.BattleTimer.Update()

            # キー入力取得期間
            if self.click_flag == True:
                self.click_flag_counter -= 1
            if self.click_flag_counter == 0:
                self.click_flag = False
                self.click_flag_counter = 5

            # ターンのタイマー
            if self.BattleTimer.GetCounter() <= 0:
                self.isUnitSelect = False
                for num in range(PLAYER_UNIT_NUM):
                    self.player[num].IsSelect == False
                self.state = self.BattleState.Stop
            return
        elif self.state == self.BattleState.Stop:
            self.TurnCount += 1
            if self.TurnCount == 7:
                self.state = self.BattleState.End
            else:
                self.TurnDisplay = TURN_DISPLAY
                self.state = self.BattleState.Counter
            return


    def Draw(self):
        if self.state == self.BattleState.Start:
            # 背景（黒）
            self.DrawPrepare()
        elif self.state == self.BattleState.Prepare:
            # 背景（黒）
            self.DrawPrepare()
            # タイマーの表示
            self.PrepareTimer.Draw(ColorList.RED, ColorList.LIME, ColorList.YELLOW, ColorList.WHITE)
            # ユニットのクリック処理
            self.SelectUnit(self.player, self.weapon)
            
            if self.isUnitselect == True:
                self.text_player.Draw(ColorList.BLACK, ColorList.WHITE, ColorList.LIME)
            
            if self.isWeaponhover == True:
                self.text_weapon.Draw(ColorList.BLACK, ColorList.LIME, ColorList.LIME)

        elif self.state == self.BattleState.Counter:
            # マップの描画
            self.DrawMap(self.map, self.player)
            # プレイヤーの描画
            self.CreatePlayer(self.player)
            # エネミーの描画
            self.CreateEnemy(self.enemy)
            # ターン経過
            self.DrawTurn()
            # 円タイマー
            self.BattleTimer.Draw(ColorList.RED, ColorList.LIME, ColorList.YELLOW, ColorList.WHITE)
        elif self.state == self.BattleState.Think:
            # マップの描画
            self.DrawMap(self.map, self.player)
            # プレイヤーの描画
            self.CreatePlayer(self.player)
            # エネミーの描画
            self.CreateEnemy(self.enemy)
            # 円タイマー
            self.BattleTimer.Draw(ColorList.RED, ColorList.LIME, ColorList.YELLOW, ColorList.WHITE)
            # マウスチェック
            self.CalcReturnPos(self.player, self.enemy, self.map, self.weapon)
            if self.isUnitselect == True:
                #self.datadisp.Draw(ColorList.BLACK, ColorList.WHITE, ColorList.LIME)
                # self.text_weapon.Draw(ColorList.WHITE, ColorList.BLACK, ColorList.LIME)
                self.text_player_status.Draw(ColorList.BLACK, ColorList.WHITE, ColorList.LIME)
                

    def DrawPrepare(self):
        width, height =PgLib.GetScreenSize()
        PgLib.DrawRect(ColorList.WHITE.value, 0, 0, width, height, 0)
        pygame.draw.line( self.screen, ColorList.LIME.value, (200, 0), (200, height), 10)
        for num in range(1, Weapon.IMAGE_NUM_MAX):
            if num < 7:
                self.weapon[num].SetPos(280 + (150 * (num - 1)), CANVAS_HEIGHT / 2)
            elif 7 <= num and num < 11:
                self.weapon[num].SetPos(130 + (150 * ((num - 1) % 5)), CANVAS_HEIGHT / 2 + 140)
            elif 11  <= num and num < 15:
                self.weapon[num].SetPos(280 + (150 * ((num - 1) % 5)), CANVAS_HEIGHT / 2 + 280)
            self.weapon[num].Draw()
            self.weapon[num].WeaponDraw()
        for num in range(PLAYER_UNIT_NUM):
            #self.player[num].Draw(ColorList.BLUE)
            self.player[num].SetSize(PREPARE_UNIT_WIDTH, PREPARE_UNIT_WIDTH)
            self.player[num].IsVisible = True
            # 左に一列で並べる。
            self.player[num].SetPos(PREPARE_UNIT_WIDTH + 30, (PREPARE_UNIT_WIDTH * 2.5 * num) + 60 )
            self.player[num].PlayerDraw()


    def SelectUnit(self, player, weapon : Weapon):       
        Point_x, Point_y = PgLib.GetInputManager().GetMouse().GetPosMouce()
        self.pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()
        # 今回のクリックイベントのみ
        weapon_flg = False
        if self.pushClick != self.before_pushClick:
            if  self.click_flag == False:
                # キー入力確認用
                print("Push Click :  x:", str(Point_x) + " y:" + str(Point_y))
                #[id, xl, yl, x, y, tagname]
                self.click_flag = True
                self.before_pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()
                if Point_x != None and Point_y !=  None:
                    if self.pushClick == 1:
                        for p_num in range(PLAYER_UNIT_NUM):
                            pos = player[p_num].GetPos()
                            if pos.x - (PREPARE_UNIT_WIDTH) < Point_x and Point_x < pos.x + (PREPARE_UNIT_WIDTH) and pos.y - (PREPARE_UNIT_WIDTH) < Point_y and Point_y < pos.y + (PREPARE_UNIT_WIDTH):
                                player[p_num].IsSelect = True
                                #self.datadisp.SetPos(280, 50)
                                #self.datadisp.SetSize(DATA_DISPLAY_WIDTH, DATA_DISPLAY_HEIGHT)
                                self.text_player.SetPos(280, 50)

                                player_font_size_list = [30, 30, 30, 30, 30]
                                player_text_list = []
                                player_text_list.append("I  D：" + str(player[p_num].ID) + "　　　　行動力：" + str(payer[p_num].Status.ActionPower))
                                player_text_list.append("名　前：" + player[p_num].Status.characterName + "　　　　体　力：" + str(player[p_num].Status.HitPoint))
                                player_text_list.append("攻撃力：" + str(player[p_num].Status.AttackPoint) + "　　　　防御力：" + str(player[p_num].Status.DeffencePoint))
                                player_text_list.append("回避力：" + str(player[p_num].Status.AvoidancePoint) + "　　　　技術力：" + str(player[p_num].Status.TechnologyPoint))

                                self.text_player.SetFontsize(player_font_size_list)
                                self.text_player.SetText(player_text_list)

                                if player[p_num].IsSelect == True:
                                    self.isUnitselect = True
                                    weaponId1 = player[p_num].WeaponId
                                    weaponId2 = player[p_num].SecondWeaponId
                                    if weaponId1 == None:
                                        self.isWeaponselect1 = False
                                        for w_num in range(1, Weapon.IMAGE_NUM_MAX):
                                            weapon[w_num].SetSelect(False)
                                    else:
                                        self.isWeaponselect1 = True
                                        for w_num in range(1, Weapon.IMAGE_NUM_MAX):
                                            weapon[w_num].IsSelect = False 
                                        weapon[weaponId1].IsSelect = True
                                    if weaponId2 == None:
                                        self.isWeaponselect2 = False
                                    else:
                                        self.isWeaponselect2 = True
                                        weapon[weaponId2].SetSelect(True)

                                    self.player_flg = p_num

                        if self.isUnitselect == True:
                            if self.isWeaponselect1 == False:
                                for w_num in range(1, Weapon.IMAGE_NUM_MAX):
                                    pos = weapon[w_num].GetPos()
                                    if pos.x - (Weapon.IMAGE_SIZE/ 2) < Point_x and Point_x < pos.x + (Weapon.IMAGE_SIZE/ 2) and pos.y - (Weapon.IMAGE_SIZE/ 2) < Point_y and Point_y < pos.y + (Weapon.IMAGE_SIZE/ 2):                                  
                                        weapon[w_num].SetSelect(True)
                                        player[self.player_flg].WeaponId = w_num

                                        if weapon[w_num].GetSelect() == True:
                                            self.isWeaponselect1 = True
                            elif self.isWeaponselect1 == True:
                                if self.isWeaponselect2 == False:
                                    for w_num in range(1, Weapon.IMAGE_NUM_MAX):
                                        pos = weapon[w_num].GetPos()
                                        if pos.x - (Weapon.IMAGE_SIZE/ 2) < Point_x and Point_x < pos.x + (Weapon.IMAGE_SIZE/ 2) and pos.y - (Weapon.IMAGE_SIZE/ 2) < Point_y and Point_y < pos.y + (Weapon.IMAGE_SIZE/ 2):                                  
                                            weapon[w_num].SetSelect(True)
                                            player[self.player_flg].SecondWeaponId = w_num
                                            if weapon[w_num].GetSelect() == True:
                                                self.isWeaponselect2 = True

                        for p_num in range(PLAYER_UNIT_NUM):
                            if self.player_flg != p_num:
                                player[p_num].IsSelect = False

                    elif self.pushClick == 3:
                        w_num = None
                        for p_num in range(PLAYER_UNIT_NUM):
                            if player[p_num].IsSelect == True:
                                weaponId1 = player[p_num].WeaponId
                                weaponId2 = player[p_num].SecondWeaponId
                                if weaponId1 == None and weaponId2 == None:
                                    player[p_num].IsSelect = False
                                if weaponId1 != None and weaponId2 == None:
                                    player[p_num].WeaponId = None
                                    w_num = weaponId1
                                if weaponId1 != None and weaponId2 != None:
                                    player[p_num].SecondWeaponId = None
                                    w_num = weaponId2

                                if w_num != None:
                                    weapon[w_num].SetSelect(False)

                        if self.isUnitselect == True and self.isWeaponselect1 == False and self.isWeaponselect2 == False:
                            self.isUnitselect = False
                        if self.isUnitselect == True and self.isWeaponselect1 == True and self.isWeaponselect2 == False:
                            self.isWeaponselect1 = False
                        if self.isUnitselect == True and self.isWeaponselect1 == True and self.isWeaponselect2 == True:
                            self.isWeaponselect2 = False
                        
        else:
            if Point_x != None and Point_y !=  None:
                for w_num in range(1, Weapon.IMAGE_NUM_MAX):
                    pos = weapon[w_num].GetPos()
                    weapon[w_num].SetHover(False)
                    if pos.x - (Weapon.IMAGE_SIZE/ 2) < Point_x and Point_x < pos.x + (Weapon.IMAGE_SIZE/ 2) and pos.y - (Weapon.IMAGE_SIZE/ 2) < Point_y and Point_y < pos.y + (Weapon.IMAGE_SIZE/ 2):
                        weapon[w_num].SetHover(True)
                        self.text_weapon.SetPos(pos.x + 65, pos.y + 65)

                        weapon_font_size_list = [30, 30, 30, 30, 30, 30, 30]
                        weapon_text_list = []
                        weapon_text_list.append("I  D：" + str(weapon[w_num].weaponId))
                        weapon_text_list.append("名　前：" + weapon[w_num].weaponName)
                        weapon_text_list.append("射　程：" + str(weapon[w_num].range))
                        weapon_text_list.append("攻撃力：" + str(weapon[w_num].power))
                        weapon_text_list.append("消　費：" + str(weapon[w_num].actioncost))
                        weapon_text_list.append("角　度：" + str(weapon[w_num].angle) + "°")
                        weapon_text_list.append("装備時行動力増減：" + str(weapon[w_num].plusdown))

                        self.text_weapon.SetFontsize(weapon_font_size_list)
                        self.text_weapon.SetText(weapon_text_list)

                    if weapon[w_num].GetHover() == True:
                        weapon_flg = True
                        self.isWeaponhover = True
                    elif weapon_flg != True:
                        self.isWeaponhover = False



    def DrawMap(self, map, player):
        # 敵ユニットの動きと連動させるタイミングはThinkが終わってから行動するタイミングになる
        # そのためここの段階でユニットの視界に入っても敵ユニットが移動中に表示されることはない（情報も出ないようにする）
        # 移動先を考えてるときの視覚情報も反映するためよく考えよう

        for num in range(PLAYER_UNIT_NUM):  # 見える範囲の色変化と移動できるかどうかの色の変化を加える（未確認）
            player_x = player[num].xl  # x = map.m_xy[num][0]
            player_y = player[num].yl  # y = map.m_xy[num][1]
            if player_y % 2 == 0:
                xl = 2 * player_x
                yl = player_y
            elif player_y % 2 == 1:
                xl = (2 * player_x) - 1
                yl = player_y

            # 移動すると見える範囲が変更されるので、移動時に更新をかける
            visible_distance = player[num].Status.Visible #見える範囲
            player[num].VisibleArea = MoveMethod.DistanceReverse(xl, yl, visible_distance)

            # ActionPowerは、移動するごとに減るようにしたいので、移動選択するたびに更新する。
            move_distance = player[num].Status.ActionPower - 10 #移動できる距離
            player[num].MoveArea = MoveMethod.DistanceReverse(xl, yl, move_distance)

        # ６点指定 六角形 30*24
        for num in range(720):
            # 優先順位　まず、壁、プレイヤー移動、プレイヤー視覚、建物
            # y = map.m_xy[num][1]   x = map.m_xy[num][0]
            if map.m_xy[num][14] == -1:
                color = DEAD_COLOR
                outline = DEAD_OUT_LINE_COLOR
            elif map.m_xy[num][14] == 0:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 1:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 2:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 3:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR
            elif map.m_xy[num][14] == 4:
                color = BOARD_COLOR
                outline = OUT_LINE_COLOR


            for p_num in range(PLAYER_UNIT_NUM):
                # 見える範囲のマスの色よりユニット選択時の移動できるマスを優先する。（合わせることができないので）
                VisibleAreaData = player[p_num].VisibleArea
                visible_count = len(VisibleAreaData)
                for visible_num in range(visible_count):
                    if map.m_xy[num][0] == VisibleAreaData[visible_num][0] and map.m_xy[num][1] == VisibleAreaData[visible_num][1] and map.m_xy[num][14] != -1 and color != CAN_MOVE_COLOR:
                        color = VISIBLE_COLOR
                        outline = OUT_LINE_COLOR

                if player[p_num].IsSelect == True:
                    MoveAreaData = player[p_num].MoveArea
                    move_count = len(MoveAreaData)
                    for move_num in range(move_count):
                        if map.m_xy[num][0] == MoveAreaData[move_num][0] and map.m_xy[num][1] == MoveAreaData[move_num][1] and map.m_xy[num][14] != -1:
                            color = CAN_MOVE_COLOR
                            outline = OUT_LINE_COLOR

            # 内側描画
            pygame.draw.polygon( self.screen, color, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])])
            # 枠線描画
            pygame.draw.polygon( self.screen, outline, [(map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][4], map.m_xy[num][5]), (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][8], map.m_xy[num][9]), (map.m_xy[num][10], map.m_xy[num][11]), (map.m_xy[num][12], map.m_xy[num][13])], 1)

            if map.m_xy[num][14] == 1:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 2)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 2)
            elif map.m_xy[num][14] == 2:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 4)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 4)
            elif map.m_xy[num][14] == 3:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 6)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 6)
            elif map.m_xy[num][14] == 4:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 8)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 8)
            elif map.m_xy[num][14] == 5:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 10)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 10)
            elif map.m_xy[num][14] == 6:
                pygame.draw.line( self.screen, outline, (map.m_xy[num][2], map.m_xy[num][3]), (map.m_xy[num][8], map.m_xy[num][9]), 12)
                pygame.draw.line( self.screen, outline, (map.m_xy[num][6], map.m_xy[num][7]), (map.m_xy[num][12], map.m_xy[num][13]), 12)


    def CreatePlayer(self, player):
        #[id, xl, yl, x, y, tagname]
        for num in range(PLAYER_UNIT_NUM):
            #self.player[num].Draw(ColorList.BLUE)
            self.player[num].IsVisible = True       # プレイヤー側は常に明るい表示（エネミー側をする場合は、エネミー側を常に明るい表示）
            self.player[num].SetPos(self.player[num].x, self.player[num].y)
            self.player[num].SetSize(20, 20)
            self.player[num].PlayerDraw()
            pos = self.player[num].GetPos()

            font = pygame.font.Font(None, 15)
            tag_length = len(player[num].tagname)
            if tag_length == 6:
                text = font.render(player[num].tagname, True, ColorList.RED.value)
                self.screen.blit(text, [pos.x - 10, pos.y])
            elif tag_length == 7:
                text = font.render(player[num].tagname, True, ColorList.RED.value)
                self.screen.blit(text, [pos.x - 14, pos.y])


    def CreateEnemy(self, enemy):
        #[id, xl, yl, x, y, tagname]
        for num in range(ENEMY_UNIT_NUM):
            #self.enemy[num].Draw(ColorList.YELLOW)
            self.enemy[num].SetPos(self.enemy[num].x, self.enemy[num].y)
            self.enemy[num].SetSize(20, 20)
            self.enemy[num].EnemyDraw()
            pos = self.enemy[num].GetPos()
            #pygame.draw.circle(self.screen, ColorList.YELLOW.value, (enemy.xy[num][3], enemy.xy[num][4]), 20)
            
            font = pygame.font.Font(None, 15)
            tag_length = len(self.enemy[num].tagname)
            if tag_length == 5:
                text = font.render(enemy[num].tagname, True, ColorList.RED.value)
                self.screen.blit(text, [pos.x  - 8, pos.y])
            elif tag_length == 6:
                text = font.render(enemy[num].tagname, True, ColorList.RED.value)
                self.screen.blit(text, [pos.x  - 10, pos.y])


    def DrawTurn(self):
        if self.TurnDisplay > 20:
            self.Turnfont = pygame.font.Font(None, 100)
            self.Turncounter = self.Turnfont.render( "Turn" + str(self.TurnCount), True, ColorList.BLACK.value)
            self.screen.blit(self.Turncounter, [CANVAS_WIDTH / 2 - 70, CANVAS_HEIGHT / 2 - 25])
        else:
            self.Turnfont = pygame.font.Font(None, 100)
            self.Turncounter = self.Turnfont.render( "Start", True, ColorList.BLACK.value)
            self.screen.blit(self.Turncounter, [CANVAS_WIDTH / 2 - 70, CANVAS_HEIGHT / 2 - 25])


#    def DrawCircleTimer(self):
#        pygame.draw.circle(self.screen, ColorList.YELLOW.value, (TIMER_X, TIMER_Y), CIRCLE_WIDTH_OUT)
#        pygame.draw.circle(self.screen, ColorList.RED.value, (TIMER_X, TIMER_Y), CIRCLE_WIDTH_IN)
#        pygame.draw.arc(self.screen, ColorList.LIME.value, [TIMER_X - CIRCLE_WIDTH_IN, TIMER_Y - CIRCLE_WIDTH_IN, CIRCLE_WIDTH_IN * 2, CIRCLE_WIDTH_IN * 2], pi/2, (pi/2) + (2*pi) * (self.counter * 0.98) / (MAX_COUNTER * FPS), CIRCLE_WIDTH_IN)
#
#
#    def DrawCountTimer(self):
#        self.Timerfont = pygame.font.Font(None, 30)
#        count = math.ceil(self.counter / FPS)
#        self.Timercounter = self.Timerfont.render( str(count), True, ColorList.BLACK.value)
#        counter_length = len( str(count) )
#        #self.screen.blit(self.Timercounter, [TIMER_X - 16, TIMER_Y - 9])               #映らない時　用
#        if counter_length == 3:
#            self.screen.blit(self.Timercounter, [TIMER_X - 16, TIMER_Y - 9])
#        elif counter_length == 2:
#            self.screen.blit(self.Timercounter, [TIMER_X - 12, TIMER_Y - 9])
#        elif counter_length == 1:
#            self.screen.blit(self.Timercounter, [TIMER_X - 9, TIMER_Y - 9])

    def MapData(self, map):
        # CalcReturnPosでマップの情報を受け渡す（表示等）
        # ユニットの表示と同じような処理（ここではできない）
        pass

    def CalcReturnPos(self, player, enemy, map, weapon):
        # 全部マップ・プレイヤー・エネミー何をクリックしても返って来るようにする。        
        Point_x, Point_y = PgLib.GetInputManager().GetMouse().GetPosMouce()
        self.pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()
        flg = False
        if self.pushClick != self.before_pushClick:
            if  self.click_flag == False:
                # キー入力確認用
                print("Push Click :  x:", str(Point_x) + " y:" + str(Point_y))
                #font = pygame.font.Font(None, 15)
                #[id, xl, yl, x, y, tagname]
                self.click_flag = True
                self.before_pushClick = PgLib.GetInputManager().GetMouse().GetPushClick()
                if Point_x != None and Point_y !=  None:
                    if self.pushClick == 1:
                        for p_num in range(PLAYER_UNIT_NUM):
                            p_x = math.floor(player[p_num].x)
                            p_y = math.floor(player[p_num].y)
                            player[p_num].IsSelect = False
                            if p_x - 21 < Point_x and Point_x < p_x + 21 and p_y - 21 < Point_y and Point_y < p_y + 21:
                                player[p_num].IsSelect = True
                                weaponid1 = player[p_num].WeaponId
                                weaponid2 = player[p_num].SecondWeaponId

                                self.text_player_status.SetPos(280, 50)

                                if weaponid1 != None and weaponid2 != None:
                                    font_size_list = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
                                    text_list = []
                                    text_list.append("I  D：" + str(player[p_num].ID))
                                    text_list.append("行動力：" + player[p_num].Status.ActionPower)
                                    text_list.append("名　前：" + player[p_num].Status.characterName)
                                    text_list.append("体　力：" + str(player[p_num].Status.HitPoint))
                                    text_list.append("攻撃力：" + str(player[p_num].Status.AttackPoint))
                                    text_list.append("防御力：" + str(player[p_num].Status.DeffencePoint))
                                    text_list.append("回避力：" + str(player[p_num].Status.AvoidancePoint))
                                    text_list.append("技術力：" + str(player[p_num].Status.TechnologyPoint))

                                    text_list.append("I  D：" + str(weapon[weaponid1].weaponId))
                                    text_list.append("名　前：" + weapon[weaponid1].weaponName)
                                    text_list.append("射　程：" + str(weapon[weaponid1].range))
                                    text_list.append("攻撃力：" + str(weapon[weaponid1].power))
                                    text_list.append("消　費：" + str(weapon[weaponid1].actioncost))
                                    text_list.append("角　度：" + str(weapon[weaponid1].angle) + "°")
                                    text_list.append("装備時行動力増減：" + str(weapon[weaponid1].plusdown))
                                    
                                    text_list.append("I  D：" + str(weapon[weaponid2].weaponId))
                                    text_list.append("名　前：" + weapon[weaponid2].weaponName)
                                    text_list.append("射　程：" + str(weapon[weaponid2].range))
                                    text_list.append("攻撃力：" + str(weapon[weaponid2].power))
                                    text_list.append("消　費：" + str(weapon[weaponid2].actioncost))
                                    text_list.append("角　度：" + str(weapon[weaponid2].angle) + "°")
                                    text_list.append("装備時行動力増減：" + str(weapon[weaponid2].plusdown))

                                elif weaponid1 != None and weaponid2 == None:
                                    font_size_list = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
                                    text_list = []
                                    text_list.append("I  D：" + str(player[p_num].ID))
                                    text_list.append("行動力：" + str(player[p_num].Status.ActionPower))
                                    text_list.append("名　前：" + player[p_num].Status.characterName)
                                    text_list.append("体　力：" + str(player[p_num].Status.HitPoint))
                                    text_list.append("攻撃力：" + str(player[p_num].Status.AttackPoint))
                                    text_list.append("防御力：" + str(player[p_num].Status.DeffencePoint))
                                    text_list.append("回避力：" + str(player[p_num].Status.AvoidancePoint))
                                    text_list.append("技術力：" + str(player[p_num].Status.TechnologyPoint))

                                    text_list.append("I  D：" + str(weapon[weaponid1].weaponId))
                                    text_list.append("名　前：" + weapon[weaponid1].weaponName)
                                    text_list.append("射　程：" + str(weapon[weaponid1].range))
                                    text_list.append("攻撃力：" + str(weapon[weaponid1].power))
                                    text_list.append("消　費：" + str(weapon[weaponid1].actioncost))
                                    text_list.append("角　度：" + str(weapon[weaponid1].angle) + "°")
                                    text_list.append("装備時行動力増減：" + str(weapon[weaponid1].plusdown))

                                elif weaponid1 == None and weaponid2 == None:
                                    font_size_list = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
                                    text_list = []
                                    text_list.append("I  D：" + str(player[p_num].ID))
                                    text_list.append("行動力：" + str(player[p_num].Status.ActionPower))
                                    text_list.append("名　前：" + player[p_num].Status.characterName)
                                    text_list.append("体　力：" + str(player[p_num].Status.HitPoint))
                                    text_list.append("攻撃力：" + str(player[p_num].Status.AttackPoint))
                                    text_list.append("防御力：" + str(player[p_num].Status.DeffencePoint))
                                    text_list.append("回避力：" + str(player[p_num].Status.AvoidancePoint))
                                    text_list.append("技術力：" + str(player[p_num].Status.TechnologyPoint))

                                    text_list.append("I  D：" + str(weapon[1].weaponId))
                                    text_list.append("名　前：" + weapon[1].weaponName)
                                    text_list.append("射　程：" + str(weapon[1].range))
                                    text_list.append("攻撃力：" + str(weapon[1].power))
                                    text_list.append("消　費：" + str(weapon[1].actioncost))
                                    text_list.append("角　度：" + str(weapon[1].angle) + "°")
                                    text_list.append("装備時行動力増減：" + str(weapon[1].plusdown))

                                self.text_player_status.SetFontsize(font_size_list)
                                self.text_player_status.SetText(text_list)
                                #font_size3 = 30
                                #text3 = "武　器：" + player[p_num].weaponId
                                #self.datadisp.SetFontsize3(font_size3)
                                #self.datadisp.SetText3(text3)
                                #font_size4 = 30
                                #text4 = "射　程：" + player[p_num].range
                                #self.datadisp.SetFontsize4(font_size4)
                                #self.datadisp.SetText4(text4)
                                #font_size5 = 30
                                #text5 = "消　費：" + player[p_num].actioncost
                                #self.datadisp.SetFontsize5(font_size5)
                                #self.datadisp.SetText5(text5)
                                if player[p_num].IsSelect == True:
                                    self.isUnitselect = True
                                    flg = True

                        for e_num in range(ENEMY_UNIT_NUM):
                            e_x = math.floor(enemy[e_num].x)
                            e_y = math.floor(enemy[e_num].y)
                            enemy[e_num].IsSelect = False
                            if e_x - 21 < Point_x and Point_x < e_x + 21 and e_y - 21 < Point_y and Point_y < e_y + 21:
                                enemy[e_num].IsSelect = True
                                self.text_enemy_status.SetPos(enemy[e_num].x + 21, enemy[e_num].y - 21)
                                self.text_enemy_status.SetSize(DATA_DISPLAY_WIDTH, DATA_DISPLAY_HEIGHT)
                                
                                enemy_font_size_list = [30, 30, 30, 30, 30, 30, 30, 30]
                                enemy_text_list = []
                                enemy_text_list.append("I  D：" + str(enemy[e_num].ID))
                                enemy_text_list.append("行動力：" + enemy[e_num].Status.ActionPower)
                                enemy_text_list.append("名　前：" + enemy[e_num].Status.characterName)
                                enemy_text_list.append("体　力：" + enemy[e_num].Status.HitPoint)
                                enemy_text_list.append("攻撃力：" + enemy[e_num].Status.AttackPoint)
                                enemy_text_list.append("防御力：" + enemy[e_num].Status.DeffencePoint)
                                enemy_text_list.append("回避力：" + enemy[e_num].Status.AvoidancePoint)
                                enemy_text_list.append("技術力：" + enemy[e_num].Status.TechnologyPoint)

                                self.text_enemy_status.SetFontsize(enemy_font_size_list)
                                self.text_enemy_status.SetText(enemy_text_list)
                                if enemy[e_num].IsSelect == True:
                                    self.isUnitselect = True
                                    flg = True

                        if flg == False:
                            self.isUnitselect = False
                        #for m_num in range(720):
                            # [x, y, xne, yne, xn, yn, xns, yns, xws, yws, xw, yw, xwe, ywe, board_number]
                            #pass
                            
                            #m_x = math.floor(map.xy[m_num][3])
                            #m_y = math.floor(map.xy[m_num][4])
                            #if m_x - 21 < Point_x and Point_x < m_x + 21 and m_y - 21 < Point_y and Point_y < m_y + 21:
                            #    print(map.xy[e_num])
                        
                    elif self.pushClick == 3:
                        for p_num in range(PLAYER_UNIT_NUM):
                            if player[p_num].IsSelect == True:
                                player[p_num].IsSelect = False

                        for e_num in range(ENEMY_UNIT_NUM):
                            if enemy[e_num].IsSelect == True:
                                enemy[e_num].IsSelect = False

                        self.isUnitselect = False


    def MoveData(self):
        # 移動できるマスは黄色にする（取り合えず）
        # リストでそれぞれの行動データを生成
        # ここの管理の仕方よくわからんどこで管理するべきなのか
        # list = [unit_id, action_number(1ターンで何回目の行動か), consumption(行動力消費量), x, y(移動先(今いる場所)), weapon_direction(武器向き), weapon(武器), shield_direction(盾向き), shield(盾)]
        # データとしては上記のものだけで成立する？

        # 行動消費量は防御（auto）でも減るため予想とは違った行動が起こる可能性あり（後の行動で武器の方向を変えて相手から外した場合、移動が優先される。）
        # 最終的に選択ユニットの1ターン行動を全部ぼかして見通せる感じのものにする。（武器の向き、盾の向き含めて）
        pass


    def MoveUnit(self, move, unit):
        pass
        # 行動数の減り方は、攻撃方法や移動で異なる
        # 行動終了時のplayer or enemy .xy[num][1, 2]に移動先のデータを入れ替え
        # 移動時の計算も必要


