import reflex as rx
from dotenv import load_dotenv

load_dotenv()
import os


class ReflexappConfig(rx.Config):
    """Additional configuration parameters"""

    # Specify GA or workbench/BAM - TBD
    watsonx_type: str = os.getenv("watsonx_type")  # ga or workbench

    # IAM API key for GA, Standard APIkey for workbench
    watsonx_api_key: str = os.getenv("watsonx_api_key")

    ### Depends if using GA or Workbench
    watsonx_api_endpoint: str = os.getenv("watsonx_api_endpoint")

    # Optional - not needed if using workbench
    watsonx_project_id: str = os.getenv("watsonx_project_id")

    # bam = 'https://bam-api.res.ibm.com'
    # workbench = 'https://workbench-api.res.ibm.com'
    watsonx_workbench_api_key: str = os.getenv("watsonx_workbench_api_key")

    ### Depends if using GA or Workbench
    watsonx_workbench_api_endpoint: str = os.getenv("watsonx_workbench_api_endpoint")


config = ReflexappConfig(
    app_name="app",
)
