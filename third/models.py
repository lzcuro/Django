from django.db import models

class Restaurant(models.Model): # Restaurant 라는 상점을 나타내는 모델을 정의
    name = models.CharField(max_length=30)  # 이름
    address = models.CharField(max_length=200)  # 주소

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)  # 저장된 레코드 수정 시 수정 시각

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # 식당 모델과의 릴레이션 정의, 식당이 추가되면 이를 key로 받아 id가 설정됨
    # on_delete CASCADE로 지정하면 식당이 삭제되면 같이 삭제된다. >> 없는 식당에 review 하는걸 방지
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)
