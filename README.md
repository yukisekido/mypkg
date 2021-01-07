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
```  

________________________________

### 実行方法

実行する方法は全部で3通りあります。  
