# eodhp-ades-demonstration

### Jupyter Notebook and HTTP files to test and demonstrate ADES deployment via OGC API endpoints, including two example OGC Application Packages that can be run

## Prerequisites

To run the HTTP files, it is recomended you use the REST Client extension (id:humao.rest-client) in VS Code which allows you to send http requests directly from the IDE and see the responses in a side panel.  
Before using either of the provided example formats ensure you provide the user and password for the running ADES endpoint to gain access to the API.

## Application Packages

Currently we provide two examples of OGC Application Packages, both provided as part of the [EOEPCA deployment guide](https://github.com/EOEPCA/deployment-guide). Both processes resize images, provided either as a URL or a STAC item, by a given scale-percentage.
