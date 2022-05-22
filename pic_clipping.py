# coding: utf-8
import os,sys
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from pic_clipping_logic import pic_clipping

global txt1,txt2,txt3,txt4,root
labellist=["画像ファイルのパス","出力先のフォルダパス"]
pramlabel=["輪郭の検出閾値","最大検出サイズ","最小検出サイズ","白地を透過する"]

def re_enter(event):
    clipping()

def clipping():
    # [0]画像ファイルのパス、[1]出力先のフォルダパス
    path_list = np.array([txt1.get(), txt2.get()])
    # [0]輪郭の検出閾値、[1]最大検出サイズ、[2]最小検出サイズ
    pram_list = np.array([f2txt1.get(), f2txt2.get(),f2txt3.get()])
    transparent = var.get()

    try:
        pic_clipping(path_list,pram_list,transparent)
    except:
        messagebox.showerror("エラー","エラーが発生しました。")
    else:
        messagebox.showinfo("完了","画像の切り抜き処理が完了しました。")

# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("画像ファイル","*.jpg;*.jpeg;*.png")]
    #iFile = os.path.abspath(os.path.dirname(__file__))
    # AP化するとカレントディレクトリが一時フォルダになるため固定
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = "./")
    txt1.delete(0,"end")
    txt1.insert(0,iFilePath)

# フォルダ指定の関数
def dirdialog_clicked():
    #iDir = os.path.abspath(os.path.dirname(__file__))
    # AP化するとカレントディレクトリが一時フォルダになるため固定
    iDirPath = filedialog.askdirectory(initialdir = "./")
    txt2.delete(0,"end")
    txt2.insert(0,iDirPath)

root = tk.Tk()
root.attributes("-topmost", True)
root.title("pic clipping")
root.geometry("300x300")

font1 = font.Font(family='Helvetica', size=10, weight='bold')
# Frame1の作成
frame1 = ttk.Frame(root, padding=10)
frame1.grid(row=0, column=1, sticky=tk.W)

# 1 対象画像のパステキストボックス
label1 = tk.Label(frame1, text=labellist[0], fg="black", font=font1)
label1.grid(row = 1, column = 0, sticky=tk.W)
txt1 = tk.Entry(frame1,width=30)
txt1.grid(row = 2, column = 0)
IDirButton = ttk.Button(frame1, text="..", command=filedialog_clicked,width=2)
IDirButton.grid(row = 2, column = 1)

# 2 出力先のパステキストボックス
label2 = tk.Label(frame1, text=labellist[1], fg="black", font=font1)
label2.grid(row = 3, column = 0,sticky=tk.W)
txt2 = tk.Entry(frame1,width=30)
txt2.grid(row = 4, column = 0)
IDirButton = ttk.Button(frame1, text="..", command=dirdialog_clicked,width=2)
IDirButton.grid(row = 4, column = 1)

# 切り取り処理のボタン生成
btn = tk.Button(frame1, text="切り取り", command=clipping, height=1,width=8)
btn.grid(row = 5, column = 0,sticky=tk.W)

label3 = tk.Label(frame1, text="※日本語パスに対応してません", fg="red", font=font1)
label3.grid(row = 6, column = 0,columnspan = 3, sticky=tk.W)

font2 = font.Font(family='Helvetica', size=12, weight='bold')

frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=1, column=1, sticky=tk.W)

oplabel = tk.Label(frame2, text="オプション", fg="black", font=font2)
oplabel.grid(row = 0, column = 0,sticky=tk.W)

f2label1 = tk.Label(frame2, text=pramlabel[0], fg="black", font=font1)
f2label1.grid(row = 1, column = 0,sticky=tk.W)
f2txt1 = tk.Entry(frame2,width=5)
f2txt1.grid(row = 1, column = 1,sticky=tk.W)
f2txt1.insert(0,200)

f2label2 = tk.Label(frame2, text=pramlabel[1], fg="black", font=font1)
f2label2.grid(row = 2, column = 0,sticky=tk.W)
f2txt2 = tk.Entry(frame2,width=5)
f2txt2.grid(row = 2, column = 1,sticky=tk.W)
f2txt2.insert(0,10000)

f2label3 = tk.Label(frame2, text=pramlabel[2], fg="black", font=font1)
f2label3.grid(row = 3, column = 0,sticky=tk.W)
f2txt3 = tk.Entry(frame2,width=5)
f2txt3.grid(row = 3, column = 1,sticky=tk.W)
f2txt3.insert(0,1500)

f2label3 = tk.Label(frame2, text=pramlabel[3], fg="black", font=font1)
f2label3.grid(row = 4, column = 0,sticky=tk.W)
var = tk.BooleanVar()
var.set( False )
chk = tk.Checkbutton(frame2,variable = var)
chk.grid(row = 4, column = 1,sticky=tk.W)

root.bind('<Return>', re_enter)
root.mainloop()