import cv2

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