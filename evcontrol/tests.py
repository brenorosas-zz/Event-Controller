from django.test import TestCase
from .models import *
from .forms import *
from django.urls import reverse
import datetime
# Create your tests here.

#Models
class EventTestCase(TestCase):

    def setUp(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()

        Event.objects.create(
            title = 'titleTest',
            slug = 'slugTest',
            description = 'descriptionTest',
            user = us
        )
    def test_retorno_str(self):
        ev1 = Event.objects.get(title = 'titleTest')
        self.assertEquals(ev1.__str__(), 'titleTest')

class GuestTestCase(TestCase):
    
    def setUp(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()

        ev = Event.objects.create(
            title = 'titleTest',
            slug = 'slugTest',
            description = 'descriptionTest',
            user = us
        )

        Guest.objects.create(
            name = 'testName',
            email = 'test@gmail.com',
            event = ev
        )
    def test_retorno_str(self):
        g = Guest.objects.get(name = 'testName')
        self.assertEquals(g.__str__(), 'testName')

#views
class LoginViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('login')) 
        self.assertTemplateUsed(response, 'login.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_post(self):
        u = User.objects.create(username="test")
        u.set_password('test')
        u.save()
        response = self.client.post(reverse('login'), data = {'username' : 'test', 'password' : 'test'}, follow = True)
        self.assertRedirects(response=response, expected_url = reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)
        u.delete()

class HomeViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')

class LogoutViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('logout'))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')

class RegisterViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response,'base.html')
        self.assertTemplateUsed(response,'register.html')
    
    def test_post(self):
        response = self.client.post(reverse('register'), data={'username' : 'test', 'password1' : 'Axksd32x', 'password2' : 'Axksd32x'}, follow = True)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')
        self.assertRedirects(response=response, expected_url = reverse('home'))

class SettingsViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('settings'))
        self.assertEquals(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse('settings'))
        self.assertTemplateUsed(response,'base.html')
        self.assertTemplateUsed(response,'settings.html')

    def test_post(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('settings'), {'old_password':'test' , 'new_password1' : 'Axksd32x', 'new_password2' : 'Axksd32x'}, follow=True)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')
        self.assertRedirects(response=response, expected_url = reverse('login'))
        self.client.logout()
        us.delete()

class EventsViewTestCase(TestCase):
    def test_status(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('events'))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'events.html')
        self.assertEquals(response.status_code, 200)
        self.client.logout()
        us.delete()

class AddEventViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('addevent'))
        self.assertEquals(response.status_code, 200)
    def test_template_used(self):
        response = self.client.get(reverse('addevent'))
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'addevent.html')
    def test_post(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('addevent'), {'title' : 'testEvent', 'slug' : 'testSlug', 'description' : 'testDescription', 'date' : '2021-04-03'}, follow=True)
        self.assertTemplateUsed(response,'base.html')
        self.assertTemplateUsed(response,'events.html')
        self.assertRedirects(response=response, expected_url = reverse('events'))
        self.client.logout()
        us.delete()

class addGuestViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('addguest'))
        self.assertEquals(response.status_code, 200)
    def test_post(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()
        self.client.login(username='test', password='test')
        ev = Event.objects.create(
            title = 'testEvent',
            slug = 'testEvent',
            description = 'testDescription',
            user = us
        )
        ev.save()
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('addguest'), {'name' : 'nameTest', 'email' : 'testemail@hotmail.com', 'event' : ev}, follow=True)
        self.assertTemplateUsed(response,'base.html')
        self.assertTemplateUsed(response,'addguest.html')
        self.client.logout()
        us.delete()
        ev.delete()

class GuestsViewTestCase(TestCase):
    def test_status(self):
        us = User.objects.create(username = 'test')
        us.set_password('test')
        us.save()
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('guests'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('guests.html')
        self.assertTemplateUsed('base.html')
        self.client.logout()
        us.delete()

class EventFormTestCase(TestCase):
    def test_field_labels(self):
        form = EventForm()
        self.assertTrue(form.fields['title'].label == 'Title')
        self.assertTrue(form.fields['description'].label == "Description")
        self.assertTrue(form.fields['slug'].label == "Slug")
        self.assertTrue(form.fields['date'].label == "Date")

class GuestFormTestCase(TestCase):
    def test_field_labels(self):
        form = GuestForm()
        self.assertTrue(form.fields['name'].label == 'Name')
        self.assertTrue(form.fields['email'].label == "Email")
        self.assertTrue(form.fields['event'].label == "Event")