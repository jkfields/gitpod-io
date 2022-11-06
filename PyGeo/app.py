from geopy import geocoders

def main():
    location = geocoders.Nominatim(user_agent="app")
    address = "404 Avondale Cir Warner Robins GA 31088"

    data = location.geocode(address)
    print(data)
    print(data.latitude, data.longitude)


if __name__ == "__main__":
    main()

