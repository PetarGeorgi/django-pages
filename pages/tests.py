from django.test import SimpleTestCase
from django.urls import reverse

# l check that the two URLs for our website, the homepage and about page, both
# return HTTP status codes61 of 200, the standard response for a successful 
# http request
# testing the URL name for each page
# the correct templates–home.html and about.html–are used on each page and 
# that they display
# the expected content 


class HomepageTests(SimpleTestCase):
    def testing_url_exists_right_location(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        
    def testing_url_exist_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        
    def testing_template_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        
    def testing_template_containing(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>homepage</h1>") 
        
        
class AboutpageTests(SimpleTestCase):
    def testing_url_exists_right_location(self):
        response = self.client.get("/about/")
        self.assertEquals(response.status_code, 200)
        
    def testing_url_exist_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        
    def testing_template_name(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
        
    def testing_template_containing(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h2>About<h2>")
