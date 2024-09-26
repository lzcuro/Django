from django.db import models


class Post(models.Model): # Post 라는 게시글을 나타내는 모델을 정의
    title = models.CharField(max_length=30)  # 30자 이하의 문자열
    content = models.TextField()  # 긴 문자열

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)  # 저장된 레코드 수정 시 수정 시각

    # num_stars = models.IntegerField()  # 숫자 필드는 이렇게 선언한다.
