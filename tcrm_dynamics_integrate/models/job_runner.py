# -*- coding: utf-8 -*-

from odoo import models, fields, api
from io import BytesIO
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

class JobRunner(models.Model):
    _name = 'tcrm_dynamics_integrate.job_runner'

    name = fields.Char('Name', required=False)
    
    def processAgreements(self, env, model, record, records, datetime, dateutil, log):

        #set these values to retrieve the oauth token
        crmorg = 'https://tcgv9.crm.dynamics.com' #base url for crm org
        clientid = 'b65d7577-1eb2-4d85-8e90-b63ab8789270' #application client id
        username = 'alexk@tractioncrm.com' #username
        userpassword = '' #password
        tokenendpoint = 'https://login.microsoftonline.com/b7681380-0df0-46af-bd50-f69afb9c4e4f/oauth2/token' #oauth token endpoint
 
        #set these values to query your crm data
        crmwebapi = 'https://tcgv9.api.crm.dynamics.com/api/data/v9.1' #full path to web api endpoint
        crmwebapiquery = '/contacts?$select=fullname,contactid' #web api query (include leading /)
 
        #build the authorization token request
        tokenpost = {
            'client_id':clientid,
            'resource':crmorg,
            'username':username,
            'password':userpassword,
            'grant_type':'password'
        }
 
        #make the token request
        tokenres = requests.post(tokenendpoint, data=tokenpost)
 
        #set accesstoken variable to empty string
        accesstoken = ''
 
        #extract the access token
        try:
            log(tokenres.text)
            accesstoken = tokenres.json()['access_token']
        except(KeyError):
            #handle any missing key errors
            log('Could not get access token')
 
        #if we have an accesstoken
        if(accesstoken!=''):
            #prepare the crm request headers
            crmrequestheaders = {
                'Authorization': 'Bearer ' + accesstoken,
                'OData-MaxVersion': '4.0',
                'OData-Version': '4.0',
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=utf-8',
                'Prefer': 'odata.maxpagesize=500',
                'Prefer': 'odata.include-annotations=OData.Community.Display.V1.FormattedValue'
            }
 
            #make the crm request
            crmres = requests.get(crmwebapi+crmwebapiquery, headers=crmrequestheaders)
 
            try:
                #get the response json
                crmresults = crmres.json()
 
                #loop through it
                for x in crmresults['value']:
                    log(x['fullname'] + ' - ' + x['contactid'])
            except KeyError:
                #handle any missing key errors
                log('Could not parse CRM results')

        #log('Create CO')
        #url='https://tcgv9.api.crm.dynamics.com/api/data/v9.1/accounts?$select=accountnumber,name'
        #
        #r = requests.post(url, auth=HTTPDigestAuth('alexk@tractioncrm.com', 'Sanya@2018'))
        #
        #log(r.status_code)
        #log(r.text)


        #request = pycurl.Curl()
        #response = BytesIO()
		#
		## Setup http request
        #request.setopt(pycurl.URL, url)
        #request.setopt(pycurl.WRITEDATA, response)
        #request.setopt(pycurl.HTTPAUTH,cURL.HTTPAUTH_NTLM)
        #request.setopt(pycurl.USERPWD,"{}:{}".format('alexk@tractioncrm.com','Sanya@2018'))
		#
        #request.perform()
        #request.close()
		#
		## Retrieve response string and encode using the json module
        #response.getvalue()
        #json.loads(response.getvalue)