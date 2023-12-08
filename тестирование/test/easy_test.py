def test_ok():
    assert 1 == 1


def test_failed():
    assert 1 == 2

# pytest - будет автоматически искать все файлы тестирования
# pytest test/easy_test.py
# pytest -v - детальный вывод результатов
