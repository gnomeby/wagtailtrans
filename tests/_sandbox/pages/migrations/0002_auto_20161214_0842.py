# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 08:42
from django.db import migrations


def create_page_structure(apps, schema_editor):
    HomePage = apps.get_model('pages', 'HomePage')
    Language = apps.get_model('wagtailtrans', 'Language')
    SiteRootPage = apps.get_model('wagtailtrans', 'TranslatableSiteRootPage')
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')

    # Delete the default root- and homepage
    Page.objects.filter(id=2).delete()

    lang, created = Language.objects.get_or_create(
        code='en',
        is_default=True,
        position=0,
        live=True
    )

    # Create a new rootpage
    trans_root = SiteRootPage.objects.create(
        title='translation root',
        slug='translation-root',
        content_type=ContentType.objects.get_for_model(SiteRootPage),
        path='00010001',
        depth=2,
        numchild=1,
        url_path='/',
    )

    HomePage.objects.create(
        title='homepage',
        subtitle='a sample homepage',
        slug=lang.code,
        language=lang,
        content_type=ContentType.objects.get_for_model(HomePage),
        path='000100010001',
        depth=3,
        numchild=0,
        url_path='/%s/' % lang.code,
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=trans_root, is_default_site=True)


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('wagtailtrans', '0006_auto_20161212_2020')
    ]

    operations = [
        migrations.RunPython(create_page_structure),
    ]
