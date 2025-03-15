# 1. WAP to find out electricity bill for a user Take month wise units of consumptions 
# User types are : Household user/business user/ industrial user
# Rate per unit : Household: 2 rs / business: 5 rs / Industrial : 10 rs.

# typeOfUser = input("Enter the type of user (Household or Small Business or Industrial): ").strip().lower()
# consumption = int(input("Enter the consumption in a month in units: "))

# if typeOfUser == "household":
#     rate = 2
# elif typeOfUser == "small business":
#     rate = 5
# elif typeOfUser == "industrial":
#     rate = 10
# else:
#     print("You are a Invalid user. Please enter Household or Small Business or Industrial.")


# 2. WAP to find out fare  for a user . Take KM wise  distance travelled as input
# Rate per KM : (0 to 10 ): 10 rs / (10-20 ): 5 rs / (above 20 ) : 4 rs.

distance=int(input("Enter the distance travelled by user(in KM):"))
if (distance==0) or (distance<0):
    print("Please enter correct the distance .")
elif(distance>0) and (distance<10):
    ratePerKm=10
    fareOfUser=(ratePerKm*distance)
    print(f"The fare of user travelled {distance}km is {fareOfUser} Rs ")
elif(distance>=10) and (distance<19):
    ratePerKm=5
    fareOfUser=(ratePerKm*distance)
    print(f"The fare of user travelled {distance}km is {fareOfUser} Rs ")
else:
    ratePerKm=4
    fareOfUser=(ratePerKm*distance)
    print(f"The fare of user travelled {distance}km is {fareOfUser} Rs ")

