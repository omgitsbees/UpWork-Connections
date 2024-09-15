import numpy as np
from scipy.ndimage import gaussian_filter
import requests
import json

class StableDiffusionBot:
    def __init__(self):
        # Initialize any necessary parameters or configurations
        self.sigma = 1.0 # Standard deviation for Gaussian kernel

    def apply_diffusion(self, image):
        """
        Apply stable diffusion to an image.
        :param image: 2D numpy array representing the image
        :return: Diffused image
        """
        return gaussian_filter(image, sigma=self.sigma)
    def process_request(self, request_data):
        """
        Process the incoming request and return the diffused image.
        :param request_data: Dictionary containing image data
        :return: Dictionary with the diffused image data
        """
        # Assume request_data contains an image as a 2D list or numpy array
        image = np.array(request_data['image'])
        diffused_image = self.apply_diffusion(image)

        # Convert the diffused image back to a list for JSON serialization
        diffused_image_list = diffused_image.tolist()
        return {'diffused_image': diffused_image_list}
    
    def handle_request(self, request_url):
        """
        Handle an incoming request from a URL and respond with the diffused image.
        :param request_url: URL to fetch request data from
        """
        try:
            response = requests.get(request_url)
            request_data = resonse.json()

            # Process the request and get the result
            result = self.process_request(request_data)

            # Send the result back as a response
            result_url = request_data.get('result_url')
            if result_url:
                request.post(result_url, json=result)
            else:
                print("Result URL not provided.")
        except Exception as e:
            print(f"Error handling request: {e}")

if __name__ == "__main__":
    bot = StableDiffusionBot()

    # Example usage
    example_image = np.random.rand(100, 100).tolist() # Random image for demonstration
    request_data = {'image': example_image, 'result_url': 'http://example.com/result'}

    # Simulate handling a request
    response = bot.process_request(request_data)
    print("Diffused Image:", response)