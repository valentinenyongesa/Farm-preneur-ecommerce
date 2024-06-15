from PIL import Image
import imageio.v2 as imageio  # Use imageio.v2 to avoid deprecation warning

# Load the AVIF image
avif_image = imageio.imread('9490.avif')

# Convert to a PIL Image
pil_image = Image.fromarray(avif_image)

# Save as PNG
pil_image.save('hero4.png')

print("Conversion complete. 'hero4.png' has been saved.")