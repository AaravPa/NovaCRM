import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_customer(email: str, name: str):
    customer = stripe.Customer.create(
        email=email,
        name=name
    )
    return customer.id

def create_subscription(customer_id: str, price_id: str):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}]
    )
    return subscription

def cancel_subscription(subscription_id: str):
    stripe.Subscription.delete(subscription_id)
    return True
