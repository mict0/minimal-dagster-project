from dagster import repository

from .jobs import jobs
from .schedules import schedules
from .sensors import sensors


@repository
def minimal_dagster_project():
    return jobs + schedules + sensors
