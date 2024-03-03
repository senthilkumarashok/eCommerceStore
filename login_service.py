class LoginService:    

    userCreds = {"user1": "password1", "user2": "password2"}
    adminCreds = {"admin1": "password1", "admin2": "password2"}
    
    @staticmethod
    def userLogin(userName, password):
        if userName in LoginService.userCreds and LoginService.userCreds[userName] == password:
            print("\nLogin successful!")
        else:
            print("\nLogin invalid")        

    @staticmethod
    def adminLogin(userName, password):
        if userName in LoginService.adminCreds and LoginService.adminCreds[userName] == password:
            print("\nLogin successful!")
        else:
            print("\nLogin invalid")        

LoginService.userLogin('senkumar', 'password2')
LoginService.userLogin('user1', 'password2')
LoginService.adminLogin('senkumar', 'password')
LoginService.adminLogin('admin1', 'password1')
