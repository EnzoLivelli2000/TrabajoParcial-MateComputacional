from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from sklearn import tree
import pydotplus
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn.preprocessing import LabelEncoder
import graphviz

import pandas as pd

def show_frame(frame):
    frame.tkraise()

window = Tk()
window.iconbitmap("./images/yinicon.ico")
window.geometry("500x500")
window.title("Trabajo Parcial")


window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)


dataUser = StringVar()
dataFinal = []
dataFinalNumbers = []
dataMatriz = []

optionGlobal = []

def setValue(selection):
    optionGlobal.append(selection)
    print(optionGlobal[0])


def getDataUser():
    data = dataUser.get()
    dataFinal = list(data.split(" "))
    dataFinalNumbers = [int(item) for item in dataFinal]
    dataMatriz.append(dataFinalNumbers)
    print(dataMatriz)

frame1 = Frame(window)
frame2 = Frame(window)

for frame in (frame1, frame2):
    frame.grid(row = 0, column = 0, sticky = "nsew")

bgImage = PhotoImage(file ="./images/cerebro_colores.png")
# upcLogo = PhotoImage(file = "./images/upclogo.png")

#Code Frame1
frame1_labeImg = Label(frame1, image = bgImage)
frame1_labeImg.place(x = 0, y = 0, relwidth = 1, relheight = 1)
# frame1_upclogo = Label(frame1, image = upcLogo, bg = "#EAE6E6" )
# frame1_upclogo.place(x = 220, y = 220)
frame1_label =  Label(frame1, text = "Trabajo Parcial", font =(None, 30))
frame1_label.place(x = 110, y = 10)
frame1_label2 =  Label(frame1, text = "Integrantes: ", padx = 10, font =(None, 30))
frame1_label2.place(x = 10, y = 70)
frame1_label3 =  Label(frame1, text = "1) Paolo Cisneros ", padx = 10, font =(None, 20))
frame1_label3.place(x = 10, y = 130)
frame1_label4 =  Label(frame1, text = "2) Enzo Livelli ", padx = 10, font =(None, 20))
frame1_label4.place(x = 10, y = 170)
frame1_label4 =  Label(frame1, text = "3) Marycielo Quispe ", padx = 10, font =(None, 20))
frame1_label4.place(x = 10, y = 210)
frame1_label4 =  Label(frame1, text = "4) Yara Gonzales", padx = 10, font =(None, 20))
frame1_label4.place(x = 10, y = 250)
frame1_label4 =  Label(frame1, text = "5) Felix Silva", padx = 10, font =(None, 20))
frame1_label4.place(x = 10, y = 290)
frame1_label4 =  Label(frame1, text = "2021-1", padx = 10, font =(None, 50))
frame1_label4.place(x = 260, y = 360)

frame1_buttonBack = Button(frame1, text = "Probar", bg = "#00B74A", cursor = "center_ptr", font = "bold", fg = "white", padx=6, pady=4, command = lambda:show_frame(frame2))
frame1_buttonBack.place(x = 20, y = 390)
# print(type(frame1_buttonBack))

