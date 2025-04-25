# Overview
![n8n Project](./docs/videos/n8n_overview.gif)

# Pre-Requisites
## Accounts
For this project you will need the following accounts:
- n8n
- Apify
- OpenAi
- xAi
- Google

## API Keys
Once you have created the necessary accounts,
you will need their respective APIs. 
Below is a list of links for how to create an 
API Key for each of the necessary accounts:
- [Apify](https://blog.apify.com/scoped-api-tokens/#:~:text=with%20your%20account.-,How%20to%20create%20scoped%20API%20tokens,-Creating%20a%20scoped)
    - You don't need to limit the token permissions, but you can if you'd like.
- [OpenAi](https://www.codecademy.com/article/creating-an-openai-api-key)
- [xAi](https://docs.typingmind.com/manage-and-connect-ai-models/xai-(grok-ai)#8d9cb96c5b85421b9ae4d025c264aba5)

# Getting Started
1. Open your n8n workspace
2. Create a new project, if you haven't already
    - You can call it whatever you want. I labeled mine as "Leads"
    - You can use your Personal project, but creating a new project is better for organization
3. Create your Credentials for the following accounts
    - Make sure they are labeled the same way. It may cause an error when running the flows if they aren't labeled the same.

![n8n Credentials](./docs/images/n8n_credentials.png)

- Apify isn't very intuative, so follow the video below will show you how to set it up
![n8n Add Apify Credential](./docs/videos/n8n_apify_credential.gif)

4. For each of the links/flows below, create a new Workflow in n8n and import flow using the links
    1. [Get Leads](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Get_Leads.json)
    2. [Get Social Media Leads](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Get_Social_Media_Leads.json)
    3. [Srape Apollo](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Srape_Apollo.json)
    4. [Scrape Google Maps](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Scrape_Google_Maps.json)
    5. [Scrape Instagram](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Scrape_Instagram.json)
    6. [Scrape LinkedIn](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Scrape_LinkedIn.json)
    7. [Scrape TikTok](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Scrape_TikTok.json)
    8. [Scrape Twitter](https://raw.githubusercontent.com/ConnorLAdams/Lead-Generation/refs/tags/latest/Leads/Scrape_Twitter.json)

![n8n Add Workflow](./docs/videos/n8n_add_workflow.gif)
