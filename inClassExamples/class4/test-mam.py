import my_astro_module as mam

def main():

    Earth = {
        "name": "Earth",
        "mass": 1.0 * mam.m_earth,
        "radius": 1.0 * mam.r_earth,
        "temperature": 288.0,
        #how much energy the Earth recieves from the Sun
        "incident_flux": 1.0 * mam.s_earth,
        #fraction of that energy that is reflected
        "albedo": 0.31
    }

    Venus = {
        "name": "Venus",
        "mass": 0.815 * mam.m_earth,
        "radius": 0.915 * mam.r_earth,
        "temperature": 737.0,
        #how much energy the Venus recieves from the Sun
        "incident_flux": 1.902 * mam.s_earth,
        #fraction of that energy that is reflected
        "albedo": 0.77
    }

    # print(Earth["name"])
    # print(Earth["mass"])

    # print()

    # print(Venus["name"])
    # print(Venus["mass"])

    # print()

    # #show the surface gravity of Earth and Venus
    # print("Earth Surface Gravity:", mam.g_surf(Earth["mass"], Earth["radius"]))
    # print("Venus Surface Gravity:", mam.g_surf(Venus["mass"], Venus["radius"]))

    # print()

    # #show the surface gravity of Earth and Venus
    # print("Earth Surface Gravity:", mam.g_surf2(Earth))
    # print("Venus Surface Gravity:", mam.g_surf2(Venus))

    mam.show_g_surf(Earth)
    mam.show_g_surf(Venus)

    print()

    # print(mam.k_to_f(Earth["temperature"]))
    # print(mam.k_to_f(Venus["temperature"]))
    
    #Displays Evidence of the Greenhouse Effect 
    #and Runaway Greenhouse Effect (Venus)
    mam.show_temp_f(Earth)
    mam.show_temp_f(Venus)

    print()

    planet_list= [Earth, Venus]
    for planet in planet_list:
        print(planet['name'])

if __name__ =="__main__":
    main()