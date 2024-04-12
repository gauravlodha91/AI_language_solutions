from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os



def getAzureSecret(secret_name):

    try: 

        load_dotenv()
        vault_url = os.environ["AZURE_VAULT_KEY"]
        client_id = os.environ['AZURE_CLIENT_ID']
        tenant_id = os.environ['AZURE_TENANT_ID']
        client_secret = os.environ['AZURE_CLIENT_SECRET']
        

        
        credentials = ClientSecretCredential(
            client_id = client_id, 
            client_secret= client_secret,
            tenant_id= tenant_id
        )

        secret_client = SecretClient(vault_url= vault_url, credential= credentials)

        temp = secret_client.get_secret(secret_name)
        if temp:
           return temp.value
        else: 
            raise Exception 

    except:
        return("Issue in login with Azure")    



def res1(document):
    endpoint = getAzureSecret("AZURE-LANGUAGE-ENDPOINT")
    key =      getAzureSecret("Azure-Language-Key")

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    result = text_analytics_client.analyze_sentiment(document, show_opinion_mining=True)[0]
    print("Text Sentiments: ",result.sentiment)
    print("Positive Score : ",result.confidence_scores.positive)
    print("Negative Score : ", result.confidence_scores.negative)
    print("Neutral Score : ", result.confidence_scores.neutral)
    
    dictt = { "Text": document[0] ,"Text Sentiments": result.sentiment, "Positive Score" : result.confidence_scores.positive,
            "Negative Score" : result.confidence_scores.negative, "Neutral Score": result.confidence_scores.neutral}
    return dictt



