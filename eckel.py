class Simple:
    def __init__(self, str):
        print('inside the simple constructor')
        self.s = str

    # two methods
    def show(self):
        print(self.s)
    def showMsg(self, msg):
        print(msg + ':', self.show()) # calling another method

if __name__ == "__main__":
    # create an object:
    x = Simple('this is my string parameter')
    
