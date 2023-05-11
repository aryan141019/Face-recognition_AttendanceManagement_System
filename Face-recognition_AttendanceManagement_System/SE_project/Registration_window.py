from dependencies import *
from create_new_face import new_entry
from os.path import exists
from database import record_exists
import os

dir_name = os.path.dirname(__file__)
print(dir_name)
register_window = tk.Tk()
s_height, s_width = register_window.winfo_screenheight(), register_window.winfo_screenwidth()
register_window.title('Registration Window')
register_window.geometry(str(s_width)+"x"+str(s_height))

# Displaying background image.
photo = comaptible_image_format(os.path.join(dir_name, 'icons/dome.jpeg'), (s_width, s_height))
canvas = tk.Canvas(register_window, width=s_width, height=s_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=photo, anchor='nw')

# Initialzing the camera to capture live feed.
vid = cv2.VideoCapture(0)
width, height = 400, 400
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Variables to get inputs from entry fields
name_var = tk.StringVar()
id_var = tk.StringVar()
gender_var = tk.StringVar()


def home():
    register_window.destroy()
    import login


def display_camera_feed():
    _, frame = vid.read()
    if frame is None:
        return 
    frame = cv2.flip(frame, 1)
    opencv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_img = Image.fromarray(opencv_img)
    photo_image = ImageTk.PhotoImage(image=captured_img)

    camera_widget.photo_image = photo_image
    camera_widget.configure(image=photo_image)
    camera_widget.after(10, display_camera_feed)

def stop_camera_feed():
    global feed
    _, feed = vid.read()
    vid.release()
    cv2.destroyAllWindows()


def submit():
    name = name_var.get()
    id = id_var.get()
    gender = gender_var.get()
    print("Name: ", name)
    print("Id: ", id)
    print("Gender: ", gender)

    if record_exists(name, id, "database.csv"):
        error_win = tk.Toplevel(canvas)
        error_win.title('Error')
        error_win.geometry('200x200')
        error_label = tk.Label(error_win,
                                text='The ID entered already exists.',
                                font=('Helvetica 18')).pack(side='top')
        # resetting the name and id fields to NULL
        name_var.set(' ')
        id_var.set(' ')
        gender_var.set(' ')

    cv2.imwrite(os.path.join(dir_name, 'photos\{}.jpeg').format(id), feed)
    # Creating encoding for the face registered.
    new_entry(name, id, gender)

    # resetting the name and id fields to NULL
    name_var.set(' ')
    id_var.set(' ')
    gender_var.set(' ')
    # display success window
    success_win = tk.Toplevel(canvas)
    success_win.title('Success')
    success_win.geometry('200x200')
    success_label = tk.Label(success_win,
                            text='Profile created!!!.',
                            font=('Helvetica 18')).pack(side='top')
    
    # Reinitalizing the camera.
    if not vid.isOpened():
        vid.open(0)
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)      
        display_camera_feed()  


def activate_submit():
    stop_camera_feed()
    submit_button['state'] = 'normal'

def retake():
    # Reinitalizing the camera.
    if not vid.isOpened():
        vid.open(0)
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)      
        display_camera_feed()


# Creating the home button.
img_photo = comaptible_image_format(os.path.join(dir_name, 'icons/home_button.jpeg'))
home_button = tk.Button(register_window,
                        text='Home',
                        font=('Times 18 bold'),
                        compound='left',
                        image=img_photo,
                        command=home)
home_button.place(x=0, y=0)

# Displays the live camera feed. 
camera_widget = tk.Label(canvas)
camera_widget.place(x=100, y=50)


# Making a details section for new user.
pallete = canvas.create_rectangle(int((s_width/2))+130, 90,
                                int((s_width/2))+500, 460,
                                fill='white', outline='white')
details_label = tk.Label(canvas,
                        text='Enter details',
                        font=('Helvetica 20 bold'),
                        foreground='blue')
details_label.place(x=int((s_width/2))+240, y=100)
name_field = tk.Label(canvas, text='Name', 
            font=('Helvetica 17'), 
            foreground='black', 
            background='white')
name_field.place(x=int((s_width/2))+150, y=200)
id_field = tk.Label(canvas, text='Id no.', 
            font=('Helvetica 17'), 
            foreground='black', 
            background='white')
id_field.place(x=int((s_width/2))+150, y=250)
gender_field = tk.Label(canvas, text='Gender.', 
            font=('Helvetica 17'), 
            foreground='black', 
            background='white')
gender_field.place(x=int((s_width/2))+150, y=300)
input_name = tk.Entry(canvas, textvariable=name_var, width=20)
input_name.place(x=int((s_width/2))+250, y=205)
input_id = tk.Entry(canvas, textvariable=id_var, width=20)
input_id.place(x=int((s_width/2))+250, y=255)
input_gender = tk.Entry(canvas, textvariable=gender_var, width=20)
input_gender.place(x=int((s_width/2))+250, y=305)

# Creating submit button to enter all details.
submit_button = tk.Button(canvas,
                        text='Submit',
                        font=('Helvetica 18 bold'),
                        state='disabled',
                        command=submit)
submit_button.place(x=int((s_width/2))+260, y=370)


# Creating buttons for taking a picture and retake.
camera_photo = comaptible_image_format(os.path.join(dir_name, 'icons/camera_icon.jpeg'))
take_pic = tk.Button(canvas,
                    text='Take Picture',
                    font=('Helvetica 18'),
                    image=camera_photo,
                    compound='left',
                    command=activate_submit)
take_pic.place(x=500, y=s_height-150)
retake_photo = comaptible_image_format(os.path.join(dir_name, 'icons/retake_icon.jpeg'))
retake_pic = tk.Button(canvas,
                    text='Retake',
                    font=('Helvetica 18'),
                    image=retake_photo,
                    compound='left',
                    command=retake)
retake_pic.place(x=200, y=s_height-150)


display_camera_feed()
register_window.mainloop()