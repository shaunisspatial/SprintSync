from dataclasses import dataclass, asdict


@dataclass
class AuthToken:
    id: int
    api_token: str
    email: str
    fullname: str
    timezone: str
    toggl_accounts_id: str
    default_workspace_id: int
    beginning_of_week: int
    image_url: str
    created_at: str
    updated_at: str
    openid_enabled: bool
    openid_email: None
    country_id: int
    has_password: bool
    intercom_hash: str
    oauth_providers: list

@dataclass
class TimeEntry:
    id: int
    workspace_id: int
    project_id: int
    billable: bool
    start: str
    stop: str
    duration: int
    description: str
    tags: list
    tag_ids: list
    duronly: bool
    at: str
    user_id: int
    uid: int
    wid: int
    pid: int
    server_deleted_at: str = None
    task_id: int = None

    def create_dict(self):
        return {k:v for k,v in asdict(self).items()}
