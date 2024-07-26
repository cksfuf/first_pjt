# Django

1. 프로젝트 생성
```bash
django-admin startproject {pjt_name} .
```

2. 가상환경 생성
```bash
python -m venv venv
```

3. 가상환경 활성화
```bash
source venv/Scripts/activate
```

4. 가상환경 내부에 django 설치
```bash
pip install django
```

5. 서버 실행 (종료 : `ctrl + c`)
```bash
python manage.py runserver
```

6. 앱생성
```bash
django-admin startapp {app_name}
```

7. 앱등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...
    '{app_name}'
]
```


# manage.py 활용
>  Django 프로젝트를 관리하는 데 필요한 다양한 명령어를 실행할 수 있는 스크립트.
1. 서버 실행
- python manage.py runserver
- 개발 서버를 실행하는 명령어
- http://127.0.0.1:8000/ 이게 나오면 ctrl + 클릭
- ctrl + c 누르면 꺼짐.
