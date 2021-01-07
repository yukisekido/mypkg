# mypkg
ロボットシステム学の課題で作成したROSを用いたプログラム

________________________________

### 内容について

これは、ロボットシステム学の講義で作成したROSプログラムを一部改変したものです。
プログラムを実行すると、約1秒間隔で数字をカウントしてくれます。プログラムは3種類あり、それぞれ異なるカウントをします。
　　
________________________________

### 必要となるもの

・Raspberry Pi 4 Model B　　×1  
・Raspberry Piを動かすのに必要なもの

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
また、端末は最低でも2つ開いておいてください。  

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
端末1でrosrun mypkg count.pyを、端末2でrostopic echo /count_upを実行すると、端末2に1秒間に1ずつカウントしていく様子が表示されます。  

##### 2.1秒間に1.の2乗ずつカウント  
```
// 端末1で実行するもの //  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ chmod +x square.py  
$ rosrun mypkg count.py  
```  
```
// 端末2で実行するもの //  
$ rostopic echo /count_up  
```
端末1でrosrun mypkg count.pyを、端末2でrostopic echo /count_upを実行すると、端末2に1秒間に1ずつカウントしていく様子が表示されます。  

##### 3.1秒間に1.の10倍ずつカウント  
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
端末1でrosrun mypkg count.pyを、端末2でrostopic echo /count_upを実行すると、端末2に1秒間に1ずつカウントしていく様子が表示されます。  
