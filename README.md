# FakeStore-Automation-Framework

Автоматизированный тестовый фреймворк для тестирования REST API и Web UI интернет-магазина **FakeStoreAPI**.

Проект разработан с использованием архитектурных подходов, применяемых в современных проектах автоматизации тестирования: разделение API и UI слоев, Page Object, Base API, модели данных, Allure Report и GitHub Actions.

---

## Технологии

* Python 3.13+
* Pytest
* Selenium WebDriver
* Requests
* Pydantic
* Faker
* Allure Report
* GitHub Actions
* Makefile
* Git

---

## Реализованный функционал

### API

* Авторизация пользователя
* Работа с продуктами (CRUD)
* Работа с пользователями (CRUD)
* Работа с корзинами (CRUD)
* Проверка негативных сценариев
* Использование моделей данных (Pydantic)
* Генерация тестовых данных через Faker

### UI

* Реализация паттерна Page Object
* Работа с корзиной
* Проверка отображения товаров
* Добавление товара в корзину
* Удаление товара из корзины
* Проверка содержимого корзины
* Тестирование процесса оформления заказа;
* Автоматизация сценария Checkout.

---

## Архитектура проекта

```text
Store_AQA/
│
├── api/
│   ├── clients/
│   ├── endpoints/ 
│   ├── models/
│   └── payloads/
│
├── ui/
│   ├── locators/
│   └── pages/
│
├── tests/
│   ├── test_api.py
│   └── test_ui.py
│
├── utils/
│   └── helper.py
│
├── .github/
│   └── workflows/
│
├── conftest.py
├── requirements.txt
├── Makefile
└── README.md
```

---

## Используемые архитектурные решения

* Page Object
* BasePage
* BaseAPI
* Requests Session
* Pydantic Models
* Pytest Fixtures
* Faker Payload Factory
* Allure Reporting

---

## Запуск проекта

### Клонирование репозитория

```bash
git clone https://github.com/pbolevoi/FakeStore-Automation-Framework
cd FakeStore-Automation-Framework
```

### Создание виртуального окружения

```bash
python -m venv venv
```

### Активация

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## Настройка переменных окружения

Создайте файл `.env`

Пример:

```env
USERNAME=your_username
PASSWORD=your_password
```

---

## Запуск тестов

API

```bash
make test-api
```

UI

```bash
make test-ui
```

Все тесты

```bash
make test-all
```

---

## Allure Report

Генерация отчета

```bash
make report
```

Открытие отчета

```bash
make open
```

Очистка результатов

```bash
make clean
```

---

## GitHub Actions

Проект поддерживает автоматический запуск тестов через GitHub Actions.

При каждом `push` выполняются:

* установка зависимостей;
* запуск тестов;
* формирование результатов выполнения.

---

## Особенности проекта

* разделение API и UI компонентов;
* переиспользуемый BaseAPI;
* переиспользуемый BasePage;
* использование `requests.Session`;
* модели данных на Pydantic;
* генерация тестовых данных;
* единая точка запуска тестов через Makefile;
* поддержка Allure Report;
* настройка CI через GitHub Actions.

---

## Планы по развитию

* публикация Allure Report в GitHub Actions;
* сохранение истории запусков Allure;
* расширение UI покрытия;
* Docker;
* улучшение CI/CD pipeline.

---

## Автор

**Vitalii (@pbolevoi)**

GitHub: github.com/pbolevoi
