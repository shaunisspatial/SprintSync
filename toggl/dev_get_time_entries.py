import keyring
from sprint_sync.time.client import TogglClient
from sprint_sync.utils.database import Database

token = keyring.get_credential('toggl_api_key', 'shaun@action.co')
client = TogglClient()
time_entries = client.get_time_entries(auth=token.password)


cols_time_entries = ['id', 'project_id', 'start', 'stop']
cols_projects = ['project_id']
cols_toggl_workspaces = ['workspace_id']

db_password = keyring.get_password(service_name='pg', username='py_read_write')
db = Database()
db.username = 'py_read_write'
db.password = db_password

time_entries_dict = [t.create_dict() for t in time_entries]
time_entries_dict = [{key: e[key] for key in cols_time_entries} for e in time_entries_dict]

db.write(table='time_entries', data=time_entries_dict)

# for entry in time_entries:
#     entry_dict = entry.create_dict()
#     entry_dict_te = {key: entry_dict[key] for key in cols_time_entries}
print('tskldjf')