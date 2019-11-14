import os
import tkinter as tk
from tkinter import *
from tkinter import colorchooser, filedialog, font, messagebox, ttk
import mpg123
from gtts import gTTS
from cryptography.fernet import Fernet
from ttkthemes import ThemedStyle
from tkinter import ttk
import webbrowser

typical = tk.Tk()
#typical.get_themes()
#typical.set_theme("plastik")
typical.geometry('400x400')
typical.title("TYPICAL")
style = ThemedStyle(typical)
style.set_theme("equilux")



#*OOOOOOOOOO   Main menu    *00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#*************   END MAIN MENU   *******************************************************************************************X

main_menu = tk.Menu()

#file Icons********************************************
new_icon = tk.PhotoImage(file ="new.png")
open_icon = tk.PhotoImage(file ="open.png")
save_icon = tk.PhotoImage(file ="save.png")
save_as_icon = tk.PhotoImage(file ="saveas.png")
exit_icon = tk.PhotoImage(file ="exit.png")



file = tk.Menu(main_menu, tearoff = False)





#edit icons********************************************
copy_icon = tk.PhotoImage(file="copy.png")
paste_icon = tk.PhotoImage(file="paste.png")
cut_icon = tk.PhotoImage(file="cut.png")
clear_all_icon = tk.PhotoImage(file="clear.png")
find_icon = tk.PhotoImage(file="find.png")

edit =tk.Menu(main_menu,tearoff=False)

#view icons**************************************************************xxxxx
toolbar = tk.PhotoImage(file ="toolbar.png")
statusbar = tk.PhotoImage(file ="statusbar.png")

view = tk.Menu(main_menu , tearoff = FALSE)


#color_theme icons************************************************************
light_default = tk.PhotoImage(file="light_default.png")
light_plus = tk.PhotoImage(file="light_plus.png")
dark = tk.PhotoImage(file="dark.png")
red  = tk.PhotoImage(file="red.png")
monokai = tk.PhotoImage(file="monokai.png")
blue = tk.PhotoImage(file="night_blue.png")

color_theme = tk.Menu(main_menu,tearoff = False)

theme_choice = tk.StringVar()
color_icons = (light_default,light_plus,dark,red,monokai,blue)

color_dict = {
    'light_default' : ('#000000','#ffffff'),
    'light_plus' : ('#474747','#e0e0e0'),
    'dark' : ('#c4c4c4','#2d2d2d'),
    'red' : ('#2d2d2d','#ffe8e8'),
    'monokai' : ('#d3b774','#474747'),
    'blue' : ('#ededed','#6b9dc2')
}


#cascadeingx menu bar0000000000000000000000000000000000000000000000000000000000

file_icon = tk.PhotoImage(file ="013-document.png")
file_btn = ttk.Button(main_menu , image = file_icon)
file_btn.grid(row =0 , column = 0, padx =1)


edit_icon = tk.PhotoImage(file ="017-edit-tool.png")
edit_btn = ttk.Button(main_menu , image = edit_icon)
edit_btn.grid(row =0 , column = 1, padx =1)

view_icon = tk.PhotoImage(file ="019-seo-and-web.png")
view_btn = ttk.Button(main_menu , image = view_icon)
view_btn.grid(row =0 , column = 2, padx =1)

theme_icon = tk.PhotoImage(file ="020-theme.png")
theme_btn = ttk.Button(main_menu ,image = theme_icon)
theme_btn.grid(row =0 ,column = 3, padx =1)





main_menu.add_cascade(image  = file_icon, menu=file)
main_menu.add_cascade(image = edit_icon, menu = edit)
main_menu.add_cascade(image = view_icon, menu = view)
main_menu.add_cascade(image = theme_icon, menu = color_theme)



toolbar = ttk.Label(typical)
toolbar.pack(side = tk.TOP,fill = tk.X)


toolbar1 = ttk.Label(typical)
toolbar1.pack(side = tk.TOP,fill = tk.X)

##########font box############################################################################################
font_tuple = tk.font.families()
font_families = tk.StringVar()
font_box = ttk.Combobox(toolbar,width = 10, textvariable = font_families ,state = "readonly")
font_box["values"]= font_tuple
font_box.current(font_tuple.index('Rasa'))
font_box.grid(row = 0 , column = 0 , padx =10)

###x#######size################################################################################################

