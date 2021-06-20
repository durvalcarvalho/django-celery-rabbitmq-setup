from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery_progress.backend import ProgressRecorder

from time import sleep


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)

    for i in range(duration):
        sleep(1)
        progress_recorder.set_progress(i+1, duration)

    return "done"
