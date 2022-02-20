#!/usr/bin/python
# -*- Coding: utf-8 -*-

# PDFの結合

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

# プログラム名を取得
baseName = args.pop(0)

# 出力ファイル名を取得
# PDFファイルと同じ場所に result.pdf で作成する
outFile = os.path.join( os.path.dirname(args[0]) , 'result.pdf')

# 引数のファイル名をソートする
args.sort()

# PDFのマージ
merger = PyPDF2.PdfFileMerger(strict=False)
# ドロップされたファイルを、ファイル名順に追加
for f in args:
    merger.append(os.path.abspath(f))
# ファイルの書き出し
merger.write(outFile)
# 終了
merger.close()
