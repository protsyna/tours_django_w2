```
========================
Author: Zinoviy PROTSYNA
Date: 12 May 2020
========================
```

# Content
- [How to run project](#how-to-run-project)
- [Project overview](#project-overview)
- [Additional information](#additional-information)
- [Project steps](#project-steps)
---


# How to run project

1. Create virtual environment 

   example:

   `$ virtualenv --python==python3.6 venv`

1. Activate virtual environment 

   example:

   `$ source venv/bin/activate`

1. Install libraries from file `requirements.txt`

   `(venv) $ pip install -r requirements.txt`

1. If need You can add env variable from .env file

   See example in file `.env.example`

   `export $(grep -v '^#' .env | xargs)`
   
   If Yoy want - You can check export .env file:
   
   `env | grep DJANGO`

1. Run project

   `(venv) $ python stepik_tours/manage.py runserver 8000`

1. Test on browser
    
    Open next urls:
    - [Main page](http://localhost:8000/)
    - [Departure page](http://localhost:8000/departure/msk)
    - [Tour page](http://localhost:8000/tour/1)

1. When this project is running - You can run tests from test/test.py
 
   In other console (need library **requests**):

   `$ python test/test.py`

   If all is well, then you will get this answer:
   
   ```
   ----------------------------------------------------------------------
   Ran 6 tests in 0.040s
   
   OK
   ```
   ---

1. You can check code with flake8 (* for Developers)

   `(venv) $ flake8 stepik_tours/`
    
   and
    
   `(venv) $ flake8 test/`

# Project overview

#### Краткое описание проекта (общее для первого и второго модуля)

В первых двух модулях нужно выполнить проект сайта про путешествия (проект по бронированию туров).

Верстка и готовый набор данных для этого проекта предоставляются.

#### Главная страница

В меню выводится список направлений, при клике на направление мы переходим на страницу направления.

Заголовок, подзаголовок и описание нужно будет вывести на первом экране.

Рекомендуемые предложения выводятся в цикле, у каждого указывается картинка, название, дата, описание, цена.
При клике на карточку мы переходим на страницу тура.

![Макет главной страницы](img/main_page.png "главная страница")

#### Список по направлению

На странице направления выводится заголовок.

Для получения данных нужно отфильтровать все туры, оставив только те, у которых destination=destination.

В подзаголовке выводится количество найденного, максимальные и минимальные значения.

Найденные предложения выводятся в цикле, у каждого указывается картинка, название, дата, описание, цена.
При клике на карточку мы переходим на страницу тура.

![Макет списка туров по направлению](img/list_of_way_page.png "список туров по направлению")

#### Страница тура

Выведите в заголовке название локации и количество звезд.

Выведите в подзаголовке страну, длительность.

Выведите изображение, описание.

Добавьте кнопку, которая будет вести в ваши личные сообщения или на гугл-форму или на сторонний сайт.

![Макет страницы туров](img/list_of_tour_page.png "список туров")

---


# Additional information

[Посмотрите макеты проекта здесь: https://academy.stepik.org/flask-projects](https://academy.stepik.org/flask-projects)

Скачайте исходники для верстки здесь:
- http://www.cssdesk.com/zHL6n
- http://www.cssdesk.com/gmmUZ
- http://www.cssdesk.com/pQqan

Получите данные здесь (опционально):
https://github.com/kushedow/flask-html/blob/master/Project%201/data.py

---


# Project steps

#### 1. Скопируйте мок-данные, объявите переменную tours

https://github.com/kushedow/flask-html/blob/master/Project%201/data.py

#### 2. Выведите информацию о туре

- изучите мок-данные,
- передайте нужные данные в шаблон,
- вставьте детальную информацию о туре в шаблон,
- обратите внимание на вывод нужного количества звездочек,
- проверьте результат.

#### 3. Доработайте главную страницу: выведите список туров

- изучите мок-данные,
- передайте нужные данные в шаблон,
- отредактируйте шаблон, выведите 6 случайных туров 
- проверьте результат.

#### 4. Доработайте страницу направления: выведите список туров

- изучите мок-данные,
- напишите логику фильтрации туров по departure=departure,
- передайте нужные данные в шаблон,
- отредактируйте шаблон: выведите направление, список туров,
- проверьте результат.

#### 5. Вынесите повторяющиеся части шаблона в base.html

- шапку сайта,
- подвал сайта.

#### 6. Исправьте те ошибки, которые нашел у вас в коде flake8

#### 7. Сделайте коммит на Github, скопируйте ссылку в поле ниже!

Если вы использовали Github для публикации кода прошлой недели, пожалуйста, создайте новый репозиторий для новой версии проекта!
