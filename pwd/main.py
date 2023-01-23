import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as tkMB
from pwd.pwd_get import GetRandomSt
#

def create_pass():
    passentry.delete(0, tk.END)
    
    letters = []
    
    try:
        if ul_check.get():
            ul_str = a.ul_str()
            letters.append(ul_str)
            
        if lc_check.get():
            lc_str = a.lc_str()
            letters.append(lc_str)
            
        if num_check.get():
            num_str = a.num_str()
            letters.append(num_str)
            
        if sym_check.get():
            sym_str = a.sym_str()
            letters.append(sym_str)
            
        length = lengthentry.get()
        
        letter = a.get_random_string(int(length), ''.join(letters))
    
        passentry.insert(tk.END, letter)
        
        tree.insert('', 'end', value=letter)
            
    except IndexError:
        tkMB.showerror('error', '文字種を選択してください')
    
    except ValueError:
        tkMB.showerror('error', '数字を入力してください')
    
def copy_text():
    txt = passentry.get()
    root.clipboard_append(txt)

root = tk.Tk()
root.title('pwdApp')
a = GetRandomSt()

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, fill=tk.Y, pady=5)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.LEFT, fill=tk.Y, pady=5)

tk.Label(frame_left, text='長さを指定').pack(pady=5)

lengthentry = tk.Entry(frame_left)
lengthentry.pack(pady=5)

ul_check = tk.BooleanVar()
tk.Checkbutton(frame_left, text='A-Z', variable=ul_check).pack(pady=5)

lc_check = tk.BooleanVar()
tk.Checkbutton(frame_left, text='a-z', variable=lc_check).pack(pady=5)

num_check = tk.BooleanVar()
tk.Checkbutton(frame_left, text='0-9', variable=num_check).pack(pady=5)

sym_check = tk.BooleanVar()
tk.Checkbutton(frame_left, text='記号', variable=sym_check).pack(pady=5)

tk.Button(frame_left, text='作成', command=create_pass).pack(pady=5)

passentry = tk.Entry(frame_left)
passentry.pack(pady=5)

tk.Button(frame_left, text='コピー', command=copy_text).pack(pady=5)

tree = ttk.Treeview(frame_right)
tree['column'] = (1,)
tree['show'] = 'headings'
tree.heading(1, text='履歴')
tree.pack(fill=tk.Y, expand=True)



root.mainloop()