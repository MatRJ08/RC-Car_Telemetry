from tkinter import *       
from PIL import ImageTk, Image
from WiFiClient import NodeMCU

import time

def write_data():
    doc = open("pilotos.txt","w")
    for i in array_pilotos:
        linea = ''
        for j in i:

            if(isinstance(j,str) == False):
                j =j.get()
            linea = linea + j + ','
               
        linea = linea[:-1]
        if(i != array_pilotos[len(array_pilotos)-1]):
            linea+="\n"
        doc.write(linea)


def fun_RGP_pilotos():
    sort_pilotos(10)


def fun_REP_pilotos():
    sort_pilotos(11)


def sort_pilotos(n):
    bandera = True
    while(bandera):
        i=0
        bandera = False
        while(i != len(array_pilotos)-1):
            if int(array_pilotos[i][n].get()) < int(array_pilotos[i+1][n].get()):
                aux = array_pilotos[i+1]
                array_pilotos[i+1] = array_pilotos[i]
                array_pilotos[i] = aux
                bandera = True
            i += 1
    write_data()
    update_data_pilotos()


def add_headers_pilotos(tipo):    
    global headers
    for widget in headers.winfo_children():
        widget.destroy()

    if(tipo == 'Normal'):
        headers_names =['Posicion','Nombre','Edad','Nacionalidad',
        'Temporada','Cant Competencias']

    elif(tipo == 'Todo'):
        headers_names =['Posicion','Nombre','Edad','Nacionalidad',
        'Temporada','Cant Competencias','Victorias','Segundo/Tercer','Podios','Fallos']    

    for headerTxt in headers_names:
        L1 = Label(headers, text = headerTxt, width = 16, justify = CENTER, relief= FLAT)
        L1.pack( side = LEFT)

    btnOrdenRGP = Button(headers, text = 'RGP',activeforeground = '#309ff4', activebackground = '#131313' ,command = fun_RGP_pilotos, width = 16, relief=FLAT)
    btnOrdenREP = Button(headers, text = 'REP',activeforeground = '#309ff4', activebackground = '#131313' ,command = fun_REP_pilotos, width = 16, relief=FLAT)
    btnOrdenRGP.pack( side = LEFT)
    btnOrdenREP.pack( side = LEFT)


def update_data_pilotos():
    botones.pack_forget()
    global Fprincipal
    for widget in Fprincipal.winfo_children():
        widget.destroy()
    doc = open("pilotos.txt","r")
    lista_pilotos = doc.readlines()
    global array_pilotos
    array_pilotos =[]
    i = 0
    for piloto in lista_pilotos:
        info_piloto= piloto.split(",")
        if(Todo):
            array_piloto = imprimir_All_tabla_pilotos(info_piloto)
        else:
            array_piloto = imprimir_tabla_pilotos(info_piloto)
        array_pilotos.append(array_piloto)
        i+=1

    botones.pack(pady=(50,0))


def imprimir_tabla_pilotos(info_piloto):    
    Fdatos = Frame(Fprincipal)
    Fdatos.pack()
    j=0
    array_piloto = []
    for dato in info_piloto:
        print(info_piloto)
        dato = dato.replace('\n','')
        if(j == 6 or j == 7 or j == 8 or j == 9 or j == 12):
            E1 = Entry(Fdatos, bd =5, width = 18, relief=FLAT, justify =CENTER)
            E1.insert(0,dato)
            array_piloto.append(E1)

        else:
            E1 = Entry(Fdatos, bd =5, width = 18, relief=FLAT, justify =CENTER)
            E1.insert(0,dato)
            E1.pack(side = LEFT)
            array_piloto.append(E1)

        j+=1
    return array_piloto


def modificar_pilotos():
    botones.pack_forget()
    global Fprincipal
    for widget in Fprincipal.winfo_children():
        widget.destroy()

    for widget in headers.winfo_children():
        widget.destroy()

    add_headers_pilotos('Todo')
    doc = open("pilotos.txt","r")
    lista_pilotos = doc.readlines()
    global array_pilotos
    array_pilotos =[]
    i = 0
    for piloto in lista_pilotos:
        info_piloto= piloto.split(",")
        array_piloto = imprimir_All_tabla_pilotos(info_piloto)
        array_pilotos.append(array_piloto)
        i+=1

    botones.pack(pady=(50,0))


def imprimir_All_tabla_pilotos(info_piloto): 
    global Todo
    Todo = True   
    Fdatos = Frame(Fprincipal)
    Fdatos.pack()
    j=0
    array_piloto = []
    for dato in info_piloto:
        print(info_piloto)
        dato = dato.replace('\n','')
        E1 = Entry(Fdatos, bd =5, width = 18, relief=FLAT, justify =CENTER)
        E1.insert(0,dato)
        E1.pack(side = LEFT)
        array_piloto.append(E1)

        j+=1
    return array_piloto


def principal_pilotos():    
    add_headers_pilotos('Normal')
    global Fprincipal
    for widget in Fprincipal.winfo_children():
        widget.destroy()
    i = 0
    global lista_pilotos
    for piloto in lista_pilotos:
        info_piloto= piloto.split(",")
        array_piloto = imprimir_tabla_pilotos(info_piloto)
        array_pilotos.append(array_piloto)
        i+=1
    botones_pilotos()


