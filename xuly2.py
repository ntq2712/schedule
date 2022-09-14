import pyodbc 
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ex
from datetime import date
from PIL import ImageTk, Image
import os


cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-FSG3LBA5\SQLEXPRESS;"
    "Database=TRUNGTAM;"
    "Trusted_Connection=yes;"
)

cursor = cnxn.cursor()

gvi = 'nguyenthihoa'
cursor = cnxn.cursor()
cursor.execute("SELECT MAGV, TENGV, DIACHI, NGAYSINH, MALOP FROM GIAOVIEN WHERE TAIKHOANG = '%s' " %gvi)
rows = cursor.fetchall() 
gv = rows[0]

cursor.execute("SELECT TENLOP FROM LOP WHERE MALOP = '%s' " %gv[4])
rows = cursor.fetchall() 
tenlp = rows[0]

cursor = cnxn.cursor()
cursor.execute("SELECT NGAYHOC,TENPG FROM LICH WHERE MALOP = '%s' " %gv[4])
rows = cursor.fetchall() 
lich = rows[0]

cursor.execute("SELECT TENLOP FROM LOP WHERE MALOP = '%s' " %gv[4])
rows = cursor.fetchall() 
lop = rows[0]
root = Tk()
root.title("GIÁO VIÊN")

fn = LabelFrame(root, text ="",bg='white')
fn.grid(row=0,column=0)

img1 = ImageTk.PhotoImage(Image.open("gtvt1.jpg"))

panel1 = Label(fn, image = img1)
panel1.grid(row=0, column=0)

fn1 = LabelFrame(root, text ="")
fn1.grid(row=1,column=0)
img2 = ImageTk.PhotoImage(Image.open("lich.jpg"))

fn2 = LabelFrame(root, text ="")
fn2.grid(row=1,column=1)
img3 = ImageTk.PhotoImage(Image.open("them.jpg"))

fn3 = LabelFrame(root, text ="")
fn3.grid(row=2,column=0)
img4 = ImageTk.PhotoImage(Image.open("xoa.png"))

fn4 = LabelFrame(root, text ="")
fn4.grid(row=2,column=1)
img5 = ImageTk.PhotoImage(Image.open("sua.jpg"))

l2 = Label(fn, text='TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI'+ '\n' + 'THÀNH PHỐ HỒ CHÍ MINH',font = "Verdana 10 bold", fg="Dark blue")

l2.grid(row=1,column=0)

f5 = LabelFrame(root, text ="THÔNG TIN CÁ NHÂN", fg='red',font = "Helvetica 10 bold italic", bg="#00BFFF",width=40)
f5.grid(row=0,column=1)

