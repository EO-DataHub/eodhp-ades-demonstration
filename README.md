# eodhp-ades-demonstration

### Jupyter Notebook and HTTP files to test and demonstrate ADES deployment via OGC API endpoints, including two example OGC Application Packages that can be run

## Prerequisites

To run the HTTP files, it is recomended you use the REST Client extension (id:humao.rest-client) in VS Code which allows you to send http requests directly from the IDE and see the responses in a side panel.  
Before using either of the provided example formats ensure you provide the user and password for the running ADES endpoint to gain access to the API.

## Application Packages

Currently we provide two examples of OGC Application Packages, both provided as part of the [EOEPCA deployment guide](https://github.com/EOEPCA/deployment-guide). Both processes resize images, provided either as a URL or a STAC item, by a given scale-percentage.

## Pre-production Implementation

Note, the examples in this repository are provided to demonstrate an initial version of the ADES being deployed to the EODH Platform and this is not representative of a final production release. We expect there to be further fine tuning to improve the integration here. If you do encounter any issues with a process not starting to execute, we recommend first deleting the process from the workspace using the **undeployProcess** function and then redeploying it again.
