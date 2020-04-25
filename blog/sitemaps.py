from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.9
	changefreq = 'daily'

	def items(self):
		return ['core:home','core:about','core:contact','blog:blog','events:events_list']

	def location(self, item):
		return reverse(item)
