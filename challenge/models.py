import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.TextField("name")
    picture = models.URLField("picture")


class Article(models.Model):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4,
                          editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.TextField("category")
    title = models.TextField("title")
    summary = models.TextField("summary")
    firstParagraph = models.TextField("firstParagraph")
    body = models.TextField("body")
