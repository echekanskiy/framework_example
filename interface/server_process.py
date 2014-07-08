import platform

if platform.system() == "Windows":
    _feature_map = {}
    import windows.server_process
    _feature_map["is_server_running"] = windows.server_process.is_server_running
else:
    _feature_map = {}
    import linux.server_process
    _feature_map["is_server_running"] = linux.server_process.is_server_running


def is_server_running(text):
    return _feature_map["is_server_running"](text)