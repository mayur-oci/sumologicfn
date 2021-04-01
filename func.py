import io
import json
import logging
import os

import requests
from fdk import response

#
# oci-logs-export-python version 1.0.
#
# Copyright (c) 2021 Oracle, Inc.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

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
