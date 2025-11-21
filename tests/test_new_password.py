import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
#2 new tests
def test_password_length():
    lengths = [5, 10, 15, 20]
    for length in lengths:
        password = generate_password(length)
        assert len(password) == length

def test_password_uniqueness():
    password  =  generate_password(100)
    password_2 = generate_password(100)
    assert password != password_2