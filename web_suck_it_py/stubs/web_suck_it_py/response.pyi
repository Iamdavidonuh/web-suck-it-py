from uuid import UUID

class Channel:
    id: UUID
    name: str
    pass_key: str
    max_connections: str | None
    user_id: UUID
    created_at: str
    updated_at: str
    def __init__(
        self, id, name, pass_key, max_connections, user_id, created_at, updated_at
    ) -> None: ...
