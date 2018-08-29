TEST_DEVICE_NAME = None
TEST_TOKEN = None

def get_test_token():
    if TEST_TOKEN is None:
        raise ValueError("Invalid token")
    return TEST_TOKEN

def get_test_device_name():
    if TEST_DEVICE_NAME is None:
        raise ValueError("Invalid name")
    return TEST_DEVICE_NAME
