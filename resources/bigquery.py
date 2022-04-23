#google library
from google.cloud import bigquery
from http import HTTPStatus

#Standar library
import requests
import json


#Funcion generar token para consumir el servicio
def access_token():

    #Code Code snippet (Otorgado por postman)
      url = "NO SE COMPARTE INFO POR PRIVACIDAD"

      payload='grant_type=client_credentials'
      headers = {
            'Authorization': '',
            'Content-Type': '',
            'Cookie': ''
        }
        
      response = requests.request("POST", url, headers=headers, data=payload)
      response = json.loads(response.text)
      return response['access_token']



    #Funcion de ejemplo Conexion a Bigquery servicio de Google Cloud Computing
def ejercicio_Bigquery():
   
     
        # llamado del cliente
        client=bigquery.Client()
   

        #Armado del query
        query_job=f"""
            SELECT 
                p1
            FROM
                `Nombre_de_proyecto.nombre_de_base_de_datos.nombre_de_tabla`
            WHERE 
                account="0103727810"
            """
            
        #Unimos query con cliente
        query_job=client.query(query_job)

    
    
        # recorremos datos
        for row in query_job:
           for i in row:
          
              print(i)
              #PRIMER SERVICIO
              # Remplazamos id=(id de categoria) de url por dato obtenido de Query
              #Vamos a consultar el servicio de acuerdo el id obtenido
              url = f"NO SE COMPARTE INFO POR PRIVACIDAD/getProductsByCategory?category={i}_1&currentPage=0&fields=DEFAULT&pageSize=20"

              payload={}
              headers = {
               'Authorization': f'Bearer {access_token()}',
               'Cookie': 'ROUTE=.api-5d4fc4b54d-6b4zr'
               }

              response = requests.request("GET", url, headers=headers, data=payload)
              #Print de referencia
              print("BODY --------------------------------------------")
              print(response.text)
              print("url --------------------------------------------")
              print(response.url)

              #convierto De JSON a Python
              response_json=json.loads(response.text)

              #---------------CONSULTA SEGUNDO SERVICIO
              #Guardo ID de response_json['products'] del primer servicio en la variable datos
              for datos in response_json['products']:
                    #Guardado de id
                    dato=datos["id"]
                    #Lo sustituyo en la URL
                    url = f"NO SE COMPARTE INFO POR PRIVACIDAD/products/delivery/{dato}?fields=FULL"

                    response = requests.request("GET", url, headers=headers, data=payload)

                    #Arroja info de acuerdo a ID
                    print("BODY --------------------------------------------")
                    print(response.text)
                    print("url --------------------------------------------")
                    print(response.url)
           
                    #convierto De JSON a Python
                    response_json=json.loads(response.text)

                    #Armo response con los datos que necesito
                    response = {
                           "name": "Datos servicio",
                           "products": {
                                "availableForPickup": response_json['availableForPickup'],
                                "averageRating": response_json['averageRating'],
                                "categories_code": response_json['categories'][0]['code'],
                                "characteristics": response_json['characteristics'],
                                 "galleryImages_url_1": response_json['galleryImages'][0]['url'],
                                 "galleryImages_url_2": response_json['galleryImages'][1]['url'],
                                 "name": response_json['name'],
                                 "price": response_json['price']['currencyIso'],
                                "value": response_json['price']['value'],
                                "categoriesFood_id":response_json['vendor']['categoriesFood'][0]['id'],
                                "vendor_code":response_json['vendor']['code']
                             },
                    }

                    #Convierto mi response a JSON
                    response=json.dumps(response)
                    httpestatus = HTTPStatus.OK                                   

            
                      
              return response,httpestatus
  
  

        