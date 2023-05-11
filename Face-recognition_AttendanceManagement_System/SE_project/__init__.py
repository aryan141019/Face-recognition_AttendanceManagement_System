from dependencies import tk
import csv
from dependencies import Image, ImageTk
from dependencies import comaptible_image_format
from database import create_database_file, create_admin_file, record_exists, add_record
import os

mainWin = tk.Tk()
s_height, s_width = mainWin.winfo_screenheight(), mainWin.winfo_screenwidth()
mainWin.geometry(str(s_width)+"x"+str(s_height))
mainWin.title('Login page')
dir_name = os.path.dirname(__file__)
create_database_file()

# Getting the background image.
# photo = comaptible_image_format(os.path.join(dir_name, 'icons/dome.jpeg'), (s_width, s_height))
# photo = comaptible_image_format(r'SE_project\dome.jpeg', (s_width, s_height))


# create_admin_file()

# Creating string variables to store entries 
# name_var = tk.StringVar()
# id_var = tk.StringVar()

# def submit():
#     name = name_var.get()
#     id = id_var.get()
#     print("Admin name: ", name)
#     print("ID: ", id)
#     if record_exists(name, id, "admin_database.csv"):
#         import login
#     else:
#         error_win = tk.Toplevel(canvas)
#         error_win.title('Error')
#         error_win.geometry('200x200')
#         error_label = tk.Label(error_win,
#                                 text='The ID entered does not exists. Register first',
#                                 font=('Helvetica 18')).pack(side='top')
#         name_var.set('')
#         id_var.set('')


# def submitNew():
#     name = name_var.get()
#     id = id_var.get()
#     print("Admin name: ", name)
#     print("ID: ", id)
#     if record_exists(id, "admin_database.csv"):
#         print("Already exists!!!")
#         error_win = tk.Toplevel(canvas)
#         error_win.title('Error')
#         error_win.geometry('200x200')
#         error_label = tk.Label(error_win,
#                                 text='The ID entered exists. Please login!',
#                                 font=('Helvetica 18')).pack(side='top')
#         name_var.set('')
#         id_var.set('')
#     else:
#         with open("admin_database.csv", 'a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow([name, id])
#             error_win = tk.Toplevel(canvas)
#             error_win.title('Success')
#             error_win.geometry('200x200')
#             error_label = tk.Label(error_win,
#                                     text='Registered successfully. Please login!',
#                                     font=('Helvetica 18')).pack(side='top')
#             name_var.set('')
#             id_var.set('')
            

# def new_admin():
#     newWin = tk.Toplevel(canvas)
#     newWin.title('Admin registration')
#     newWin.geometry('300x300')

#     name_field = tk.Label(newWin, text='Name', 
#                         font=('Helvetica 17'), 
#                         foreground='black',
#                         background='white')
#     name_field.place(x=15, y=50)
#     id_field = tk.Label(newWin, text='ID', 
#                         font=('Helvetica 17'), 
#                         foreground='black', 
#                         background='white')
#     id_field.place(x=15, y=100)
#     input_name = tk.Entry(newWin, textvariable=name_var, width=20, border=3)
#     input_name.place(x=100, y=55)
#     input_id = tk.Entry(newWin, textvariable=id_var, width=20, border=3)
#     input_id.place(x=100, y=105)
#     submit_btn = tk.Button(newWin,
#                                 text='Submit',
#                                 font=('Helvetica 16 bold'),
#                                 borderwidth=3,
#                                 command=submitNew)
#     submit_btn.place(x=115, y=170)
    

# Displaying the background image.
# canvas = tk.Canvas(mainWin, width=s_width, height=s_height)
# canvas.pack(fill='both', expand=True)
# canvas.create_image(0, 0, image=photo, anchor='nw')
# canvas.create_rectangle((s_width/2)-200, (s_height/2)+50, 
#                         (s_width/2)+200, (s_height/2)+330, 
#                         fill='white', outline='white')

# login_label = tk.Label(canvas,
#                         text='Login',
#                         font=('Helvetica 20 bold'),
#                         foreground='blue',
#                         background='white')
# login_label.place(x=(s_width/2)-50, y=(s_height/2)+80)
# name_field = tk.Label(canvas, text='Name', 
#             font=('Helvetica 17'), 
#             foreground='black',
#             background='white')
# name_field.place(x=(s_width/2)-120, y=(s_height/2)+150)
# id_field = tk.Label(canvas, text='ID', 
#             font=('Helvetica 17'), 
#             foreground='black', 
#             background='white')
# id_field.place(x=(s_width/2)-120, y=(s_height/2)+210)
# input_name = tk.Entry(canvas, textvariable=name_var, width=20, border=3)
# input_name.place(x=(s_width/2)+15, y=(s_height/2)+160)
# input_id = tk.Entry(canvas, textvariable=id_var, width=20, border=3)
# input_id.place(x=(s_width/2)+15, y=(s_height/2)+220)


# # Creating submit button to enter all details.
# submit_button = tk.Button(canvas,
#                         text='Submit',
#                         font=('Helvetica 16 bold'),
#                         borderwidth=3,
#                         command=submit)
# submit_button.place(x=(s_width/2)-130, y=(s_height/2)+275)

# canvas.create_line((s_width/2), (s_height/2)+270,
#                     (s_width/2), (s_height/2)+325,
#                     width=2)

# # Creating new admin button
# admin_button = tk.Button(canvas,
#                         text='New Admin',
#                         font=('Helvetica 16 bold'),
#                         borderwidth=3,
#                         command=new_admin)
# admin_button.place(x=(s_width/2)+30, y=(s_height/2)+275)

# mainWin.mainloop()
