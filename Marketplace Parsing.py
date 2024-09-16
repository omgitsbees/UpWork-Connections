import requests
from bs4 import BeautifulSoup

def parse_product(product_link):
    # Fetch the webpage
    response = requests.get(product_link)

    if response.status_code == 200:
        # Parse the webpage content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract product details (this is just an example, you'll need to adjust selectors)
        product_name = soup.find('h1', class_='product-title').text
        price = soup.find('span', class_='price').text
        description = soup.find('div', class_='product-description').text

        return {
            "name": product_name,
            "price": price,
            "description": description
        }
    else:
        print("Error fetching the product page.")
        return None
    
def upload_to_marketplace(product_data, category_name):
    # Example API call to upload product to your marketplace 
    api_url = "https://yourmarketplace.com/api/upload_product"
    data = {
        "name": product_data['name'],
        "price": product_data['price'],
        "description": product_data['description'],
        "category": category_name
    }

    # Send the data to the marketplace 
    response = requests.post(api_url, json=data)

    if response.status_code == 201:
        print("Product successfully uploaded!")
    else:
        print("Failed to upload the product.")

# Main Function
if __name__ == "__main__":
    product_link = input("Enter the product link: ")
    category_name = input("Enter the category name: ")

    # Parse the product
    product_data = parse_product(product_link)

    if product_data:
        # Upload to marketplace
        upload_to_marketplace(product_data, category_name)