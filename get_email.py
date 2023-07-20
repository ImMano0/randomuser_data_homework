import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    email=[]
    for user in data["results"]:
        email.append(user["email"])
    return email
data=get_data.get_data("randomuser_data.json")


print(get_email(data))