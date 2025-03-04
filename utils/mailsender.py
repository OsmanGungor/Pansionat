from __future__ import print_function

import os
from pprint import pprint

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

api_key = os.environ.get("BREVO_API_KEY")


def send_mail(subject, body):

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key["api-key"] = api_key
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender={"name": "Osman Gungor", "email": "osmangungor83@gmail.com"},
        to=[{"email": "osmangungor83@gmail.com", "name": "Osman Gungor"}],
        subject=subject,
        html_content=f"<html><body><h1>{body}</h1></body></html>",
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling TransactionalEmailsApi->send_transac_email: %s\n"
            % e
        )
