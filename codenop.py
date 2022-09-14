cursor = cnxn.cursor()
cursor.execute("SELECT MAQTV, HOTENQTV, DIACHI, NGAYSINH FROM QUANTRIVIEN WHERE TAIKHOANG = '%s' " %qtvi)
rows = cursor.fetchall()    
qtvj = rows[0]
root = Tk()
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
        malop = l.get()
        ssi = ss.get()
        ssi = int(ssi)
        if tamp == 1 :
            cursor.execute("UPDATE PHONG SET TRANGTHAI = \'L\', TIME = ? WHERE TENPG = ? ", (time,phong))
            cursor.execute("UPDATE LOP SET SS = ? WHERE MALOP = ? ", (ssi,malop))
            cursor.execute('INSERT INTO LICH VALUES (?,?,?,?)', (malop,'C',phong,time))
            cursor.commit() 
        elif tamp == 2 :
            cursor.execute("UPDATE PHONG SET TRANGTHAI = \'C\', TIME = ? WHERE TENPG = ? ", (time,phong))
            cursor.execute("UPDATE LOP SET SS = ? WHERE MALOP = ? ", (ssi,malop))
            cursor.execute('INSERT INTO LICH VALUES (?,?,?,?)', (malop,'L',phong,time))
            cursor.commit() 
        elif tamp == 3 :
            cursor.execute("UPDATE PHONG SET TRANGTHAI = \'Full\', TIME = ? WHERE TENPG = ? ", (time,phong))
            cursor.execute("UPDATE LOP SET SS = ? WHERE MALOP = ? ", (ssi,malop))
            cursor.execute('INSERT INTO LICH VALUES (?,?,?,?)', (malop,'Full',phong,time))
            cursor.commit() 
        else :
            def phongcho() :
                cursor.execute("SELECT MALOP FROM LOPCHO")
                lops = cursor.fetchall()
                LP = [20]
                for lop in lops:
                    lp = "".join(lop)
                    LP.append(lp)
                tam = LP.count(l.get())
                if tam > 0 :
                    messagebox.showerror('THÔNG BÁO', 'LỚP ĐÃ CÓ TRONG HÀNG CHỜ')
                else :
                    cursor.execute("SELECT TIME FROM PHONG  WHERE TENPG = '%s' " %phong)    
                    PC = cursor.fetchall()
                    timecho = PC[0]
                    timecho1 = timecho[0]
                    timecho1 = int(timecho1)
                    cursor.execute('INSERT INTO LOPCHO VALUES (?,?,?)', (malop,timecho1,phong))
                    cursor.execute("UPDATE LOP SET SS = ? WHERE MALOP = ? ", (ssi,malop))
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
        cursor.execute('INSERT INTO LOP VALUES (?,?,?,?)', (mlp,tlp,mgvlp,0))
        cursor.commit() 
    Button(fxl3, text = "THÊM",width=20,height=2, command=them).grid(row = 3, column=1)  

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
