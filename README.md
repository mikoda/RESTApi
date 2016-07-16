# REST APi (DRF)

- зарегистрировать пользователя
    Method: POST 
    Path: http://[hostname]/api/auth/register/ 
    request: email, password

- авторизоваться пользователем и получить токен
    Method: POST 
    Path: http://[hostname]/api/auth/login/
    request: email, password
    response: auth_token

- получить его профайл по токену
    Method: GET
    Path: http://[hostname]/api/auth/me/
    Headers: Authorization - Token <auth_token>

- создавать пост пользователя (через токен) (Title, Body)
    Method: POST
    Path: http://[hostname]/api/post/add/
    request: title, body
    Headers: Authorization - Token <token>

- получать список постов пользователя через токен
    Method: GET
    Path: http://[hostname]/api/post/my/
    Headers: Authorization - Token <token>

-получать список всех постов через токен, желательно с пагинацией
    Method: GET
    Path: http://[hostname]/api/post/ (pagination: ?page=2)
    Headers: Authorization - Token <token>

-поиск постов
    Method: GET
    Path: http://[hostname]/api/post/?search=<value>
    Headers: Authorization - Token <token>
    
-профайл пользователя должен быть кастомный - без username, основные поля авторизации email/password: DONE!
