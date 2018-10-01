
"""
Automagically generate client code based on an API adapter.
"""

import requests


CLIENT_CODE_TEMPLATE = r"""

class DomainClient(BaseClient):

    _API_VERSION = '{docs[info][version]}'
    _API_HOST = '{docs[host]}'
    _API_SCHEMES = {docs[schemes]}


"""

def parse_path_params(parameters):

    path_keys = []
    query_keys = []

    code_param = ["**kwargs"]
    code_param_template = "{name}{default_if_optional}"

    doc_param_template = """
        :param {name}: {optional}
            {description}.
        """

    doc_type_template = """
        :type {name}:
            {type} {format}
        """

    doc_param, doc_type = ("", "")

    for parameter in parameters:

        kwds = parameter.copy()
        kwds.setdefault("format", "")

        if not kwds["required"]:
            kwds.update(optional="[optional]",
                        default_if_optional="=None")
        else:
            kwds.update(optional="", default_if_optional="")


        code_param.insert(-1, code_param_template.format(**kwds))

        doc_param += doc_param_template.format(**kwds)
        doc_type += doc_type_template.format(**kwds)

        relevant_kwds = dict(path=path_keys, query=query_keys)[parameter["in"]]
        relevant_kwds.append(parameter["name"])

    method_parameters_str = ", ".join(code_param)

    return (method_parameters_str, doc_param, doc_type, path_keys, query_keys)


def parse_method_name(path):
    items = path.strip("/").split("/")[1:]
    return "_".join([item for item in items if not item.startswith("{")]).lower()


def autogen_method_code(path, method_kwds):

    method_parameters_str, doc_param, doc_type, path_keys, query_keys \
        = parse_path_params(method_kwds.get("parameters", []))

    method_name = parse_method_name(path)

    versionless_path = "/".join(path.strip("/").split("/")[1:])
    query_params_repr = ", ".join([f"{k}={k}" for k in query_keys])
    summary = method_kwds["summary"]
    description = method_kwds.get("description", "")

    scopes = ", ".join([f'"{scope}"' for scope in method_kwds["security"][0]["oauth2"]])

    autogen_code = f'''
    @requires_scope({scopes})
    def {method_name}(self, {method_parameters_str}):
        r"""
        {summary}

        {description}

        {doc_param}

        """

        payload = dict({query_params_repr})
        self._api_request(f"{versionless_path}", payload, **kwargs)
    '''

    return autogen_code



def autogen(adapter_documentation_uri):

    docs = requests.get(adapter_documentation_uri).json()

    code = [CLIENT_CODE_TEMPLATE.format(docs=docs)]
    for path, path_kwds in docs["paths"].items():
        
        print(len(path_kwds))

        method = list(path_kwds.keys())[0]
        if method != "get":
            print("Skipping {}".format(path))
            continue

        code.append(autogen_method_code(path, path_kwds[method]))

    return "\n".join(code)






if __name__ == "__main__":

    # Automatically generate client-side Python code based on the public Swagger adapter.
    code = autogen("https://dev.domain.com.au/static/docs/media/public-adapter-v1.json")

