from custom_types import RawUserDict,ValidationError

class UserValidator:
    def __init__(self,data : RawUserDict):
        self.data : RawUserDict = data
        self.errors : list[ValidationError] = []


    def string_is_not_empty(self) -> None:
        if not all(self.data.values()):
            self.errors.append('Отсутсвуют данные о пользователе! (строки пусты)')

    def validate_age(self) -> None:
        age = self.data["age"]

        if not age.isdigit():
            self.errors.append("Возраст должен быть числом.")
            return

        age_number = int(age)

        if age_number < 0 or age_number > 120:
            self.errors.append("Возраст должен быть от 0 до 120.")
        
    def validate_email(self) -> None:
        email = self.data.get('email')

        if not isinstance(email,str) or '@' not in email or '.' not in email or email[-1] == '.' or email[-2] == '@' or email[-1] == '@':
            self.errors.append('Почта должна быть строкой и содержать "@", ".", и не заканчиваться на эти символы!')

    def validate_user_data(self) -> bool:
        self.string_is_not_empty()
        self.validate_age()
        self.validate_email()
        return len(self.errors) == 0
    
    