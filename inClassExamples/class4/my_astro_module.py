#----------------------------------------------
#Defining all useful units and constants
#all values are in SI (INternational System Unit)
#second, meter, kilogram, kelvin, etc

#mass of earth (kg)
m_earth = 5.97216787e+24
#radius of earth (m)
r_earth = 6.3781e+6
#incident flux of earth (W/m^2)
s_earth = 1370.0

#gravitational constant
g_grav = 6.6743e-11
#Stefan-Boltzmann constant
sigma_sb = 5.67037442e-8
#----------------------------------------------
#Functions

#function that returns the surface gravity of a planet
def g_surf(mass, radius):
    return (g_grav * mass) / (radius**2)

#return surface gravity using a dictionary
def g_surf2(planet):
    return (g_grav * planet["mass"]) / (planet["radius"]**2)

#convert temperatures

def c_to_f(celsius):
    """Celsius to Fahrenheit"""
    return celsius * 9.0 / 5.0 + 32

def f_to_c(fahrenheit):
    """Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5.0 / 9.0

def c_to_k(celsius):
    """celsius to kelvin"""
    return celsius + 273.15

def k_to_c(kelvin):
    """kelvin to celsius"""
    return kelvin - 273.15

def f_to_k(fahrenheit):
    """fahrenheit to kelvin"""
    return c_to_k(f_to_c(fahrenheit))

def k_to_f(kelvin):
    return c_to_f(k_to_c(kelvin))


#----------------------------------------------
#SUBROUTINES

#show the surface gravity of a planet in a nice way
def show_g_surf(planet):
    #create an f-string containing all useful info
    sentence = f"The acceleration of gravity\n"
    sentence += f"on the surface of {planet['name']}\n"
    #                               #(totalchrs).(chrsAfterDecimal)(Type)
    sentence += f'is {g_surf2(planet):6.4f} m/s^2.\n'

    print(sentence)

def show_temp_f(planet):
    Tsurf = k_to_f(planet["temperature"])

    #effective temperature: the temperature if the planet
    #absorbed all the energy from the Sun
    #Teff = (incident flux / (4.0 * Steffan-Boltzmann Constant)) ^ (1/4)
    Teff = (planet["incident_flux"] / (4.0 * sigma_sb)) ** (0.25)
    Teff = k_to_f(Teff)

    #equilibrium temperature:
    #temp accounting for the reflected energy
    #Teq = (1 - Albedo)^(1.4) * Teff
    Teq = ((1-planet['albedo'])**(0.25)) * Teff

    sentence = f"Temperatures of {planet['name']} \n"
    sentence += f"Surface Temperature: {Tsurf:6.2f} F\n"
    sentence += f"Effective Temperature: {Teff:6.2f} F\n"
    sentence += f"Equilibrium Temperature: {Teq:6.2f} F\n"

    print(sentence)