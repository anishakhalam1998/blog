from django.urls import reverse, resolve

class TestUrls:
    def test_post_list_url(self):
        path = reverse('post_list')
        assert resolve(path).view_name == 'post_list'
    
    def test_post_detail_url(self):
        path = reverse('post_detail', kwargs={'pk': 1})  # Assuming pk is 1 for this test
        assert resolve(path).view_name == 'post_detail'
    
    def test_post_create_url(self):
        path = reverse('post_create')
        assert resolve(path).view_name == 'post_create'
    
    def test_post_update_url(self):
        path = reverse('post_update', kwargs={'pk': 1})  # Assuming pk is 1 for this test
        assert resolve(path).view_name == 'post_update'
    
    def test_post_delete_url(self):
        path = reverse('post_delete', kwargs={'pk': 1})  # Assuming pk is 1 for this test
        assert resolve(path).view_name == 'post_delete'