def botones_pilotos():
    global botones
    for widget in botones.winfo_children():
        widget.destroy()
    botones.pack_forget()
    botones.pack(pady=(50,0))
    Btnguardar = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'Guardar Datos', command = write_data)
    Btnmodificar_pilotos = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'Modificar Datos', command = modificar_pilotos)
    Btnvolver = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'Volver', command = principal_menu)
    Btnguardar.pack(side = LEFT)
    Btnmodificar_pilotos.pack(side = LEFT)
    Btnvolver.pack(side = LEFT)


def principal_about():
    global ventana
    ventana.title("About")
    add_headers_about()
    global Fprincipal
    for widget in Fprincipal.winfo_children():
        widget.destroy() 

    FTEC = Frame(Fprincipal)
    FTEC.pack(side = "top")

    imgTEC_Logo = ImageTk.PhotoImage(Image.open('TEC_Logo.png '))
    TEC_LogoLabel = Label(FTEC)
    TEC_LogoLabel.image = imgTEC_Logo
    TEC_LogoLabel.configure(image=imgTEC_Logo)
    TEC_LogoLabel.pack(side = "left", fill = "both", expand = "yes")
    
    FNombres = Frame(Fprincipal)
    FCurso = Frame(Fprincipal)
    FExtra = Frame(Fprincipal)
    FNombres.pack(side = "top")
    FCurso.pack(side = "top")
    FExtra.pack(side = "top")

    Nombre1 = Label(FNombres, text= 'Mathiw Rojas Jimenez:\t2019176634',fg='#1d2023')
    Nombre1.config(font =('Courier New Baltic',18)) 
    Nombre2 = Label(FNombres, text= 'Felipe Quesada Sanches:\t2019039685',fg='#1d2023')
    Nombre2.config(font =('Courier New Baltic',18)) 
    Nombre1.pack(side = "top")
    Nombre2.pack(side = "bottom")

    Carrera = Label(FCurso, text= 'Ingenieria en computadores | Taller de Programacion GR 3',fg='#1d2023')
    Carrera.config(font =('Courier New Baltic',18)) 
    Profesor = Label(FCurso, text= 'Profesor | Pedro Gutierres',fg='#1d2023')
    Profesor.config(font =('Courier New Baltic',18)) 
    Carrera.pack(side = "top")
    Profesor.pack(side = "top")

    Pais = Label(FExtra, text= 'Costa Rica',fg='#1d2023')
    Pais.config(font =('Courier New Baltic',18))  
    Ver = Label(FExtra, text= 'Version = 1.0',fg='#1d2023')
    Ver.config(font =('Courier New Baltic',18))
    Pais.pack(side = "top")
    Ver.pack(side = "top") 


    botones_about()


def add_headers_about():
    global headers
    for widget in headers.winfo_children():
        widget.destroy()


def botones_about():
    global botones
    for widget in botones.winfo_children():
        widget.destroy()
    Btnvolver = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'Volver', command = principal_menu)
    Btnvolver.pack(side = LEFT)


def principal_menu():
    global ventana
    ventana.title("Menu")
    add_headers_menu()    
    global Fprincipal
    for widget in Fprincipal.winfo_children():
        widget.destroy() 

    FEscuderia = Frame(Fprincipal)
    FEscuderia.pack(side = 'top')
    Nombre = Label(FEscuderia, text= 'Escuderia',fg='#1d2023')
    Nombre.config(font =('Courier New Baltic',44)) 
    imgEscuderia = ImageTk.PhotoImage(Image.open('f1-helmet.png '))
    EscuderiaLabel = Label(FEscuderia)
    EscuderiaLabel.image = imgEscuderia
    EscuderiaLabel.configure(image=imgEscuderia)
    Nombre.pack(side = "left")
    EscuderiaLabel.pack(side = "left", fill = "both", expand = "yes")
    
    FCarro = Frame(Fprincipal)
    FCarro.pack(side = "bottom")
    state = "Disponible"
    imgCarro = ImageTk.PhotoImage(Image.open('formulaE_car2.jpg '))
    CarroLabel = Label(FCarro, width="200")
    CarroLabel.image = imgCarro
    CarroLabel.configure(image=imgCarro)
    CarroLabel.pack(side = "left", fill = "both", expand = "yes")
    Disponible = Label(FCarro, text= 'Estado: ' + state ,fg='#1d2023')
    Disponible.config(font =('Courier New Baltic',20)) 
    Disponible.pack(side = 'right',anchor='s')
    botones_menu()


def botones_menu():
    global botones
    for widget in botones.winfo_children():
        widget.destroy()      
    BtnPilotos = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'Mostrar Tabla', command = principal_pilotos)
    BtnPilotos.config(font =('Courier New Baltic',11) )

    BtnTestD = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'Test Drive', command = principal_test)
    BtnTestD.config(font =('Courier New Baltic',11) )

    BtnAbout = Button(botones,bg= "#131313",fg="#D9E01C",relief=FLAT, text = 'About', command = principal_about)
    BtnAbout.config(font =('Courier New Baltic',11) )

    BtnPilotos.pack(side = LEFT,padx="5")
    BtnTestD.pack(side = LEFT,padx="5")
    BtnAbout.pack(side = LEFT,padx="5")


