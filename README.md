# test-re-invent

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function.
- template.yaml - A template that defines the application's AWS resources.
- Makefile - Build definition using `uv`.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
* uv - [Install uv](https://github.com/astral-sh/uv)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
test-re-invent$ sam build
```

The SAM CLI installs dependencies defined in `pyproject.toml` (via `uv export` in Makefile), creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
test-re-invent$ sam local invoke HelloWorldFunction
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
test-re-invent$ sam local start-api
test-re-invent$ curl http://localhost:3000/hello
```
