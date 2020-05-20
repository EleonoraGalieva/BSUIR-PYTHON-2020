from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase, SimpleTestCase, Client, RequestFactory
from .models import Author, Article
from django.utils import timezone
from django.urls import reverse, resolve
from .views import *
from .forms import UserCreationForm, AccountForm


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

    def test_was_published_recently(self):
        article = Article.objects.get(id=1)
        self.assertEqual(True, article.was_published_recently())


class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url = reverse("articles:login")
        self.assertEqual(resolve(url).func, login_method)

    def test_logout_url_is_resolved(self):
        url = reverse("articles:logout")
        self.assertEqual(resolve(url).func, logout_method)

    def test_home_url_is_resolved(self):
        url = reverse("articles:home")
        self.assertEqual(resolve(url).func, home)

    def test_register_url_is_resolved(self):
        url = reverse("articles:register")
        self.assertEqual(resolve(url).func, register)

    def test_myprofile_url_is_resolved(self):
        url = reverse("articles:my_profile")
        self.assertEqual(resolve(url).func, my_profile)

    def test_article_url_is_resolved(self):
        url = reverse("articles:article", args=['1'])
        self.assertEqual(resolve(url).func, show_article)

    def test_comment_url_is_resolved(self):
        url = reverse("articles:leave_comment", args=['1'])
        self.assertEqual(resolve(url).func, leave_comment)


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client(enforce_csrf_checks=True)
        pic = "prof_pic1.png"
        Article.objects.create(article_title="Title1", pub_date=timezone.now(), article_text="Text", article_pic=pic,
                               type="OTHER", id=1)
        Article.objects.create(article_title="Title2", pub_date=timezone.now(), article_text="Text", article_pic=pic,
                               type="TECH", id=2)
        Article.objects.create(article_title="Title3", pub_date=timezone.now(), article_text="Text", article_pic=pic,
                               type="BUSINESS", id=3)
        cls.user = User.objects.create_user(username='Kate', email='kate@gmail.com', password='kate98')
        cls.account = Account.objects.create(name="Kate J", email='kate@gmail.com', user=cls.user)
        cls.factory = RequestFactory()

    def test_home_page(self):
        data = {'latest_article_1': Article.objects.get(article_title="Title1"),
                'latest_article_2': Article.objects.get(article_title="Title2"),
                'latest_article_3': Article.objects.get(article_title="Title3")}
        home_url = reverse("articles:home")
        response = self.client.get(home_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_article_list_page(self):
        list = Article.objects.filter(type="OTHER")
        data = {'latest_articles_list': list, 'type_of_article': 'OTHER'}
        list_url = reverse("articles:articles_list", args=["OTHER"])
        response = self.client.get(list_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        login_url = reverse("articles:login")
        self.client.login(username='lfk', password='erj')
        response = self.client.post(login_url)
        self.assertEqual(response.status_code, 200)

    def test_login_with_user(self):
        login_url = reverse("articles:login")
        request = self.factory.get(login_url)
        request.user = self.user
        response = login_method(request)
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        logout_url = reverse("articles:logout")
        self.client.logout()
        response = self.client.post(logout_url)
        self.assertEqual(response.status_code, 302)

    def test_article_page(self):
        a = Article.objects.get(article_title="Title1")
        comments_list = {}
        article_url = reverse("articles:article", args=['1'])
        data = {'article': a}
        response = self.client.get(article_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_article_page_error(self):
        a = Article.objects.get(article_title="Title1")
        Article.objects.filter(id=1).delete()
        comments_list = {}
        article_url = reverse("articles:article", args=['1'])
        data = {'article': a}
        response = self.client.get(article_url, data=data)
        self.assertEqual(response.status_code, 404)

    def test_my_profile(self):
        my_profile_url = reverse("articles:my_profile")
        self.client.login(username='lfk', password='erj')
        response = self.client.post(my_profile_url, {'form': AccountForm()})
        self.assertEqual(response.status_code, 302)

    def test_my_profile_with_user(self):
        my_profile_url = reverse("articles:my_profile")
        request = self.factory.get(my_profile_url)
        request.user = self.user
        response = my_profile(request)
        self.assertEqual(response.status_code, 200)

    def test_comments(self):
        comments_url = reverse("articles:leave_comment", args=['1'])
        request = self.factory.get(comments_url)
        request.user = self.user
        response = leave_comment(request, 1)
        self.assertEqual(response.status_code, 302)

    def test_comments_error(self):
        comments_url = reverse("articles:leave_comment", args=['1'])
        request = self.factory.get(comments_url)
        request.user = AnonymousUser()
        response = leave_comment(request, 1)
        self.assertEqual(response.status_code, 302)
