#!/usr/bin/python
# -*- Coding: utf-8 -*-

# PDFの結合

# PDFファイルが壊れているとき、あるいは誤った構造で作られているときは、下記のエラーが出ます。
# 「PyPDF2.utils.PdfReadError: Could not find xref table at specified location」
# この場合は、不正なPDFをブラウザ等で開いて、PDFとして印刷をし、作成しなおしてください。

# ライブラリのインポート
import os
import sys
import PyPDF2


# 引数の取得
args = sys.argv

# もし引数が指定されていなかったら説明を出力
if len(args) == 1:
    print("PDFファイルの結合")
    print(" 複数のPDFファイルを結合し、result.pdf で出力.")
    print(" 使い方：")
    print("   python PDFJoin.py pdfFile1 [pdfFile2]...")
    exit(1)

# 配列の先頭は、本プログラム名が入っているので取り除く
baseName = args.pop(0)

# 出力ファイル名を取得
# PDFファイルと同じ場所に result.pdf で作成する
outFile = os.path.join( os.path.dirname(args[0]) , 'result.pdf')

# 引数のファイル名をソートする
args.sort()

# PDFオブジェクトの作成
merger = PyPDF2.PdfFileMerger(strict=False)
# ドロップされたファイルを、ファイル名順に追加
for f in args:
    merger.append(os.path.abspath(f))
# ファイルの書き出し
merger.write(outFile)
# 終了
merger.close()
