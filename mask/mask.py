def oval():
    # from PIL import Image, ImageDraw

    # def crop_to_oval(image_path):
    #     # Open the image
    #     img = Image.open(image_path).convert("RGBA")
        
    #     # Create a mask with the same size as the image (initialized as fully transparent)
    #     width, height = img.size
    #     mask = Image.new("L", (width, height), 0)  # 0 for black (transparent)
        
    #     # Create an elliptical mask (white inside, black outside)
    #     draw = ImageDraw.Draw(mask)
    #     draw.ellipse([(0, 0), (width, height)], fill=255)  # Draw ellipse (oval)
        
    #     # Apply the mask to the image
    #     img.putalpha(mask)  # This adds transparency where the mask is black
        
    #     return img

    # # Use the function
    # image_path = 'me.png'  # Replace with your image path
    # oval_image = crop_to_oval(image_path)

    # print(oval_image.size)
    # # Save or display the cropped image
    # oval_image.save('doug.png')
    # oval_image.show()
    blah = True

from PIL import Image, ImageDraw, ImageFilter

def crop_to_oval_with_smooth_edges(image_path, radius=30):
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    
    # Create a mask with the same size as the image (initialized as fully transparent)
    width, height = img.size
    mask = Image.new("L", (width, height), 0)  # 0 for black (transparent)
    
    # Create an elliptical mask with smooth edges using a gradient
    draw = ImageDraw.Draw(mask)
    draw.ellipse([(0, 0), (width, height)], fill=255)  # Draw the oval (ellipse)
    
    # Apply Gaussian blur to the mask to create a soft, feathered edge
    mask = mask.filter(ImageFilter.GaussianBlur(radius))  # Apply blur for smooth edges
    
    # Apply the mask to the image
    img.putalpha(mask)  # This adds transparency where the mask is black, and smooth edges
    
    return img

# Use the function
image_path = 'me.png'  # Replace with your image path
smooth_oval_image = crop_to_oval_with_smooth_edges(image_path)

# Save or display the cropped image with smooth edges
smooth_oval_image.save('doug2.png')
smooth_oval_image.show()
