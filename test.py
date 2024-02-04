from pydantic import BaseModel, Field
import boto3

from dyntastic import Dyntastic
from pydantic import Field


class Record(Dyntastic):
    __table_name__ = "house_codex"
    __hash_key__ = "user_name"

    user_name: str = Field(description="The user's name.")
    unit: str = Field(description="The unit of measure.")
    value: int = Field(description="The value of the measurement.")
    subject: str = Field(description="The subject of the measurement.")
    record_type: str = Field(description="The type of record.")


# class HouseElf:
#     """Encapsulates an Amazon DynamoDB table of record data."""

#     def __init__(self, region="us-west-2"):
#         boto3.setup_default_session(region_name=region)
#         self.dynamodb = boto3.resource("dynamodb")
#         self.table = self.dynamodb.Table("house_codex")

#     def record(self, record: dict):
#         print(self.table.put_item(Item=record))


# elf = HouseElf()

try:
    Record.create_table()
except Exception as e:
    print(e)

record = Record(
    **{
        "user_name": "thomas",
        "unit": "lbs",
        "value": 200,
        "subject": "weight",
        "record_type": "measurement",
    }
)

record.save()

# elf.record({"user_name": "thomas", "event": "Hello, e!"})
