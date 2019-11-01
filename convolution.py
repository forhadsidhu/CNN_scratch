import cv2
import numpy as np



def conv(image):

    #laod the image and scale to 0...1


    #for each pixel in the input image we will inspect its neighbourhood

    kernel=(np.array(

        [[0,0,0],
         [1,1,1],
         [0,0,0]
        ]
    ))
    '''
     1 2 3 3 4
     6 7 8 8 8
     9 9 9 9 9
     9 9 9 9 9
     
    
     k_height=6
     k_width=8
     
     x=3 y=3
     
     ky= -3 -2 -1 0 1 2 3
     kx= -3 -2 -1 0 1 2 3
     
    
    '''
    #print("yes")
    kernel_sum=kernel.sum()

    i_width,i_height=image.shape[0],image.shape[1]
    k_width,k_height=kernel.shape[0],kernel.shape[1]

    #prepae the output array

    filtered=np.zeros_like(image)

    #print(i_width,i_height)


    #iterate over each (x,y) pixel in the image




    for y in range(i_width):

            for x in range(i_height):

                weighted_pixel_sum=0


                for ky in range(-int(k_height/2),k_height-1):

                    for kx in range(-int(k_width/2),k_width-1):

                        #print(kx,ky)
                        pixel=0
                        pixel_x=x-kx
                        pixel_y=y-ky


                        #print(pixel_y,pixel_x)
                        if (pixel_y>=0) and (pixel_y<i_width) and (pixel_x>=0) and (pixel_x<i_height):
                            #print("yes")
                            #print(pixel_y,pixel_x,i_height)
                            #print(i_height,i_width)
                            #print(pixel_y,pixel_x,image[pixel_y,pixel_x])

                            pixel=image[pixel_y,pixel_x]



                        weight= kernel[ky+int(k_height/2),kx+int(k_width/2)]
                        weighted_pixel_sum+=pixel*weight

    # finally, the pixel at location (x,y) is the sum of the weighed neighborhood
                #print(y,x)

                filtered[y,x]=weighted_pixel_sum/kernel_sum
    '''
    cv2.imshow("DIY convolution",filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    return filtered



if __name__ == "__main__":
    image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE).astype(float) / 255.0

    filter=conv(image)

    for i in range(0,300):
        filter=conv(filter)

    cv2.imshow("DIY convolution", filter)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




