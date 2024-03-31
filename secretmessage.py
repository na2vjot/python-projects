
from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()

screen.geometry('460x400')
screen.title('Encryption and Decryption')
screen.configure(bg='grey')
screen.iconbitmap('Gartoon-Team-Gartoon-Mimetype-App-x-php.ico')


def encrypt():
    password=code.get()
    if password=="12345":
        screen1=Toplevel(screen)
        screen1.title("Encrypted text")
        screen1.geometry("300x300")
        screen1.configure(bg='pink')
        screen1.iconbitmap('Colebemis-Feather-Send.ico')
        
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        b64_bytes=base64.b64encode(encode_message)
        encrypt=b64_bytes.decode("ascii")
        
        Label(screen1,text="Your text is encrypted:",font="impack 13 bold").place(x=5,y=5)  
        text2=Text(screen1,font="20",bd=4,wrap=WORD)
        text2.place(x=5,y=40,width=250,height=200)   
        text2.insert(END,encrypt)         
    
    elif password=="":
        messagebox.showerror("Error","Please enter the secret key :)")    
        
    elif password != "12345":
        messagebox.showerror("Oops!","Inavlid Secret Key")
        
        
def decrypt():
    password=code.get()
    if password=="12345":
        screen2=Toplevel(screen)
        screen2.title("Decrypted text")
        screen2.geometry("300x300")
        screen2.configure(bg='green')
        screen2.iconbitmap('Colebemis-Feather-Send.ico')
        
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        b64_bytes=base64.b64decode(encode_message)
        encrypt=b64_bytes.decode("ascii")
        
        Label(screen2,text="Your text is decrypted:",font="impack 13 bold").place(x=5,y=5)  
        text2=Text(screen2,font="20",bd=4,wrap=WORD)
        text2.place(x=5,y=40,width=250,height=200)   
        text2.insert(END,encrypt)         
    
    elif password=="":
        messagebox.showerror("Error","Please enter the secret key :)")    
        
    elif password != "12345":
        messagebox.showerror("Oops!","Inavlid Secret Key")
        
 
def reset():       
        text1.delete(1.0,END)
        code.set("")

Label1=Label(screen,text="Enter the term for your encryption or decryption",font="Impack 14 bold").place(x=5,y=10)

text1=Text(screen,font="20")
text1.place(x=3,y=50,width=450,height=60)

Label(screen,text="Enter your secret text",font="Impack 13",bg='yellow').place(x=135,y=130)

# storing the secret key variable named code
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=120,y=160)

Button(screen,text="ENCRYPT",font="arial 15 bold",bg='red',fg='white',command=encrypt).place(x=15,y=210,width=200)
Button(screen,text="DECRYPT",font="arial 15 bold",bg='green',fg='white',command=decrypt).place(x=230,y=210,width=200)
Button(screen,text="RESET",font="arial 15 bold",bg='blue',fg='white',command=reset).place(x=120,y=280,width=200)


screen.mainloop()
