#!/usr/bin/python3
""" 
User classaa
"""

class User():
    """ Documentatiozzzn """

    def __init__(self):
        """ Documentatidddon """
        self.__email = None

    @email.setter
    def email(self, value):
        """ Documentaaaation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """ Documessntation """
        return self.__email
   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
