# Azure Functions binding examples in Python

The following samples are used as a basis for [Azure Functions 2.x+ binding](https://docs.microsoft.com/azure/azure-functions/functions-triggers-bindings#supported-bindings) examples in Python.

## Settings and configuration

The *local.settings.example.json* file is provided for your convenience. Rename the file to *local.settings.json* and add your own connection and API values before trying to run the examples in this repo.

If you're using Visual Studio Code, you can use the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension with the *routes.http* file. This file gives you the ability to call sample functions with a single click inside VS Code.

## Samples

The following samples are available in this repo.

| Name | Description  | Trigger | Input | Output |
|------|--------------|---------|-------|--------|
| [HttpTrigger](HttpTrigger) | Triggered by an HTTP request. | Http | N/A | Http |
| [HttpTriggerRoutes](HttpTriggerRoutes) | Triggered by an HTTP request, configured with a custom route. | Http | N/A | Http |
| [HttpTriggerSendGrid](HttpTriggerSendGridDemo)  | Send an email message via [SendGrid](https://sendgrid.com/). | Http | N/A | SendGrid message |
|[EventGridTrigger](EventGridTriggerDemo)|Triggered by an Event Grid event|Event Grid event|Event Grid message|N/A|
|[QueueTrigger](QueueTrigger)|Triggered by a Queue message|Queue message|Queue message|N/A|
|[TableStorageInput](TableStorageInput)|Accepts table row ID as a route parameter and makes table row available to function|Http|Storage Table Row|Http|
|[TableStorageOutput](TableStorageOutput)|Create table storage row|Http|N/A|Storage Table Row|
|[ServiceBusOutput](ServicecBusOutput)|Read Service Bus message.|Http|N/A|Service Bus|
|[ServiceBusTriggerDemo](ServiceBusTriggerDemo)|Create a Service Bus message.|Service Bus|Service Bus message|N/A|
