# 나이계산기
- 만나이 연나이 한국식나이 띠를 알려드립니다.
### Use
- https://acalc.jacob53.shop

### Reference
- https://docs.python.org/ko/3.10/library/datetime.html


### DEV
```
$ pyenv global
3.10.12
# $ python -m venv venv
$ source venv/bin/activate
# $pip install -r requirements.txt
$ uvicorn api.index:app --reload
```

### Postgresql
```
create view view_select_table
as
select 
    lunch_menu.menu_name AS menu,
    member.name AS ename,
    lunch_menu.dt
FROM member
INNER JOIN lunch_menu 
ON member.id = lunch_menu.member_id
ORDER BY lunch_menu.dt desc;
```