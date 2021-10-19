from django.db import models

class Location(models.Model):
  location = models.CharField(max_length=200)

  def saveLocation(self):
    self.save()

  @classmethod
  def deleteLocation(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def updateLocation(cls, id, locaUpdate):
    cls.objects.filter(id=id).update(location=locaUpdate)

  def __str__(self):
    return self.location

class Category(models.Model):
  category = models.CharField(max_length=200)

  def saveCategory(self):
    self.save()

  @classmethod
  def deleteCategory(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def updateCategory(cls, id, cateUpdate):
    cls.objects.filter(id=id).update(category=cateUpdate)

  def __str__(self):
    return self.category

class Image(models.Model):
  image = models.ImageField(upload_to='photos')
  image_name =  models.CharField(max_length=200)
  image_description = models.TextField()
  location_id = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  date_upload = models.DateTimeField(auto_now_add=True)

  def save_image(self):
    self.save()

  def delete_image(self, id):
    self.objects.filter(id=id).delete()

  def update_image(self, id, imagechange):
    self.objects.filter(id = id).update(image = imagechange)

  def get_images_by_id(self, id):
    try:
      image = self.objects.get(id=id)
      return image
    except Image.DoesNotExist:
      print('Image does not exist')

  def search_image(self, category):
    image_search = self.objects.filter(category_id__category__icontains=category)
    return image_search

  def filter_by_location(self, location):
    image_location_search = self.objects.filter(location_id__location__icontains=location)
    return image_location_search

  class Meta:
    ordering = ['date_upload']
    
  def __str__(self):
    return self.image_name