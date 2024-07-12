# Introduction

This page contains instructions for choosing and maintaining a Google Cloud CLI installation. The Google Cloud CLI includes the `gcloud`, `gsutil` and `bq` command-line tools. For a list of gcloud CLI features, see [All features](https://cloud.google.com/sdk#all-features).

To access the [Google Cloud APIs](https://cloud.google.com/apis/docs/overview) using a supported programming language, you can download the [Cloud Client Libraries](https://cloud.google.com/apis/docs/cloud-client-libraries).

## Installation instructions

These instructions are for installing the Google Cloud CLI. For information about installing additional components, such as gcloud CLI commands at the alpha or beta release level, see [Managing gcloud CLI components](https://cloud.google.com/sdk/gcloud/guide/managing-components).

[Linux](https://cloud.google.com/sdk/docs/install#linux)[Debian/Ubuntu](https://cloud.google.com/sdk/docs/install#debianubuntu)[Red Hat/Fedora/CentOS](https://cloud.google.com/sdk/docs/install#red-hatfedoracentos)[macOS](https://cloud.google.com/sdk/docs/install#macos)[Windows](https://cloud.google.com/sdk/docs/install#windows)

**Package contents**

The gcloud CLI is available in package format for installation on Debian and Ubuntu systems. This package contains the `gcloud`, `gcloud alpha`, `gcloud beta`, `gsutil`, and `bq` commands only. It doesn't include `kubectl` or the App Engine extensions required to deploy an application using `gcloud` commands. If you want these components, you must [install them separately](https://cloud.google.com/sdk/docs/install#deb-additional).

**Before you begin**

Before you install the gcloud CLI, make sure that your operating system meets the following requirements:

-   It is an Ubuntu release that hasn't reached [end-of-life](https://wiki.ubuntu.com/Releases) or a Debian stable release that hasn't reached [end-of-life](https://wiki.debian.org/DebianReleases)
-   It has recently updated its packages:
    
    ```text
    sudo apt-get update
    
    
-   It has [`apt-transport-https`](https://packages.debian.org/bullseye/apt-transport-https) and `curl` installed:
    
    ```text
    sudo apt-get install apt-transport-https ca-certificates gnupg curl
    
    

**Installation**

1.  Import the Google Cloud public key.
    -   For newer distributions (Debian 9+ or Ubuntu 18.04+) run the following command:
        
        ```text
        curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
        
    -   For older distributions, run the following command:
        
        ```text
        curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
        
    -   If your distribution's apt-key command doesn't support the `--keyring` argument, run the following command:
        
        ```text
        curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
        
    -   If you can't get latest updates due to an expired key, [obtain the latest apt-get.gpg key file](https://cloud.google.com/compute/docs/troubleshooting/known-issues#keyexpired).
        
2.  Add the gcloud CLI distribution URI as a package source.
    -   For newer distributions (Debian 9+ or Ubuntu 18.04+), run the following command:
        
        ```text
        echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
        
    -   For older distributions that don't support the signed-by option, run the following command:
        
        ```text
        echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
        
3.  Update and install the gcloud CLI:
    
    ```text
    sudo apt-get update && sudo apt-get install google-cloud-cli
    
    For additional `apt-get` options, such as disabling prompts or dry runs, refer to the [`apt-get` man pages](https://linux.die.net/man/8/apt-get).
    
    **Docker Tip:** If installing the gcloud CLI inside a Docker image, use a single RUN step instead:
    
    ```text
    RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-sdk -y
    
    For older base images that do not support the `gpg --dearmor` command:
    ```text
    RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-cli -y
      
4.  (Optional) Install any of the following [additional components](https://cloud.google.com/sdk/docs/components#additional_components):
    
    -   `google-cloud-cli`
    -   `google-cloud-cli-anthos-auth`
    -   `google-cloud-cli-app-engine-go`
    -   `google-cloud-cli-app-engine-grpc`
    -   `google-cloud-cli-app-engine-java`
    -   `google-cloud-cli-app-engine-python`
    -   `google-cloud-cli-app-engine-python-extras`
    -   `google-cloud-cli-bigtable-emulator`
    -   `google-cloud-cli-cbt`
    -   `google-cloud-cli-cloud-build-local`
    -   `google-cloud-cli-cloud-run-proxy`
    -   `google-cloud-cli-config-connector`
    -   `google-cloud-cli-datastore-emulator`
    -   `google-cloud-cli-firestore-emulator`
    -   `google-cloud-cli-gke-gcloud-auth-plugin`
    -   `google-cloud-cli-kpt`
    -   `google-cloud-cli-kubectl-oidc`
    -   `google-cloud-cli-local-extract`
    -   `google-cloud-cli-minikube`
    -   `google-cloud-cli-nomos`
    -   `google-cloud-cli-pubsub-emulator`
    -   `google-cloud-cli-skaffold`
    -   `google-cloud-cli-spanner-emulator`
    -   `google-cloud-cli-terraform-validator`
    -   `google-cloud-cli-tests`
    -   `kubectl`
    
    For example, the `google-cloud-cli-app-engine-java` component can be installed as follows:
    
    ```text
    sudo apt-get install google-cloud-cli-app-engine-java
    
5.  Run [`gcloud init`](https://cloud.google.com/sdk/gcloud/reference/init) to get started:
    
    ```text
    gcloud init
    

**Downgrading gcloud CLI versions**

To revert to a specific version of the gcloud CLI, where `VERSION` is of the form `123.0.0`, run the following command:

```
sudo apt-get update &amp;&amp; sudo apt-get install google-cloud-cli=123.0.0-0
```

The ten most recent releases are always available in the repo.

NOTE: For releases prior to 371.0.0, the package name is `google-cloud-sdk`

## Other installation options

Depending on your development needs, instead of the [recommended installation](https://cloud.google.com/sdk/docs/install#installation_instructions), you can use an alternative method of installing the gcloud CLI:

-   **Using the gcloud CLI with scripts or Continuous Integration/Deployment?** Download a [versioned archive](https://cloud.google.com/sdk/docs/downloads-versioned-archives) for a non-interactive installation of a specific version of the gcloud CLI.
-   **Need to run the gcloud CLI as a Docker image?** Use the [gcloud CLI Docker image](https://cloud.google.com/sdk/docs/downloads-docker) for the latest release (or a specific version) of the gcloud CLI.
-   **Running Ubuntu and prefer automatic updates?** Use a [snap package](https://cloud.google.com/sdk/docs/downloads-snap) to install the gcloud CLI.
-   For Windows and macOS interactive installations, and all other use cases, run the [interactive installer](https://cloud.google.com/sdk/docs/downloads-interactive) to install the latest release of the gcloud CLI.

## Manage an installation

After you have installed the gcloud CLI, you can use commands in the [`gcloud components`](https://cloud.google.com/sdk/gcloud/reference/components) command group to [manage your installation](https://cloud.google.com/sdk/gcloud/guide/managing-components). This includes viewing installed components, adding and removing components, and upgrading to a new version or downgrading to a specific version of the gcloud CLI.

## Earlier versions of the gcloud CLI

If you need a different version of the gcloud CLI, install the current version using the instructions that appear earlier on this page and then [log in](https://cloud.google.com/sdk/docs/authorizing). After you are logged in, you can [download earlier releases](https://console.cloud.google.com/storage/browser/cloud-sdk-release). To see the versions sorted by date, be sure to enable **Sort and filter** and click the **Created** column.

## Supported Python versions

The Google Cloud CLI requires Python 3.8 to 3.12. For information on how to choose and configure your Python interpreter, see [`gcloud topic startup`](https://cloud.google.com/sdk/gcloud/reference/topic/startup).

## Try it for yourself

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads.

[Get started for free](https://console.cloud.google.com/freetrial)