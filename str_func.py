def func(s):
    """Высокий  регистр"""
    return s.upper()

def func2(s):
    """Функция  делает буквы  заглавными"""
    return "".join([word.capitalize() for word in s.split()])
