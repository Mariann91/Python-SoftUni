class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __str__(self):
        password_len = "*" * len(self.__password)
      
        return f'You have a profile with username: "{self.__username}" and password: {password_len}'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):

        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
      
        return self.__password

    @password.setter
    def password(self, value):
        if not len(value) >= 8 or not value.isalnum():
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value