size_var = tk.IntVar()
font_size = ttk.Combobox(toolbar,width=10,textvariable = size_var , state = "readonly")
font_size["values"]= tuple(range(6,96,6))
font_size.current(3)
font_size.grid(row =0,column=1, padx=10)


undo_icon = tk.PhotoImage(file = "undo.png")
undo_btn = ttk.Button(toolbar1,image =undo_icon)
undo_btn.grid(row =0,column =1, padx=1)

undo_btn.configure(command = lambda :editor.edit_undo())



new = 1
url = "https://www.google.com"

network_icon = tk.PhotoImage(file = "google.png")
network_btn = ttk.Button(toolbar1,image =network_icon)
network_btn.grid(row =0,column =3, padx=1)

network_btn.configure(command = lambda : webbrowser.open(url,new=new))

redo_icon = tk.PhotoImage(file = "redo.png")
redo_btn = ttk.Button(toolbar1,image =redo_icon)
redo_btn.grid(row =0,column =2, padx=1)
redo_btn.configure(command = lambda :editor.edit_redo())

#***********************BOLD*******************************************************************************************

bold_icon = tk.PhotoImage(file = "bold.png")
bold_btn = ttk.Button(toolbar,image =bold_icon)
bold_btn.grid(row =0,column =3, padx=1)

#***********************ITALIC*****************************************************************************************

italic_icon = tk.PhotoImage(file="italic.png")
italic_btn = ttk.Button(toolbar,image =italic_icon)
italic_btn.grid(row =0,column =4 ,padx = 1)

underline_icon = tk.PhotoImage(file="underline.png")
under_btn = ttk.Button(toolbar,image =underline_icon)
under_btn.grid(row =0,column =5 ,padx =1  )


paste1_icon = tk.PhotoImage(file ="paste.png")
paste1_btn = ttk.Button(toolbar , image = paste1_icon)
paste1_btn.grid(row =0 , column = 14, padx =1)
paste1_btn.configure(command = lambda :editor.event_generate("<Control v>"))


font_color = tk.PhotoImage(file = "font_color.png")
font_btn = ttk.Button(toolbar, image = font_color)
font_btn.grid(row = 0 ,column = 6 , padx = 1)
#**********************************ALIGNMENT************************************************************
center_icon = tk.PhotoImage(file ="align_center.png")
center_btn = ttk.Button(toolbar , image = center_icon)
center_btn.grid(row =0 , column = 7 , padx =1)

left_icon = tk.PhotoImage(file ="align_left.png")
left_btn = ttk.Button(toolbar , image = left_icon)
left_btn.grid(row =0 , column = 8 , padx =1)

right_icon = tk.PhotoImage(file ="align_right.png")
right_btn = ttk.Button(toolbar , image = right_icon)
right_btn.grid(row =0 , column = 9, padx =1)



speak_icon = tk.PhotoImage(file="speak.png")
speak_btn = ttk.Button(toolbar,image =speak_icon)
speak_btn.grid(row =0,column =10 ,padx = 1)

encrypt_icon = tk.PhotoImage(file="encrypt.png")
encrypt_btn = ttk.Button(toolbar,image =encrypt_icon)
encrypt_btn.grid(row =0,column =11 ,padx = 1)

decrypt_icon = tk.PhotoImage(file="decrypt.png")
decrypt_btn = ttk.Button(toolbar,image =decrypt_icon)
decrypt_btn.grid(row =0,column =12 ,padx = 1)
decrypt_btn.configure(command = lambda :editor.edit_undo())
###############################################END--TOLBAAR-----########################################################

editor = tk.Text(typical)
editor = Text( undo = True)
editor.config(wrap = 'word' , relief = tk.FLAT )

scroll_bar = ttk.Scrollbar(typical)
editor.focus_set()
scroll_bar.pack(side = tk.RIGHT ,fill = tk.Y )
editor.pack(fill = tk.BOTH ,expand = True)

scroll_bar.config(command = editor.yview)
editor.config(yscrollcommand = scroll_bar.set)

scroll_bar1 = ttk.Scrollbar(typical)
editor.focus_set()
scroll_bar1.pack(side = tk.LEFT , fill = tk.Y)
editor.pack(fill = tk.BOTH , expand = True)
scroll_bar1.config(command = editor.yview())
editor.config(xscrollcommand = scroll_bar1.set)



current_font_family = 'Rasa'
current_font_size = 24



def change_font(event = None ):
    global current_font_family
    current_font_family =font_families.get()
    editor.config(font = (current_font_family,current_font_size))

