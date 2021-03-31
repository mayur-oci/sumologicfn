

# Monitor Oracle Cloud Infrastructure with Datadog

## Introduction

The Oracle Cloud  [Observability and Manageability platform](https://blogs.oracle.com/cloud-infrastructure/announcing-the-oracle-cloud-observability-and-management-platform)  aims to meet our customers where they are. We understand that they have standardized their operational postures with popular 3rd party Observability tools and we want to be interoperable with those tools so our customers can continue using the tools they have invested in with Oracle Cloud Infrastructure.

In this tutorial, we will walk you through how you can move logs from Oracle Cloud Infrastructure into  [Datadog](https://www.sumologic.com/). Datadog is a popular Observability tool that provides monitoring and security services that provide full visibility into your applications.

Our solution architecture at high level is as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/sl_archi.png?raw=true)

## Create a Custom HTTP Source Collector in Sumologic

In Sumologic account, you need to create [HTTP custom collector app](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source) as described in the steps below.

1. Click on the  *Setup Wizard* as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/1sl.png?raw=true)

2. Click on the option of *Start streaming data to Sumo Logic* as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/2sl.png?raw=true)

3. Click on the option *Your custom app* as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/3sl.png?raw=true)

4. Click on the option *HTTPS Source*
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/4sl.png?raw=true)

5. Configure your *HTTP Source* as shown below. Note *Source Category* is custom and depends on your application needs. It is a metadata tag, stored with your logs and is usefull when searching logs later in *Sumologic*, one ingested. Loglines we  are going to start with timestamps, hence we also choose the option *Use time zone from log file*.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/6sl.png?raw=true)

6. As you move to the next screen, we get the HTTPS endpoint for our logs to upload from OCI, using *POST* HTTP call, as shown below. 
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/8sl.png?raw=true)

## Configure the logs you want to capture

1. In the Oracle Cloud Infrastructure console, click the Navigation menu, select **Log Groups** under the **Logging** menu.

2. To create a log group, click **Create Log Group**.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/loggroupSL0.png?raw=true)

3. Select your compartment, add a name **LogGroupForBucketActivity,** and a **description**.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/loggroupsl.png?raw=true)

4. After you create **Log Group**, select **Logs** in the left menu. You will see screen similar to shown below.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/enableLogs2fs.png?raw=true)

5. Click **Enable Service Log**, fill our the dialog box and click **Enable Log**. Select **Log Category** on Service.

-   Resource: Enter the log that you will use as a resource.
-   Log name: Enter a name for your log, for example,  **logForBucketActivity**.

Fill the rest of the fields appropriately. Refer to this example, in which Oracle Object Store with a bucket name  **BucketForSumoLogic**  is shown. Make sure you select loggroup **LogGroupForBucketActivity** for the log, you just created in previous step.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/enableObjectLogs.png?raw=true)

Now everytime a object is uploaded to bucket **BucketForSumoLogic**, logentry will be added to log **logForBucketActivity**. 

## Configure Oracle Function for ingesting logs into SumoLogic

1.  Click on the Navigation menu and then select the **Solution and Platform**  section. Select **Functions**  under the **Developer Services**  menu.  
    
2.  Click  **Create Application**  and enter a name, for example,  **sumologicFnApp**. 
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/fnApp.png?raw=true)
3. Once you create the  **Application**, click your application name and select **Getting Started**  on the left menu.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/cloudShell.png?raw=true)

4.  Launch Cloud Shell.
5.  Use the context for your region.
    ```Shell
    fn list context
    fn use context us-ashburn-1
    ```
6. Update the context with the function’s compartment ID.    
	```Shell
    fn update context oracle.compartment-id <compartment-id>
	```
7. Update the context with the location of the Registry you want to use.
	```Shell
    fn update context registry iad.ocir.io/<tenancy_name>/[YOUR-OCIR-REPO]
	```
	   Replace iad with the three-digit region code.