# Code Frame2
def trainAlgorithm(listGeneral, listResults):
    length = len(listGeneral)
    for i in range(length):
        for j in range(4):
            if listGeneral[i][j] == "lluvioso":
                listGeneral[i][j] = 0

            elif listGeneral[i][j] == "nublado":
                listGeneral[i][j] = 1

            elif listGeneral[i][j] == "soleado":
                listGeneral[i][j] = 2

            elif listGeneral[i][j] == "calido":
                listGeneral[i][j] = 0

            elif listGeneral[i][j] == "tempmedia":
                listGeneral[i][j] = 1

            elif listGeneral[i][j] == "frio":
                listGeneral[i][j] = 2

            elif listGeneral[i][j] == "normal":
                listGeneral[i][j] = 0

            elif listGeneral[i][j] == "alto":
                listGeneral[i][j] = 1

            elif listGeneral[i][j] == "bajo":
                listGeneral[i][j] = 0

            elif listGeneral[i][j] == "alto":
                listGeneral[i][j] = 1


    clf = tree.DecisionTreeClassifier()

    clf = clf.fit(listGeneral, listResults)

    decisionTree = clf

    # data1 = [[1, 0, 0, 0]]

    prediction = clf.predict(dataMatriz)

    response = str(prediction)

    # PDF
    # dot_data = tree.export_graphviz(decisionTree, out_file='juego.dot',feature_names=list(inputs_n), class_names=['No', 'Si'], rounded=True, filled=True)
    # with open('juego.dot') as f:
    #     dot_graph=f.read()
    # graphviz.Source(dot_graph).view()
    
    # Form
    var = StringVar()

    l2 = Label(frame2, text = "La respuesta sería:  ", font =(None, 20))
    l2.place(x = 100, y = 270)
    l3 = Label(frame2, textvariable = var, font =(None, 20))
    l3.place(x = 350, y = 270)
    var.set(prediction)
    
      
    dataMatriz.clear()

def trainAlgorithmNotas():
    #Se crea la instancia del árbol de decisión.
    clf = tree.DecisionTreeClassifier()

    #instanciamos calf como dataframe, con el propósito de poder acceder a sus datos por medio de una matriz
    calf = pd.DataFrame()

    #nuestro data set
    calf['tiempo'] = [10,20,10,30,10,20,40,30,10,30,20,40,10,30,10,20]
    calf['materia'] = ['matematica', 'historia', 'ciencia', 'historia', 
    'matematica', 'matematica', 'matematica', 'ciencia',
    'historia', 'ciencia', 'ciencia', 'historia',
    'ciencia', 'matematica', 'matematica', 'ciencia']
    calf['nota'] = [11,16,11,18,11,15,20,17,10,17,15,20,11,18,11,15]

    #convertimos las variables a dummies para poder accder a sus posiciones con mayor facilidad
    one_hot_data = pd.get_dummies(calf[ ['tiempo', 'materia'] ])

    print(one_hot_data)

    # instanciamos el arbol de desiciones y lo asignamos a la variable clf
    clf = tree.DecisionTreeClassifier()

    # entrenamos nuestro arbol con los data ses creados
    clf_train = clf.fit(one_hot_data, calf['nota'])

    # realizamos una predicción en funcion de los siguientes datos
    prediction = clf_train.predict(dataMatriz)

    print(prediction)

    #realizamos una simple condicional para poder mostrar un mensaje en la pantalla
    if prediction >= 13:
        print("Estas aprobado")
    else:
        print("Estas reprobado")

     # Form
    var = StringVar()

    l2 = Label(frame2, text = "La respuesta sería:  ", font =(None, 20))
    l2.place(x = 100, y = 270)
    l3 = Label(frame2, textvariable = var, font =(None, 20))
    l3.place(x = 350, y = 270)
    var.set(prediction)
    
      
    dataMatriz.clear()


def trainAlgorithmPetalos():
    iris = load_iris()
    AEntrena,APruebas,BEntrena,BPruebas=train_test_split(iris['data'],iris['target'])

    clasficadorArbol=DecisionTreeClassifier()
    clasficadorArbol.fit(AEntrena,BEntrena)

    DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, 
    min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None,
    random_state=None, max_leaf_nodes=None, 
    min_impurity_split=None, class_weight=None, ccp_alpha=0.0)

    print("Aprendió en un: ")
    print(clasficadorArbol.score(APruebas,BPruebas))
    print(clasficadorArbol.score(AEntrena,BEntrena))

    export_graphviz(clasficadorArbol,out_file='arbol.dot', class_names=iris['target_names'],feature_names=iris['feature_names'],impurity=False,filled=True)

    with open('arbol.dot') as f:
        dot_graph=f.read()
    graphviz.Source(dot_graph).view()
    

    dataMatriz.clear()

