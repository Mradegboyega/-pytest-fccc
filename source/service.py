import requests

database = {
    1: 'toyin',
    2: 'michelle',
    3: 'adegboyega'
}


def get_user_from_db(user_id):
    """
    Get the user's name from the in-memory database based on the user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        str or None: The user's name if found, or None if the user ID does not exist in the database.
    """
    if user_id in database:
        return database[user_id]
    else:
        return None


def get_users():
    """
    Get the list of users from the 'https://jsonplaceholder.typicode.com/users' API.

    Returns:
        dict or None: The JSON content of the response if the request is successful, or None if an error occurs.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    # Log the status code for debugging
    print(f"Status Code: {response.status_code}")

    response.raise_for_status()  # Raise an HTTPError for bad responses
    return response.json()


