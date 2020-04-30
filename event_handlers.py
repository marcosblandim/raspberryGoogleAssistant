import requests

from lib.base_handlers import request_handler, function_handler
from handle_functions import example_of_function, okgoogle_function

example_of_function_handler = function_handler(
    handler_name = "example of function handler,",
    regex = "(?<![a-z])example of get handler(?![a-z])",
    function=example_of_function
)

example_of_get_handler = request_handler(
    handler_name = "example of get handler",
    regex = "example of get handler",
    method = "get",
    request = {
        "url": "",
        "header": {},
    }
)

led_on_handler = request_handler(
    handler_name = "led off handler",
    regex = "(?<![a-z])turn lights on(?![a-z])",
    method = "post",
    request = {
        "url": "http://192.168.0.3/admin/ledSettings?form=enable",
        "header": {
            "Host": "192.168.0.3",
            "Connection": "keep-alive",
            "Content-Length": "39",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://192.168.0.3",
            "Referer": "http://192.168.0.3/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "Authorization=Basic%20admin%3A21232f297a57a5a743894a0e4a801fc3",
        },
        "data": {
            "operation": "write",
            "enable": "toggle",
            "toggle": "on"
        }
    }
)

led_off_handler = request_handler(
    handler_name = "led off handler",
    regex = "(?<![a-z])turn lights off(?![a-z])",
    method = "post",
    request = {
        "url": "http://192.168.0.3/admin/ledSettings?form=enable",
        "header": {
            "Host": "192.168.0.3",
            "Connection": "keep-alive",
            "Content-Length": "39",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://192.168.0.3",
            "Referer": "http://192.168.0.3/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "Authorization=Basic%20admin%3A21232f297a57a5a743894a0e4a801fc3",
        },
        "data": {
            "operation": "write",
            "enable": "toggle",
            "toggle": "off"
        }
    }
)

reboot_handler = request_handler(
    handler_name = "reboot handler",
    regex = "(?<![a-z])reboot(?![a-z])",
    method = "post",
    request = {
        "url": "http://192.168.0.3/admin/reboot.js",
        "header": {
            "Host": "192.168.0.3",
            "Connection": "keep-alive",
            "Content-Length": "39",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://192.168.0.3",
            "Referer": "http://192.168.0.3/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "Authorization=Basic%20admin%3A21232f297a57a5a743894a0e4a801fc3",
        },
        "data": {
            "operation": "write",
        }
    }
)

okgoogle_handler = function_handler(
    handler_name = "ok google handler",
    regex = "",
    function = okgoogle_function
)

HANDLERS = list(
    example_of_function_handler,
    example_of_get_handler,
    reboot_handler,
)