8. Assuming you have created the [Auth Token](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm#Generate_an_Auth_Token_to_Enable_Login_to_Oracle_Cloud_Infrastructure_Registry) already, log into the Registry using the **Auth Token** as your password.
	```Shell
    docker login iad.ocir.io
	```
Replace iad with the three-digit region code.
You are prompted for the following information:

-   Username: <tenancyname>/<username>
-   Password: Create a password

**Note**: If you are using Oracle Identity Cloud Service, your username is <tenancyname>/oracleidentitycloudservice/<username>.	

9.  Generate a ‘hello-world’ boilerplate function.
	```Shell
    fn init --runtime python sumologicfn
	``` 
	The  **fn init**  command will generate a folder called  **datadog**  with 3 files inside;  **func.py**,  **func.yaml,**  and **requirements.txt**.

Open  **func.py**  and replace the content of the file with the following code

	

    

# Monitor Oracle Cloud Infrastructure with Datadog

## Introduction

The Oracle Cloud  [Observability and Manageability platform](https://blogs.oracle.com/cloud-infrastructure/announcing-the-oracle-cloud-observability-and-management-platform)  aims to meet our customers where they are. We understand that they have standardized their operational postures with popular 3rd party Observability tools and we want to be interoperable with those tools so our customers can continue using the tools they have invested in with Oracle Cloud Infrastructure.

In this tutorial, we will walk you through how you can move logs from Oracle Cloud Infrastructure into  [Datadog](https://www.sumologic.com/). Datadog is a popular Observability tool that provides monitoring and security services that provide full visibility into your applications.

Our solution architecture at high level is as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/sl_archi.png?raw=true)

## Create a Custom HTTP Source Collector in Sumologic

In Sumologic account, you need to create [HTTP custom collector app](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source) as described in the steps below.

1. Click on the  *Setup Wizard* as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/1sl.png?raw=true)

2. Click on the option of *Start streaming data to Sumo Logic* as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/2sl.png?raw=true)

3. Click on the option *Your custom app* as shown below
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/3sl.png?raw=true)

4. Click on the option *HTTPS Source*
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/4sl.png?raw=true)

5. Configure your *HTTP Source* as shown below. Note *Source Category* is custom and depends on your application needs. It is a metadata tag, stored with your logs and is usefull when searching logs later in *Sumologic*, one ingested. Loglines we  are going to start with timestamps, hence we also choose the option *Use time zone from log file*.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/6sl.png?raw=true)

6. As you move to the next screen, we get the HTTPS endpoint for our logs to upload from OCI, using *POST* HTTP call, as shown below. 
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/8sl.png?raw=true)

## Configure the logs you want to capture

1. In the Oracle Cloud Infrastructure console, click the Navigation menu, select **Log Groups** under the **Logging** menu.

2. To create a log group, click **Create Log Group**.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/loggroupSL0.png?raw=true)

3. Select your compartment, add a name **LogGroupForBucketActivity,** and a **description**.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/loggroupsl.png?raw=true)

4. After you create **Log Group**, select **Logs** in the left menu. You will see screen similar to shown below.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/enableLogs2fs.png?raw=true)

5. Click **Enable Service Log**, fill our the dialog box and click **Enable Log**. Select **Log Category** on Service.

-   Resource: Enter the log that you will use as a resource.
-   Log name: Enter a name for your log, for example,  **logForBucketActivity**.

Fill the rest of the fields appropriately. Refer to this example, in which Oracle Object Store with a bucket name  **BucketForSumoLogic**  is shown. Make sure you select loggroup **LogGroupForBucketActivity** for the log, you just created in previous step.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/enableObjectLogs.png?raw=true)

Now everytime a object is uploaded to bucket **BucketForSumoLogic**, logentry will be added to log **logForBucketActivity**. 

## Configure Oracle Function for ingesting logs into SumoLogic

1.  Click on the Navigation menu and then select the **Solution and Platform**  section. Select **Functions**  under the **Developer Services**  menu.  
    
