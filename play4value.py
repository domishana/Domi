#coding: utf-8
import play

playernum = 2
times_of_battle = 10

player_winpts = [0 for i in range(playernum)]

for m in range(times_of_battle):
    game = play.game_setup(playernum,1)
    game.begingame()

    nowmax = 0     #最高点
    playnum = [i for i in range(game.number)]
    scores = [game.player[i].victorycount() for i in range(game.number)]

    for (i, n) in zip(playnum, scores):#勝利判定は多分本来はgameクラスに書かないといけなさそう(そのうちちゃんと書きます！！！)
        if nowmax <= n:
            nowmax = n
            winnerIndex = i
    player_winpts[winnerIndex] += 1


print("トータル結果")
print(player_winpts)