def add_headers_menu():
    global headers
    for widget in headers.winfo_children():
        widget.destroy()


def principal_test():    
    global Fprincipal
    for widget in Fprincipal.winfo_children():
        widget.destroy() 
    dibuja_test("yo")
    botones_test()


def dibuja_test(name):
    ancho=ventana.winfo_screenwidth()
    ventana.geometry("%dx500"%(ancho))
    dibujo=Canvas(ventana,width=ancho,height=500)
    ventana.title("Test Drive")
    ventana.resizable(0,1)
    dibujo.create_rectangle(0,0,ancho,250,fill="#0099FF")
    dibujo.create_rectangle(0,250,ancho,500,fill="green")
    dibujo.create_rectangle(330,325,(ancho/4)+100,500,fill="#464849")
    dibujo.create_rectangle((ancho/2)+(ancho/4)-100,325,(ancho/2)+(ancho/4),500,fill="#464849")
    nombre = Label(ventana,text='''"Nombre"''')
    nombre_produ = Label(ventana,text='''"Nombre del producto"''')
    dibujo.create_text(40,100,text="Escuderia")
    dibujo.create_rectangle(675,65,790,100,fill="white")
    dibujo.create_text(720,82,text='''"Nacionalidad"''')
    dibujo.create_polygon(ancho/4,500,ancho/2,200,(ancho/2)+(ancho/4),500,fill="#A3B23C")
    nombre_produ.place(x = 0, y = 10)
    nombre.place(x = ancho-150, y = 40)
    dibujo.place(x=0,y=0)


def direccionalD():
    global onDer
    if(onDer == 1):
        onDer = 0
        direccional("der",onDer)
    else:
        onDer = 1
        direccional("der",onDer)


def direccionalI():
    global onIzq
    if(onIzq == 1):
        onIzq = 0
        luces("izq",onIzq)
    else:
        onIzq = 1
        luces("izq",onIzq)


def luzF():
    global onFront
    if(onFront == 1):
        onFront = 0
        luces("front",onFront)
    else:
        onFront = 1
        luces("front",onFront)


def luzB():
    global onBack
    if(onBack == 1):
        onBack = 0
        luces("back",onBack)
    else:
        onBack = 1
        luces("back",onBack)


def luces(luz,on):
    led = "l"
    if(luz == der):
        led+="r:"+on+";"
    elif(luz == izq):
        led+="l:"+on+";"
    elif(luz == back):
        led+="b:"+on+";"
    elif(luz == front):
        led+="f:"+on+";"
    myCar.send(led)


def botones_test():    
    imgCelebracion=ImageTk.PhotoImage(Image.open("celebration.png"))
    Btncelebracion=Button(ventana,command=None,bg="#087604")
    Btncelebracion.image= imgCelebracion
    Btncelebracion.configure(image= imgCelebracion)

    imgSpecial=ImageTk.PhotoImage(Image.open("special-move.png"))
    BtnSpecial=Button(ventana,text="Especial",command=None,bg="#087604")
    BtnSpecial.image= imgSpecial
    BtnSpecial.configure(image= imgSpecial)

    def Acelerar():
        p=""
        p+="pwm:"+poder.get()+";"
        myCar.send(p) 
    
    Btnacelerar=Button(ventana,text="Acelerar",command=Acelerar)
    poder=Entry(ventana) 

    BtnDird= Button(ventana,text="Derecha", command=direccionalD )
    BtnDiri= Button(ventana,text="izuiera", command=direccionalI )
    BtnFront= Button(ventana,text="Luz Frontal", command=luzF )
    BtnBack= Button(ventana,text="Luza Trasera", command=luzB )

    Btnacelerar.place(x=525,y=420) 
    poder.place(x=490,y=450)

    Btncelebracion.place(x=ancho-250,y=260)
    BtnSpecial.place(x=ancho-250,y=340)
    
    BtnDird.place(x=ancho-150,y=400)
    BtnDiri.place(x=ancho-150,y=430)
    BtnFront.place(x=ancho-150,y=370)
    BtnBack.place(x=ancho-150,y=460)





ventana = Tk()
ancho=ventana.winfo_screenwidth()
ventana.geometry("%dx500"%(ancho)) #You want the size of the app to be 500x500
ventana.resizable(0, 1)
top= Frame(ventana)
top.pack()
headers = Frame(top)
headers.pack(pady=(50,0))
Todo=False
doc = open("pilotos.txt","r")
lista_pilotos = doc.readlines()
array_pilotos = []
Fprincipal = Frame(top)
Fprincipal.pack()
botones = Frame(top,bg="#101010")
botones.pack(side='bottom', pady=(100,0))

onDer = 1
onIzq = 1
onFront = 1
onBack = 1
myCar= NodeMCU()

principal_menu()





top.mainloop()