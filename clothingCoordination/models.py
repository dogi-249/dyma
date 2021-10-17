from django.db import models

class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'

from django.db import models


""" カテゴリーモデル """
class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name

""" Blogモデル """122
class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')

    """ プラスアルファ """
    category = models.ForeignKey(
                    Category, verbose_name='カテゴリー',
                    on_delete=models.PROTECT
               )
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'

    """ Tagモデル"""
class Tag(models.Model):
    name = models.CharField('タグ', max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')
    category = models.ForeignKey(
                    Category, verbose_name='カテゴリー',
                    on_delete=models.PROTECT
               )

    """ Tagモデルと紐づけ """
    tag = models.ManyToManyField(Tag, verbose_name='タグ')

    """ Blogモデル内の要素と紐づけ """
    relation = models.ManyToManyField('self', verbose_name='関連', blank=True, null=True)
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'
