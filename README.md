## Запуск проекта

### 1. Запуск контейнеров
```
cd /workspaces/codespaces-blank/project_practice
docker-compose up
```
### 2. Настройка окружения для Playwright
```
cd /workspaces/codespaces-blank/project_practice/playwright/
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
playwright install
```
### 3. Запуск тестов Playwright
```
pytest test.py -v
```
### 4. Настройка окружения для Locust
```
cd /workspaces/codespaces-blank/project_practice/locust/
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```
### 5. Запуск тестов Locust
```
locust -f locustfile.py
```
## Требования
* Docker и Docker Compose
* Python (совместимая версия)
* Playwright
* Locust
* Установленные зависимости из requirements.txt
