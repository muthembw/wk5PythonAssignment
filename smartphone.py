# Base class for Smartphone
class Smartphone:
    def __init__(self, brand, model, operating_system, battery_percentage):
        self.brand = brand
        self.model = model
        self.operating_system = operating_system
        self.battery_percentage = battery_percentage

    def display_details(self):
        print(f"Smartphone Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Operating System: {self.operating_system}")
        print(f"Battery: {self.battery_percentage}%")

    def make_call(self, contact):
        print(f"Calling {contact}...")

    def charge_phone(self, charge_amount):
        self.battery_percentage += charge_amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100  # Max battery
        print(f"Charging... Battery is now at {self.battery_percentage}%")


# Subclass that inherits from Smartphone, adding camera functionality
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, operating_system, battery_percentage, camera_megapixels):
        super().__init__(brand, model, operating_system, battery_percentage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera!")


# Create an instance of the Smartphone class
phone = Smartphone("Samsung", "Galaxy S21", "Android", 50)
phone.display_details()
phone.make_call("John Doe")
phone.charge_phone(30)

# Create an instance of the SmartphoneWithCamera class
smartphone_with_camera = SmartphoneWithCamera("Apple", "iPhone 13", "iOS", 80, 12)
smartphone_with_camera.display_details()
smartphone_with_camera.take_photo()
smartphone_with_camera.charge_phone(10)
