# Django

1. 프로젝트 생성
- 폴더 생성 후 들어가서 code로 열기
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

5. 앱생성
```bash
django-admin startapp {app_name}
```

6. git init 관리
- git init 후 구글에 gitignore.io 검색
- python, VisualStudioCode, windows, macOS, Django 생성
- code로 돌아와 .gitignore 파일 만들고 생성된 코드 붙여넣기

7. 서버 실행(서버 종료는 ctrl+c)
- 실행후 나오는 주소 (예를들어 http://127.0.0.1:8000/ 에 ctrl+클릭하면 이동됨.)
```bash
python manage.py runserver
```

8. templates 폴더 생성.
- html 파일 관리 장소
- 5번에서 생성한 폴더에 마우스 우클릭 하고 templates 폴더 생성.

9. app 등록
- 1번에서 생성한 폴더의 setting.py 찾아 들어가기
- 33번 줄 INSTALLED_APPS에 우리가 만든 train_app 등록하기
- 앱등록 (내가 만든 앱은 `first_app`)
```python
INSTALLED_APPS = [
    ...
    'first_app'
]
```

10. urls.py 경로 매핑
- 1번에서 생성한 firt_pjt의 urls.py 들어가기
- 18번 줄 아래 from first_app import views(first_app을 지정해주기)
- 20번 줄의 urlpatterns에 코드 작성
- `path('', views.root)`: root 라는 기본 홈페이지 지정
- `path('index/', views.index)`: index 요청이 들어오면 views.index로 처리.

```python
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('index/', views.index),
]
```

11. 로직 정의
- 애플리케이션에서 요청을 처리하는 로직을 정의하는 파일
- 5번에서 생성한 앱(first_app)의 views.py 파일 찾아 들어가기
- 여기에 urls.py 에서 지정한 로직정의하는 함수 만들기
```python
def root(request):
    return render(request, 'root.html')

def index(request):
    return render(request, 'index.html')
```

12. html 생성
- 위 로직에서 정의한 html 파일 만들기
- 5번에서 생성한 앱(first_app)의 templates폴더에 html파일 생성
- 파일 이름 은 .html 형식 `root.html`
- ! 탭 누르면 형태 완성되고, body 아래에 보여주고싶은 값 작성({{result}})
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{result}}</h1>
</body>
</html>
```

13. 결과 확인
- http://127.0.0.1:8000/ 에 ctrl+클릭 하여 결과 확인