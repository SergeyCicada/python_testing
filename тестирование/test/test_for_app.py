"""Тесты можно объединять в классы

Тесты можно параметризировать - выполнение функции с разными наборами параметров

Тест можно пропустить с помощью декоратора

@pytest.mark.skip(reason='i know what i do')
def test_me():
    pass

Если ошибка - это корректное поведение

def call_method():
    raise Exception()

def test_fail_is_ok():
    with pytest.raises(Exception)
        call_method()"""
from app import sum_func, call_method


class TestSumFunc:
    def test_sum_positive(self):
        c = sum_func(1, 1)
        assert c > 0
        assert c == 2

    def test_sum_positive_and_negative(self):
        c = sum_func(1, -1)
        assert c == 0

    def test_sum_negative2(self):
        c = sum_func(-30, -10)
        assert c < 0
        assert c == -40

    parameters = [(1, 2, 3), (3, 4, 7), (-3, -4, -7)]

    @pytest.mark.parametrize('numbers', parameters)
    def test_sum_numbers(self, numbers: list[tuple]):
        assert (numbers[0]) + numbers[2] == numbers[3]

    def test_has_to_fail(self):
        with pytest.raises(Exception):
            call_method()

    @pytest.mark.skip(reason="OK")
    def test_skip(self):
        raise Exception
