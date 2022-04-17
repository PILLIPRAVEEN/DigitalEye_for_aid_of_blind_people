import destination_coordinates  # To recieve destination from the user and to get the coordinates of the destination.

import user_coordinates #To recieve the cuurent location coordinates of the user

import requests # To collect the data from an URL by sending a request ot the server

import json # To decode the json format data.



#   user_coord  -> coordinates of the user's current location
#   dest_coord  -> coordinates of the user's destination loacation

def getpath(user_coord,dest_coord):
    
    
    #                      PATH MAPPING URL
    #This URL is operated from our Cloud resource group using Azure maps.
    
    def url(x1,y1,x2,y2):
        link='https://atlas.microsoft.com/route/directions/json?api-version=1.0&subscription-key=HbUKMrc95Sb2A-ID4VmyPdfi5qTJyo70XXSMWEMFqcM&query='+str(x1)+','+str(y1)+':'+str(x2)+','+str(y2)+'&routeRepresentation=polyline&travelMode=car&instructionsType=text'
        return(link)
    
    
    
    #                           FETCHING PATH COORDINATES
    
    # Let's name the user's coordinates as (x1,y1) and the destination coordinates as (x2,y2)
    
    x1=user_coord[0]
    y1=user_coord[1]
    
    x2=dest_coord[0]
    y2=dest_coord[1]
    
    #URL for fetching the coordinates of the path from the user cuurent location to destination.
    path_url = url(x1,y1,x2,y2)
    
    #sending request to the server
    req=requests.get(path_url)
    
    #Recieved json format data
    json_data=req.json()
    
    #Collects the data of the path coordinates form the server in the format of a list of dictionaries.
    path_coord = json_data['routes'][0]['legs'][0]['points']
    
    
    #The path coordinates are stored in a final path coordinate list
    final_path = []
    for coord in path_coord:
        final_path.append([coord['latitude'],coord['longitude']])

    return(final_path)















