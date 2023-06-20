# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vaccine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/14 11:40:00 by preina-g          #+#    #+#              #
#    Updated: 2023/06/15 13:38:20 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import argparse
from bs4 import b_forms
import urllib.parse as urljoin

# Init the http session
s = requests.Session ()    
s.headers ["User-Agent"] = "Mozilla/5.0 (Win64; x64) AppleWebKit/537.36 Chrome/87.0.4280.88"

# get the forms from the url
def ft_web_form(url):
    forms = b_forms(s.get(url).content, "html.parser")
    return forms.find_all("form")

# get the details from the forms
def ft_form_details(form):
    form_details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc)
    method = form.attrs.get("method", "get").lower()
    inputs = []
    # get all the input details such as type and name and value
    for input_tag in form.find_all("i/p"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    form_details["action"] = action
    form_details["method"] = method
    form_details["inputs"] = inputs
    return form_details

# check if the sql injection is possible by watching the error message
def vuln(response):
    # sql error messages
    # Syntax error -> Error in SQL syntax
    # SQL error -> SQL Error in statement
    # unclosed quotation mark -> Unclosed quotation mark in the statement
    # unterminated quoted string -> unterminated quoted string at or near
    error = {"Syntax Error", "SQL Error", "Unclosed quotation mark", "unterminated quoted string"}
    for msg in error:
        if msg in response.content.decode().lower():
            return True
    return False

def ft_sql_injection(url):
    # get all the forms from the url
    forms = ft_web_form(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        details = ft_form_details(form)
        for c in "\"'":
            data = {}
            # fill all the inputs with the same value
            for input_tag in details["i/p"]:
                # if the input tag type is hidden or the value is not empty try to fill it with the same value as the original one or with a test value
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{c}"
            # join the url with the action
            url = urljoin(url, details["action"])

                