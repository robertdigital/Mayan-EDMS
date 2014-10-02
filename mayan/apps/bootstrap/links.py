from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from .permissions import (PERMISSION_BOOTSTRAP_VIEW, PERMISSION_BOOTSTRAP_CREATE,
    PERMISSION_BOOTSTRAP_EDIT, PERMISSION_BOOTSTRAP_DELETE,
    PERMISSION_BOOTSTRAP_EXECUTE, PERMISSION_BOOTSTRAP_DUMP,
    PERMISSION_NUKE_DATABASE, PERMISSION_BOOTSTRAP_EXPORT,
    PERMISSION_BOOTSTRAP_IMPORT, PERMISSION_BOOTSTRAP_REPOSITORY_SYNC)

link_bootstrap_setup_tool = {'text': _(u'Bootstrap'), 'view': 'bootstrap:bootstrap_setup_list', 'icon': 'lightning.png', 'permissions': [PERMISSION_BOOTSTRAP_VIEW]}
link_bootstrap_setup_list = {'text': _(u'Bootstrap setup list'), 'view': 'bootstrap:bootstrap_setup_list', 'famfam': 'lightning', 'permissions': [PERMISSION_BOOTSTRAP_VIEW]}
link_bootstrap_setup_create = {'text': _(u'Create new bootstrap setup'), 'view': 'bootstrap:bootstrap_setup_create', 'famfam': 'lightning_add', 'permissions': [PERMISSION_BOOTSTRAP_CREATE]}
link_bootstrap_setup_edit = {'text': _(u'Edit'), 'view': 'bootstrap:bootstrap_setup_edit', 'args': 'object.pk', 'famfam': 'pencil', 'permissions': [PERMISSION_BOOTSTRAP_EDIT]}
link_bootstrap_setup_delete = {'text': _(u'Delete'), 'view': 'bootstrap:bootstrap_setup_delete', 'args': 'object.pk', 'famfam': 'lightning_delete', 'permissions': [PERMISSION_BOOTSTRAP_DELETE]}
link_bootstrap_setup_view = {'text': _(u'Details'), 'view': 'bootstrap:bootstrap_setup_view', 'args': 'object.pk', 'famfam': 'lightning', 'permissions': [PERMISSION_BOOTSTRAP_VIEW]}
link_bootstrap_setup_execute = {'text': _(u'Execute'), 'view': 'bootstrap:bootstrap_setup_execute', 'args': 'object.pk', 'famfam': 'lightning_go', 'permissions': [PERMISSION_BOOTSTRAP_EXECUTE]}
link_bootstrap_setup_dump = {'text': _(u'Dump current setup'), 'view': 'bootstrap:bootstrap_setup_dump', 'famfam': 'arrow_down', 'permissions': [PERMISSION_BOOTSTRAP_DUMP]}
link_bootstrap_setup_export = {'text': _(u'Export'), 'view': 'bootstrap:bootstrap_setup_export', 'args': 'object.pk', 'famfam': 'disk', 'permissions': [PERMISSION_BOOTSTRAP_EXPORT]}
link_bootstrap_setup_import_from_file = {'text': _(u'Import from file'), 'view': 'bootstrap:bootstrap_setup_import_from_file', 'famfam': 'folder', 'permissions': [PERMISSION_BOOTSTRAP_IMPORT]}
link_bootstrap_setup_import_from_url = {'text': _(u'Import from URL'), 'view': 'bootstrap:bootstrap_setup_import_from_url', 'famfam': 'world', 'permissions': [PERMISSION_BOOTSTRAP_IMPORT]}
link_bootstrap_setup_repository_sync = {'text': _(u'Sync with repository'), 'view': 'bootstrap:bootstrap_setup_repository_sync', 'famfam': 'world', 'permissions': [PERMISSION_BOOTSTRAP_REPOSITORY_SYNC]}
link_erase_database = {'text': _(u'Erase database'), 'view': 'bootstrap:erase_database_view', 'icon': 'radioactivity.png', 'permissions': [PERMISSION_NUKE_DATABASE]}
