import numpy as np 
import matplotlib.pyplot as  plt
import cv2 as cv
import os 

root = os.getcwd()
img_path = os.path.join(root,'cute_dog.jpg')

def visualize_all():
    img = cv.imread(img_path)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Create a single figure with subplots
    fig, axes = plt.subplots(3, 4, figsize=(12, 8))
    fig.suptitle('Image Histogram')

    # Color image histogram
    axes[0, 0].imshow(imgRGB)
    axes[0, 0].set_title('Color Image')
    colors_channel = ['r', 'g', 'b']
    for i in range(len(colors_channel)):
        hist = cv.calcHist([imgRGB], [i], None, [256], [0, 256])
        axes[0, i+1].plot(hist, colors_channel[i])
        axes[0, i+1].set_xlabel('Image Intensity')
        axes[0, i+1].set_ylabel('No of Pixels')
        axes[0, i+1].set_title(colors_channel[i].upper() + ' Channel')

    # Contrast image
    contrast_image = cv.addWeighted(imgRGB, 1.5, np.zeros(imgRGB.shape, imgRGB.dtype), 0, 0)
    axes[1, 0].imshow(contrast_image)
    axes[1, 0].set_title('Contrast Image')
    for i in range(len(colors_channel)):
        hist = cv.calcHist([contrast_image], [i], None, [256], [0, 256])
        axes[1, i+1].plot(hist, colors_channel[i])
        axes[1, i+1].set_xlabel('Image Intensity')
        axes[1, i+1].set_ylabel('No of Pixels')
        axes[1, i+1].set_title(colors_channel[i].upper() + ' Channel')

    # Reduce brightness
    gamma = 2
    img = cv.imread(img_path,).astype(np.float32)/256
    imgRGB= cv.cvtColor(img,cv.COLOR_BGR2RGB)
    gamma_img = np.power(imgRGB, gamma)
    axes[2, 0].imshow(gamma_img)
    axes[2, 0].set_title('Reduced Brightness')
    for i in range(len(colors_channel)):
        hist = cv.calcHist([gamma_img], [i], None, [256], [0, 256])
        axes[2, i+1].plot(hist, colors_channel[i])
        axes[2, i+1].set_xlabel('Image Intensity')
        axes[2, i+1].set_ylabel('No of Pixels')
        axes[2, i+1].set_title(colors_channel[i].upper() + ' Channel')

    plt.tight_layout()
    plt.show()
   
if __name__ == '__main__':
    visualize_all()
