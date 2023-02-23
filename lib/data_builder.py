
from faker import Faker
import random
import json

faker = Faker('ko_KR')

descriptions = [
    "VIP 고객",
    "신규 가입자",
    "재구매 고객",
    "할인 이벤트 참여자",
    "불만 제기한 고객",
    "만족도 조사 참여자",
    "추천인 고객",
    "평가 리뷰 작성자",
    "최근 구매한 고객",
    "정기 구매자"
]

customers = []

for i in range(10):
    customer = {
        "이름": faker.name(),
        "이메일": faker.email(),
        "전화번호": faker.phone_number(),
        "주소": {
            "도시": faker.city(),
            "구": faker.borough(),
            "동": faker.street_name(),
            "우편번호": faker.postcode()
        },
        "설명": random.choices(descriptions, k=2)
    }
    customers.append(customer)

print(json.dumps(customers, ensure_ascii=False, indent=2))



