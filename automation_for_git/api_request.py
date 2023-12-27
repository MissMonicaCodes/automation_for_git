import requests

url = 'https://swapi.dev/api/people'
people_id = 25
var_height = 176
var_vehicles_count = 0

def star_wars_1():
    response = requests.get(f"{url}/{people_id}")
    try:
        if response.status_code == 200:
            json_response = response.json()
            print(response.status_code)

            height=int(json_response['height'])
            print(height)
            assert height > var_height,(f"身高大於{var_height}")
            print(f"身高大於{var_height}")

            vehicles = json_response['vehicles']
            print(len(vehicles))
            assert len(vehicles) == var_vehicles_count,(f"Vehicles數量 == {var_vehicles_count}")
            print("數量等於0")


    except AssertionError as e:
        if "身高" in str(e):
            print(f"身高不大於{var_height}")
        elif "Vehicles" in str(e):
            print(f"Vehicles數量不等於{var_vehicles_count}")
        else:
            print("其他AssertionError:", e)


if __name__ == "__main__":
    star_wars_1()