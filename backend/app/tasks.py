from celery import Celery
import os

celery_app = Celery(
    "novacrm",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
)

@celery_app.task
def send_email_async(to_email: str, subject: str, body: str):
    from app.email import send_email
    return send_email(to_email, subject, body)

@celery_app.task
def score_leads(user_id: int):
    from app.ai import ai_model
    # TODO: Fetch contacts and score them
    return "Leads scored"

@celery_app.task
def sync_stripe_subscription(user_id: int, stripe_customer_id: str):
    import stripe
    # TODO: Sync subscription status
    return "Subscription synced"

@celery_app.task(bind=True)
def retry_failed_emails(self, email_id: int, retries: int = 0):
    max_retries = 3
    if retries < max_retries:
        # TODO: Retry email
        raise self.retry(countdown=60, max_retries=max_retries)
