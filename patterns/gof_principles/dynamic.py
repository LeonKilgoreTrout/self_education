class PatternFilteredLog: ...
class SeverityFilteredLog: ...
class FileLog: ...
class SocketLog: ...
class SyslogLog: ...


filters = {
    'pattern': PatternFilteredLog,
    'severity': SeverityFilteredLog
}

outputs = {
    'file': FileLog,
    'socket': SocketLog,
    'syslog': SyslogLog
}

with open('config') as f:
    filter_name, output_name = f.read().split()

filter_cls = filters[filter_name]
output_cls = outputs[output_name]

name = filter_name.title() + output_name.title() + 'Log'
cls = type(name, (filter_cls, output_cls), {})

logger = cls(...)
