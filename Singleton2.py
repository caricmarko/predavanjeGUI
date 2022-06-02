class Singleton:
 
    __shared_instance = 'GeeksforGeeks'
 
    @staticmethod
    def getInstance():
 
        """Static Access Method"""
        if Singleton.__shared_instance == 'GeeksforGeeks':
            Singleton()
        return Singleton.__shared_instance
 
    def __init__(self):
        print("Poziv")
        print(Singleton.__shared_instance)
        print("Poziv ispod")
        """virtual private constructor"""
        if Singleton.__shared_instance != 'GeeksforGeeks':
            raise Exception ("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
# main method
if __name__ == "__main__":
 
    # create object of Singleton Class
    obj = Singleton()
    print(obj)
    #obj = Singleton() # drugi put __shared_instance pokazuje na objekat
    #print(obj)
  
    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)