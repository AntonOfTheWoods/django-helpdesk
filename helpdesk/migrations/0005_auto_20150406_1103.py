# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('helpdesk', '0004_initial_data_import'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='email_box_file_glob',
            field=models.CharField(help_text='If using email files, what files do you want to process? The file must be found with a normal "glob" and must be present in a subdirectory of the MEDIA_ROOT', max_length=250, null=True, verbose_name='Email File Glob', blank=True),
        ),
        migrations.AddField(
            model_name='queue',
            name='site',
            field=models.ForeignKey(default=1, to='sites.Site', help_text='Site to associate queue to'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='queue',
            name='email_address',
            field=models.EmailField(help_text='All outgoing e-mails for this queue will use this e-mail address. If you use IMAP or POP3, this should be the e-mail address for that mailbox.', max_length=254, null=True, verbose_name='E-Mail Address', blank=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='email_box_type',
            field=models.CharField(choices=[(b'pop3', 'POP 3'), (b'imap', 'IMAP'), (b'file', 'FILE')], max_length=5, blank=True, help_text='E-Mail server type for creating tickets automatically from a mailbox - both POP3, IMAP and FILE are supported.', null=True, verbose_name='E-Mail Box Type'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='submitter_email',
            field=models.EmailField(help_text='The submitter will receive an email for all public follow-ups left for this task.', max_length=254, null=True, verbose_name='Submitter E-Mail', blank=True),
        ),
        migrations.AlterField(
            model_name='ticketcc',
            name='email',
            field=models.EmailField(help_text='For non-user followers, enter their e-mail address', max_length=254, null=True, verbose_name='E-Mail Address', blank=True),
        ),
    ]
