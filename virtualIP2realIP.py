# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:23:49 2024

@author: Allen
"""

import socket
import requests

def get_internal_ip():
    try:
        # 透過 socket 獲取內部 IP
        hostname = socket.gethostname()
        internal_ip = socket.gethostbyname(hostname)
        return internal_ip
    except Exception as e:
        return f"無法獲取內部 IP: {e}"

def get_external_ip():
    try:
        # 使用公共 API 獲取外部 IP
        response = requests.get("https://api64.ipify.org?format=json")
        external_ip = response.json().get("ip")
        return external_ip
    except Exception as e:
        return f"無法獲取外部 IP: {e}"

if __name__ == "__main__":
    internal_ip = get_internal_ip()
    external_ip = get_external_ip()

    print(f"內部 IP: {internal_ip}")
    print(f"外部 IP: {external_ip}")

    
    
    
    
    