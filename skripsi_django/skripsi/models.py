# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class ConAction(models.Model):
    con_action_id = models.IntegerField(primary_key=True)
    con_action_data = models.CharField(max_length=127L, blank=True)
    con_action_message = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'con_action'

class ConActionUserRole(models.Model):
    con_action_user_role_con_action_id = models.IntegerField()
    con_action_user_role_user_role_id = models.IntegerField()
    class Meta:
        db_table = 'con_action_user_role'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class File(models.Model):
    file_id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=255L)
    file_mime = models.CharField(max_length=63L, blank=True)
    class Meta:
        db_table = 'file'

class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=255L)
    project_url = models.CharField(max_length=255L, blank=True)
    project_description = models.TextField(blank=True)
    project_budget = models.BigIntegerField(null=True, blank=True)
    project_icon = models.CharField(max_length=45L, blank=True)
    project_is_active = models.CharField(max_length=1L)
    project_user = models.ForeignKey('User', null=True, blank=True)
    class Meta:
        db_table = 'project'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255L)
    migration = models.CharField(max_length=255L)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

class Sprint(models.Model):
    sprint_id = models.IntegerField(primary_key=True)
    sprint_name = models.CharField(max_length=127L)
    sprint_start_date = models.DateField(null=True, blank=True)
    sprint_end_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'sprint'

class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_title = models.CharField(max_length=127L)
    task_description = models.TextField(blank=True)
    task_point = models.IntegerField()
    task_creator_user = models.ForeignKey('User', null=True, blank=True)
    task_assign_user = models.ForeignKey('User', null=True, blank=True)
    task_create_datetime = models.DateTimeField(null=True, blank=True)
    task_start_datetime = models.DateTimeField(null=True, blank=True)
    task_end_datetime = models.DateTimeField(null=True, blank=True)
    task_estimate_hour = models.IntegerField(null=True, blank=True)
    task_project = models.ForeignKey(Project, null=True, blank=True)
    task_task_type = models.ForeignKey('TaskType', null=True, blank=True)
    task_is_end = models.CharField(max_length=1L)
    task_is_start = models.CharField(max_length=1L)
    task_progress = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'task'

class TaskComment(models.Model):
    task_comment_id = models.IntegerField(primary_key=True)
    task_comment_user = models.ForeignKey('User', null=True, blank=True)
    task_comment_task = models.ForeignKey(Task, null=True, blank=True)
    task_comment_text = models.TextField(blank=True)
    task_comment_datetime = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'task_comment'

class TaskCommentFile(models.Model):
    task_comment_file_task_comment = models.ForeignKey(TaskComment)
    task_comment_file_file = models.ForeignKey(File)
    class Meta:
        db_table = 'task_comment_file'

class TaskFile(models.Model):
    task_file_task = models.ForeignKey(Task)
    task_file_file = models.ForeignKey(File)
    class Meta:
        db_table = 'task_file'

class TaskSprint(models.Model):
    task_task = models.ForeignKey(Task, null=True, blank=True)
    sprint_sprint = models.ForeignKey(Sprint, null=True, blank=True)
    class Meta:
        db_table = 'task_sprint'

class TaskType(models.Model):
    task_type_id = models.IntegerField(primary_key=True)
    task_type_name = models.CharField(max_length=45L)
    task_type_color = models.CharField(max_length=10L)
    task_type_icon = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'task_type'

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=127L)
    user_realname = models.CharField(max_length=45L, blank=True)
    user_email = models.CharField(max_length=255L)
    user_password = models.CharField(max_length=255L, blank=True)
    user_is_active = models.CharField(max_length=1L, blank=True)
    user_is_administrator = models.CharField(max_length=1L)
    user_avatar = models.CharField(max_length=127L, blank=True)
    user_role_user_role = models.ForeignKey('UserRole', null=True, blank=True)
    class Meta:
        db_table = 'user'

class UserRole(models.Model):
    user_role_id = models.IntegerField(primary_key=True)
    user_role_name = models.CharField(max_length=127L)
    user_role_is_active = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'user_role'