def trainAlgorithmHyM():
    clf = tree.DecisionTreeClassifier()

    #[altura, peso, talla de zapato]
    X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
        [190, 90, 47], [175, 64, 39],
        [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
    #La salida donde se dice si es hombre o mujer
    Y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer',
        'mujer', 'hombre', 'hombre']
    #Se le pasa los datos  X y Y

    clf = clf.fit(X, Y)
    print(clf)

    #Se definen los datos 1 y 2, estos datos corresponde a un hombre

    prediction = clf.predict(dataMatriz)


    print(prediction)
    if prediction == 'hombre':
        print("Estas caraterísticas corresponden a un hombre")
    else:
        print("Estas caraterísticas corresponden a un mujer")

    var = StringVar()

    l2 = Label(frame2, text = "La respuesta sería:  ", font =(None, 20))
    l2.place(x = 100, y = 270)
    l3 = Label(frame2, textvariable = var, font =(None, 20))
    l3.place(x = 350, y = 260)
    var.set(prediction)
    
      

    dataMatriz.clear()


def openFile():
    print("Value: " + optionGlobal[0])
    if optionGlobal[0] == "Clima":
        # Read file
        file = filedialog.askopenfilename(title = "Abrir")
        data = pd.read_csv(file, header = None)

        # Get number rows
        numbersRows = data.shape[0]
        listFirst = []

        # Guardamos las filas en la lista
        for i in range(numbersRows):
            listFirst.append(data.iloc[i])

        listGeneral = []

        # Delete headers
        del listFirst[0]
        # Eliminamos una fila, porque se eliminaron los headers
        numbersRows -= 1
    
        for i in range(numbersRows):
            listData = listFirst[i].tolist()
            listGeneral.append(listData[0].split(";"))

        listResults = []

        # Get last column
        for i in range(numbersRows):
            listResults.append(listGeneral[i][-1])

        # Delete last column
        for i in range(numbersRows):
            listGeneral[i].pop()

        trainAlgorithm(listGeneral, listResults)

    elif optionGlobal[0] == "HyM":
        trainAlgorithmHyM()
    elif optionGlobal[0] == "Notas":
        trainAlgorithmNotas()
    elif optionGlobal[0] == "Petalos":
        trainAlgorithmPetalos()

    optionGlobal.pop(0)





# style = ttk.Style()
frame2_l1 = Label(frame2, text = "Arbol de decisión", font =(None, 30)).pack()
# l2 = Label(window, text = "Ingrese el archivo: ").pack()
frame2_buttonExe = Button(frame2, text = "Cargar Archivo", bg = "#1266F1", cursor = "center_ptr", font = "bold", fg = "white", padx=6, pady=4, command = openFile )
frame2_buttonExe.place(x = 250, y = 110)
frame2_label = Label(frame2, text = "Ingrese dato de prueba: ", font=(None, 20))
frame2_label.place(x = 20, y = 60)
name = StringVar()
value = Entry(frame2, width = 15, textvariable = dataUser)
value.place(x = 320, y =70)
frame2_buttonExe = Button(frame2, text = "Guardar dato", bg = "#1266F1", cursor = "center_ptr", font = "bold", fg = "white", padx=6, pady=4, command = getDataUser )
frame2_buttonExe.place(x = 100, y = 110)

options = StringVar()
frame2_inputSelect = OptionMenu(frame2, options, "Clima", "HyM", "Notas", "Petalos", command= setValue)
frame2_inputSelect.place(x = 100, y = 200)


frame2_buttonBack = Button(frame2, text = "Regresar", bg = "#00B74A", cursor = "center_ptr", font = "bold", fg = "white", padx=6, pady=4, command = lambda:show_frame(frame1))
frame2_buttonBack.place(x=30, y= 390)


def run():
    show_frame(frame17)
    window.mainloop()


if __name__ == "__main__":
    run()