2.  Click  **Create Application**  and enter a name, for example,  **sumologicFnApp**. 
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/fnApp.png?raw=true)
3. Once you create the  **Application**, click your application name and select **Getting Started**  on the left menu.
![enter image description here](https://github.com/mayur-oci/sumologic/blob/main/cloudShell.png?raw=true)

4.  Launch Cloud Shell.
5.  Use the context for your region.
    ```Shell
    fn list context
    fn use context us-ashburn-1
    ```
6. Update the context with the function’s compartment ID.    
	```Shell
    fn update context oracle.compartment-id <compartment-id>
	```
7. Update the context with the location of the Registry you want to use.
	```Shell
    fn update context registry iad.ocir.io/<tenancy_name>/[YOUR-OCIR-REPO]
	```
	   Replace iad with the three-digit region code.
8. Assuming you have created the [Auth Token](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm#Generate_an_Auth_Token_to_Enable_Login_to_Oracle_Cloud_Infrastructure_Registry) already, log into the Registry using the **Auth Token** as your password.
	```Shell
    docker login iad.ocir.io
	```
Replace iad with the three-digit region code.
You are prompted for the following information:

-   Username: <tenancyname>/<username>
-   Password: Create a password

**Note**: If you are using Oracle Identity Cloud Service, your username is <tenancyname>/oracleidentitycloudservice/<username>.	

Verify your setup by listing applications in the compartment
        ```
			fn list apps
    ```

9.  Generate a ‘hello-world’ boilerplate function.
 
	```Shell
    fn init --runtime python sumologicfn
	``` 
	The  **fn init**  command will generate a folder called  **sumologicfn**  with 3 files inside;  **func.py**,  **func.yaml,**  and **requirements.txt** .

Open  **func.py**  and replace the content of the file with the following code:

```Python
import io
import json
import logging
import os

import requests
from fdk import response

# This method is the entrypoint for your Function invokation 
# aka the method invoked by the OCI Fn platform
# it will receive the list of log entries from OCI as input in the form of bytestream
# the method name will be defined in func.yml
def handler(ctx, data: io.BytesIO = None):
    logger = logging.getLogger()
    logger.info("function start")

    # Sumologic endpoint URL to upload OCI logs to HTTP custom app.
    # this value will be defined defined in func.yaml
    sumologic_endpoint = os.environ['SUMOLOGIC_ENDPOINT']

    # Retrieving the log entrie(s) via Service Connector Hub as part of the Function call payload
    try:
        logentries = json.loads(data.getvalue()) # deserialize the bytesstream input as JSON array
        if not isinstance(logentries, list):
            logger.error('Invalid connector payload. No log queries detected')
            raise
            
        # Optional...log the input to the function as human readble JSON. 
        # Not to be used in production
        logger.info("json input from SCH")
        logger.info(data.getvalue()) 

        # loop through the logs one by one
        for logEntry in logentries: 
            logger.info("Extracting/Parse log details from the log entry json")
            event_name = logEntry["data"]["requestResourcePath"] + '\t'
            time_of_event = logEntry["time"] + '\t'
            cmpt_name = logEntry["data"]["compartmentName"] + '\t'
            bucket_namespace = logEntry["data"]["namespaceName"] + '\t'
            bucket_name = logEntry["data"]["bucketName"] + '\t'
            request_action = logEntry["data"]["requestAction"]

            log_line = time_of_event + event_name + cmpt_name + \
                        bucket_namespace + bucket_name + request_action

            # Call the Sumologic with the payload and ingest the OCI logs
            headers = {'Content-type': 'text/plain'}
            response_from_sumologic = requests.post(sumologic_endpoint,
                                                    data=log_line,
                                                    headers=headers)
            logging.getLogger().info(response_from_sumologic.text)

        logger.info("function end")
        return

    except Exception as e:
         logger.error("Failure in the function: {}".format(str(e)))
         raise
```
For information about the format of the logs generated by the Oracle Cloud Infrastructure Logging service, see [Logging Format Overview.](https://docs.cloud.oracle.com/en-us/iaas/Content/Logging/Reference/top_level_logging_format.htm#top_level_logging_format)    
    
10.  Replace **func.yml** contents as follows
```yml
   	schema_version: 20180708
		name: sumologicfn
		version: 0.0.1
		runtime: python
		entrypoint: /python/bin/fdk /function/func.py handler
		memory: 1024
        timeout: 120
		config:
		  SUMOLOGIC_ENDPOINT: [YOUR SUMOLOGIC API ENDPOINT URL HERE]
```

12. Replace **requirements.txt** contents as follows

    ```
    	fdk
        requests
    ```
13. Deploy your function
    ```
     fn -v deploy --app sumologicFnApp --no-bump
    ```

## Create a Service Connector for reading logs from Logging and triggering the Function

1.  Click the Navigation menu, and select the **Solution and Platform**  section. Select **Service Connectors**  under the **Logging**  menu.  
    
2.  Click  **Create Connector**  and select the source as Logging and Target as Functions.  
    
3.  On  **Configure Source Connection**  select your compartment name, your log group  **datadog_log_group**, and your logs  **datadog**.  
    
4.  If you want to use audit logs click on  **+Another log**  button, choose your compartment and add  **_Audit**  for Log Group.
