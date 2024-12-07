import datetime

class AgriculturalAccount:
    def __init__(self, name, age, crop_type):
        self.name = name
        self.age = age
        self.crop_type = crop_type

class User:
    def __init__(self, username, password, account):
        self.username = username
        self.__password = password  # Encapsulated password
        self.account = account

    def check_password(self, password):
        return self.__password == password

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class FarmerProduct:
    def __init__(self, product_code, name, description, price, quantity):
        self.product_code = product_code
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def create_account(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter your full name: ")
        age = int(input("Enter age: "))
        crop_type = input("Enter Occupation: ")

        account = AgriculturalAccount(name, age, crop_type)
        new_user = User(username, password, account)
        self.users.append(new_user)
        print("Sign up successful!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.check_password(password):
                self.logged_in_user = user
                print("Login successful!")
                return
        print("Login failed. Invalid username or password.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully!")

    def display_profile(self):
        if self.logged_in_user:
            user = self.logged_in_user
            print("User Profile:")
            print(f"Username: {user.username}")
            print(f"Name: {user.account.name}")
            print(f"Age: {user.account.age}")
            print(f"Occupation: {user.account.crop_type}")
        else:
            print("Please log in first.")

    def change_password(self):
        if self.logged_in_user:
            current_password = input("Enter current password: ")
            if self.logged_in_user.check_password(current_password):
                new_password = input("Enter new password: ")
                self.logged_in_user.set_password(new_password)
                print("Password changed successfully!")
            else:
                print("Current password is incorrect.")
        else:
            print("Please log in first.")

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        product_id = int(input("Enter Product Code: "))
        name = input("Enter Product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        new_product = Product(product_id, name, price, quantity)
        self.products.append(new_product)
        print("Product added successfully.")

    def display_products(self):
        print("\nProduct List:")
        for product in self.products:
            print(f"Code: {product.product_id}, Name: {product.name}, Price: {product.price:.2f}, Quantity: {product.quantity}")

    def delete_product(self):
        product_id = int(input("Enter the Code of the product to delete: "))
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product with Code {product_id} deleted successfully.")
                return
        print(f"Product with Code {product_id} not found.")

    def update_product(self):
        product_id = int(input("Enter the Code of the product to update: "))
        for product in self.products:
            if product.product_id == product_id:
                product.name = input("Enter Product name: ")
                product.price = float(input("Enter price: "))
                product.quantity = int(input("Enter quantity: "))
                print("Product details updated successfully.")
                return
        print(f"Product with Code {product_id} not found.")

    def buy_product(self):
        self.display_products()
        product_id = int(input("Enter the Code of the product you want to buy: "))
        quantity = int(input("Enter the quantity you want to buy: "))
        for product in self.products:
            if product.product_id == product_id:
                if 0 < quantity <= product.quantity:
                    product.quantity -= quantity
                    print(f"Purchase successful. Total cost: {product.price * quantity:.2f}")
                    return
                else:
                    print("Invalid quantity. Please enter a valid quantity.")
                    return
        print(f"Product with Code {product_id} not found.")

class FarmerProductManager:
    def __init__(self):
        self.farmer_products = []

    def create_farmer_product(self, logged_in_user):
        if not logged_in_user:
            print("Please log in to add a Farmer product.")
            return
        product_code = int(input("Enter product code: "))
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        new_product = FarmerProduct(product_code, name, description, price, quantity)
        self.farmer_products.append(new_product)
        print("Farmer product added successfully.")

    def display_farmer_products(self):
        print("\nFarmer Products:")
        for product in self.farmer_products:
            print(f"Code: {product.product_code}, Name: {product.name}, Description: {product.description}, Price: {product.price:.2f}, Quantity: {product.quantity}")

    def buy_farmer_product(self):
        self.display_farmer_products()
        product_code = int(input("Enter the Code of the farmer product you want to buy: "))
        quantity = int(input("Enter the quantity you want to buy: "))
        for product in self.farmer_products:
            if product.product_code == product_code:
                if 0 < quantity <= product.quantity:
                    product.quantity -= quantity
                    print(f"Purchase successful. Total cost: {product.price * quantity:.2f}")
                    return
                else:
                    print("Invalid quantity. Please enter a valid quantity.")
                    return
        print(f"Farmer Product with Code {product_code} not found.")

class AdminManager:
    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "admin123"
        self.contents = []
        self.videos = []

    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if self.admin_username == username and self.admin_password == password:
            return True
        else:
            print("Admin login failed. Invalid username or password.")
            return False

    def admin_functions(self, product_manager):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Display Products")
            print("3. Delete Product")
            print("4. Update Product")
            print("5. Upload Content")
            print("6. Upload Video Tutorial")
            print("7. Exit Admin Panel")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                product_manager.add_product()
            elif choice == 2:
                product_manager.display_products()
            elif choice == 3:
                product_manager.delete_product()
            elif choice == 4:
                product_manager.update_product()
            elif choice == 5:
                self.upload_content()
            elif choice == 6:
                self.upload_video()
            elif choice == 7:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    def upload_content(self):
        print("\nUpload Content:")
        title = input("Enter content title: ")
        description = input("Enter content description: ")
        file_path = input("Enter the file path of the content: ")
        content = {"title": title, "description": description, "file_path": file_path}
        self.contents.append(content)
        print(f"Content '{title}' uploaded successfully from {file_path}.")

    def upload_video(self):
        print("\nUpload Video Tutorial:")
        title = input("Enter video title: ")
        description = input("Enter video description: ")
        file_path = input("Enter the file path of the video: ")
        video = {"title": title, "description": description, "file_path": file_path}
        self.videos.append(video)
        print(f"Video '{title}' uploaded successfully from {file_path}.")

    def display_contents(self):
        print("\nContents:")
        for content in self.contents:
            print(f"Title: {content['title']}, Description: {content['description']}, File Path: {content['file_path']}")

    def display_videos(self):
        print("\nVideo Tutorials:")
        for video in self.videos:
            print(f"Title: {video['title']}, Description: {video['description']}, File Path: {video['file_path']}")

class ChatBot:
    @staticmethod
    def chat_with_me():
        print("Welcome to our Platform Agri Smart Solutions")
        print("Type 'exit' to end the conversation.")
        while True:
            user_query = input("You: ")
            if user_query.lower() == "exit":
                print("Exiting ...")
                break
            response = ChatBot.get_chat_bot_response(user_query)
            print(response)

    def get_chat_bot_response(user_query):
      if "hello" in user_query.lower() or "hi" in user_query.lower():
        return "Hello! How can I help you?"
      elif "products" in user_query.lower():
        return ("We offer a variety of agricultural products such as:\n"
                "1. Seasonal Fruits and vegetables\n"
                "2. Veterinary Medicine\n"
                "3. Animal feed\n"
                "4. Seeds, pesticides, fertilizers, etc.\n"
                "5. Veterinary Medicine\n"
                "etc.")
      elif "buy" in user_query.lower():
         return "To buy products, please visit our Website or contact our farmers directly.\nLink: ........................"
      elif "contact expert" in user_query.lower():
         return "To contact our expert directly, please call our toll-free number: 01512120909"
      else:
         return "Our expert will be available soon, please wait a minute. And this is a suggested tutorial link."


class HelpAndSupport:
    @staticmethod
    def help_and_support():
        print("\nHelp and Support:")
        print("For assistance, please contact support@agri_assist.com or call 01512120909")

class ExpertAppointment:
    @staticmethod
    def expert_appointment():
        print("\nExpert Appointment:")
        print("To book an appointment with an expert, please visit our website or call 01512120909 ")

class WeatherUpdate:
    @staticmethod
    def get_weather_update():
        print("\nWeather Update:")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Date: {current_date}")
        print("\nDhaka:")
        print("Weather: Clear sky")
        print("Temperature: 30°C")
        print("Humidity: 70%")
        print("Rainfall Prediction: No rainfall predicted")
        print("\nRajshahi:")
        print("Weather: Partly cloudy")
        print("Temperature: 32°C")
        print("Humidity: 60%")
        print("Rainfall Prediction: Light rain predicted")
        print("\nChittagong:")
        print("Weather: Overcast")
        print("Temperature: 28°C")
        print("Humidity: 80%")
        print("Rainfall Prediction: Heavy rain predicted")

class MainMenu:
    def __init__(self):
        self.user_manager = UserManager()
        self.product_manager = ProductManager()
        self.farmer_product_manager = FarmerProductManager()
        self.admin_manager = AdminManager()

    def display_menu(self):
        while True:
            print("\n Welcome to Agri Assist:")
            print("1. Create Account")
            print("2. Login")
            print("3. Change Password")
            print("4. View Profile")
            print("5. Chat with me")
            print("6. Help and Support")
            print("7. Expert Appointment")
            print("8. Admin Login")
            print("9. Farmer Sell Product")
            print("10. Display Farmer Products")
            print("11. Buy Farmer Product")
            print("12. Display Admin Products")
            print("13. Buy Admin Products")
            print("14. View Uploaded Content")
            print("15. View Video Tutorials")
            print("16. Weather Update")
            print("17. Log Out")
            print("18. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.user_manager.create_account()
            elif choice == 2:
                self.user_manager.login()
            elif choice == 3:
                self.user_manager.change_password()
            elif choice == 4:
                self.user_manager.display_profile()
            elif choice == 5:
                ChatBot.chat_with_me()
            elif choice == 6:
                HelpAndSupport.help_and_support()
            elif choice == 7:
                ExpertAppointment.expert_appointment()
            elif choice == 8:
                if self.admin_manager.admin_login():
                    self.admin_manager.admin_functions(self.product_manager)
            elif choice == 9:
                self.farmer_product_manager.create_farmer_product(self.user_manager.logged_in_user)
            elif choice == 10:
                self.farmer_product_manager.display_farmer_products()
            elif choice == 11:
                self.farmer_product_manager.buy_farmer_product()
            elif choice == 12:
                self.product_manager.display_products()
            elif choice == 13:
                self.product_manager.buy_product()
            elif choice == 14:
                self.admin_manager.display_contents()
            elif choice == 15:
                self.admin_manager.display_videos()
            elif choice == 16:
                WeatherUpdate.get_weather_update()
            elif choice == 17:
                self.user_manager.logout()
            elif choice == 18:
                print("Exiting the application...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 18.")

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.display_menu()
