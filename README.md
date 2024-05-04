# Image-Histogram-Using-OpenCV-
This code performs image histogram visualization and applies some image processing operations using the OpenCV library and Matplotlib in Python. Here's a breakdown of the code:

- The required libraries are imported: `numpy` for numerical operations, `matplotlib.pyplot` for plotting, `cv2` (OpenCV) for image processing, and `os` for handling file paths.

- The current working directory is obtained using `os.getcwd()` and stored in the `root` variable.

- The image path is created by joining the `root` path with the filename `'cute_dog.jpg'`.

- The `visualize_all()` function is defined, which encapsulates the code for visualizing histograms and performing image processing operations.

- Inside the `visualize_all()` function:
  - The image is read using `cv.imread()` from the specified `img_path`.
  - The image is converted from BGR to RGB color space using `cv.cvtColor()`, and the result is stored in `imgRGB`.
  - A figure with subplots is created using `plt.subplots()`, with a 3x4 grid of subplots and a specified figure size.
  - The title of the figure is set to 'Image Histogram' using `fig.suptitle()`.
  - The color image is displayed in the first subplot using `axes[0, 0].imshow()`, and its title is set to 'Color Image'.
  - For each color channel (red, green, blue):
    - The histogram is calculated using `cv.calcHist()` for the corresponding channel of `imgRGB`.
    - The histogram is plotted in the respective subplot using `axes[0, i+1].plot()`.
    - The x-axis label is set to 'Image Intensity' using `axes[0, i+1].set_xlabel()`.
    - The y-axis label is set to 'No of Pixels' using `axes[0, i+1].set_ylabel()`.
    - The title of the subplot is set to the uppercase channel name followed by 'Channel' using `axes[0, i+1].set_title()`.

  - A contrast image is created by adjusting the image intensity using `cv.addWeighted()`, and the result is stored in `contrast_image`.
  - The contrast image is displayed in the second subplot, and histograms for each color channel are plotted in the subsequent subplots, similar to the previous step.

  - The brightness of the image is reduced by applying a gamma transformation. The value of gamma is set to 2.
  - The image is read again using `cv.imread()` and converted to a float32 data type. Then, it is divided by 256 to normalize the pixel values.
  - The image is converted to RGB color space, and the result is stored in `imgRGB`.
  - The gamma transformation is applied to `imgRGB` using `np.power()`, and the result is stored in `gamma_img`.
  - The gamma-reduced image is displayed in the third subplot, and histograms for each color channel are plotted in the subsequent subplots, similar to the previous steps.

  - Finally, `plt.tight_layout()` is called to improve the spacing between subplots, and `plt.show()` is used to display the figure.

- The block `if __name__ == '__main__':` ensures that the `visualize_all()` function is only executed when the script is run directly, not when it's imported as a module.

> Final Output :
![Screenshot 2024-05-05 004817](https://github.com/Abdalrahmanhassan237/Image-Histogram-Using-OpenCV-/assets/158060043/d04f0d25-61da-4b18-a292-5f9b9485cb3c)


Overall, this code reads an image, visualizes its color histogram, applies contrast adjustment, and reduces brightness using gamma transformation. The resulting images and their histograms are displayed using `matplotlib` 
