from django.db import models
from django.contrib.auth.models import User
from pytils.translit import slugify
from django.urls import reverse


class Tag(models.Model):
    """Модель тегов"""

    name = models.CharField(max_length=256)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        """Переопределение метода"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    """Модель категорий"""

    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):
    """Модель статей"""

    title = models.CharField(max_length=512, blank=False)
    text: str = models.TextField()
    # poster = RichTextUploadingField()
    slug = models.SlugField(max_length=512, null=True, blank=True, unique=True,
                            db_index=True)
    datetime = models.DateTimeField(auto_now=True)
    views = models.IntegerField(null=True, blank=True, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='Tags')

    class Meta:
        verbose_name_plural = 'Статьи'
        ordering = ['-datetime']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        """Переопределение метода"""
        self.slug = slugify(self.title)
        self.text = self.text.replace(
            '<br />', '\n'
        ).replace(
            '</pre>', '</code></pre>'
        ).replace('<pre>', '<pre><code>')
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        """Переопределение метода"""
        return reverse('post', kwargs={'post_slug': self.slug})


class Comment(models.Model):
    """Модель комментариев"""

    text = models.TextField(blank=False)
    datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Комменты'

    def __str__(self):
        return self.author