def change_size(event = None):
        global current_font_size
        current_font_size= size_var.get()
        editor.config(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>" , change_font)
font_size.bind("<<ComboboxSelected>>" , change_size)


def change_bold():
    text_property = tk.font.Font(font = editor['font'])
    if text_property.actual()['weight']== 'normal':
        editor.configure(font=(current_font_family,current_font_size,"bold"))
    if text_property.actual()['weight']== 'bold':
        editor.configure(font=(current_font_family,current_font_size,"normal"))

bold_btn.configure(command = change_bold)


def change_italic():
    text_property = tk.font.Font(font = editor['font'])
    if text_property.actual()['slant']== 'roman':
        editor.configure(font=(current_font_family,current_font_size,"italic"))
    if text_property.actual()['slant']== 'italic':
        editor.configure(font=(current_font_family,current_font_size,"normal"))

italic_btn.configure(command = change_italic)

def change_underline():
    text_property = tk.font.Font(font = editor['font'])
    if text_property.actual()['underline']== 0:
        editor.configure(font=(current_font_family,current_font_size,"underline"))
    if text_property.actual()['underline']== 1:
        editor.configure(font=(current_font_family,current_font_size,"normal"))

under_btn.configure(command = change_underline)



########################font color###################################################
def change_color():
    color_var = tk.colorchooser.askcolor()
    editor.configure(fg = color_var[1])


font_btn.configure(command = change_color)

def align_left():
    text_content = editor.get(1.0,'end')
    editor.tag_config('left',justify = tk.LEFT)
    editor.delete(1.0 , tk.END)
    editor.insert(tk.INSERT ,text_content, 'left')

left_btn.configure(command=align_left)

def speak_save():
    speak_content = editor.get(1.0,'end')
    language = 'en'
    myobj = gTTS(text=speak_content, lang=language, slow =False)
    myobj.save("welcome.mp3")
    os.system("mpg123 welcome.mp3")


speak_btn.configure(command = speak_save)



def add_image():

    editor.image_create(tk.END, image = img) # Example 1

img = tk.PhotoImage(file="x.png")

photo_icon = tk.PhotoImage(file ="landscape.png")
photo_btn = ttk.Button(toolbar1,image =photo_icon)
photo_btn.grid(row =0,column =4, padx=1)
photo_btn.configure(command = add_image)







key = Fernet.generate_key()
f = Fernet(key)
def encrypt_save():
    global  f
    message = editor.get(1.0, END)
    l=0
    data = message.encode()

    encrypted = f.encrypt(data)
    editor.delete(1.0, END)
    editor.insert(tk.END , encrypted)




encrypt_btn.configure(command = encrypt_save)


def align_center():
    text_content = editor.get(1.0,'end')
    editor.tag_config('center', justify = tk.CENTER)
    editor.delete(1.0 ,tk.END)
    editor.insert(tk.INSERT , text_content , 'center')

center_btn.configure(command = align_center)

def align_right():
    text_content = editor.get(1.0,'end')
    editor.tag_config('right',justify = tk.RIGHT)
    editor.delete(1.0 , tk.END)
    editor.insert(tk.INSERT , text_content , 'right')

right_btn.configure(command = align_right)


editor.configure(font = ('Rasa',24))

status_bar = ttk.Label(typical, text ="Status Bar")
status_bar.pack( side=tk.BOTTOM )

text_changed = False

def changed(event = None):
    global text_changed
    if editor.edit_modified():
        text_changed = True
        words = len(editor.get(1.0,'end-1c').split())
        characters = len(editor.get(1.0,'end-1c'))
        status_bar.configure(text =f'characters : {characters} words : {words}')
        editor.edit_modified(False)

editor.bind("<<Modified>>",changed)




def new_file():
    global save_file_id
    editor.delete(1.0,END)
    save_file_id = ' '

file.add_command(label="NEW", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)




def open_file():
	global save_file_id
	open_file_loc= filedialog.askopenfilename(initialdir = os.getcwd(),title = 'Select file', filetypes=(('Text files', '*.txt'), ('All files','*.*')))
	open_file=open(open_file_loc,'r')
	editor.delete(1.0,END)
	editor.insert(END,open_file.read())
	save_file_id=open_file_loc

file.add_command(label = "OPEN",image = open_icon,compound = tk.LEFT, accelerator = "Ctrl+O", command = open_file)


def save_file():
	global text,save_file_id
	if save_file_id=="":
		save_as_file()
	else:
		with open(save_file_id,'w') as f:
			f.write(editor.get(0.0,END))

file.add_command(label = "SAVE",image = save_icon,compound = tk.LEFT, accelerator = "Ctrl+S", command = save_file)

def save_as_file():
	global text,save_file_id
	name=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
	text2save=str(editor.get(0.0,END))
	name.write(text2save)
	name=str(name)[(str(name).find("name='")+6):str(name).find("'",(str(name).find("name='")+6))]
	save_file_id=name

file.add_command(label = "SAVE AS ",image = save_as_icon,compound = tk.LEFT, accelerator = "Ctrl+Alt+S" ,command = save_as_file)



file.add_command(label = "Exit",image = exit_icon,compound = tk.LEFT, command = typical.quit)






def find_file(event =None):

    def find():
        word = find_input.get()
        editor.tag_remove("match",'1.0',tk.END)
        matches = 0
        if word :
            start_pos ='1.0'
            while True:
                start_pos = editor.search(word,start_pos,stopindex= tk.END)
                if not start_pos:
                    break;
                end_pos = f'{start_pos}+{len(word)}c'
                editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos= end_pos
                editor.tag_config("match",foreground='red',background='green')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = editor.get(1.0, tk.END)
        new_content = content.replace(word,replace_text)
        editor.delete(1.0,tk.END)
        editor.insert(1.0,new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    find_frame = ttk.LabelFrame(find_dialog, text = "Find/Replace")
    find_frame.pack(pady =20)

    text_find_label= ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text = 'Replace :')

    find_input = ttk.Entry(find_frame,width = 10)
    replace_input = ttk.Entry(find_frame,width =10)

    find_button = ttk.Button(find_frame,text = 'Find', command = find)
    replace_button = ttk.Button(find_frame,text = 'Replace',command = replace)

    text_find_label.grid(row=0,column=0,padx =4,pady = 4)
    text_replace_label.grid(row= 1, column = 0,padx = 4, pady = 4)

    find_input.grid(row = 0 ,column = 1,padx = 4, pady =4)
    replace_input.grid(row=1, column=1,padx = 4, pady = 4)

    find_button.grid(row=2,column=0,padx=8,pady = 4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)



    find_dialog.mainloop()

edit.add_command(label = "FIND",image = find_icon,compound = tk.LEFT, accelerator = "Ctrl+F",command = find_file)


edit.add_command(label = "COPY",image = copy_icon,compound = tk.LEFT , accelerator = "Ctrl+C", command = lambda :editor.event_generate("<Control c>"))
edit.add_command(label = "PASTE",image = paste_icon,compound = tk.LEFT, accelerator = "Ctrl+V", command = lambda :editor.event_generate("<Control v>"))
edit.add_command(label = "CUT",image = cut_icon,compound = tk.LEFT, accelerator = "Ctrl+X", command = lambda :editor.event_generate("<Control x>"))
edit.add_command(label = "COPY",image = copy_icon,compound = tk.LEFT , accelerator = "Ctrl+C", command = lambda :editor.event_generate("<Control c>"))
edit.add_command(label = "CLEAR ALL ",image = clear_all_icon,compound = tk.LEFT, command = lambda :editor.delete(1.0,tk.END) )


show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)

def hide_toolbar():
    global  show_tool_bar
    if show_tool_bar:
        toolbar.pack_forget()
        show_tool_bar = False
    else:
        editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side = tk.TOP , fill = tk.X)
        editor.pack(fill = tk.BOTH,expand = True)
        status_bar.pack(side=tk.LEFT,fill = tk.X)
        show_tool_bar = True




def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_status_bar = True



view.add_checkbutton(label = "Status_bar",onvalue=1,offvalue=False,image = statusbar , compound = tk.LEFT , command = hide_statusbar)
#view.add_checkbutton( label = "Tool bar",onvalue = True , offvalue = 0, image = toolbar , compound = tk.LEFT, command = hide_toolbar)



def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color ,bg_color =  color_tuple[0],color_tuple[1]
    editor.config(background = bg_color,fg = fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton (label = i,image = color_icons[count], variable = theme_choice , compound = tk.LEFT, command = change_theme)
    count += 1



typical.config(menu = main_menu)

typical.bind("<Control-n>",new_file)
typical.bind("<Control-o>",open_file)
typical.bind("<Control-s>",save_file)
typical.bind("<Control-Alt-s>",save_as_file)
typical.bind("<Control-f>",find_file)


typical.mainloop()
