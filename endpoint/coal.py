from fastapi import APIRouter, Request, HTTPException
from setting import *
from utility import *
from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from enum import Enum, IntEnum

router=APIRouter(tags=["coal"])

#scehema
#1 coal filter
class coal_filter(BaseModel):
   grade_id:Optional[int]
   origin_id:Optional[int]
   port_id:Optional[int]


class coal_selling_price(BaseModel):
   competitor_price:float
   base_price:float
   index_price:float
   grade_id:int
   port_id:int
   origin_id:int




#endpoint
#1 coal details
@router.post("/coal/stock")
async def coal_stock_detail(request:Request,limit:int,offset:int,payload:coal_filter):
   #prework
   payload=payload.dict()   
   #query set
   query="""select * from tbl_coal_purchase_detail where grade_id=:grade_id and port_id=:port_id and origin_id=:origin_id limit:limit offset:offset"""
   values={"grade_id":payload['grade_id'],"port_id":payload['port_id'],"origin_id":payload['origin_id'],"limit":limit,"offset":offset}
   #query run
   response=await database_fetch_all(query,values)
   if response["status"]=="false":
      raise HTTPException(status_code=401,detail=response)

   return response


#2 coal grade
@router.get("/coal/grade")
async def coal_grade(request:Request,limit:int,offset:int):
   #prework
   payload=payload.dict()   
   #query set
   query="""select * from tbl_coal_grade limit:limit offset:offset"""
   values={"limit":limit,"offset":offset}
   #query run
   response=await database_fetch_all(query,values)
   if response["status"]=="false":
      raise HTTPException(status_code=401,detail=response)

   return response



#3 coal origin
@router.get("/coal/origin")
async def coal_origin(request:Request,limit:int,offset:int):
   #prework
   payload=payload.dict()   
   #query set
   query="""select * from tbl_coal_origin limit:limit offset:offset"""
   values={"limit":limit,"offset":offset}
   #query run
   response=await database_fetch_all(query,values)
   if response["status"]=="false":
      raise HTTPException(status_code=401,detail=response)

   return response



#3 coal port
@router.get("/coal/port")
async def coal_port(request:Request,limit:int,offset:int):
   #prework
   payload=payload.dict()   
   #query set
   query="""select * from tbl_coal_port limit:limit offset:offset"""
   values={"limit":limit,"offset":offset}
   #query run
   response=await database_fetch_all(query,values)
   if response["status"]=="false":
      raise HTTPException(status_code=401,detail=response)

   return response



#4 coal competitor 
@router.post("/coal/competitor")
async def coal_competitor(request:Request,limit:int,offset:int,payload:coal_filter):
   #prework
   payload=payload.dict()   
   #query set
   query="""select * from tbl_coal_competitor where grade_id=:grade_id and port_id=:port_id and origin_id=:origin_id limit:limit offset:offset"""
   values={"grade_id":payload['grade_id'],"port_id":payload['port_id'],"origin_id":payload['origin_id'],"limit":limit,"offset":offset}
   #query run
   response=await database_fetch_all(query,values)
   if response["status"]=="false":
      raise HTTPException(status_code=401,detail=response)

   return response



#4 coal price calculation 
@router.post("/coal/selling-price")
async def coal_selling_price(request:Request,payload:coal_selling_price):
   #prework
   payload=payload.dict()   

   handling_charge = 300 #inr
   other_cost = 100 #inr
   premium_cost = 3 #usd
   fright_cost = 8 #usd
   exchange_rate_usd_inr = 76 #inr

   total_expense = handling_charge + other_cost + (premium_cost*exchange_rate_usd_inr) + (fright_cost*exchange_rate_usd_inr)

   base_price = payload['base_price']
   index_price = payload['index_price']
   competitor_price = payload['competitor_price']

   total_expense = handling_charge + other_cost + (premium_cost*exchange_rate_usd_inr) + (fright_cost*exchange_rate_usd_inr)

   normal_price = base_price+total_expense
   
   # business logic
   if normal_price < competitor_price and normal_price < index_price:

      if competitor_price < index_price:
         price_diff = competitor_price - normal_price
         minimum_sale_margin = (price_diff*0.5)/100

         for x in range(int(price_diff//minimum_sale_margin)):
               print(competitor_price - ((x+1)*minimum_sale_margin))
               selling_price_one = competitor_price - ((x+1)*minimum_sale_margin)
               if normal_price <= selling_price_one:
                  print(selling_price_one)
                  break
   
   if normal_price > competitor_price:
      selling_price_one = normal_price

   if normal_price > index_price:
      selling_price_one = index_price

   #query set
   query="""insert into tbl_coal_sale_price (grade_id,origin_id,port_id,base_price,sale_price,handling_charge,other_cost,premium_cost,fright_cost,rate_usd_inr) values (:grade_id,:origin_id,:port_id,:base_price,:sale_price,:handling_charge,:other_cost,:premium_cost,:fright_cost,:rate_usd_inr) returning *"""

   values={"grade_id":payload['grade_id'],"origin_id":payload['origin_id'],"port_id":payload['port_id'],"base_price":payload['base_price'],"sale_price":selling_price_one,"handling_charge":handling_charge,"other_cost":other_cost,"premium_cost":premium_cost,"fright_cost":fright_cost,"rate_usd_inr":exchange_rate_usd_inr}
   #query run
   response=await database_execute(query,values)
   if response["status"]=="false":
      raise HTTPException(status_code=400,detail=response)


   response = {"best-selling-price":selling_price_one}
   return response                  



         

