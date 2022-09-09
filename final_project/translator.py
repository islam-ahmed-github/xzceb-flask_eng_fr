import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
api_key = '9gEW9sNI-hZIiE-7RFCCfiSETDHLZYn8ZfbokjriCpwj'
api_url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/5236f27f-ae76-4f61-945e-88bc5533ca4b'
 



# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3( version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(api_url )



def Translate_en_to_fr(enstr):
  return language_translator.translate(enstr,'fr-it').get_result()


def Translate_fr_to_en(frstr):
  return language_translator.translate(frstr,'en-it').get_result()
