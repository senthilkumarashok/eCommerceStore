class LoginService:

    userCreds = {"user1": "password1", "user2": "password2"}
    adminCreds = {"admin1": "password1", "admin2": "password2"}

    @staticmethod
    def userLogin(userName, password):
        is_authenticated = False
        if (
            userName in LoginService.userCreds
            and LoginService.userCreds[userName] == password
        ):
            print("\nLogin successful!")
            is_authenticated = True
        else:
            print("\nLogin invalid")
        return is_authenticated

    @staticmethod
    def adminLogin(userName, password):
        is_authenticated = False
        if (
            userName in LoginService.adminCreds
            and LoginService.adminCreds[userName] == password
        ):
            print("\nLogin successful!")
            is_authenticated = True
        else:
            print("\nLogin invalid")
        return is_authenticated
