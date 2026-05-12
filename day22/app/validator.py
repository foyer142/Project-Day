class UserValidator:
    def __init__(self,data):
        self.data = data
        self.errors = []

    def string_is_not_empty(self):
        if not all(self.data.values()):
            self.errors.append('Отсутсвуют данные о пользователе! (строки пусты)')

    def validate_age(self):
        age = self.data.get('age')
        if not isinstance(age,int) or age < 0 or age > 120:
            self.errors.append('Возраст должен быть числом и не меньше 0 и не больше 120.')
    
    def validate_email(self):
        email = self.data.get('email')

        if not isinstance(email,str) or '@' not in email or '.' not in email or email[-1] == '.' or email[-2] == '@':
            self.errors.append('Почта должна быть строкой и содержать "@", ".", и не заканчиваться на эти символы!')

    def validate_user_data(self):
        self.string_is_not_empty()
        self.validate_age()
        self.validate_email()
        return len(self.errors) == 0
    
    