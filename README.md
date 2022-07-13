# azuremgmtdatafactory

Update Data Factory pipelines using azure-mgmt-datafactory

This project is looking at two ways to update the pipeline for Azure Data Factory. The first process is looking at leveraging the Azure Mgmt datafactory python package. This will allow anyone to connect to an Azure Data Factory and edit existing pipelines.  The second is looking at editing the code that is checked into Azure DevOps and modify any branch within the repository. Either process should allow for editing the underlying Data Factory Artifacts, however, the process for editing pipelines in Azure DevOps does provide more flexibility in that one can edit any branch in the repository instead of just the collaboration branch.

## Azure Data Factory Management

The notebook called pipeline has the code for editing any ADF pipeline using the Azure Mgmt SDK. This provides a step in editing pipeline properties.

### Getting Started
|Package|Version|
|---|---|
|azure-mgmt| 4.0|
|azure-identity|1.10|

#### Notebooks
The `pipeline.ipynb` is used for editing Azure Data Factory pipelines on the collaboration branch. If for any reason you need to edit alternate branches of your ADF pipelines please use the notebooks in the next process **Azure DevOps SDK**

## Azure DevOps SDK

The Azure DevOps SDK allows a person to connect to Azure DevOps and traverse a Git tree to edit any blob in any branch. The editgit notebook has code for updating blobs in a Git repository.

### Getting Started

You will need the following python packages installed in your environment.
|Package|Version|
|---|---|
|azure-devops| 6.0|
|azure-identity|1.10|
|azure-cli|2.0.81|
|azure devops extension for azure-cli||

#### Installing the Azure-CLI
The python sdk leverages the Azure-CLI to interact with the Azure DevOps APIs. The packages are thin wrappers around the APIs. If you need to install the Azure-CLI please find the corresponding link to your OS and follow the instructions for installation.

<ul>
<li>Install on <a href="https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows">Windows</a></li>
<li>Install on <a href="https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos">Mac OS</a></li>
<li>Install on Linux or Windows Subsystem for Linux (WSL)</li>
<ul>
<li>Install on <a href="https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt">Ubuntu or Debian</a></li>
<li>Install with DNF on <a href="https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=dnf">RHEL, Fedora, CentOS</a></li>
<li>Install with zypper on <a href="https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=zypper">OpenSuse, SLE</a></li>
</ul>
<li>Run in <a href="https://docs.microsoft.com/en-us/cli/azure/run-azure-cli-docker">docker container</a></li>
<li>Run in <a href="https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart">Azure Cloud Shell</a></li>
</ul>

#### Adding the Azure DevOps extension
On the command line you can type the following commands to add the extension
```
az extension add --name azure-devops

```

#### Creating a Personal Access Token (PAT)

1. Sign into your organization (https://dev.azure.com/{yourorganization})
2. From the home page, open the user settings and then select Personal Access Token
3. Select + **New Token**
4. Name your token, select the organization where you want to use the token, and then set your token to automatically expire after a set number of days
5. Select the scope for this token to authorize for your *specific tasks*
6. When your done, make sure to copyt the token and store it in a secure location. For your security, it won't be shown again after you close the dialog box.

You can find the above instructions at the following [Microsoft Document location](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)

#### Authorizing your PAT with Azure DevOps

You can do a one time authorization of your PAT with Azure DevOps using the following commonad

#### Notebook
You will start by using the `editgit.ipynb`. There are a few variables that you will need to adjust to control how the data will look for a branch and the properites it will update. The current example in the notebook edits the "copy" activity of an Azure Data Factory (ADF) pipeline. You can modify the activity and policies to update other pipelines.
