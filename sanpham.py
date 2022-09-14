import pyodbc 
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ex
from datetime import date, datetime
from PIL import ImageTk, Image
import os


cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-FSG3LBA5\SQLEXPRESS;"
    "Database=TRUNGTAM;"
    "Trusted_Connection=yes;"
)

cursor = cnxn.cursor()

cursor.execute('SELECT TAIKHOANG FROM GIAOVIEN')
rows = cursor.fetchall() 
L = [50]
for row in rows: 
    tkgv = " ".join(row)
    L.append(tkgv)

cursor.execute('SELECT TAIKHOANG FROM SINHVIEN')
rows = cursor.fetchall() 
SV = [50]
for row in rows: 
    tksv = " ".join(row)
    SV.append(tksv)

cursor.execute('SELECT TAIKHOANG FROM QUANTRIVIEN')
rows = cursor.fetchall() 
QTV = [50]
for row in rows: 
    tkqtv = " ".join(row)
    QTV.append(tkqtv)
   
window = Tk()
window.title("Trung tâm ngoại ngữ GTVT")

img = ImageTk.PhotoImage(Image.open("gtvt.jpg"))

panel = Label(window, image = img,bg="light gray")

panel.place(x=0,y=0, relheight=5, relwidth=1)

panel.grid(row=0, column=0)

l1 = Label(window, text='TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI'+ '\n' + 'THÀNH PHỐ HỒ CHÍ MINH',font = "Verdana 16 bold", height=5, width=34, fg="Dark blue")

l1.grid(row=1,column=0)

f2 = LabelFrame(window, text ="ĐĂNG NHẬP",font = "Helvetica 16 bold italic",fg='red', bg="light gray", bd=5)
f2.grid(row=10,column=0)
mylb1 = Label(f2, text="TÀI KHOẢN:",font = "Verdana 10 bold", fg="dark green",bg="light gray",height=3)
mylb1.grid(row = 0 , column = 1)
e = Entry(f2,selectforeground='blue', width = 50,bd=1)
e.grid(row = 0, column = 2)
e.get()

mylb4 = Label(f2, text="MẬT KHẨU:",font = "Verdana 10 bold", fg="dark green",bg="light gray", height=2)
mylb4.grid(row = 1, column = 1)

e1 = Entry(f2, width = 50,show="*",bd=1)
e1.grid(row = 1, column = 2)
e1.get()

r = IntVar()
TK = e.get()

temp = 0
def myClick(x) :
    global temp
    tkgv = L.count(e.get())
    tksv = SV.count(e.get())
    tkqtv = QTV.count(e.get())
    if x == 1:
        if tkgv == 1:
            TKGV = e.get()
            cursor.execute("SELECT PASS FROM GIAOVIEN WHERE TAIKHOANG = '%s' " %TKGV)
            rows = cursor.fetchall() 
            for row in rows :
                matkhaugv = " ".join(row)
            if e1.get() == matkhaugv :
                temp = 1
                
            else :
                messagebox.showerror('THÔNG BÁO','MẬT KHẨU SAI')
        else :
            messagebox.showerror('THÔNG BÁO','TÀI KHOẢN KHÔNG TỒN TẠI')
    elif x == 2  :
        if  tksv == 1 :
            TKSV = e.get()
            cursor.execute("SELECT PASS FROM SINHVIEN WHERE TAIKHOANG = '%s' " %TKSV)
            rows = cursor.fetchall() 
            for row in rows :
                matkhausv = " ".join(row)
            if e1.get() == matkhausv :
                temp = 2
                
            else :
                messagebox.showerror('THÔNG BÁO','MẬT KHẨU SAI')
        else :
            messagebox.showerror('THÔNG BÁO','TÀI KHOẢN KHÔNG TỒN TẠI')
    elif x == 3 :
        if  tkqtv == 1 :
            TKQTV = e.get()
            cursor.execute("SELECT PASS FROM QUANTRIVIEN WHERE TAIKHOANG = '%s' " %TKQTV)
            rows = cursor.fetchall() 
            for row in rows :
                matkhauqtv = " ".join(row)
            if e1.get() == matkhauqtv :
                temp = 3
                
            else :
                messagebox.showerror('THÔNG BÁO','MẬT KHẨU SAI')
        else :
            messagebox.showerror('THÔNG BÁO','TÀI KHOẢN KHÔNG TỒN TẠI')


