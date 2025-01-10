from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random
import korean_age_calculator as kac


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
    zod = ["🐒 Monkey 원숭이띠","🐓 Rooster 닭띠","🐕 Dog 개띠","🐖 Pig 돼지띠","🐀 Rat 쥐띠","🐂 Ox 소띠","🐅 Tiger 호랑이띠","🐇 Rabbit 토끼띠","🐉 Dragon 용띠","🐍 Snake 뱀띠","🐎 Horse 말띠","🐐 Goat 양띠"]
    
    pool ={
   	 0: "안재영",
   	 1: "조성근",
   	 2: "배형균",
    	 3: "강현룡",
    	 4: "전희진",
    	 5: "권오준",
   	 6: "조민규",
   	 7: "백지원",
   	 8: "서민혁"
           }
     
    speaker = pool[random.randint(0,8)]
    kage = kac.how_korean_age(year_of_birth = birth_date.year)
    
    if birth_date.month == 1 or (birth_date.month == 2 and birth_date.day < 4):
        zod_year = birth_date.year-1
    else:
        zod_year = birth_date.year
    agezod = zod[int(zod_year)%12]
    
    if (today.month,today.day)>=(birth_date.month,birth_date.day):
        age = age
        bday_chek = "네"
    else:
        age = age - 1
        bday_chek = "아니요"
    
    return {
            "birthday": birthday,
            "age": f"{age}살  -  한국나이는 : {kage} 살  -   당신의 띠는: {agezod}    -  발표자는 : {speaker}",
            "kage": str(kage),
	    "speaker":f"{speaker} 입니다",
	    "zodiac": agezod,
 	    #"만나이": str(man_age),
            "basedate": str(today),
            #"bdaypass": bday_chek ,
            "message": "Age calculated successfully!"

            }
