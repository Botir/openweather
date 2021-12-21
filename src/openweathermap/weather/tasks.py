from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command

logger = get_task_logger(__name__)

@shared_task
def forest_data():
    logger.info("Hi am.")
    call_command("get_forest", )

