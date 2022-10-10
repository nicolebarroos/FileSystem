from django.db import models


class Files(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=150, blank=False, null=False)
    file = models.FileField(verbose_name='Arquivos', upload_to='files/', null=True, blank=True)

    def __str__(self):
        return 'Arquivos'

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'


class FileSystem(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    directory = models.ManyToManyField('self', null=True, related_name='self', blank=True)
    files = models.ManyToManyField(Files)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Gerenciador de arquivo'
        verbose_name_plural = 'Gerenciador de arquivos'


