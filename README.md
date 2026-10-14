# Warehouse

Django-застосунок для перегляду каталогу товарів.

## Запуск у Docker

Потрібні Docker і Docker Compose v2.

```bash
cd warehouse
cp .env.example .env
docker compose up --build
```

Застосунок буде доступний за адресою <http://localhost:8000/>.
Міграції виконуються автоматично при старті контейнера.
Docker запускає Django з параметром `--insecure`, щоб static-файли (CSS)
працювали навіть при `DJANGO_DEBUG=0`.

База SQLite зберігається в Docker volume `django_data` і не втрачається після
перезапуску контейнера.

Зупинка:

```bash
docker compose down
```

Зупинка з видаленням бази даних:

```bash
docker compose down -v
```

## Налаштування

Значення зберігаються у `warehouse/.env`:

| Змінна | Призначення |
| --- | --- |
| `DJANGO_SECRET_KEY` | секретний ключ Django |
| `DJANGO_DEBUG` | режим debug (`1`, `true`, `yes`) |
| `DJANGO_ALLOWED_HOSTS` | дозволені хости через кому |

Для створення адміністратора:

```bash
docker compose exec web python manage.py createsuperuser
```

Основні сторінки:

- `/` — головна;
- `/products/` — каталог товарів;
- `/admin/` — адміністративна панель.

## Локальний запуск без Docker

```bash
cd warehouse
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
