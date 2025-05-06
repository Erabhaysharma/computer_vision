# input image
import os
import cherrypy
from PIL import Image
from io import BytesIO
import  numpy as np
class ImageUploadApp:
    uploaded_image = None  # Variable to store the uploaded image

    @cherrypy.expose
    def index(self):
        return """
        <html>
    <head>
        <title>Image Upload</title>
    </head>
    <body style="margin: 0; padding: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background-color: #eef2f7; font-family: Arial, sans-serif; flex-direction: column;">

        <div style="text-align: center; background: white; padding: 40px 60px; border-radius: 12px; box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);">
            <h4 style="color: #777; margin-top: 0;">A Minor Project of CV i.e Image Compression</h4>
            <h2 style="color: #333; margin-bottom: 30px;">📤 Upload an Image</h2>

            <form action="upload" method="post" enctype="multipart/form-data">
                <input 
                    type="file" 
                    name="image" 
                    accept="image/*" 
                    required 
                    style="padding: 10px; border: 1px solid #ccc; border-radius: 6px; width: 100%; margin-bottom: 20px;" 
                />
                <br>
                <input 
                    type="submit" 
                    value="Upload Image" 
                    style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 6px; font-size: 16px; cursor: pointer;"
                />
            </form>
        </div>

        <footer style="margin-top: 20px; font-size: 13px; color: #888;">
            &copy; 2025 Abhay Sharma
        </footer>
    </body>
</html>

        """

    @cherrypy.expose
    def upload(self, image):
        # Store the uploaded image in a variable
        self.uploaded_image = Image.open(image.file)
        save_path = os.path.join(os.getcwd(), "uploaded_image.png")
        self.uploaded_image.save(save_path)
        # Provide feedback to the user
        return """
        <html>
    <head>
        <title>Image Uploaded</title>
    </head>
    <body style="margin: 0; padding: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background-color: #f4f4f9; font-family: Arial, sans-serif;">
        <div style="text-align: center; background: white; padding: 40px 60px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h2 style="color: #4CAF50;">✅ Image Uploaded Successfully!</h2>
            <p style="color: #555; font-size: 16px;">The image has been stored in a variable for further processing.</p>
            <a href="/" style="display: inline-block; margin-top: 20px; text-decoration: none; background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">⬅ Go Back</a>
        </div>

         
    </body>
</html>

        """
    def get_image_matrix(self, image):
        """
        Convert the uploaded image to a numpy matrix.
        :param image: PIL Image object
        :return: numpy array representing the image
        """
        # Convert the image to grayscale (optional, if needed)
        grayscale_image = image.convert("L")
        # Convert the image to a numpy array
        image_matrix = np.array(grayscale_image)
        return image_matrix



if __name__ == '__main__':
    config = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        }
    }
    cherrypy.quickstart(ImageUploadApp(), '/', config)