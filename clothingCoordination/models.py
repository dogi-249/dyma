from django.db import models

from accounts.models import User


# Create your models here.
class coordinateInfo(models.Model):
    """服情報"""

    user_id = models.ForeignKey(User, on_delete=models.PROTECT)  # ユーザID
    coordinate_name = models.CharField(max_length=150)  # 名称
    image_path = models.URLField()  # 画像のパス
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時
    is_deleted = models.BooleanField(default=False)  # 削除フラグ
