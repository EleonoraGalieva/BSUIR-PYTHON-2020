from django.test import TestCase
from .models import Author, Article
from django.utils import timezone


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(author_name="Kate", author_organisation="BBC")

    def test_author_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('author_name').verbose_name
        self.assertEquals(field_label, "Author's name")

    def test_author_organisation_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("author_organisation").verbose_name
        self.assertEquals(field_label, "Author's organisation")

    def test___str__(self):
        author = Author.objects.get(id=1)
        expected_str = author.author_name
        self.assertEqual(expected_str, author.__str__())


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(article_title="Some title", article_text="Some text", pub_date=timezone.now())

    def test_article_title(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field("article_title").verbose_name
        self.assertEqual(field_label, "Article name")

    def test_article_text(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field("article_text").verbose_name
        self.assertEqual(field_label, "Article text")

    def test_article_type(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field("type").verbose_name

    def test___str__(self):
        article = Article.objects.get(id=1)
        expected_str = article.article_title
        self.assertEqual(expected_str, article.__str__())




