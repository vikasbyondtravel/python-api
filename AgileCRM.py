import requests
import json
from urlparse import urljoin


APIKEY = "123456"   # Your API KEY
EMAIL = "sample@agilecrm.com"  # Your API EMAIL
DOMAIN = "sample"  # Your DOMAIN

DURL = "https://" + DOMAIN + ".agilecrm.com/dev/api/"

# Function definition is here
def agileCRM(nextURL,method,data,contenttype):

   url = DURL + nextURL

   headers = {
        'Accept': 'application/json',
        'content-type': contenttype,
    }

   if ( method  == "GET" ) :
       
       response = requests.get(
        url,
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text
    
   if ( method  == "POST" ) :
       
       response = requests.post(
        url,
        data=json.dumps(data),
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text
    
   if ( method  == "PUT" ) :
       response = requests.put(
        url,
        data=json.dumps(data),
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text

   if ( method  == "DELETE" ) :
       response = requests.delete(
        url,
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response

   if ( method  == "POSTFORM" ) :
       
       response = requests.post(
        url,
        data=data,
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text

   
   return "Wrong method provided"

# ================================================= CREATE CONTACT===============================================
contact_data = {
    "star_value": "4",
    "lead_score": "92",
    "tags": [
        "Lead",
        "Likely Buyer"
    ],
    "properties": [
        {
            "type": "SYSTEM",
            "name": "first_name",
            "value": "Los "
        },
        {
            "type": "SYSTEM",
            "name": "last_name",
            "value": "Bruikheilmer"
        },
        {
            "type": "SYSTEM",
            "name": "company",
            "value": "steady.inc"
        },
        {
            "type": "SYSTEM",
            "name": "title",
            "value": "VP Sales"
        },
        {
            "type": "SYSTEM",
            "name": "email",
            "subtype": "work",
            "value": "akrambakram@yabba.com"
        },
        {
            "type": "SYSTEM",
            "name": "address",
            "value": "{\"address\":\"225 George Street\",\"city\":\"NSW\",\"state\":\"Sydney\",\"zip\":\"2000\",\"country\":\"Australia\"}"
        },
        {
            "type": "CUSTOM",
            "name": "My Custom Field",
            "value": "Custom value"
        }
    ]
}

# print agileCRM("contacts","POST",contact_data,"application/json")

# ================================================= UPDATE CONTACT===============================================

update_contact_data = {
    "id": "5707397775491072",
    "properties": [
        {
            "type": "SYSTEM",
            "name": "last_name",
            "value": "Chan"
        },
        {
            "type": "CUSTOM",
            "name": "My Custom Field",
            "value": "Custom value chane"
        }
    ]
}

#print agileCRM("contacts/edit-properties","PUT",update_contact_data,"application/json")

# ================================================= GET CONTACT BY ID===============================================

#print agileCRM("contacts/5707397775491072","GET",None,"application/json")

# ================================================= GET CONTACT BY Email===============================================

#print agileCRM("contacts/search/email/support+id20297@agilecrm.zendesk.com","GET",None,"application/json")

# ================================================= DELETE CONTACT BY ID===============================================

#print agileCRM("contacts/5716466867372032","DELETE",None,"application/json")

# ================================================= SEAR CONTACT BY OF EMAIL ID 2===============================================

email_data = "email_ids=[%s]" % "poonam.baranwal@invenio-solutions.com"

#print agileCRM("contacts/search/email","POSTFORM",email_data,"application/x-www-form-urlencoded")

# ================================================= 1.5 Update lead score by ID  ==============================================

update_lead_score = {
    "id": "5708993221623808",
    "lead_score": 20
}

# print agileCRM("contacts/edit/lead-score","PUT",update_lead_score,"application/json")

# ================================================= 1.6 Update star value by ID  ==============================================

update_star_value = {
    "id": "5708993221623808",
    "star_value": 2
}

#print agileCRM("contacts/edit/add-star","PUT",update_star_value,"application/json")

# ================================================= 7 Update tags value by ID  ==============================================

update_tag_value = {
    "id": "5708993221623808",
    "tags": [
        "test1",
        "test2"
    ]
}

#print agileCRM("contacts/edit/tags","PUT",update_tag_value,"application/json")

# ================================================= 8 Delete tags value by ID  ==============================================

delete_tag_value = {
    "id": "5708993221623808",
    "tags": [
        "test1",
        "test2"
    ]
}

#print agileCRM("contacts/delete/tags","PUT",delete_tag_value,"application/json")

# ================================================= 9 Delete contact value by ID  ==============================================


# print agileCRM("contacts/5737789366730752","DELETE",None,"application/json")

# ================================================= CREATE COMPANY===============================================

company_data = {
    "type": "COMPANY",
    "star_value": 4,
    "lead_score": 120,
    "tags": [
        "Permanent",
        "USA",
        "Hongkong",
        "Japan"
    ],
    "properties": [
        {
            "name": "Company Type",
            "type": "CUSTOM",
            "value": "MNC Inc"
        },
        {
            "type": "SYSTEM",
            "name": "name",
            "value": "Spicejet"
        },
        {
            "type": "SYSTEM",
            "name": "url",
            "value": "http://www.spicejet.com/"
        },
        {
            "name": "email",
            "value": "care@spicejet.com  ",
            "subtype": ""
        },
        {
            "name": "phone",
            "value": "45500000",
            "subtype": ""
        },
        {
            "name": "website",
            "value": "http://www.linkedin.com/company/agile-crm",
            "subtype": "LINKEDIN"
        },
        {
            "name": "address",
            "value": "{\"address\":\"MS 35, 440 N Wolfe Road\",\"city\":\"Sunnyvale\",\"state\":\"CA\",\"zip\":\"94085\",\"country\":\"US\"}",
            "subtype": "office"
        }
    ]
}

#print agileCRM("contacts","POST",company_data,"application/json")

# ================================================= UPDATE COMPANY===============================================

update_company_data = {
    "id": 5661396394049536,
    "properties": [
        {
            "type": "SYSTEM",
            "name": "name",
            "value": "SPICE JET"
        },
        {
            "type": "SYSTEM",
            "name": "url",
            "value": "http://www.spicejet.com/"
        },
        {
            "name": "phone",
            "value": "45500000",
            "subtype": ""
        }
    ]
}

#print agileCRM("contacts/edit-properties","PUT",update_company_data,"application/json")

# ================================================= GET COMPANY BY ID===============================================

#print agileCRM("contacts/5661396394049536","GET",None,"application/json")

# ================================================= DELETE COMPANY BY ID===============================================

#print agileCRM("contacts/5661396394049536","DELETE",None,"application/json")

# ================================================= CREATE DEAL===============================================

deal_data = {
    "name": "Deal-Tomato",
    "expected_value": "500",
    "probability": "75",
    "close_date": 1455042600,
    "milestone": "Proposal",
    "contact_ids": [
        "5661679325020160"
    ],
    "custom_data": [
        {
            "name": "Group Size",
            "value": "10"
        }
    ]
}

#print agileCRM("opportunity","POST",deal_data,"application/json")

# ================================================= Update DEAL===============================================

update_data = {
    "id": "5647457211908096",
    "expected_value": "1000",
    "probability": "20",
    "milestone": "Proposal",
    "contact_ids": [
        "5661679325020160",
        "5684821548335104"
    ],
    "custom_data": [
        {
            "name": "dealTester",
            "value": "hello hello2"
        }
    ]
}

#print agileCRM("opportunity/partial-update","PUT",update_data,"application/json")