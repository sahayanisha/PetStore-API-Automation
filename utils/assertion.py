import logging

def assert_status_code(response,expected_code):
    assert response.status_code == expected_code,(
        f"Expected {expected_code} but got {response.status_code}."
        f"Response: {response.text}.")

def assert_status_in_range(response,min_code,max_code):
    assert min_code <= response.status_code <= max_code,(
        f"Expected {min_code}-{max_code} but got {response.status_code}."
        f"Response: {response.text}.")

def assert_response_not_empty(response):
    assert response.text and response.text.strip(),"Response body is empty."

def assert_json_response(response):
    try:
        return response.json()
    except Exception:
        logging.error(f"Response is not valid json. Body: {response.text}")

def assert_response_time(response,max_seconds = 2.0):
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_seconds,(f"Response time {elapsed:.2f}s exceeds {max_seconds}s.")

def assert_field_equal(actual,expected,field_name):
    assert actual == expected,(
        f"Mismatch in {field_name}, Expected {expected} but got {actual}."
    )




