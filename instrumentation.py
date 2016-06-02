
class Trace:
    def __init__(self, file_name, class_name, method_name):
        self.file_name = file_name
        self.class_name = class_name
        self.method_name = method_name

    def to_string(self):
        s = 'file=%s, class=%s, method=%s' % (self.file_name, self.class_name, self.method_name)
        return s


def file_trace_fn(trace):
    pass


def print_trace_fn(trace):
    print(trace.to_string())


def trace_fn(file_name, class_name, method_name):
    trace = Trace(file_name, class_name, method_name)
    print_trace_fn(trace)
    file_trace_fn(trace)
