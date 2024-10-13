import glob
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import face_recognition
import mysql.connector
import numpy as np
from mysql_database import connections
import cv2
import imutils
import datetime
import matplotlib.pyplot as plt
from twilio.rest import Client


def delete2():
    screen3.destroy()
    screen2.destroy()
    screen.destroy()


def delete3():
    screen4.destroy()


def delete4():

    screen5.destroy()


def login_sucess():
    def after_callback():
        screen3.destroy()
        screen2.destroy()
        screen.destroy()
        system()

    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("400x250")
    Label(screen3, text="Login Success").pack()
    Button(screen3, text="OK", height='2', width="15").pack()
    screen3.after(2000, after_callback)

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("500x350")
    Label(screen4, text="Password or Email Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("500x350")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def des2():
    screen2.destroy()
    screen1.destroy()


def success():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Successfully Register")
    screen2.geometry("500x350")
    Label(screen2, text="Registration Successful", fg="green", font=("calibri", 11)).pack()
    Label(screen1, text="").pack()
    Button(screen2, text="ok", bg="lightgreen", height="2", width="20", command=des2).pack()


def register_user():
    print("working")

    email_info = email.get()
    password_info = password.get()
    contact_info = contact.get()
    address_info = address.get()
    connection1 = connections()
    res = connection1.database_insert(email_info, password_info, contact_info, address_info)
    print(res)

    file = open("Details.txt", "a")
    file.write("\n" + email_info + "\n")
    file.write(password_info)
    file.close()

    email_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
    success()


def verify_user():
    email1 = email_verify.get()
    password1 = password_verify.get()

    connection = connections()

    ans = connection.my_verify_user(email1, password1)
    print(ans)

    if ans is True:
        login_sucess()
    else:
        user_not_found()


def login_verify():
    email1 = email_verify.get()
    password1 = password_verify.get()
    email_entry1.delete(0, END)
    password_entry1.delete(0, END)

    f = open("Details.txt", "r")
    verify = (f.readlines())
    if (verify != ""):
        if email1 and password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    global email
    global password
    global contact
    global address
    global email_entry
    global password_entry
    global contact_entry
    global address_entry

    screen1 = Toplevel(screen)
    screen1.title("Register Here")
    screen1.geometry("1600x900")


    register_frame = Frame(screen1, bg="#f0f0f0")
    register_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(register_frame, text="Please enter your details", font=("Arial", 20,"bold"), bg="#f0f0f0").pack()
    Label(register_frame, text="", bg="#f0f0f0").pack()

    email = StringVar()
    password = StringVar()
    contact = StringVar()
    address = StringVar()

    Label(register_frame, text="Email or Username*", bg="#f0f0f0", font=("Arial", 14)).pack()
    email_entry = Entry(register_frame, textvariable=email, font=("Arial", 14))
    email_entry.pack()
    Label(register_frame, text="", bg="#f0f0f0").pack()

    Label(register_frame, text="Password*", bg="#f0f0f0", font=("Arial", 14)).pack()
    password_entry = Entry(register_frame, textvariable=password, show="*", font=("Arial", 14))
    password_entry.pack()
    Label(register_frame, text="", bg="#f0f0f0").pack()

    Label(register_frame, text="Contact No*", bg="#f0f0f0", font=("Arial", 14)).pack()
    contact_entry = Entry(register_frame, textvariable=contact, font=("Arial", 14))
    contact_entry.pack()
    Label(register_frame, text="", bg="#f0f0f0").pack()

    Label(register_frame, text="Address*", bg="#f0f0f0", font=("Arial", 14)).pack()
    address_entry = Entry(register_frame, textvariable=address, font=("Arial", 14))
    address_entry.pack()
    Label(register_frame, text="", bg="#f0f0f0").pack()

    Button(register_frame, text="Register", bg="#2196F3", fg="white", font=("Arial", 14), height="2", width="20",
           command=register_user).pack()


def login():
    global screen2
    global email_verify
    global password_verify
    global email_entry1
    global password_entry1
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("1600x900")

    # Create a frame for the login form
    login_frame = Frame(screen2, bg="#f0f0f0")
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(login_frame, text="Please enter your details", font=("Arial", 20,"bold"), bg="#f0f0f0").pack()
    Label(login_frame, text="", bg="#f0f0f0").pack()

    email_verify = StringVar()
    password_verify = StringVar()

    Label(login_frame, text="Email or Username*", bg="#f0f0f0", font=("Arial", 14)).pack()
    email_entry1 = Entry(login_frame, textvariable=email_verify, font=("Arial", 14))
    email_entry1.pack()
    Label(login_frame, text="", bg="#f0f0f0").pack()

    Label(login_frame, text="Password*", bg="#f0f0f0", font=("Arial", 14)).pack()
    password_entry1 = Entry(login_frame, textvariable=password_verify, show="*", font=("Arial", 14))
    password_entry1.pack()
    Label(login_frame, text="", bg="#f0f0f0").pack()

    Button(login_frame, text="Login", bg="#4CAF50", fg="white", font=("Arial", 14), height="2", width="20",
           command=verify_user).pack()


def main_screen():
    global screen

    screen = Tk()
    screen.geometry("1600x900")
    screen.configure(bg="#f0f0f0")
    screen.title("Intruder Detection and Automatic Email Alerting System")

    title_label = Label(text="Welcome to Intruder Detection System", bg="#f0f0f0", font=("Roboto", 32, "bold"))
    title_label.pack(pady=20)

    image_path = "C:/Users/Kenjales/Downloads/thumb.png"
    img = PhotoImage(file=image_path)
    img = img.subsample(3)
    image_label = Label(image=img, bg="#f0f0f0")
    image_label.pack(pady=10)

    login_button = Button(text="Login", bg="#4CAF50", fg="white", font=("Arial", 14), height=2, width=30, command=login)
    login_button.pack(pady=10)

    register_button = Button(text="Register", bg="#2196F3", fg="white", font=("Arial", 14), height=2, width=30,
                             command=register)
    register_button.pack(pady=10)

    login_signup_label = Label(text="Already have an account? Login", bg="#f0f0f0", fg="#333333",
                               font=("Arial", 12, "italic", "underline"))
    login_signup_label.pack(pady=10)

    screen.mainloop()


def system():

    paths = glob.glob('C:/Users/Kenjales/PycharmProjects/pythonProject2/Images_Data_understanding/*')
    images = []
    image_encodings = []
    image_names = []
    count_img = 0
    flag = 0

    for i in paths:
        images.append(face_recognition.load_image_file(i))
        image_encodings.append(face_recognition.face_encodings(images[count_img])[0])
        image_names.append(i.split('\\')[-1].split('.')[0])
        count_img += 1
        print(image_names)

    count = 0
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # gray = frame[:, :, ::-1]
        gray = np.ascontiguousarray(frame[:, :, ::-1])
        face_locations = face_recognition.face_locations(gray)
        face_encodings = face_recognition.face_encodings(gray, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(image_encodings, face_encoding)
            name = 'Unknown'
            face_distances = face_recognition.face_distance(image_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = image_names[best_match_index]
            if (name == 'Unknown'):
                cv2.imwrite('C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images/intru-{}.jpg'.format(count), frame)
                flag = 1
                count += 1
                # print("df")
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow("output", frame)
        print("df0")
        if (cv2.waitKey(1) == ord('q')):
            print("j")
            break
    print("df1")
    cap.release()
    print("df2")
    cv2.destroyAllWindows()
    myPath = glob.glob('C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images/*')
    global countFolder
    count = 0
    print("uuiy")
    for i in myPath:
        img = cv2.imread(i)
        # print(blur)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.Laplacian(gray_img, cv2.CV_64F).var()

        if (count % 1 == 0 and blur > 320):
            cv2.imwrite(
                'C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images/intru-{}.jpg'.format(count),
                img)
            count += 1
    Weapon(flag)
    print("SMTP")

def Weapon(flag):
 if (flag == 1):
     net = cv2.dnn.readNet("yolov3_training_2000.weights", "yolov3_testing.cfg")
     net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
     net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
     classes = ["Weapon"]

     cap = cv2.VideoCapture(0)

     while True:
         _, img = cap.read()
         height, width, channels = img.shape

         blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
         net.setInput(blob)

         layer_names = net.getLayerNames()

         output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
         colors = np.random.uniform(0, 255, size=(len(classes), 3))
         outs = net.forward(output_layers)


         class_ids = []
         confidences = []
         boxes = []
         for out in outs:
             for detection in out:
                 scores = detection[5:]
                 class_id = np.argmax(scores)
                 confidence = scores[class_id]
                 if confidence > 0.5:

                     center_x = int(detection[0] * width)
                     center_y = int(detection[1] * height)
                     w = int(detection[2] * width)
                     h = int(detection[3] * height)


                     x = int(center_x - w / 2)
                     y = int(center_y - h / 2)

                     boxes.append([x, y, w, h])
                     confidences.append(float(confidence))
                     class_ids.append(class_id)

         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
         print(indexes)
         if indexes == 0:   flag = 2
         font = cv2.FONT_HERSHEY_PLAIN
         for i in range(len(boxes)):
             if i in indexes:
                 x, y, w, h = boxes[i]
                 label = str(classes[class_ids[i]])
                 color = colors[class_ids[i]]
                 cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                 cv2.putText(img, label, (x, y + 30), font, 3, color, 3)


         cv2.imshow("Image", img)
         key = cv2.waitKey(1)
         if key == 27:
             break
     cap.release()
     cv2.destroyAllWindows()
     if flag==1:
         SMTP1()
     if flag==2:
         SMTP2()

def SMTP1():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PotterHead2106",
        database="edi_project"
    )
    cap = cv2.VideoCapture(0)


    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images/intru.avi', fourcc, 20.0,
                          (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:

            out.write(frame)


            cv2.imshow('frame', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


    cap.release()
    out.release()
    cv2.destroyAllWindows()

    cursor = connection.cursor()
    cursor.execute("SELECT username FROM login")  # Assuming 'login' is your table name
    email_records = cursor.fetchall()
    print(email_records)


    sender_email = "klo73268@gmail.com"
    subject = "Alert!!! Intruder Images"
    body = "Check these sample unknown person images, if something *fishy!!* check the intruder folder immediately"


    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))


    directory = "C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images"
    file_names = os.listdir(directory)


    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        with open(file_path, "rb") as attachment:
            part = MIMEApplication(attachment.read())
            part.add_header("Content-Disposition", "attachment", filename=file_name)
            message.attach(part)

    to_emails = ", ".join([record[0] for record in email_records])


    message["To"] = to_emails


    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "klo73268@gmail.com"
    smtp_password = "gzyr kzbp witq zhae"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)


    server.sendmail(sender_email, to_emails.split(", "), message.as_string())


    server.quit()


    cursor.close()
    connection.close()

    print("Emails sent successfully!")


def SMTP2():

    account_sid = 'AC5a99ca7bee197593fb43a67f0e541af8'
    auth_token = 'fb495539828707c67eeb125d37d743b4'
    client = Client(account_sid, auth_token)


    call = client.calls.create(
        twiml='<Response><Say>+919890107615</Say></Response>',
        to='+919890107615',
        from_='+12254604195'
    )

    print(f"Call SID: {call.sid}")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PotterHead2106",
        database="edi_project"
    )
    cap = cv2.VideoCapture(0)


    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images/intru.avi', fourcc, 20.0,
                          (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:

            out.write(frame)


            cv2.imshow('frame', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


    cap.release()
    out.release()
    cv2.destroyAllWindows()

    cursor = connection.cursor()
    cursor.execute("SELECT username FROM login")  # Assuming 'login' is your table name
    email_records = cursor.fetchall()
    print(email_records)


    sender_email = "klo73268@gmail.com"
    subject = "Alert!!! Intruder Images"
    body = "Check these sample unknown person images, Intruder has some suspisious object/weapon plz take action as soon as possible"


    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))


    directory = "C:/Users/Kenjales/PycharmProjects/pythonProject2/Intruder_Images"
    file_names = os.listdir(directory)


    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        with open(file_path, "rb") as attachment:
            part = MIMEApplication(attachment.read())
            part.add_header("Content-Disposition", "attachment", filename=file_name)
            message.attach(part)

    to_emails = ", ".join([record[0] for record in email_records])


    message["To"] = to_emails


    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "klo73268@gmail.com"
    smtp_password = "gzyr kzbp witq zhae"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)


    server.sendmail(sender_email, to_emails.split(", "), message.as_string())


    server.quit()


    cursor.close()
    connection.close()

    print("Emails sent weapon successfully!")


main_screen()