Label(f5, text = 'Mã giáo viên: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=0, column=0)
Label(f5, text = gv[0], bg="#00BFFF",font = "Helvetica 10 bold italic",fg='#000000',width=24).grid(row=0, column=1)
Label(f5, text = 'Họ và Tên: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=1, column=0)
Label(f5, text = gv[1], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=1, column=1)
Label(f5, text = 'Địa chỉ: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=2, column=0)
Label(f5, text = gv[2], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=2, column=1)
Label(f5, text = 'Ngày sinh: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=3, column=0)
Label(f5, text = gv[3], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=3, column=1)
Label(f5, text = 'Dạy lớp: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=4, column=0)
Label(f5, text = lop[0], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=4, column=1)

def open():
    top = Toplevel()
    top.title("LỊCH HỌC THEO TUẦN")
    fl = LabelFrame(top,text='')
    fl.grid(row=0,column=0)
    Label(fl, text='Lịch học,thi theo tuần',font = "Helvetica 12 bold italic", width=35, anchor=SW).grid(row = 0, column=0)
    Radiobutton(fl, text="Tất cả").grid(row = 0, column=1)
    Radiobutton(fl, text="Lịch học").grid(row = 0, column=2)
    Radiobutton(fl, text="Lịch thi",width=15,anchor=SW).grid(row = 0, column=3)
    Button(fl,text='Hiện tại',bg='#0000FF',font = "Helvetica 8 bold italic",fg='white',width=10).grid(row=0, column=4)
    Button(fl,text='In lịch',bg='#0000FF',font = "Helvetica 8 bold italic",fg='white',width=10).grid(row=0, column=5)
    Button(fl,text='<Trở về',bg='#0000FF',font = "Helvetica 8 bold italic",fg='white',width=7).grid(row=0, column=6)
    Button(fl,text='Tiếp>',bg='#0000FF',font = "Helvetica 8 bold italic",fg='white',width=7).grid(row=0, column=7)
    fl1 = LabelFrame(top,text='')
    fl1.grid(row=1,column=0)
    Label(fl1, text='Ca học',font = "Helvetica 8 bold italic",fg='blue', width=8,height=4,bd=5).grid(row = 0, column=0)
    Label(fl1, text='Thứ 2',font = "Helvetica 8 bold italic",fg='blue', width=16,height=4,bd=2).grid(row = 0, column=1)
    Label(fl1, text='Thứ 3',font = "Helvetica 8 bold italic",fg='blue', width=16,height=4,bd=2).grid(row = 0, column=2)
    Label(fl1, text='Thứ 4',font = "Helvetica 8 bold italic",fg='blue', width=16,height=4,bd=2).grid(row = 0, column=3)
    Label(fl1, text='Thứ 5',font = "Helvetica 8 bold italic",fg='blue', width=16,height=4,bd=2).grid(row = 0, column=4)
    Label(fl1, text='Thứ 6',font = "Helvetica 8 bold italic",fg='blue', width=16,height=4,bd=2).grid(row = 0, column=5)
    Label(fl1, text='Thứ 7',font = "Helvetica 8 bold italic",fg='blue', width=16,height=4,bd=2).grid(row = 0, column=6)
    Label(fl1, text='Chủ nhật',font = "Helvetica 8 bold italic",fg='blue', width=17,height=4,bd=2).grid(row = 0, column=7)
    Label(fl1, text='Sáng',font = "Helvetica 8 bold italic",fg='blue', width=8,height=6,bg='#BDB76B').grid(row = 1, column=0)
    Label(fl1, text='Chìu',font = "Helvetica 8 bold italic",fg='blue', width=8,height=6,bg='#663399').grid(row = 2, column=0)
    Label(fl1, text='Tối',font = "Helvetica 8 bold italic",fg='blue', width=8,height=6,bg='#181818').grid(row = 3, column=0)
    fl2 = LabelFrame(top,text='')
    fl2.grid(row=2,column=0)
    Label(fl2, width=8,bd=5,bg='#00FF00').grid(row = 0, column=0)
    Label(fl2,text = 'Lịch học', width=8,bd=5).grid(row = 0, column=1)
    Label(fl2, width=8,bd=5,bg='yellow').grid(row = 0, column=2)
    Label(fl2,text = 'Lịch thi', width=8,bd=5).grid(row = 0, column=3)
    Label(fl2, width=8,bd=5,bg='#00BFFF').grid(row = 0, column=4)
    Label(fl2,text = 'Lịch học trực tuyến', width=15,bd=5).grid(row = 0, column=5)
    Label(fl2, width=8,bd=5,bg='red').grid(row = 0, column=6)
    Label(fl2,text = 'Tạm ngưng', width=52,bd=5, anchor=SW).grid(row = 0, column=7)
    Label(top,text ='Lưu ý:    Giáo viên cần theo giỏi lịch thường xuyên', width=120, anchor=SW).grid(row=3,column=0)
   
    if lich[0] == 'L':
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0], bg='#00FF00',width = 16, height=5).grid(row=1, column=1)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0], bg='#00FF00',width = 16, height=5).grid(row=1, column=3)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0], bg='#00FF00',width = 16, height=5).grid(row=1, column=5)
    elif lich[0] == 'C':
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=2)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=4)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=6)
    elif lich[0] == 'Full':
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=1)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=2)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=3)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=4)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=5)
        Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=6)
    top.mainloop()
    


Button(fn1,image=img2,bg='#00FF00', command=open).grid(row=0, column=0)
Button(fn1, text ='XEM LỊCH',font = "Helvetica 8 bold italic",bg='#6A5ACD', command=open, width=35,height=3).grid(row=0, column=1)


Button(fn2,image=img3,bg='#00FF7F').grid(row=0, column=0)
Button(fn2, text ='THÊM HỌC VIÊN',font = "Helvetica 8 bold italic",bg='#6495ED', width=35,height=3).grid(row=0, column=1)


Button(fn3,image=img4,bg='#00FFFF').grid(row=0, column=0)
Button(fn3, text ='XÓA HỌC VIÊN',font = "Helvetica 8 bold italic",bg='#006400', width=35,height=3).grid(row=0, column=1)


Button(fn4,image=img5,bg='#0000FF').grid(row=0, column=0)
Button(fn4, text ='ĐỔI MẬT KHẨU',font = "Helvetica 8 bold italic",bg='#0000FF', width=35,height=3).grid(row=0, column=1)

root.mainloop()    