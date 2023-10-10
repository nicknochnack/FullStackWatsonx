# Import base deps
import reflex as rx 
from pydantic import BaseModel
# Import IBM Gen 
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM

# Get reflex config
config = rx.config.get_config()

class WatsonxLangchainLLM(BaseModel): 
    
    generate_params: dict = { GenParams.MAX_NEW_TOKENS: 25 }

    model_id: str = "google/flan-ul2"


    def from_pretrained(self):

        model = Model(
            model_id=self.model_id,
            credentials={
                "apikey": config.watsonx_api_key,
                "url": config.watsonx_api_endpoint
            },
            params=self.generate_params,
            project_id=config.watsonx_project_id
        )

        llm = WatsonxLLM(model=model)
        return llm 
