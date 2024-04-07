import numpy as np
import cv2
import matplotlib.pyplot as plt


def harris_corner_detection(image, threshold, radius):
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   

    # Calculate the image gradients Ix and Iy
    Ix = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    Iy = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    
    
    plt.subplot(1,2,1)
    plt.title("Ix")
    plt.imshow(Ix)
    
    
    plt.subplot(1,2,2)
    plt.title("Iy")
    plt.imshow(Iy)
    plt.show()

    # Calculate the structure tensors Ixx, Ixy, and Iyy
    Ixx = Ix * Ix
    Ixy = Ix * Iy
    Iyy = Iy * Iy

    # Apply a Gaussian filter to smooth the structure tensors reduce noise
    Ixx = cv2.GaussianBlur(Ixx, (5, 5), 0)
    Ixy = cv2.GaussianBlur(Ixy, (5, 5), 0)
    Iyy = cv2.GaussianBlur(Iyy, (5, 5), 0)

    # Calculate the Harris corner response R
    R = np.zeros((image.shape[0], image.shape[1]))

    # Assign the value 0.04 to the variable 'k' before using it
    k = 0.04

    detA = Ixx*Iyy - Ixy**2
    traceA = Ixx + Iyy
    harris_response = detA - k * traceA**2  #Harris Formula
    
    # Threshold the Harris response
    thresholded_response = harris_response > threshold

    # Normalize the thresholded response to range [0, 255]
    normalized_response = cv2.normalize(thresholded_response.astype(np.uint8), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Convert normalized response to RGB color format
    color_response = cv2.cvtColor(normalized_response, cv2.COLOR_BGR2RGB)

   
    #Show the thesholded response
    plt.imshow(color_response)
    plt.title('Thresholded Harris Response')
    plt.show()
    
    #Show the Harris Response
    plt.imshow(harris_response)
    plt.title('Corner Response')
    plt.show()

    #Harris Corner Detection
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            det = Ixx[i, j] * Iyy[i, j] - Ixy[i, j] * Ixy[i, j]
            trace = Ixx[i, j] + Iyy[i, j]
            R[i, j] = det - k * trace * trace
            

    # Apply non-maximum suppression to identify corners
    
    corners = []  # Initializes an empty list to store the detected corner coordinates.
    
 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if R[i, j] < threshold:
                continue
           
            skip = False
            
            for k in range(-radius, radius + 1):
                for l in range(-radius, radius + 1):
                    if k == 0 and l == 0:             
                        continue

                    new_i = i + k                   
                    new_j = j + l

                    #Skips if the neighboring pixel is outside the image boundaries.
                    if new_i < 0 or new_i >= image.shape[0] or new_j < 0 or new_j >= image.shape[1]:
                        continue
                    
                    #Comparison for Suppression:
                    if skip or R[new_i, new_j] >= R[i, j]:           
                        skip = True                                 
                        break
            #Adding Significant Corners:
            if not skip:
                corners.append((i, j, R[i, j])) 
                                               
    return corners 



def main():
    # Load the image
    image = cv2.imread('sample4.jpg')

    # Detect corners using Harris corner detection
    corners = harris_corner_detection(image,10**8, 10)

    # Draw the detected corners on the image
    for corner in corners:
        i, j, _ = corner
        cv2.circle(image, (j, i), 1, (0 , 255, 0), 2)

    #Resizing the image for user    
    print("Input is in percentage.")
    print("1 = 100%, 2 = 200%, 0.5 = 50%")
    scale = float(input("Enter scale: "))
    height = int(image.shape[0] * scale)
    width = int(image.shape[1] * scale)

    #Display the image with detected corners
    resized_image = cv2.resize(image, (width, height))
    cv2.imshow('Detected Corners ',resized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()
