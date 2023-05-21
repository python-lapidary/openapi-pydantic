from typing import Optional

from pydantic import BaseModel, Extra


class ExternalDocumentation(BaseModel):
    """Allows referencing an external resource for extended documentation."""

    description: Optional[str] = None
    """
    A short description of the target documentation.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text 
    representation.
    """

    url: str
    """
    **REQUIRED**. The URL for the target documentation.
    Value MUST be in the format of a URL.
    """

    class Config:
        extra = Extra.allow
        schema_extra = {
            "examples": [
                {"description": "Find more info here", "url": "https://example.com"}
            ]
        }
