# 🛠️ **Установка и настройка**

* Создание папки виртуального окружения
  ```bash 
  python.exe -m venv venv
  ```
* Активация папки:
  ```bash 
  .\venv\Scripts\activate
  ```
* Настраиваем *interpreter*
  ```bash
  python.exe -m pip install --upgrade pip
  ```

### *Зависимости*

* Установить зависимости из requirements.txt
  ```bash
  python.exe -m pip install -r requirements.txt
  ```
* Удалить все пакеты
  ```bash
  python.exe -m pip freeze > unins | pip uninstall -y -r unins 
  rm unins
  ```

### **Сохранить requirements:**
  ```bash
  python.exe -m pip list --not-required --format=freeze > requirements.txt
  ```