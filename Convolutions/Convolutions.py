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

def mean_filter(img, width):
  result = copy.deepcopy(img)
  for r in range(len(img)):
    for c in range(len(img[r])):
      mean = 0
      counter = 0
      for mr in range(int(r - width/2), int(r + width/2)):
        for mc in range(int(c - width/2), int(c + width/2)):
          if((mr >= 0 and mr < len(result)) and (mc >= 0 and mc < len(result[r]))):
            mean += img[mr][mc]
            counter+=1
      result[r][c] = mean/counter
  return result

def genGausKernel1D(length, sigma):
    # define you 1d kernel here
    # Fill in your code here
    x = [x-int(length/2) for x in range(length)]
    g = np.exp((np.square(x) / np.square(sigma))/-2) # Gauss formula 1D
    #print("gauss = ", gauss)
    kernel_1d = g/np.sum(g) #multiply 2 1D vectors to make 2D kernel and normalize
    return kernel_1d
  
def cannyEnhancer(img):
    
    # Calculate edges in x and y direction
    # Return edge_map and grad_dir (gradient directions at each pixel location)
    canny_x = np.asarray([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])
    canny_y = np.asarray([[-1,-2,-1],
               [0,0,0],
               [1,2,1]])
    img_gauss_filtered = cv2.filter2D(src = img, ddepth = -1, kernel = genGaussianKernel(50, 2))
    img_gauss_cx = cv2.filter2D(src = img_gauss_filtered, ddepth = -1, kernel = canny_x)
    img_gauss_cy = cv2.filter2D(src = img_gauss_filtered, ddepth = -1, kernel = canny_y)
    img_gauss_cxy = cv2.bitwise_or(img_gauss_cx, img_gauss_cy) #You can combine two images by doing bitwise or over them
    img_gauss_cmag = img_gauss_cmag = np.hypot(img_gauss_cx, img_gauss_cy)
    img_gauss_cang = np.arctan(np.divide(img_gauss_cy, img_gauss_cx))

    edge_map = img_gauss_cmag
    grad_dir = img_gauss_cang
    combined = img_gauss_cxy 
    return np.asarray((edge_map), dtype=np.uint8), np.asarray((grad_dir), dtype = np.uint8), np.asarray((combined), dtype = np.float)

def nonMaxSuppression(edge_map, grad_dir):
    
    # Fill in your code here
    # For each pixel location, look in the direction of gradient and suppress non-max values

    #Discretize gradients:
    grad_dir2 = copy.deepcopy(grad_dir)
    for r in range(len(grad_dir)):
      for c in range(len(grad_dir[r])):
        curr_angle = 0 if math.isnan(grad_dir[r][c]) else grad_dir[r][c] * 180/math.pi
        if curr_angle > -22.5 and curr_angle <= 22.5:
          grad_dir2[r][c] = 0
        elif curr_angle > 22.5 and curr_angle <= 67.5:
          grad_dir2[r][c] = 45
        elif curr_angle > 67.5 and curr_angle <= 90:
          grad_dir2[r][c] = 90
        elif curr_angle > -90 and curr_angle <= -67.5:
          grad_dir2[r][c] = 90
        elif curr_angle > -67.5 and curr_angle <= -22.5:
          grad_dir2[r][c] = 135
    #print("Gradient Angles: ", grad_dir2)

    #Suppress Non Maximal Noise:
    edge_map_supp = copy.deepcopy(edge_map)
    for r in range(len(edge_map_supp)):
      for c in range(len(edge_map_supp[r])):
        center = edge_map[r][c]
        if(grad_dir2[r][c] == 0):
          #Left and right
          left = 0
          right = 0
          try:
            left = edge_map[r][c-1]
            right = edge_map[r][c+1] 
          except Exception:
            pass
          if(center < left or center < right):
            edge_map_supp[r][c] = 0

        elif(grad_dir2[r][c] == 45):
          #top right, bottom left
          t_right = 0
          b_left = 0
          try:
            t_right = edge_map[r-1][c+1] 
            b_left = edge_map[r+1][c-1] 
          except Exception:
            pass
          if(center < b_left or center < t_right):
            edge_map_supp[r][c] = 0

        elif(grad_dir2[r][c] == 90):
          #top and bottom
          top = 0
          bottom = 0 
          try:
            top = edge_map[r-1][c] 
            bottom = edge_map[r+1][c] 
          except Exception:
            pass
          if(center < bottom or center < top):
            edge_map_supp[r][c] = 0

        elif(grad_dir2[r][c] == 135):
          #top left and bottom right
          t_left = 0
          b_right = 0
          try:
            t_left = edge_map[r-1][c-1] 
            b_right = edge_map[r+1][c+1] 
          except Exception:
            pass
          if(center < b_right or center < t_left):
            edge_map_supp[r][c] = 0
    return edge_map_supp
# Load images
img       = cv2.imread('Images/img2.png', 0)
# Create your Gaussian kernel
Gaussian_kernel = np.asarray(genGaussianKernel(23, 3))

# Create your Laplacian of Gaussian
LoG = cv2.filter2D(src = Gaussian_kernel, ddepth = -1, kernel = Laplacian_kernel)

# Convolve with image and noisy image
#S & P Filter
noisy_img = noisy_image_generator(img, probability=.1)
res_img_kernel1 = cv2.filter2D(src = sharpen_img(img), ddepth = -1, kernel = LoG)
res_img_kernel1_sharpened = cv2.filter2D(src = img, ddepth = -1, kernel = LoG)

# Write out result images

cv2.imwrite("Results/P1_01.jpg", res_img_kernel1)

img_sp = noisy_image_generator(img, .6)
#img_denoised = median_filter(img_sp, 5)
print("Kernel Gauss: \n", genGaussianKernel(5, 2))
# Plot results

plt.figure(figsize = (10, 10))

plt.subplot(2, 2, 1)
plt.imshow(img, 'gray')
plt.title('Image: Original')
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(res_img_kernel1, 'gray')
plt.title('Image: Discrete Laplacian Convolved with Gaussian')
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(noisy_image_generator(img, .2), 'gray')
plt.title('Image: noisy')
plt.axis("off")

plt.subplot(2, 2, 4)
img_g  = cv2.filter2D(src = noisy_image_generator(img, .2), ddepth = -1, kernel = Gaussian_kernel)
plt.imshow(img_g, 'gray')
plt.title('Image: filtered noise')
plt.axis("off")

'''
plt.subplot(2, 2, 4)
plt.imshow(cv2.filter2D(src = img, ddepth = -1, kernel=Gaussian_kernel), 'gray')
plt.title('Image: SHARPENED Discrete Laplacian Convolved with Gaussian')
plt.axis("off")
'''

plt.show()

