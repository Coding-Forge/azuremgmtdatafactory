# azuremgmtdatafactory

Update Data Factory pipelines using azure-mgmt-datafactory

This project is looking at two ways to update the pipeline for Azure Data Factory. The first process is looking at leveraging the Azure Mgmt datafactory python package. This will allow anyone to connect to an Azure Data Factory and edit existing pipelines.  The second is looking at editing the code that is checked into Azure DevOps and modify any branch within the repository. Either process should allow for editing the underlying Data Factory Artifacts, however, the process for editing pipelines in Azure DevOps does provide more flexibility in that one can edit any branch in the repository instead of just the collaboration branch.

## Azure Data Factory Management

The notebook called pipeline has the code for editing any ADF pipeline using the Azure Mgmt SDK. This provides a step in editing pipeline properties.

### Getting Started

## Azure DevOps SDK

The Azure DevOps SDK allows a person to connect to Azure DevOps and traverse a Git tree to edit any blob in any branch. The editgit notebook has code for updating blobs in a Git repository.

### Getting Started
