from diator.requests import Request
from diator.response import Response

import dataclasses

@dataclasses.dataclass(frozen=True, kw_only=True)
class JoinMeetingRequest(Request):
    meeting_id: int = dataclasses.field(default=1)
    user_id: int = dataclasses.field(default=1)

