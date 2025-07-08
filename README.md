# 🍔 Дипломный проект: Юнит-тесты для Stellar Burgers

Автотесты для проверки программы заказа бургеров в **Stellar Burgers**

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)  
*Полное покрытие кода тестами (см. [отчет](htmlcov/index.html))*

## 🧪 Реализованные сценарии

Созданы юнит-тесты, покрывающие основные классы системы:
- `Bun` - тестирование работы с булочками
- `Burger` - тестирование сборки бургера
- `Ingredient` - тестирование ингредиентов
- `Database` - тестирование базы данных

## 📂 Структура проекта
project/
├── praktikum/ # Пакет с основной логикой приложения
├── tests/ # Пакет с тестами
│ ├── bun_test.py # Тесты для класса Bun
│ ├── burger_test.py # Тесты для класса Burger
│ ├── ingredient_test.py # Тесты для класса Ingredient
│ └── database_test.py # Тесты для класса Database
├── requirements.txt # Зависимости
└── htmlcov/ # Отчет о покрытии (генерируется)

text

## 🚀 Запуск автотестов

1. Установите зависимости:
```bash
pip install -r requirements.txt
Запустите тесты с генерацией отчета о покрытии:

bash
pytest --cov=praktikum --cov-report=html
После выполнения откройте htmlcov/index.html для просмотра детального отчета.

🔹 Проект разработан в рамках дипломной работы
🔹 *100% покрытие кода unit-тестами*
