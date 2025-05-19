import cv2
import os
import tkinter as tk

def mostrarImagemOriginal():
    camImaEsc = archiveList.curselection()
    aux = archiveList.get(camImaEsc)
    imagem = cv2.imread(aux)
    return imagem


def mostrarImagemEscolhida():
    imagem = mostrarImagemOriginal()
    cv2.imshow("Imagem Original", imagem)
    cv2.waitKey(0)

    info = imagem.shape
    lbValorCanaisCores.config(text = str(info[2]))
    lbValorDimensaoY.config(text = str(info[1]))
    lbValorDimensaoX.config(text = str(info[0])) 

def redimensionarImagem():
    imagem = mostrarImagemOriginal()
    novaLargura = int(enNovaDimX.get())
    novaAltura = int(enNovaDimY.get())

    alturaOriginal, larguraOriginal = imagem.shape[:2]

    if novaAltura > alturaOriginal or novaLargura > larguraOriginal:
        interpolacao = cv2.INTER_LINEAR
    else:
        interpolacao = cv2.INTER_AREA

    imagem_redimensionada = cv2.resize(imagem, (novaLargura, novaAltura), interpolation=interpolacao)
    cv2.imshow("Imagem Redimensionada", imagem_redimensionada)
    cv2.waitKey(0)


#Criando vetor com as imagens da lista
pathImages = r"C:\Users\Luiz Eduardo\Documents\VSCode\Python\VisaoComputacional\Sistem de Redimensionamento de Imagens\assets\fotos"
dirImages = []
os.chdir(pathImages)
dirImages = os.listdir()
print(f'Lista arquivos de imagens \n{dirImages}')

#Criando interface
screen = tk.Tk()
screen.title('Image Resizing')
screen.geometry('500x500')

#Criando botao 'Abrir'
btAbrir = tk.Button(screen, text = 'Abrir', relief = 'raised', bg = 'light blue', width = 10, command = mostrarImagemEscolhida)
btAbrir.place(x = 10, y = 20)

#Criando botao redimensionar
btRed = tk.Button(screen, text = 'Redimensionar', relief = 'raised', bg = 'light blue', width = 15, command = redimensionarImagem)
btRed.place(x = 10, y = 250)

#Criar labels para dimensao original da imagem
lbDimensaoX = tk.Label(screen, text = "Dimensao X:")
lbDimensaoX.place(x = 160, y = 20)

lbValorDimensaoX = tk.Label(screen, text = "--")
lbValorDimensaoX.place(x = 160, y = 40)

lbDimensaoY = tk.Label(screen, text = "Dimensao Y:")
lbDimensaoY.place(x = 160, y = 60)

lbValorDimensaoY = tk.Label(screen, text = "--")
lbValorDimensaoY.place(x = 160, y = 80)

#labels canais de cores
lbCanaisCores = tk.Label(screen, text = "Canais de cores:")
lbCanaisCores.place(x = 160, y = 100)

lbValorCanaisCores = tk.Label(screen, text = "--")
lbValorCanaisCores.place(x = 160, y = 120) 

#Label e entradas para novas dimensoes
lbNovaDimX = tk.Label(screen, text = "Nova Dimensao de X")
lbNovaDimX.place(x = 270, y = 20)

enNovaDimX = tk.Entry(screen, justify = "center")
enNovaDimX.place(x = 270, y = 40)

lbNovaDimY = tk.Label(screen, text = "Nova Dimensao de Y")
lbNovaDimY.place(x = 270, y = 60)

enNovaDimY = tk.Entry(screen, justify = "center")
enNovaDimY.place(x = 270, y = 80)

#Criando lista de imagens
archiveList = tk.Listbox(screen)
archiveList.place(x = 20, y = 50)

#Preenchendo lista
x = 0
for i in dirImages:
    x += 1
    archiveList.insert(x, i)

tk.mainloop()

'''
#Funcao de redimensionamento
def redimensionar(imagem, nova_largura, nova_altura):
    altura_original, largura_original = imagem.shape[:2]

    if nova_altura > altura_original or nova_largura > largura_original:
        interpolacao = cv2.INTER_LINEAR
    else:
        interpolacao = cv2.INTER_AREA
    
    nova_dimensao = (nova_largura, nova_altura)

    return cv2.resize(imagem, nova_dimensao, interpolation=interpolacao)


imagem = cv2.imread('assets/fotos/cat_large.jpg')

imagem_redimencionada = redimensionar(imagem, 300, 200)

cv2.imshow("Redimensionada", imagem_redimencionada)
cv2.imshow("Normal", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

def redimensionarImagem():
    aux = mostrarImagemOriginal().shape
    auxX = (float(enNovaDimX.get())/aux[0])
    auxY = (float(enNovaDimY.get())/aux[1])
    imRed = cv2.resize(mostrarImagemOriginal(), (0,0), fx = auxX, fy = auxY)
    cv2.imshow("Imagem Redimensionada", imRed)
    cv2.waitKey(0)
'''