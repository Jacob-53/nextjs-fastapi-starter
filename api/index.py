from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이를 포함한 JSON 응답
    """
    today = date.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    age = today.year - birth_date.year
    zod=["말띠","양띠","원숭이띠","닭띠","개띠","돼지띠","쥐띠","소띠","호랑이띠","토끼띠","용띠","뱀띠"]
    agezod=zod[int(birth_date.year)%12]
    if (today.month,today.day)>=(birth_date.month,birth_date.day):
        age = age
        bday_chek = "네"
    else:
        age = age - 1
        bday_chek = "아니요"
    
    return {
            "birthday": birthday,
            "age": str(age),
	    "띠": agezod
            #"만나이": str(man_age),
            "basedate": str(today),
            "생일이 지났습니까?": bday_chek ,
            "message": "Age calculated successfully!"
            }
