import pytest
from unittest.mock import patch, MagicMock
from app.billing import create_customer, create_subscription

@patch('app.billing.stripe.Customer.create')
def test_create_customer(mock_create):
    mock_create.return_value = MagicMock(id='cus_123')
    
    customer_id = create_customer('test@example.com', 'Test User')
    
    assert customer_id == 'cus_123'
    mock_create.assert_called_once()

@patch('app.billing.stripe.Subscription.create')
def test_create_subscription(mock_create):
    mock_create.return_value = MagicMock(id='sub_123')
    
    subscription = create_subscription('cus_123', 'price_standard')
    
    assert subscription.id == 'sub_123'
