from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Mostrar la primera imagen
result_image_path = r"C:\Users\User\Pictures\PREDICCIONES\predict\gato1.jpeg"
result_image = Image.open(result_image_path)

plt.figure(figsize=(6, 6))  # Tamaño de la figura
plt.imshow(result_image)
plt.axis('off')  # Ocultar los ejes
plt.title('Primera imagen - Gato1')
plt.show()

# Mostrar las otras dos imágenes en un solo gráfico con subplots

# Rutas a tus imágenes
ruta1 = r"C:\Users\User\Pictures\PREDICCIONES\predict\gato1.jpeg"
ruta2 = r"C:\Users\User\Pictures\PREDICCIONES\predict\gato12.jpeg"

# Cargar las imágenes
img1 = mpimg.imread(ruta1)
img2 = mpimg.imread(ruta2)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))
plt.subplots_adjust(wspace=0.1)  # Ajusta el espacio horizontal entre subplots

# Mostrar las imágenes en cada subplot
axes[0].imshow(img1)
axes[0].set_title('Pelusa')
axes[0].axis('off')

axes[1].imshow(img2)
axes[1].set_title('Minicky')
axes[1].axis('off')

plt.show()
