from unittest.mock import Mock

mock = Mock()

# 🔮 Магия 1: любой атрибут
print(mock.anything)  # <Mock name='mock.anything' ...> — не ошибка!

# 🔮 Магия 2: любой метод
mock.do_something(1, 2, 3)  # <Mock name='mock.do_something()' ...>

# 🔮 Магия 3: цепочки
mock.a.b.c(42)  # Работает на любой глубине!

# 🔮 Магия 4: автоматический возврат
result = mock.get_data()
print(result)  # <Mock name='mock.get_data()' ...> — мок вернулся сам из себя




# 1. Настраиваем возврат значения
#mock = Mock()
mock.json.return_value = {"title": "Mocked"}  # При вызове .json() вернёт dict

# 2. Проверяем вызов
mock.process(42)
mock.process.assert_called_once_with(42)  # ✅ True

# 3. Эмулируем ошибку
mock.fetch.side_effect = ConnectionError("Network error")
# При вызове mock.fetch() будет выброшено исключение
# mock.fetch()