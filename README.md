# Hi-Performance-Python

以下の目的で教材として使用します。

- コンピュータサイエンスについて理解を深める
- パフォーマンスに関する問題解決の方法について知識を得る

## なぜPythonを使うか

Pythonは記述力が大変高い言語です。実行するまでに必要なステップがすくないためすぐに実行して結果を確認できます。
また、ライブラリが充実しておりすぐに重要でかつ安定した機能を使うことができます。

しかし一方で、パフォーマンスの問題を引き起こしやすい言語でもあるので、学習用としても最適であると考えています。


## 各ファイルの説明

- decorate.py  
処理時間を計測するためのデコレータ

- julia.py  
ジュリア集合を計算し可視化するコード  
このファイルを基本として、パフォーマンスを計測する各種方法を記述します

- julia_guppy.py  
heapyを使ってヒープ上のオブジェクトを計測した例  

- julia_memory_label.py  
memory_profilerを使ってラベルをつけてメモリ使用量を計測するコード

- julia_profile_memory_cpu.py  
cpu_profiler、memory_profilerを使ってcpuとメモリについて計測するコード

- prime.py  
素数かどうかチェックするコード  
コードのどの部分をベクタライズできると嬉しいでしょうか？

- search.py  
簡単な工夫で計算を高速化する例を示すコードです
