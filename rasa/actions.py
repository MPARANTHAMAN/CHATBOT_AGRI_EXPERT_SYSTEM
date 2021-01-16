# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import urllib.request
import json
from typing import Any, Text, Dict, List, Union
from weather import Weather

from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher


from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, UserUtteranceReverted, \
                                 ConversationPaused

logger = logging.getLogger(__name__)



#from typing import Any, Text, Dict, List

#from rasa_sdk import Action, Tracker
#from rasa_sdk.ejhxecutor import CollectingDispatcher



        



class ActionGreet(Action):
    
	def name(self):
		return "action_greet"

	def run(self, dispatcher, tracker, domain):
		
		person_name = next(tracker.get_latest_entity_values('person_name'), None)
		dispatcher.utter_message("Nice to meet you "+ person_name+ " How can I help you ?")
		
		return [SlotSet("person_name", person_name)]

class ActionBye(Action):

	def name(self):
		return "action_bye"

	def run(self, dispatcher, tracker, domain):
		person_name = tracker.get_slot('person_name')
		dispatcher.utter_message("See you soon "+ person_name)
		
		return []


class ActionWeatherApi(Action):
    
    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        temp=int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp",tracker,temp=temp)

        return []

class ActionGreetUser(Action):
     
    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        dispatcher.utter_message("Hello, Welcome to CAES how can i help you")

        return [UserUtteranceReverted()]         
     

class ActionSugarcane(Action):
    
    def name(self) -> Text:
        return "action_sugarcane"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sugarcane or sugar cane refer to several species and hybrids of tall perennial grasses in the genus Saccharum, tribe Andropogoneae, that are used for sugar production. ")

        return [UserUtteranceReverted()]


