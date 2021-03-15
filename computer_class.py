# Brand
# Processor
# RAM
# Color


class computer:
    
    def __init__(self,brand = "Acer",processor="i7 9300h",ram="16GB",color='Obsidian black'):
        """

        Args:
            brand ,
            processor ,
            ram ,
            color 
        """ 

        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.color = color

    #Getter and Setter for attribute brand
    def set_brand(self,brand):
        self.brand = brand
    def get_brand(self):
        return self.brand
       #Getter and Setter for attribute processor
    def set_processor(self,processor):
        self.processor = processor
    def get_processor(self):
        return self.processor
   #Getter and Setter for attribute ram
    def set_ram(self,ram):
        self.ram = ram
    def get_ram(self):
        return self.ram
    #Getter and Setter for attribute color
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color

    def __str__(self):
        print("Printing Configuration of Computer:")
        self.print_config()
        return ""

    def print_config(self):
        '''
            This acts like show() funtion 
            This function prints the brand,processor,ram and color of computer object
        '''
        print("Brand is:{}".format(self.brand))
        print("Processor  is:{}".format(self.processor))
        print("Ram  is:{}".format(self.ram))
        print("Color  is:{}".format(self.color))


macbook = computer("Apple","i5","8GB","Silver")
macbook.set_processor("M1 chip")
print(macbook)