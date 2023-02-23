# Написать функцию проверки "силы" пароля, возвращающую всегда строку
#   - если пароль короче 8 символов, то вернуть строку "Too Weak"
#   - если пароль содержит только цифры, только строчные, только заглавные то вернуть строку "Weak"
#   - если пароль содержит символы любых 2 наборов, то вернуть "Good"
#   - если пароль содержит символы любых 3 наборов, то вернуть "Very Good"
import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for simbols in (digits, lowers, uppers):
        if any(e in simbols for e in value):
            count += 1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('qwertyu') == 'Too Weak'
    assert password_strength('QWERTYU') == 'Too Weak'
    assert password_strength('QWas12') == 'Too Weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('123456789077') == 'Weak'
    assert password_strength('qwertyui') == 'Weak'
    assert password_strength('qwertyuiwrwfs') == 'Weak'
    assert password_strength('QWERTYUI') == 'Weak'
    assert password_strength('QWERTYUIKLJKK') == 'Weak'
    assert password_strength('1234qwer') == 'Good'
    assert password_strength('1234qwerdfd') == 'Good'
    assert password_strength('1234QWER') == 'Good'
    assert password_strength('1234QWERDFD') == 'Good'
    assert password_strength('tyuiQWER') == 'Good'
    assert password_strength('tyuiQWERSDF') == 'Good'
    assert password_strength('123qweRTY') == 'Very Good'
    assert password_strength('1234567qW') == 'Very Good'
    assert password_strength('qwertyuI1') == 'Very Good'
    assert password_strength('QWERTYUi1') == 'Very Good'
