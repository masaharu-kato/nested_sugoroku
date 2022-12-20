# nested_sugoroku

Nested Sugoroku Game Simulation

「ネストすごろく」のシミュレーションプログラム．

## Rule of "Nested Sugoroku"

Sugoroku Map:

[Start] -> [Nest] -> [Nest] -> [Nest] -> [Nest] -> [Nest] -> [Goal]

- Player starts from [Start].
- Roll a dice and move forward as many as the number of the dice.
  - If the player reached (or exceeded) [Goal], finish the current "Nested Sugoroku" game.
  - Else (on [Nest] positions), Start a new "Nested Sugoroku" game (recursively).

## 「ネストすごろく」のルール

すごろくのマップ:

[Start] -> [Nest] -> [Nest] -> [Nest] -> [Nest] -> [Nest] -> [Goal]

- [Start]地点から始める．
- サイコロを振り，出た目の数だけ進む．
- [Goal]に到達した(もしくは超えた)場合は，現在のゲームを終了する．
- それ以外([Nest]の位置)の場合は，新たに「ネストすごろくを」（再帰的に）開始する．

(参考: https://twitter.com/koteitan/status/1604851675604209664 )
