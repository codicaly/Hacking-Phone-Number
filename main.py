import phonenumbers
from phonenumbers import timezone,geocoder,carrier

print("---Phone Number Details Extractor---") #@codicaly
number = input("Enter the Phone number with country code : ")

phoneNumber = phonenumbers.parse(number)
timeZone = timezone.time_zones_for_number(phoneNumber)
serviceProvider = carrier.name_for_number(phoneNumber,'en')
if serviceProvider == '':
    serviceProvider = "Can't be found"
Nation = geocoder.description_for_number(phoneNumber,'en')

print("\nTime Zone : ",timeZone)
print("Service Provider : ",serviceProvider)
print("Nation : ",Nation)
