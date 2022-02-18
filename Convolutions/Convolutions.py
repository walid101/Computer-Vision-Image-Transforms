import sys
import cv2
import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, misc
from IPython.display import display, Image
from matplotlib import cm

Laplacian_kernel = np.asarray([[0,1,0],
                              [1,-4,1],
                              [0,1,0]])


# function for image thresholding
def imThreshold(img, threshold, maxVal):
    assert len(img.shape) == 2 # input image has to be gray
    
    height, width = img.shape
    bi_img = np.zeros((height, width), dtype=np.uint8)
    for x in range(height):
        for y in range(width):
            if img.item(x, y) > threshold:
                bi_img.itemset((x, y), maxVal)
                
    return bi_img

def genGaussianKernel(width, sigma):
    
    # define your 2d kernel here 
    x = [x-int(width/2) for x in range(width)] # Create std defined 1D array with difference of 1
    g = np.exp((np.square(x) / np.square(sigma))/-2) # Gauss formula 1D
    kernel = np.outer(g, g) #multiply 2 1D vectors to make 2D kernel => Seperability
    kernel = kernel / np.sum(kernel) # normalize
    return kernel

def sharpen_img(img):
  kernel = np.asarray([[0,-1,0],
                      [-1,4,0],
                      [0,-1,0]])
  return cv2.filter2D(src = img, ddepth = -1, kernel=kernel)
def noisy_image_generator(img_in, probability):
  # define your function here
  # Fill in your code here
  img_out = copy.deepcopy(img_in)
  for r in range(len(img_out)):
    for c in range(len(img_out[r])):
      rand_num = np.random.uniform(0.0, 1.0)
      if(rand_num <= probability):
        #color pixel either black or white
        choose_rand_color =  np.random.uniform(0.0, 1.0)
        if(choose_rand_color <= .5):
          img_out[r][c] = 255 # white
        else:
          img_out[r][c] = 0 # black
  return img_out
  
# Function to apply median filter(window size kxk) on the input image  
def median_filter(img_in, window_size):
  # define your function here
  # Fill in your code here
  # If you're at an edge, consider that edge as "-1"
  result = copy.deepcopy(img_in)
  for r in range(len(result)):
    for c in range(len(result[r])):
      curr_nums = []
      for mr in range(int(r - window_size/2), int(r + window_size/2)):
        for mc in range(int(c - window_size/2), int(c + window_size/2)):
          if((mr >= 0 and mr < len(result)) and (mc >= 0 and mc < len(result[r]))):
            curr_nums.append(img_in[mr][mc])
      curr_nums.sort()
      #print("Length of currnums should be <= 25: ", len(curr_nums))
      result[r][c] = curr_nums[int(len(curr_nums)/2)] # median
  return result

def genGausKernel1D(length, sigma):
    
    # define you 1d kernel here
    # Fill in your code here
    x = [x-int(length/2) for x in range(length)]
    g = np.exp((np.square(x) / np.square(sigma))/-2) # Gauss formula 1D
    #print("gauss = ", gauss)
    kernel_1d = g/np.sum(g) #multiply 2 1D vectors to make 2D kernel and normalize
    return kernel_1d
# Load images
img       = cv2.imread('Images/img.jpg', 0)

# Create your Gaussian kernel
Gaussian_kernel = np.asarray(genGaussianKernel(23, 3))

# Create your Laplacian of Gaussian
LoG = cv2.filter2D(src = Gaussian_kernel, ddepth = -1, kernel = Laplacian_kernel)

# Convolve with image and noisy image
#S & P Filter
noisy_img = noisy_image_generator(img, probability=.1)
res_img_kernel1 = cv2.filter2D(src = img, ddepth = -1, kernel = LoG)
#res_img_kernel1_sharpened = cv2.filter2D(src = img, ddepth = -1, kernel = LoG)

# Write out result images
cv2.imwrite("Results/P1_01.jpg", res_img_kernel1)

img_sp = noisy_image_generator(img, .2)
img_denoised = median_filter(img_sp, 5)
# Plot results
plt.figure(figsize = (10, 10))

plt.subplot(2, 2, 1)
plt.imshow(img, 'gray')
plt.title('Image: Original')
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(sharpen_img(img_denoised), 'gray')
plt.title('Image: denoised')
plt.axis("off")
'''
plt.subplot(2, 2, 2)
plt.imshow(res_img_kernel1, 'gray')
plt.title('Image: Discrete Laplacian Convolved with Gaussian')
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sharpen_img(img), 'gray')
plt.title('Image: Sharpened')
plt.axis("off")
'''
plt.subplot(2, 2, 4)
plt.imshow(res_img_kernel1, 'gray')
plt.title('Image: SHARPENED Discrete Laplacian Convolved with Gaussian')
plt.axis("off")


plt.show()
