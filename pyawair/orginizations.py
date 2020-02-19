from pyawair.devices import *


def get_organizations(auth):
    response = requests.get("https://developer-apis.awair.is/v1/org-users/self/orgs",
                            headers=auth.headers)
    return "Function not implemented yet"
