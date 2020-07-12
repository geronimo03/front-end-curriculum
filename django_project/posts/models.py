from django.db import models
from django.urls import reverse
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Post(models.Model):
    class Meta:
        ordering = ['-created_at']

    POST_TYPES = [
        (0, "메인"),
        (1, "이달의테마"),
        (2, "사용자선택")
    ]
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, default=0)
    highlight = models.TextField(default=None)

    title = models.CharField(max_length=200,
                             verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    view_count = models.IntegerField(default=0,
                                     verbose_name="조회수")
    _type = models.PositiveSmallIntegerField(choices=POST_TYPES,
                                             verbose_name="게시글타입")
    image = models.ImageField(upload_to="posts/img", default="posts/default/default_post_img.jpg")

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="업데이트시간")

    def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, full=True, **options)
        self.highlighted = highlight(self.code, formatter)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:show', args=[self.pk])
