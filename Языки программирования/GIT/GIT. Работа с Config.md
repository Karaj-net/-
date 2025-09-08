### **Как работает `git config`**  
Команда `git config` управляет **настройками Git** (глобальными, локальными и системными). Она изменяет параметры в конфигурационных файлах, которые влияют на поведение Git.  

---

## **1. Уровни конфигурации**  
| Уровень | Файл | Команда |  
|---------|------|---------|  
| **Локальный** (для текущего репозитория) | `.git/config` | `git config` |  
| **Глобальный** (для пользователя) | `~/.gitconfig` или `~/.config/git/config` | `git config --global` |  
| **Системный** (для всех пользователей) | `/etc/gitconfig` | `git config --system` |  

**Приоритет:** Локальный > Глобальный > Системный.

---

## **2. Основные команды**  

### **Просмотр настроек**  
```bash
git config --list          # Показать все текущие настройки
git config user.name       # Показать имя пользователя
git config --global --list # Показать глобальные настройки
```

### **Установка параметров**  
```bash
git config user.name "Ваше Имя"           # Локально
git config --global user.email "email@example.com"  # Глобально
git config --global core.editor "code --wait"  # Установить VS Code как редактор
```

### **Удаление параметров**  
```bash
git config --unset user.name          # Удалить локальное имя
git config --global --unset user.email # Удалить глобальный email
```

---

## **3. Часто используемые настройки**  

### **Основные**  
```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
git config --global init.defaultBranch main  # Установить ветку по умолчанию
```

### **Настройка редактора**  
```bash
git config --global core.editor "nano"       # Для Linux/macOS
git config --global core.editor "notepad"    # Для Windows
git config --global core.editor "code --wait" # Для VS Code
```

### **Псевдонимы (aliases)**  
```bash
git config --global alias.st "status -s"     # Короткий статус
git config --global alias.lg "log --oneline --graph --all"
```
Теперь можно использовать:  
```bash
git st  # Вместо git status -s
git lg  # Красивое дерево коммитов
```

### **Кеширование учётных данных** (чтобы не вводить пароль)  
```bash
git config --global credential.helper cache  # На 15 минут
git config --global credential.helper "store --file ~/.git-credentials"  # Навсегда (осторожно!)
```

---

## **4. Где хранятся настройки?**  
- **Локальные**: `.git/config` (в папке репозитория).  
- **Глобальные**:  
  - Linux/macOS: `~/.gitconfig`  
  - Windows: `C:\Users\ВашПользователь\.gitconfig`  
- **Системные**: `/etc/gitconfig` (требует прав администратора).  

**Пример файла `~/.gitconfig`:**  
```ini
[user]
    name = John Doe
    email = john@example.com
[alias]
    st = status -s
    lg = log --oneline --graph --all
[core]
    editor = code --wait
```

---

## **5. Проверка настроек**  
```bash
git config --get user.name    # Показать имя
git config --get-regexp alias # Показать все псевдонимы
```

---

## **6. Как использовать в Obsidian?**  
Создайте заметку **Git Config** и добавьте:  
````markdown
```bash
# Установка имени/email
git config --global user.name "Ваше Имя"
git config --global user.email "ваш@email.com"

# Псевдонимы
git config --global alias.st "status -s"
```
**Файлы конфига:**  
- Глобальный: `~/.gitconfig`  
- Локальный: `.git/config`
````

**Теги:** `#git #настройки #cheatsheet`  

Теперь у вас есть шпаргалка по настройке Git! 🛠️