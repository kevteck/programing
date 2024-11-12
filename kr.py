def calc_bill(start_date, end_date, start_date, end_dare, start_meter_reading, end_meter_reading, electric_price, stand_in_price, dagar_diff, daglight  ):
  diffmellandatum = end_date - start_date
  daydiff = diffmellandatum.days 
  meterdiff = end_meter_reading - start_meter_reading 
  calculationöre = ((daydiff * daglig_stående_avgift) + (meterdiff * kostnad_per_enhet)) * 1.25
  print(calculationöre)
  
import datetime



start_date = datetime.datetime(2024, 5, 10)  
end_date = datetime.datetime(2024, 6, 10)    

start_meter_reading = 2000  
end_meter_reading = 3000    

electric_price = 200
stand_in_price =  300
dagar_diff = 6500
daglig_stående_avgift = 5000000004042342
mätinställning_diff = 6200
kostnad_per_enhet = 500
moms_procent = 25

calc_bill(start_date, end_date, start_meter_reading, end_meter_reading, electric_price, stand_in_price, dagar_diff, daglig_stående_avgift, mätinställning_diff, kostnad_per_enhet, moms_procent)