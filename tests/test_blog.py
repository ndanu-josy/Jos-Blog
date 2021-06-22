import unittest
from app.models import Blog,User
from app import db


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_jos= User(username='toto', password='1233', email='mosonik@gmail.com', id=1)
        self.new_blog = Blog( title_blog='Encapusation', description='Testing', posted = 'today', user_id=self.user_jos.id)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title_blog, 'Encapusation')
        self.assertEquals(self.new_blog.description, 'Testing')
        self.assertEquals(self.new_blog.user_id, self.user_jos.id)
        self.assertEquals(self.new_blog.posted, 'today') 

    def test_save_blog(self):
        self.new_blog.saveBlog()
        self.assertTrue(len(Blog.query.all()) > 0)

    