from pydantic import BaseModel


class SFWResponseSchema(BaseModel):
    status: str = 'OK'

class NSWFResponseSchema(BaseModel):
    status: str = "REJECTED"
    reason: str = "NSFW content"