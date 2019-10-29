# coding: utf-8
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--meal-weight", help="meal weight in grams: 2000", type=float, required=True)
    parser.add_argument("--delta-auth", help="authorised difference between real and ideal distribution: 0.05", type=float, required=True)
    parser.add_argument("--csv-file-path", help="path to csv file: '/home/ubuntu/input/listing.csv'", type=str, required=True)
    parser.add_argument("--request-id", help="unique request id: 123456789", type=int, required=True)
    args = parser.parse_args()

    # access variables via args.meal_weight, args.csv_file_path etc.
    request_id = args.request_id

    test_result = {
      "weight": args.meal_weight,
      "pct_input_items": [
         [
            "Viande, poisson, oeufs",
            0.06121894571887815
         ],
         [
            "Produits gras sucrés salés",
            0.24292811142750698
         ],
         [
            "Produits laitiers",
            0.17405525299186245
         ],
         [
            "Féculents",
            0.05400006425838616
         ],
         [
            "Fruits et légumes",
            0.46779762560336624
         ]
      ],
      "pct_allocated_items":[
         [
            "Viande, poisson, oeufs",
            0.03220187318160643
         ],
         [
            "Produits gras sucrés salés",
            0.0
         ],
         [
            "Produits laitiers",
            0.058458785160454746
         ],
         [
            "Féculents",
            0.050697308034631655
         ],
         [
            "Fruits et légumes",
            0.11917912945713675
         ]
      ],
      "pct_remaining_items":[
         [
            "Viande, poisson, oeufs",
            0.029017072537271725
         ],
         [
            "Produits gras sucrés salés",
            0.24292811142750698
         ],
         [
            "Produits laitiers",
            0.11559646783140769
         ],
         [
            "Féculents",
            0.0033027562237545054
         ],
         [
            "Fruits et légumes",
            0.3486184961462295
         ]
      ],
      "nb_balanced_meals":8,
      "nb_allocated_items":52,
      "nb_remaining_items":89,
      "total_input_weight":60555,
      "total_allocated_weight":15776,
      "total_weight_remaining_items":44778,
      "pct_weight_allocated_items":0.2605370958338296,
      "pct_weight_remaining_items":0.7394629041661704,
      "meal_completion": [{
         "nb_meals":0,
         "meal_price":0,
         "categ_bought":[
            ["Viande, poisson, oeufs",13450,13610,11160],
            ["Produits gras sucrés salés",1875,33775,3525],
            ["Matières grasses ajoutées",0,0,5400],
            ["Produits laitiers",32700,60200,24750],
            ["Féculents",15990,16350,38250],
            ["Fruits et légumes",67700,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":0.375,
            "categ_bought":[
               ["Viande, poisson, oeufs",6850,13610,0],
            ["Produits gras sucrés salés",1575,33775,0],
            ["Matières grasses ajoutées",0,0,1575],
            ["Produits laitiers",17640,60200,0],
            ["Féculents",15990,16350,0],
            ["Fruits et légumes",18100,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.6875,
            "categ_bought":[
               ["Viande, poisson, oeufs",7250,13610,0],
            ["Produits gras sucrés salés",1650,33775,0],
            ["Matières grasses ajoutées",0,0,1650],
            ["Produits laitiers",18560,60200,0],
            ["Féculents",15990,16350,750],
            ["Fruits et légumes",18900,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.6875,
            "categ_bought":[
               ["Viande, poisson, oeufs",7650,13610,0],
            ["Produits gras sucrés salés",1725,33775,0],
            ["Matières grasses ajoutées",0,0,1725],
            ["Produits laitiers",19480,60200,0],
            ["Féculents",15990,16350,1500],
            ["Fruits et légumes",19700,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.6875,
            "categ_bought":[
               ["Viande, poisson, oeufs",8050,13610,0],
            ["Produits gras sucrés salés",1800,33775,0],
            ["Matières grasses ajoutées",0,0,1800],
            ["Produits laitiers",20400,60200,0],
            ["Féculents",15990,16350,2250],
            ["Fruits et légumes",20500,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.6875,
            "categ_bought":[
               ["Viande, poisson, oeufs",8450,13610,0],
            ["Produits gras sucrés salés",1875,33775,0],
            ["Matières grasses ajoutées",0,0,1875],
            ["Produits laitiers",21320,60200,0],
            ["Féculents",15990,16350,3000],
            ["Fruits et légumes",21300,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",8750,13610,0],
            ["Produits gras sucrés salés",1875,33775,75],
            ["Matières grasses ajoutées",0,0,1950],
            ["Produits laitiers",22240,60200,0],
            ["Féculents",15990,16350,3750],
            ["Fruits et légumes",22100,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",9050,13610,0],
            ["Produits gras sucrés salés",1875,33775,150],
            ["Matières grasses ajoutées",0,0,2025],
            ["Produits laitiers",23100,60200,0],
            ["Féculents",15990,16350,4500],
            ["Fruits et légumes",22900,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",9350,13610,0],
            ["Produits gras sucrés salés",1875,33775,225],
            ["Matières grasses ajoutées",0,0,2100],
            ["Produits laitiers",23900,60200,0],
            ["Féculents",15990,16350,5250],
            ["Fruits et légumes",23700,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",9650,13610,0],
            ["Produits gras sucrés salés",1875,33775,300],
            ["Matières grasses ajoutées",0,0,2175],
            ["Produits laitiers",24700,60200,0],
            ["Féculents",15990,16350,6000],
            ["Fruits et légumes",24500,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",9950,13610,0],
            ["Produits gras sucrés salés",1875,33775,375],
            ["Matières grasses ajoutées",0,0,2250],
            ["Produits laitiers",25500,60200,0],
            ["Féculents",15990,16350,6750],
            ["Fruits et légumes",25300,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",10250,13610,0],
            ["Produits gras sucrés salés",1875,33775,450],
            ["Matières grasses ajoutées",0,0,2325],
            ["Produits laitiers",26300,60200,0],
            ["Féculents",15990,16350,7500],
            ["Fruits et légumes",26200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",10550,13610,0],
            ["Produits gras sucrés salés",1875,33775,525],
            ["Matières grasses ajoutées",0,0,2400],
            ["Produits laitiers",27100,60200,0],
            ["Féculents",15990,16350,8250],
            ["Fruits et légumes",27200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",10850,13610,0],
            ["Produits gras sucrés salés",1875,33775,600],
            ["Matières grasses ajoutées",0,0,2475],
            ["Produits laitiers",27900,60200,0],
            ["Féculents",15990,16350,9000],
            ["Fruits et légumes",28200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",11150,13610,0],
            ["Produits gras sucrés salés",1875,33775,675],
            ["Matières grasses ajoutées",0,0,2550],
            ["Produits laitiers",28700,60200,0],
            ["Féculents",15990,16350,9750],
            ["Fruits et légumes",29200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",11450,13610,0],
            ["Produits gras sucrés salés",1875,33775,750],
            ["Matières grasses ajoutées",0,0,2625],
            ["Produits laitiers",29500,60200,0],
            ["Féculents",15990,16350,10500],
            ["Fruits et légumes",30200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",11750,13610,0],
            ["Produits gras sucrés salés",1875,33775,825],
            ["Matières grasses ajoutées",0,0,2700],
            ["Produits laitiers",30300,60200,0],
            ["Féculents",15990,16350,11250],
            ["Fruits et légumes",31200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",12050,13610,0],
            ["Produits gras sucrés salés",1875,33775,900],
            ["Matières grasses ajoutées",0,0,2775],
            ["Produits laitiers",31100,60200,0],
            ["Féculents",15990,16350,12000],
            ["Fruits et légumes",32200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",12410,13610,0],
            ["Produits gras sucrés salés",1875,33775,975],
            ["Matières grasses ajoutées",0,0,2850],
            ["Produits laitiers",31900,60200,0],
            ["Féculents",15990,16350,12750],
            ["Fruits et légumes",33200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":1.9874999999999998,
            "categ_bought":[
               ["Viande, poisson, oeufs",12810,13610,0],
            ["Produits gras sucrés salés",1875,33775,1050],
            ["Matières grasses ajoutées",0,0,2925],
            ["Produits laitiers",32700,60200,0],
            ["Féculents",15990,16350,13500],
            ["Fruits et légumes",34200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":5.175000000000001,
            "categ_bought":[
               ["Viande, poisson, oeufs",13130,13610,0],
            ["Produits gras sucrés salés",1875,33775,1125],
            ["Matières grasses ajoutées",0,0,3000],
            ["Produits laitiers",32700,60200,750],
            ["Féculents",15990,16350,14250],
            ["Fruits et légumes",35200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":5.175000000000001,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,0],
            ["Produits gras sucrés salés",1875,33775,1200],
            ["Matières grasses ajoutées",0,0,3075],
            ["Produits laitiers",32700,60200,1500],
            ["Féculents",15990,16350,15000],
            ["Fruits et légumes",36200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,360],
            ["Produits gras sucrés salés",1875,33775,1275],
            ["Matières grasses ajoutées",0,0,3150],
            ["Produits laitiers",32700,60200,2250],
            ["Féculents",15990,16350,15750],
            ["Fruits et légumes",37200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,720],
            ["Produits gras sucrés salés",1875,33775,1350],
            ["Matières grasses ajoutées",0,0,3225],
            ["Produits laitiers",32700,60200,3000],
            ["Féculents",15990,16350,16500],
            ["Fruits et légumes",38200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,1080],
            ["Produits gras sucrés salés",1875,33775,1425],
            ["Matières grasses ajoutées",0,0,3300],
            ["Produits laitiers",32700,60200,3750],
            ["Féculents",15990,16350,17250],
            ["Fruits et légumes",39200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,1440],
            ["Produits gras sucrés salés",1875,33775,1500],
            ["Matières grasses ajoutées",0,0,3375],
            ["Produits laitiers",32700,60200,4500],
            ["Féculents",15990,16350,18000],
            ["Fruits et légumes",40200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,1800],
            ["Produits gras sucrés salés",1875,33775,1575],
            ["Matières grasses ajoutées",0,0,3450],
            ["Produits laitiers",32700,60200,5250],
            ["Féculents",15990,16350,18750],
            ["Fruits et légumes",41200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,2160],
            ["Produits gras sucrés salés",1875,33775,1650],
            ["Matières grasses ajoutées",0,0,3525],
            ["Produits laitiers",32700,60200,6000],
            ["Féculents",15990,16350,19500],
            ["Fruits et légumes",42200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,2520],
            ["Produits gras sucrés salés",1875,33775,1725],
            ["Matières grasses ajoutées",0,0,3600],
            ["Produits laitiers",32700,60200,6750],
            ["Féculents",15990,16350,20250],
            ["Fruits et légumes",43200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,2880],
            ["Produits gras sucrés salés",1875,33775,1800],
            ["Matières grasses ajoutées",0,0,3675],
            ["Produits laitiers",32700,60200,7500],
            ["Féculents",15990,16350,21000],
            ["Fruits et légumes",44200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,3240],
            ["Produits gras sucrés salés",1875,33775,1875],
            ["Matières grasses ajoutées",0,0,3750],
            ["Produits laitiers",32700,60200,8250],
            ["Féculents",15990,16350,21750],
            ["Fruits et légumes",45200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,3600],
            ["Produits gras sucrés salés",1875,33775,1950],
            ["Matières grasses ajoutées",0,0,3825],
            ["Produits laitiers",32700,60200,9000],
            ["Féculents",15990,16350,22500],
            ["Fruits et légumes",46200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,3960],
            ["Produits gras sucrés salés",1875,33775,2025],
            ["Matières grasses ajoutées",0,0,3900],
            ["Produits laitiers",32700,60200,9750],
            ["Féculents",15990,16350,23250],
            ["Fruits et légumes",47200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,4320],
            ["Produits gras sucrés salés",1875,33775,2100],
            ["Matières grasses ajoutées",0,0,3975],
            ["Produits laitiers",32700,60200,10500],
            ["Féculents",15990,16350,24000],
            ["Fruits et légumes",48200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,4680],
            ["Produits gras sucrés salés",1875,33775,2175],
            ["Matières grasses ajoutées",0,0,4050],
            ["Produits laitiers",32700,60200,11250],
            ["Féculents",15990,16350,24750],
            ["Fruits et légumes",49200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,5040],
            ["Produits gras sucrés salés",1875,33775,2250],
            ["Matières grasses ajoutées",0,0,4125],
            ["Produits laitiers",32700,60200,12000],
            ["Féculents",15990,16350,25500],
            ["Fruits et légumes",50200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,5400],
            ["Produits gras sucrés salés",1875,33775,2325],
            ["Matières grasses ajoutées",0,0,4200],
            ["Produits laitiers",32700,60200,12750],
            ["Féculents",15990,16350,26250],
            ["Fruits et légumes",51300,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,5760],
            ["Produits gras sucrés salés",1875,33775,2400],
            ["Matières grasses ajoutées",0,0,4275],
            ["Produits laitiers",32700,60200,13500],
            ["Féculents",15990,16350,27000],
            ["Fruits et légumes",52200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,6120],
            ["Produits gras sucrés salés",1875,33775,2475],
            ["Matières grasses ajoutées",0,0,4350],
            ["Produits laitiers",32700,60200,14250],
            ["Féculents",15990,16350,27750],
            ["Fruits et légumes",53200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,6480],
            ["Produits gras sucrés salés",1875,33775,2550],
            ["Matières grasses ajoutées",0,0,4425],
            ["Produits laitiers",32700,60200,15000],
            ["Féculents",15990,16350,28500],
            ["Fruits et légumes",54200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,6840],
            ["Produits gras sucrés salés",1875,33775,2625],
            ["Matières grasses ajoutées",0,0,4500],
            ["Produits laitiers",32700,60200,15750],
            ["Féculents",15990,16350,29250],
            ["Fruits et légumes",55200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,7200],
            ["Produits gras sucrés salés",1875,33775,2700],
            ["Matières grasses ajoutées",0,0,4575],
            ["Produits laitiers",32700,60200,16500],
            ["Féculents",15990,16350,30000],
            ["Fruits et légumes",56200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,7560],
            ["Produits gras sucrés salés",1875,33775,2775],
            ["Matières grasses ajoutées",0,0,4650],
            ["Produits laitiers",32700,60200,17250],
            ["Féculents",15990,16350,30750],
            ["Fruits et légumes",57200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,7920],
            ["Produits gras sucrés salés",1875,33775,2850],
            ["Matières grasses ajoutées",0,0,4725],
            ["Produits laitiers",32700,60200,18000],
            ["Féculents",15990,16350,31500],
            ["Fruits et légumes",58200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,8280],
            ["Produits gras sucrés salés",1875,33775,2925],
            ["Matières grasses ajoutées",0,0,4800],
            ["Produits laitiers",32700,60200,18750],
            ["Féculents",15990,16350,32250],
            ["Fruits et légumes",59200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,8640],
            ["Produits gras sucrés salés",1875,33775,3000],
            ["Matières grasses ajoutées",0,0,4875],
            ["Produits laitiers",32700,60200,19500],
            ["Féculents",15990,16350,33000],
            ["Fruits et légumes",60200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,9000],
            ["Produits gras sucrés salés",1875,33775,3075],
            ["Matières grasses ajoutées",0,0,4950],
            ["Produits laitiers",32700,60200,20250],
            ["Féculents",15990,16350,33750],
            ["Fruits et légumes",61200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,9360],
            ["Produits gras sucrés salés",1875,33775,3150],
            ["Matières grasses ajoutées",0,0,5025],
            ["Produits laitiers",32700,60200,21000],
            ["Féculents",15990,16350,34500],
            ["Fruits et légumes",62200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,9720],
            ["Produits gras sucrés salés",1875,33775,3225],
            ["Matières grasses ajoutées",0,0,5100],
            ["Produits laitiers",32700,60200,21750],
            ["Féculents",15990,16350,35250],
            ["Fruits et légumes",63200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,10080],
            ["Produits gras sucrés salés",1875,33775,3300],
            ["Matières grasses ajoutées",0,0,5175],
            ["Produits laitiers",32700,60200,22500],
            ["Féculents",15990,16350,36000],
            ["Fruits et légumes",64200,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,10440],
            ["Produits gras sucrés salés",1875,33775,3375],
            ["Matières grasses ajoutées",0,0,5250],
            ["Produits laitiers",32700,60200,23250],
            ["Féculents",15990,16350,36750],
            ["Fruits et légumes",65300,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,10800],
            ["Produits gras sucrés salés",1875,33775,3450],
            ["Matières grasses ajoutées",0,0,5325],
            ["Produits laitiers",32700,60200,24000],
            ["Féculents",15990,16350,37500],
            ["Fruits et légumes",66500,68000,0]
            ]
         },
         {
            "nb_meals":1,
            "meal_price":8.955000000000002,
            "categ_bought":[
               ["Viande, poisson, oeufs",13450,13610,11160],
            ["Produits gras sucrés salés",1875,33775,3525],
            ["Matières grasses ajoutées",0,0,5400],
            ["Produits laitiers",32700,60200,24750],
            ["Féculents",15990,16350,38250],
            ["Fruits et légumes",67700,68000,0]]}]
   }

    print json.dumps(test_result)


if __name__ == '__main__':
    main()