def dangnhap() :
    if temp == 1:
        messagebox.showinfo('THÔNG BÁO','ĐĂNG NHẬP THÀNH CÔNG')
        gvi = e.get()
        cursor = cnxn.cursor()
        cursor.execute("SELECT MAGV, TENGV, DIACHI, NGAYSINH, MALOP FROM GIAOVIEN WHERE TAIKHOANG = '%s' " %gvi)
        rows = cursor.fetchall() 
        gv = rows[0]

        cursor = cnxn.cursor()
        cursor.execute("SELECT NGAYHOC,TENPG FROM LICH WHERE MALOP = '%s' " %gv[4])
        rows = cursor.fetchall() 
        lich = rows[0]
        
        cursor.execute("SELECT TENLOP,TGBD,TGKT FROM LOP WHERE MALOP = '%s' " %gv[4])
        rows = cursor.fetchall() 
        lop = rows[0]
        tenlp = lop[0]
        root = Toplevel()
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
            top.title("LỊCH DẠY THEO TUẦN")
            fl = LabelFrame(top,text='')
            fl.grid(row=0,column=0)
            r = IntVar()
            Label(fl, text='Lịch học,thi theo tuần',font = "Helvetica 12 bold italic", width=35, anchor=SW).grid(row = 0, column=0)
            Radiobutton(fl, text="Tất cả", value= 1, variable=r).grid(row = 0, column=1)
            Radiobutton(fl, text="Lịch học", value= 2, variable=r).grid(row = 0, column=2)
            Radiobutton(fl, text="Lịch thi", value= 3, variable=r,width=15,anchor=SW).grid(row = 0, column=3)
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
            Label(top,text ='Lưu ý: bắt đầu từ ' + lop[1]+ ' đến '+ lop[2] , width=120, anchor=SW, fg='red').grid(row=3,column=0)
        
            if lich[0] == 'L':
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp, bg='#00FF00',width = 16, height=5).grid(row=1, column=1)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp, bg='#00FF00',width = 16, height=5).grid(row=1, column=3)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp, bg='#00FF00',width = 16, height=5).grid(row=1, column=5)
            elif lich[0] == 'C':
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=2)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=4)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=6)
            elif lich[0] == 'Full':
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=1)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=2)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=3)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=4)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=5)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'Lớp: ' + tenlp,bg='#00FF00',width = 16, height=6).grid(row=1, column=6)
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
    elif temp == 2:
        messagebox.showinfo('THÔNG BÁO','ĐĂNG NHẬP THÀNH CÔNG')
        svi = e.get()
        cursor = cnxn.cursor()
        cursor.execute("SELECT MASV, TENSV, DIACHI, NGAYSINH, MALOP FROM SINHVIEN WHERE TAIKHOANG = '%s' " %svi)
        rows = cursor.fetchall() 
        sv = rows[0]

        cursor.execute("SELECT NGAYHOC,TENPG FROM LICH WHERE MALOP = '%s' " %sv[4])
        rows = cursor.fetchall() 
        lich = rows[0]

        cursor.execute("SELECT MAGV,TENLOP,TGBD, TGKT FROM LOP WHERE MALOP = '%s' " %sv[4])
        rows = cursor.fetchall() 
        lop = rows[0]
        magvx = int(lop[0])

        cursor.execute("SELECT TENGV FROM GIAOVIEN WHERE MAGV = '%s' " %magvx)
        rows = cursor.fetchall() 
        tngvx = rows[0]

        
        root = Toplevel()
        root.title("SINH VIÊN")

        fn = LabelFrame(root, text ="",bg='white')
        fn.grid(row=0,column=0)

        img1 = ImageTk.PhotoImage(Image.open("gtvt1.jpg"))

        panel9 = Label(fn, image = img1)
        panel9.grid(row=0, column=0)

        fn9 = LabelFrame(root, text ="")
        fn9.grid(row=1,column=0)
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

        Label(f5, text = 'Mã sinh viên: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=0, column=0)
        Label(f5, text = sv[0], bg="#00BFFF",font = "Helvetica 10 bold italic",fg='#000000',width=24).grid(row=0, column=1)
        Label(f5, text = 'Họ và Tên: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=1, column=0)
        Label(f5, text = sv[1], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=1, column=1)
        Label(f5, text = 'Địa chỉ: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=2, column=0)
        Label(f5, text = sv[2], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=2, column=1)
        Label(f5, text = 'Ngày sinh: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=3, column=0)
        Label(f5, text = sv[3], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=3, column=1)
        Label(f5, text = 'Học lớp: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=4, column=0)
        Label(f5, text = lop[0], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24).grid(row=4, column=1)

        def open():
            top = Toplevel()
            top.title("LỊCH HỌC THEO TUẦN")
            fl = LabelFrame(top,text='')
            fl.grid(row=0,column=0)
            r = IntVar()
            Label(fl, text='Lịch học,thi theo tuần',font = "Helvetica 12 bold italic", width=35, anchor=SW).grid(row = 0, column=0)
            Radiobutton(fl, text="Tất cả", value= 1, variable=r).grid(row = 0, column=1)
            Radiobutton(fl, text="Lịch học", value= 2, variable=r).grid(row = 0, column=2)
            Radiobutton(fl, text="Lịch thi", value= 3, variable=r,width=15,anchor=SW).grid(row = 0, column=3)
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
            Label(top,text ='Lưu ý: bắt đầu từ ' + lop[2]+ ' đến '+ lop[3] , width=120, anchor=SW, fg='red').grid(row=3,column=0)
        
            if lich[0] == 'L':
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0], bg='#00FF00',width = 16, height=5).grid(row=1, column=1)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0], bg='#00FF00',width = 16, height=5).grid(row=1, column=3)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0], bg='#00FF00',width = 16, height=5).grid(row=1, column=5)
            elif lich[0] == 'C':
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=2)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=4)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=6)
            elif lich[0] == 'Full':
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=1)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=2)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=3)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=4)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=5)
                Label(fl1, text ='Phòng: ' + lich[1] + '\n'+ 'GV: ' + tngvx[0],bg='#00FF00',width = 16, height=6).grid(row=1, column=6)
            top.mainloop()
            


        Button(fn9,image=img2,bg='#00FF00', command=open).grid(row=0, column=0)
        Button(fn9, text ='XEM LỊCH',font = "Helvetica 8 bold italic",bg='#6A5ACD', command=open, width=35,height=3).grid(row=0, column=1)


        Button(fn2,image=img3,bg='#00FF7F').grid(row=0, column=0)
        Button(fn2, text ='THÊM HỌC PHẦN',font = "Helvetica 8 bold italic",bg='#6495ED', width=35,height=3).grid(row=0, column=1)


        Button(fn3,image=img4,bg='#00FFFF').grid(row=0, column=0)
        Button(fn3, text ='XÓA ĐĂNG KÝ',font = "Helvetica 8 bold italic",bg='#006400', width=35,height=3).grid(row=0, column=1)


        Button(fn4,image=img5,bg='#0000FF').grid(row=0, column=0)
        Button(fn4, text ='ĐỔI MẬT KHẨU',font = "Helvetica 8 bold italic",bg='#0000FF', width=35,height=3).grid(row=0, column=1)
        root.mainloop() 

    elif temp == 3:
        messagebox.showinfo('THÔNG BÁO','ĐĂNG NHẬP THÀNH CÔNG')
        qtvi = e.get()
        cursor = cnxn.cursor()
        cursor.execute("SELECT MAQTV, HOTENQTV, DIACHI, NGAYSINH FROM QUANTRIVIEN WHERE TAIKHOANG = '%s' " %qtvi)
        rows = cursor.fetchall()    
        qtvj = rows[0]
        root = Toplevel()
        root.title("QUẢN TRỊ VIÊN")

        fn = LabelFrame(root, text ="",bg='white')
        fn.grid(row=0,column=0)

        img1 = ImageTk.PhotoImage(Image.open("qui.jpg"))
        imgxl = ImageTk.PhotoImage(Image.open("gtvt2.jpg"))

        panel = Label(fn, image = img1)

        panel.grid(row=0, column=0)

        f3 = LabelFrame(root, text ="THÔNG TIN CÁ NHÂN", fg='#FF1493',font = "Helvetica 10 bold italic", bg="#00BFFF",width=40)
        f3.grid(row=0,column=1)
        Label(f3, text = 'Mã giáo viên: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=0, column=0)
        Label(f3, text = qtvj[0], bg="#00BFFF",font = "Helvetica 10 bold italic",fg='#000000',width=24,height=2).grid(row=0, column=1)
        Label(f3, text = 'Họ và Tên: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=1, column=0)
        Label(f3, text = qtvj[1], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24,height=2).grid(row=1, column=1)
        Label(f3, text = 'Địa chỉ: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=2, column=0)
        Label(f3, text = qtvj[2], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24,height=2).grid(row=2, column=1)
        Label(f3, text = 'Ngày sinh: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=3, column=0)
        Label(f3, text = qtvj[3], bg="#00BFFF",font = "Helvetica 10 bold italic",width=24,height=2).grid(row=3, column=1)
        Label(f3, text = 'Chức vụ: ', bg="#00BFFF",font = "Verdana 10 bold").grid(row=4, column=0)
        Label(f3, text = 'Hiệu trưởng',fg='red', bg="#00BFFF",font = "Helvetica 10 bold italic",width=24,height=2).grid(row=4, column=1)
        r = IntVar()

        cursor.execute("SELECT MALOP FROM LOP")
        rows = cursor.fetchall() 
        malop = [10]
        for row in rows:
            ml = "".join(row)
            malop.append(ml)

        tamp = 0
        phong = ' '
        def xeplich() :
            top = Toplevel()
            top.title("XẾP LỊCH HỌC")

            fxl = LabelFrame(top, text ="",bg='white')
            fxl.grid(row=0,column=0)

            
            Label(fxl, image = imgxl).grid(row=0, column=0)
            Label(fxl, text='TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI'+ '\n' + 'THÀNH PHỐ HỒ CHÍ MINH',font = "Verdana 10 bold", fg="Dark blue").grid(row=1,column=0)

            fxl1 = LabelFrame(top, text ="")
            fxl1.grid(row=0,column=1)

            Label(fxl1, text = "Ma Lớp :",width=10,height=2,font = "Verdana 10 bold").grid(row=0, column=0)
            l = ex.Combobox(fxl1, width=30, values= malop)
            l.grid(row=0, column=1)
            Label(fxl1, text = "Sỉ Số :",width=10,height=2,font = "Verdana 10 bold").grid(row=1, column=0)
            ss = Entry(fxl1, width=34,bd=2)
            ss.grid(row=1, column=1)
            Label(fxl1, text = "Số TC :",width=10,height=2,font = "Verdana 10 bold").grid(row=2, column=0)
            tg = ex.Combobox(fxl1, width=30, values= [1,2,3,4]) 
            tg.grid(row=2, column=1)
            
            
            
            def kiemtra(x) : 
                global tamp
                cursor.execute('SELECT * FROM PHONG')
                rows = cursor.fetchall() 
                L = [10]
                for row in rows: 
                    L.append(row[1])
            
                ssi = ss.get()
                ssi = int(ssi)
                if ssi > 14 and ssi < 41:
                    m = 100
                    count = 0
                    i = 0
                    for l in L:
                        i = i + 1
                        if l - ssi > 0 and l - ssi < m :
                            m = l - ssi
                            count = i - 1
                    pg = L[count]
                    cursor.execute("SELECT TENPG,TRANGTHAI FROM PHONG  WHERE SOGHE = '%s' " %pg)
                    P = cursor.fetchall()
                    PG = P[0]
                    global phong
                    phong = PG[0]
                    if x == 3:
                        if PG[1] == 'K         ' :
                            tamp = 3
                    
                        else :
                            tamp= 0
                    elif x == 1 :
                        if PG[1] == 'C         ' or  PG[1] == 'K         ':
                            tamp = 1
                            
                        else :
                            tamp= 0
                    elif x == 2 :
                        if PG[1] == 'L         ' or  PG[1] == 'K         ':
                            tamp = 2
                            
                        else :
                            tamp = 0
                elif ssi > 40 :
                    messagebox.showerror('THÔNG BÁO', 'SỐ LƯỢNG HỌC VIÊN THAM GIA NHIỀU HƠN 40')

                else :
                    messagebox.showerror('THÔNG BÁO', 'SỐ LƯỢNG HỌC VIÊN THAM GIA DƯỚI 15')


            def laplich() :
                global tamp, phong
                time = tg.get()
                time = int(time)
                hientai = datetime.today()

                d = hientai.day
                m = hientai.month + time
                y = hientai.year
                end = datetime(y,m,d)

                malop = l.get()

                ssi = ss.get()
                ssi = int(ssi)

                if tamp == 1 :
                    cursor.execute("UPDATE PHONG SET TRANGTHAI = \'L\' WHERE TENPG = ? ", (phong))
                    cursor.execute('UPDATE LOP SET SS = ?, TGBD = ?, TGKT = ? WHERE MALOP = ? ', (ssi,hientai,end,malop))
                    cursor.execute('INSERT INTO LICH VALUES (?,?,?)', (malop,'C',phong))
                    cursor.commit() 
                elif tamp == 2 :
                    cursor.execute("UPDATE PHONG SET TRANGTHAI = \'C\'WHERE TENPG = ? ", (phong))
                    cursor.execute('UPDATE LOP SET SS = ?, TGBD = ?, TGKT = ? WHERE MALOP = ? ', (ssi,hientai,end,malop))
                    cursor.execute('INSERT INTO LICH VALUES (?,?,?)', (malop,'L',phong))
                    cursor.commit() 
                elif tamp == 3 :
                    cursor.execute("UPDATE PHONG SET TRANGTHAI = \'Full\'WHERE TENPG = ? ", (phong))
                    cursor.execute('UPDATE LOP SET SS = ?, TGBD = ?, TGKT = ? WHERE MALOP = ? ', (ssi,hientai,end,malop))
                    cursor.execute('INSERT INTO LICH VALUES (?,?,?)', (malop,'Full',phong))
                    cursor.commit() 
                else :
                    def phongcho() :
                        cursor.execute("SELECT MALOP FROM CHO")
                        lops = cursor.fetchall()
                        LP = [20]
                        for lop in lops:
                            lp = "".join(lop)
                            LP.append(lp)
                        tam = LP.count(l.get())
                        if tam > 0 :
                            messagebox.showerror('THÔNG BÁO', 'LỚP ĐÃ CÓ TRONG HÀNG CHỜ')
                        else :
                            cursor.execute("SELECT MALOP FROM LICH  WHERE TENPG = '%s' " %phong)    
                            PC = cursor.fetchall()
                            ml = PC[0]
                            malop = ml[0]
                            

                            cursor.execute("SELECT TGKT FROM LOP  WHERE MALOP = '%s' " %malop)  
                            L = cursor.fetchall()
                            T = L[0]

                            tx = datetime.today()
                            d1 = tx.day
                            m1 = tx.month + time
                            y1 = tx.year
                            
                            timec = datetime(y1,m1,d1)

                            d2 = timec.day
                            m2 = timec.month + time
                            y2 = timec.year
                            timecend = datetime(y2,m2,d2)
                            cursor.execute('INSERT INTO CHO VALUES (?,?,?,?)', (malop,timec,timecend,phong))
                            cursor.commit() 
                          
                    messagebox.showerror('THÔNG BÁO', 'Trùng lịch')
                    Button(top, text = "Xếp vào lớp chờ",font = "Verdana 10 bold",bg='#0000FF',fg='white',width=20,height=2, command=phongcho).grid(row = 5, column=0)
                    Button(top, text = "Quay lại",font = "Verdana 10 bold",bg='#0000FF',fg='white',width=20,height=2, command=laplich).grid(row = 5, column=1)
            Radiobutton(fxl1, text="2-4-6", variable= r, value = 1,command=lambda : kiemtra(r.get())).grid(row = 3, column=0)
            Radiobutton(fxl1, text="3-5-7", variable= r, value = 2,command=lambda : kiemtra(r.get())).grid(row = 3, column=1)
            Radiobutton(fxl1, text="FULL",  variable= r, value = 3,fg='red',command=lambda : kiemtra(r.get())).grid(row = 3, column=2)
            Button(fxl1, text = "Bắt đầu",font = "Verdana 10 bold",bg='#0000FF',fg='white',width=20,height=2, command=laplich).grid(row = 4, column=1) 
        def themlop() :
            cursor.execute("SELECT MAGV FROM GIAOVIEN WHERE MALOP = \'null\' ") 
            rows = cursor.fetchall() 
            magv = [30]
            for i in rows:
                mgvk = "".join(map(str,i))
                magv.append(mgvk)
            top1 = Toplevel()
            top1.title("THÊM LỚP")

            fxl2 = LabelFrame(top1, text ="",bg='white')
            fxl2.grid(row=0,column=0)

            
            Label(fxl2, image = imgxl).grid(row=0, column=0)
            Label(fxl2, text='TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI'+ '\n' + 'THÀNH PHỐ HỒ CHÍ MINH',font = "Verdana 10 bold", fg="Dark blue").grid(row=1,column=0)

            fxl3 = LabelFrame(top1, text ="")
            fxl3.grid(row=0,column=1)

            Label(fxl3, text = "Mã Lớp :",width=10,height=2,font = "Verdana 10 bold").grid(row=0, column=0)
            lp = Entry(fxl3, width=34)
            lp.grid(row=0, column=1) 
            Label(fxl3, text = "Tên lớp :",width=10,height=2,font = "Verdana 10 bold").grid(row=1, column=0)
            ten = Entry(fxl3, width=34)
            ten.grid(row=1, column=1) 
            Label(fxl3, text = "Mã giáo viên :",width=10,height=2,font = "Verdana 10 bold").grid(row=2, column=0)
            ma = ex.Combobox(fxl3, width=30, values= magv)
            ma.grid(row=2, column=1)
            def them():
                mlp = lp.get()
                tlp = ten.get()
                mgvlp = ma.get()
                mgvlp = int(mgvlp)
                tx = datetime(1880,1,1)
                cursor.execute('INSERT INTO LOP VALUES (?,?,?,?,?,?)', (mlp,tlp,mgvlp,0,tx,tx))
                cursor.execute('UPDATE GIAOVIEN SET MALOP = ? WHERE MAGV = ? ', (mlp,mgvlp))
                cursor.commit() 
            Button(fxl3, text = "THÊM",width=20,height=2,bg= '#0000FF', command=them).grid(row = 3, column=1)  

        def themgv():
            ngay = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
            thang = (1,2,3,4,5,6,7,8,9,10,11,12)
            nams = (1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000)
            top2 = Toplevel()
            top2.title("THÊM GIÁO VIÊN")
            Label(top2, text = "Mã giáo viên :").grid(row=0, column=0)
            magv = Entry(top2, width=20)
            magv.grid(row=0, column=1)   
            Label(top2, text = "Họ tên :").grid(row=1, column=0)
            hten = Entry(top2, width=20)
            hten.grid(row=1, column=1)  
            Label(top2, text = "Địa chỉ:").grid(row=2, column=0)
            dc = Entry(top2, width=20)
            dc.grid(row=2, column=1) 
            Label(top2, text = "Ngày:").grid(row=3, column=0)
            ng = ex.Combobox(top2, width=17, values= ngay)
            ng.grid(row=3, column=1) 
            Label(top2, text = "Tháng:").grid(row=4, column=0)
            thg = ex.Combobox(top2, width=17, values= thang)
            thg.grid(row=4, column=1)  
            Label(top2, text = "Năm:").grid(row=5, column=0)
            nam = ex.Combobox(top2, width=17, values= nams)
            nam.grid(row=5, column=1) 
            Label(top2, text = "Tài khoảng:").grid(row=6, column=0)
            tkh = Entry(top2, width=20)
            tkh.grid(row=6, column=1)  
            Label(top2, text = "Passwork:").grid(row=7, column=0)
            pw = Entry(top2, width=20)
            pw.grid(row=7, column=1)   
            Label(top2, text = "Mã lớp:").grid(row=8, column=0) 
            malpd = Entry(top2, width=20)
            malpd.grid(row=8, column=1)  
            def them():
                ng1 = int(ng.get())
                thang1= int(thg.get())
                nam1 = int(nam.get())
                d = datetime.date(nam1, thang1, ng1)
                mgvk = int(magv.get())
                htenk = hten.get()
                dck= dc.get()
                tkhk = tkh.get()
                pwk = pw.get()
                malpk = malpd.get()
                cursor.execute('INSERT INTO GIAOVIEN VALUES (?,?,?,?,?,?,?)', (mgvk,htenk,dck,d,tkhk,pwk,malpk))
                cursor.commit() 
            Button(top2, text = "THÊM", command=them).grid(row = 9, column=1)  
            
        def danhsach() :
            top2 = Toplevel()
            top2.title("Quản lý")
            Button(top2, text = "Danh sách hoc viên", command=themgv).grid(row = 0, column=0)
            Button(top2, text = "Danh sách giáo viên", command=themgv).grid(row = 0, column=1)
            Button(top2, text = "Danh sách lớp", command=themgv).grid(row = 0, column=2)
            Button(top2, text = "Danh sách phòng học", command=themgv).grid(row = 0, column=0)

        fn1 = LabelFrame(root, text ="")
        fn1.grid(row=1,column=0)
        img2 = ImageTk.PhotoImage(Image.open("lich.jpg"))
        Button(fn1,image=img2,bg='#00FF00', command=xeplich).grid(row=0, column=0)
        Button(fn1, text ='XẾP LỊCH',font = "Helvetica 8 bold italic",bg='#6A5ACD', command=xeplich, width=21,height=3).grid(row=0, column=1)

        fn2 = LabelFrame(root, text ="")
        fn2.grid(row=1,column=1)
        img3 = ImageTk.PhotoImage(Image.open("them.jpg"))
        Button(fn2,image=img3,bg='#00FF7F', command=themlop).grid(row=0, column=0)
        Button(fn2, text ='THÊM LỚP MỚI', command=themlop,font = "Helvetica 8 bold italic",bg='#6495ED', width=35,height=3).grid(row=0, column=1)

        fn3 = LabelFrame(root, text ="")
        fn3.grid(row=2,column=0)
        img4 = ImageTk.PhotoImage(Image.open("gv.jpg"))
        Button(fn3,image=img4,bg='#00FFFF', command=themgv).grid(row=0, column=0)
        Button(fn3, text ='THÊM GIAO VIÊN', command=themgv,font = "Helvetica 8 bold italic",bg='#006400', width=21,height=3).grid(row=0, column=1)

        fn4 = LabelFrame(root, text ="")
        fn4.grid(row=2,column=1)
        img5 = ImageTk.PhotoImage(Image.open("quanly.jpg"))
        Button(fn4,image=img5,bg='#0000FF', command=danhsach).grid(row=0, column=0)
        Button(fn4, text ='QUẢN LÝ', command=danhsach,font = "Helvetica 8 bold italic",bg='#0000FF', width=35,height=3).grid(row=0, column=1)

        root.mainloop()


 
    else :
        messagebox.showerror('THÔNG BÁO','ĐĂNG NHẬP KHÔNG THÀNH CÔNG')


Radiobutton(f2, text="Giáo viên", variable= r, value = 1, command=lambda : myClick(r.get()), bg="light gray").grid(row = 3, column=1)
Radiobutton(f2, text="Sinh Viên", variable= r, value = 2, command=lambda : myClick(r.get()), bg="light gray").grid(row = 3, column=2)
Radiobutton(f2, text="Quản Trị Viên", variable= r, value = 3, command=lambda : myClick(r.get()), fg="red", bg="light gray").grid(row = 3, column=3)

myButton1 = Button(f2, text = "ĐĂNG NHẬP",fg='white', font = "Verdana 10 bold", bg='Dark blue',width=20,height=2, command=dangnhap)
myButton1.grid(row = 4, column=2)

window.mainloop()