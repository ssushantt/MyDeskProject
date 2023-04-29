from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from sqlite3 import *

def f1():
	mw.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	mw.deiconify()
def f3():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con=None
def f4():
	vw.withdraw()
	mw.deiconify()
def f5():
	con=None
	try:
		con=connect("kc.db")
		cursor=con.cursor()
		sql="insert into student values('%d','%s')"
		try:
			rno=int(aw_ent_rno.get())
		except valueError:
			showerror("issue", "rno should be integer only")
			return
		if rno < 1:
			showerror("issue","rno should be min 1")
			return
		name=aw_ent_name.get()
		if not name.isalpha():
			showerror("issue","name can contain only alphabets")
			return
		if len(name) <2:
			showerror("issue","name should contain min of 2 alphabets")
			return
		
		cursor.execute(sql %(rno,name))
		con.commit()
		showinfo("success","record created")
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_rno.focus()
mw=Tk()
mw.title("S.M.S. By Sushant")
mw.geometry("700x700+50+50")
f=("Arial",36,"bold")


mw_btn_add=Button(mw,text="Add Student",font=f,width=15,command=f1)
mw_btn_view=Button(mw,text="View Student",font=f,width=15,command=f3)
mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)


aw=Toplevel(mw)
aw.title("Add Student")
aw.geometry("700x700+50+50")


aw_lab_rno=Label(aw,text="enter rno",font=f)
aw_ent_rno=Entry(aw,font=f)
aw_lab_name=Label(aw,text="enter name",font=f)
aw_ent_name=Entry(aw,font=f)
aw_btn_save=Button(aw,text="save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)



aw_lab_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()

vw=Toplevel(mw)
vw.title("View Student")
vw.geometry("700x700+50+50")


vw_st_data=ScrolledText(vw,width=20,height=8,font=f)
vw_btn_back=Button(vw,text="Back",font=f,command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

mw.mainloop()