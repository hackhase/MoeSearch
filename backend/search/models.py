from django.db import models

class NetdiskResource(models.Model):
    title = models.TextField(blank=True, null=True, verbose_name="标题")
    download_url = models.TextField(verbose_name="链接")
    category = models.CharField(max_length=50, default='netdisk', verbose_name="分类")
    desc = models.TextField(blank=True, null=True, verbose_name="描述")
    source_site = models.CharField(max_length=100, blank=True, null=True, verbose_name="来源")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="时间")

    class Meta:
        # 🎯 关键：指定你的旧表名，这样 Django 就不会新建表了
        db_table = 'netdisk_netdiskresource'
        managed = False # 🎯 关键：告诉 Django 不要去管理（修改）这张表的结构
        ordering = ['-id']