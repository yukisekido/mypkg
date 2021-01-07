# mypkg
ロボットシステム学の課題で作成したROSを用いたプログラム

________________________________

### 内容について

これは、ロボットシステム学の講義で作成したROSプログラムを一部改変したものです。
プログラムを実行すると、約1秒間隔で数字をカウント、または表示してくれます。プログラムは3種類あり、それぞれ異なる動作をします。
　　
________________________________

### 必要となるもの

・Raspberry Pi 4 Model B　×1  
・Raspberry Piを動かすのに必要なもの  

また、ROSの環境は以下の通りです。  
● ROS Noetic  
・OS：Ubuntu 20.04.1 LTS  
・ROS Distribution：Noetic Ninjemys

________________________________

### 実行の前準備

実行の前に以下の作業をお願いします。  
```
$ cd ~/catkin_ws/src  
$ git clone https://github.com/yukisekido/mypkg.git  
$ cd ~/catkin_ws  
$ catkin_make  
$ cd src/mypkg/scripts  
$ ls //プログラムがあるかの確認  
```  
また、端末は必要に応じて複数開いておいてください。  

________________________________

### 実行方法

まずは端末1で以下を実行します。  
```
$ roscore &  
```  
次にプログラムを実行します。プログラムは全部で3種類あります。  

##### 1.1秒間に1ずつカウント  
```
// 端末1で実行するもの //  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ chmod +x count.py  
$ rosrun mypkg count.py  
```  
```
// 端末2で実行するもの //  
$ rostopic echo /count_up  
```
端末1で rosrun mypkg count.py を、端末2で rostopic echo /count_up を実行すると、端末2に1秒間に1ずつカウントしていく様子が表示されます。  

##### 2.1秒毎に1.の2乗を表示  
まず1.の「端末1で実行するもの」を実行させてください。その上で以下を実行します。  
```
// 端末2で実行するもの //  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ chmod +x square.py  
$ rosrun mypkg square.py  
```  
```
// 端末3で実行するもの //  
$ rostopic echo /square  
```
端末1で rosrun mypkg count.py を、端末2で rosrun mypkg square.py を、端末3で rostopic echo /square を実行すると、端末1の情報を受け取って、端末3に1秒毎に1.の2乗を表示していきます。  
＊ rosrun mypkg count.py | rosrun mypkg square.py とすることで一気に実行させることもできます。

##### 3.1秒毎に1.の10倍を表示  
2.と同様、1.の「端末1で実行するもの」を実行させてください。その上で以下を実行します。  
```
// 端末2で実行するもの //  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ chmod +x tentimes.py  
$ rosrun mypkg tentimes.py  
```  
```
// 端末3で実行するもの //  
$ rostopic echo /tentimes  
```
端末1で rosrun mypkg count.py を、端末2で rosrun mypkg tentimes.py を、端末3で rostopic echo /tentimes を実行すると、端末1の情報を受け取って、端末3に1秒毎に1.の10倍を表示していきます。  
＊ rosrun mypkg count.py | rosrun mypkg tentimes.py とすることで一気に実行させることもできます。
________________________________

### 動画
  
こちらから動画に移動できます。  
動画では4つの端末を使い、3つのプログラムを同時に動かしています。  

________________________________

### ライセンス
[BSD 3-Clause "New" or "Revised" License](https://github.com/yukisekido/mypkg/blob/main/LICENSE)
