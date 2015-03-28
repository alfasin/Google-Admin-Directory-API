# Google APIs

If you ever worked with Google APIs you already know how this world is full of pain:
minimal documentation, almost no code-examples, unclear error messages and etc...

This repo was created to help other people avoid the pain that I went through.

## Content
Starting with [admin directory APIs](https://developers.google.com/admin-sdk/directory/) we'll go through some examples of using the [groups](https://developers.google.com/admin-sdk/directory/v1/reference/groups) and [members](https://developers.google.com/admin-sdk/directory/v1/reference/members) using both the **SDK** as well as implement **REST** calls to *groups*.

## Setup
In order to use Google APIs you first have to register in [Google cloud console](https://console.developers.google.com/), create a project and set credentials (on the left menu-bar). 

All the examples that we'll use are server-side, which means you have to create keys and save the generate .p12 file in a directory which is accessible from your code. When you generate the .p12 file you'll also receive an "account email" (which is your email by default, but assuming you're admin, you can create another email for your organization and use it) and "service account email" which you'll have to use in different cases (I know it's confusing - don't blame me - blame Google). 

The "service account email" is generated for you and has an ugly format that looks like this: 390109889102-qmmpidjfyadcvb9pek054mmnq0sdfppr@developer.gserviceaccount.com

In order to make your life easier I'll use the naming convention: 
```
FULL_PATH_TO_P12 = '/full/path/to/your/file.p12'
ACCOUNT_EMAIL = 'the email you are using in your organization'
SERVICE_EMAIL = 'a generated email address - see example above'
```

When time allows, I'll add code examples for using [Google spreadsheet API](https://developers.google.com/google-apps/spreadsheets/) as well.

Enjoy!