class ActionPaddy(Action):
    
    def name(self) -> Text:
        return "action_paddy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/paddy/Index.html" 
        dispatcher.utter_template("utter_rice_plant",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionNationalInstitutions(Action):

    def name(self) -> Text:
        return "action_national_institutions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://agritech.tnau.ac.in/expert_system/sugar/institution&schemes.html#2" 
        dispatcher.utter_template("utter_National_Institutions",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionSugarcaneResearchStation(Action):

    def name(self) -> Text:
        return "action_sugarcane_research_station"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://agritech.tnau.ac.in/expert_system/sugar/institution&schemes.html#3" 
        dispatcher.utter_template("utter_Sugarcane_Research_Station",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []
                               

class ActionMarketing(Action):

    def name(self) -> Text:
        return "action_marketing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/marketing.html" 
        dispatcher.utter_template("utter_Marketing",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionHarvestingProcess(Action):

    def name(self) -> Text:
        return "action_harvesting_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/harvesting.html#1" 
        dispatcher.utter_template("utter_Harvesting_Process",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionTypesHarvesting(Action):

    def name(self) -> Text:
        return "action_types_harvesting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/harvesting.html#2" 
        dispatcher.utter_template("utter_Types_Harvesting",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionMaturitySymptomsHarvestingPeriod(Action):

    def name(self) -> Text:
        return "action_maturity_symptoms_harvesting_period"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/harvesting.html#3" 
        dispatcher.utter_template("utter_Maturity_symptoms_Harvesting_period",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionProcessingSugarcane(Action):

    def name(self) -> Text:
        return "action_processing_sugarcane"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/harvesting.html#4" 
        dispatcher.utter_template("utter_Processing_Sugarcane",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionHarvestingProducts(Action):

    def name(self) -> Text:
        return "action_harvesting_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/harvesting.html#5" 
        dispatcher.utter_template("utter_Harvesting_Products",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return [] 


class ActionDiseaseManagement(Action):

    def name(self) -> Text:
        return "action_disease_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cropprotection.html#2" 
        dispatcher.utter_template("utter_Disease_Management",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionPestManagement(Action):

    def name(self) -> Text:
        return "action_pest_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cropprotection.html#1" 
        dispatcher.utter_template("utter_Pest_Management",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionRoleNutrient(Action):

    def name(self) -> Text:
        return "action_role_nutrient"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/nutrientmanagement.html#2" 
        dispatcher.utter_template("utter_Role_Nutrient",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionNutrientApplication(Action):

    def name(self) -> Text:
        return "action_nutrient_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/nutrientmanagement.html#3" 
        dispatcher.utter_template("utter_Nutrient_Application",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionOrganicManure(Action):

    def name(self) -> Text:
        return "action_organic_manure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/nutrientmanagement.html#4" 
        dispatcher.utter_template("utter_Organic_Manure",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionNutritionalDisorder(Action):

    def name(self) -> Text:
        return "action_nutritional_disorder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/nutrientmanagement.html#5" 
        dispatcher.utter_template("utter_Nutritional_Disorder",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionIntegrated_Nutrient_Management(Action):

    def name(self) -> Text:
        return "action_Integrated_Nutrient_Management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/nutrientmanagement.html#6" 
        dispatcher.utter_template("utter_Integrated_Nutrient_Management",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionFertilizerRequirements(Action):

    def name(self) -> Text:
        return "action_fertilizer_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/nutrientmanagement.html#7" 
        dispatcher.utter_template("utter_Fertilizer_Requirements",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionWaterRequirement(Action):

    def name(self) -> Text:
        return "action_water_requirement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/irrigationmanagement.html#1" 
        dispatcher.utter_template("utter_Water_requirement",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionIrrigationMethods(Action):

    def name(self) -> Text:
        return "action_irrigation_methods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/irrigationmanagement.html#5" 
        dispatcher.utter_template("utter_Irrigation_Methods",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionDripIrrigation(Action):

    def name(self) -> Text:
        return "action_drip_irrigation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/irrigationmanagement.html#2" 
        dispatcher.utter_template("utter_Drip_irrigation",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionFertigation(Action):

    def name(self) -> Text:
        return "action_fertigation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/irrigationmanagement.html#3" 
        dispatcher.utter_template("utter_Fertigation",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionDroughtManagement(Action):

    def name(self) -> Text:
        return "action_drought_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/irrigationmanagement.html#4" 
        dispatcher.utter_template("utter_Drought_management",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionSustainableSugarcaneInitiative(Action):

    def name(self) -> Text:
        return "action_sustainable_sugarcane_initiative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/ssi.html" 
        dispatcher.utter_template("utter_Sustainable_Sugarcane_Initiative",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []


class ActionLandPreparation(Action):

    def name(self) -> Text:
        return "action_land_preparation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cultivationpractices.html#1" 
        dispatcher.utter_template("utter_Land_Preparation",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionInterculturalOperation(Action):

    def name(self) -> Text:
        return "action_intercultural_operation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cultivationpractices.html#7" 
        dispatcher.utter_template("utter_Intercultural_Operation",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionMethodPlanting(Action):

    def name(self) -> Text:
        return "action_method_planting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cultivationpractices.html#8" 
        dispatcher.utter_template("utter_Method_Planting",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionWeedManagement(Action):

    def name(self) -> Text:
        return "action_weed_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cultivationpractices.html#9" 
        dispatcher.utter_template("utter_Weed_Management",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionRatoonManagement(Action):

    def name(self) -> Text:
        return "action_ratoon_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/cultivationpractices.html#10" 
        dispatcher.utter_template("utter_Ratoon_Management",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionParticularsVarieties(Action):

    def name(self) -> Text:
        return "action_particulars_varieties"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#4" 
        dispatcher.utter_template("utter_Particulars_varieties",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionMorphologicalCharacters(Action):

    def name(self) -> Text:
        return "action_morphological_characters"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#5" 
        dispatcher.utter_template("utter_Morphological_characters",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionSeasonWiseSuitableVarieties(Action):

    def name(self) -> Text:
        return "action_season_wise_suitable_varieties"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#6" 
        dispatcher.utter_template("utter_Season_wise_suitable_varieties",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionSuitableVarietiesTamilNadu(Action):

    def name(self) -> Text:
        return "action_suitable_varieties_tamilNadu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#7" 
        dispatcher.utter_template("utter_Suitable_varieties_TamilNadu",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionNewVarietiesSugarcane(Action):

    def name(self) -> Text:
        return "action_new_varieties_sugarcane"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#8" 
        dispatcher.utter_template("utter_New_varieties_sugarcane",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionImportantVarietyPerformance(Action):

    def name(self) -> Text:
        return "action_important_variety_performance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#9" 
        dispatcher.utter_template("utter_Important_variety_performance",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []


class ActionSuitableVarietiesKerala(Action):

    def name(self) -> Text:
        return "action_suitable_varieties_kerala"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#10" 
        dispatcher.utter_template(" utter_Suitable_varieties_Kerala",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionSuitableVarietiesKarnataka(Action):

    def name(self) -> Text:
        return "action_Suitable_varieties_karnataka"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/season&varieties.html#11" 
        dispatcher.utter_template("utter_Suitable_varieties_Karnataka",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionClimaticFactor(Action):

    def name(self) -> Text:
        return "action_climatic_factor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/botany&climate.html#5" 
        dispatcher.utter_template("utter_Climatic_factor",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []

class ActionBotanicalDescription(Action):

    def name(self) -> Text:
        return "action_botanical_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/botany&climate.html#4" 
        dispatcher.utter_template("utter_Botanical_Description",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []   

class ActionVernacularNames(Action):

    def name(self) -> Text:
        return "action_vernacular_names"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        Link="http://www.agritech.tnau.ac.in/expert_system/sugar/botany&climate.html#1" 
        dispatcher.utter_template("utter_Vernacular_Names",tracker,link=Link) 
        # dispatcher.utter_message(text="Hello World!")

        return []  



		



