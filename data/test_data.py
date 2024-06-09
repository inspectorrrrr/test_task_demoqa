import os

test_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "gender": "Male",
    "mobile": "1234567890",
    "date_of_birth": {
        "day": "27",
        "month": "May",
        "year": "1984"
    },
    "subjects": ["Arts"],
    "hobbies": ["Sports", "Music"],
    "picture": os.path.abspath(os.path.join("resources", "photo.jpg")),
    "current_address": "123 Main St",
    "state": "NCR",
    "city": "Delhi"
}
