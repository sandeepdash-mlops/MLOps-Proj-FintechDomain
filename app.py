from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import FintechData, FintechDataClassifier
from src.pipline.training_pipeline import TrainPipeline

# Initialize FastAPI application
app = FastAPI()

# Mount the 'static' directory for serving static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine for rendering HTML templates
templates = Jinja2Templates(directory='templates')

# Allow all origins for Cross-Origin Resource Sharing (CORS)
origins = ["*"]

# Configure middleware to handle CORS, allowing requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    """
    DataForm class to handle and process incoming form data.
    This class defines the fintech-related attributes expected from the form.
    """
    def __init__(self, request: Request):
        self.request: Request = request
        self.Gender: Optional[int] = None
        self.Age: Optional[int] = None
        self.KYC_Verified: Optional[int] = None
        self.Region_Code: Optional[float] = None
        self.Previously_Onboarded: Optional[int] = None
        self.Avg_Txn_Amt: Optional[float] = None
        self.Payment_Channel: Optional[float] = None
        self.Vintage: Optional[int] = None
        self.Account_Tenure_lt_1_Year: Optional[int] = None
        self.Account_Tenure_gt_2_Years: Optional[int] = None
        self.Chargeback_History_Yes: Optional[int] = None
                

    async def get_fintech_data(self):
        """
        Method to retrieve and assign form data to class attributes.
        This method is asynchronous to handle form data fetching without blocking.
        """
        form = await self.request.form()
        self.Gender = form.get("Gender")
        self.Age = form.get("Age")
        self.KYC_Verified = form.get("KYC_Verified")
        self.Region_Code = form.get("Region_Code")
        self.Previously_Onboarded = form.get("Previously_Onboarded")
        self.Avg_Txn_Amt = form.get("Avg_Txn_Amt")
        self.Payment_Channel = form.get("Payment_Channel")
        self.Vintage = form.get("Vintage")
        self.Account_Tenure_lt_1_Year = form.get("Account_Tenure_lt_1_Year")
        self.Account_Tenure_gt_2_Years = form.get("Account_Tenure_gt_2_Years")
        self.Chargeback_History_Yes = form.get("Chargeback_History_Yes")

# Route to render the main page with the form
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page for fintech data input.
    """
    return templates.TemplateResponse(
            "fintechdata.html",{"request": request, "context": "Rendering"})

# Route to trigger the model training process
@app.get("/train")
async def trainRouteClient():
    """
    Endpoint to initiate the model training pipeline.
    """
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful!!!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

# Route to handle form submission and make predictions
@app.post("/")
async def predictRouteClient(request: Request):
    """
    Endpoint to receive form data, process it, and make a prediction.
    """
    try:
        form = DataForm(request)
        await form.get_fintech_data()
        
        fintech_data = FintechData(
                                Gender= form.Gender,
                                Age = form.Age,
                                KYC_Verified = form.KYC_Verified,
                                Region_Code = form.Region_Code,
                                Previously_Onboarded = form.Previously_Onboarded,
                                Avg_Txn_Amt = form.Avg_Txn_Amt,
                                Payment_Channel = form.Payment_Channel,
                                Vintage = form.Vintage,
                                Account_Tenure_lt_1_Year = form.Account_Tenure_lt_1_Year,
                                Account_Tenure_gt_2_Years = form.Account_Tenure_gt_2_Years,
                                Chargeback_History_Yes = form.Chargeback_History_Yes
                                )

        # Convert form data into a DataFrame for the model
        fintech_df = fintech_data.get_fintech_input_data_frame()

        # Initialize the prediction pipeline
        model_predictor = FintechDataClassifier()

        # Make a prediction and retrieve the result
        value = model_predictor.predict(dataframe=fintech_df)[0]

        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Response-Yes" if value == 1 else "Response-No"

        # Render the same HTML page with the prediction result
        return templates.TemplateResponse(
            "fintechdata.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}

# Main entry point to start the FastAPI server
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)