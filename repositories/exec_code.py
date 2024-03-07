import requests


def get_languages():
    src = "http://backend_server:2358/languages"
    languages = requests.get(src)
    print(languages.json())
    return languages.json()

def execute_code(code, lang, stdin, out):
    src = "http://backend_server:2358/submissions?wait=true"
    format_exec = {
    "source_code": code,
    "language_id": lang,
    "number_of_runs": "1",
    "stdin": stdin,
    "expected_output": out,
    "enable_per_process_and_thread_time_limit": True,
    "enable_per_process_and_thread_memory_limit": True,
    "enable_network": True
}
    hasil = requests.post(src,format_exec).json()['token']
    src_submissions = 'http://backend_server:2358/submissions/%s'%hasil
    output = requests.get(src_submissions).json()
    return output

def execute_program(code , lang):
    src = "http://backend_server:2358/submissions?wait=true"
    format_exec = {
    "source_code": code,
    "language_id": lang,
    "number_of_runs": "1",
    "stdin": None,
    "enable_per_process_and_thread_time_limit": True,
    "enable_per_process_and_thread_memory_limit": True,
    "enable_network": True
}
    hasil = requests.post(src,format_exec).json()['token']
    src_submissions = 'http://backend_server:2358/submissions/%s'%hasil
    output = requests.get(src_submissions).json()["stdout"]
    return output
