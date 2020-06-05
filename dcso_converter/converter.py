import jinja2
import rdflib

DCSO_TEMPLATE = 'madmp.ttl.j2'


class DCSOConverter:

    FORMATS = ['ttl', 'xml', 'n3', 'ntriples', 'trig', 'json-ld']

    def __init__(self):
        self.j2_env = jinja2.Environment(
            loader=jinja2.PackageLoader('dcso_converter', 'templates'),
            extensions=['jinja2.ext.do'],
        )
        self.template = self.j2_env.get_template(DCSO_TEMPLATE)

    @staticmethod
    def _rdf_convert(content: str, input_format: str, output_format: str):
        graph = rdflib.Graph().parse(data=content, format=input_format)
        result = graph.serialize(format=output_format)
        return result

    def convert(self, madmp: dict, format: str = 'ttl') -> str:
         ttl_content = self.template.render(madmp=madmp)
         if format == 'ttl':
             return ttl_content
         else:
             return self._rdf_convert(ttl_content, 'ttl', format)
