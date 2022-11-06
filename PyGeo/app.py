from geopy import geocoders

def address_to_geo(addr):
    try:
        location = geocoders.Nominatim(user_agent="app").geocode(addr)

    except ValueError:
        raise

    else:
        return location


def geo_to_address(geoloc):
    location = geocoders.Nominatim(user_agent="app").geocode(geoloc)



def main():
    address = "404 Avondale Cir Warner Robins GA 31088"
    address = "2545 VZ County Rd 2120 Canton TX 75103"
    address = "Canton TX 75103"
    address = "Tyler, TX"
    
    data = address_to_geo(address)
    print(data)
    print(data.latitude, data.longitude)

    print()


if __name__ == "__main__":
    main()