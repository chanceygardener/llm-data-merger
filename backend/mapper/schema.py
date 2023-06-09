from dataclasses import dataclass
from dataclasses_json import dataclass_json
import re
from typing import Dict, List
import datetime
import json


def unescape_regex(restring: str):
    return restring.replace('\\\\', '\\')


@dataclass_json()
@dataclass
class ColumnMeta:
    description: str
    python_type: str
    regex: re.Pattern
    # format_template: str
    sample_values: List[str]

    def __post_init__(self):
        unescaped = unescape_regex(self.regex)
        self.regex = re.compile(unescaped)

    def format_value(self, **kwargs):
        return self.format_template.format(**kwargs)


@dataclass_json()
@dataclass
class TableMeta:

    description: str
    columns: Dict[str, ColumnMeta]

    def __post_init__(self):
        self.columns = {k: ColumnMeta(**v) for k, v in self.columns.items()}

    def mapping_description(self):
        '''Returns an abbreviated description to be used in column mapping prompts'''
        return json.dumps({
            "description": self.description,
            "columns": {
                k: {
                    "description": self.columns[k].description,
                    "regex": self.columns[k].regex.pattern,
                    "sample_values": self.columns[k].sample_values,
                    "components": list(self.columns[k].regex.groupindex.keys())
                }
                for k in self.columns}
        }, indent=4)


@dataclass_json()
@dataclass
class TableColumnMapping:
    input_obj_key: str
    reason: str
    translation_format: str

    def format_value(self, **kwargs):
        return self.translation_format.format(**kwargs)
