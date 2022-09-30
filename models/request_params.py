from typing import Dict, Any

from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_PARAMS = (
    "filter",
    "sort",
    "map",
    "unique",
    "limit"
)


class RequestParams(Schema):
    file_name = fields.Str(required=True)
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_params(self, values: Dict[str, str | int], *args: Any, **kwargs: Any) -> Dict[str, str | int]:
        for k, v in values.items():
            if "cmd" in k:
                if v not in VALID_CMD_PARAMS:
                    raise ValidationError(f"'{k}' contains invalid value")
        return values
