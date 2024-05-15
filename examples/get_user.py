from transistor.client import TransistorClient

if __name__=="__main__":

    client = TransistorClient(api_key="your_api_key_here")
    user = client.get_authenticated_user()
    print(user)