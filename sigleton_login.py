class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.authenticated = False
    def login(self,username,psw):
        usuarios = {"persona1":"1234","person2":"5678"}

        if self.authenticated is True:
            print("Usuario ya logeado")
        
        if username in usuarios: 
            if psw == usuarios[username]:
                print("Sesion iniciada") 
                self.authenticated = True

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    s1.login("persona1","1234")