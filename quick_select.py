from jinja2 import Environment, FileSystemLoader
from IPython.display import IFrame
from IPython.display import display
import base64

class QuickSelect:

    PLATE_6_WELLS = "6wp"
    PLATE_12_WELLS = "12wp"
    PLATE_24_WELLS = "24wp"
    PLATE_48_WELLS = "48wp"
    PLATE_96_WELLS = "96wp"
    PLATE_384_WELLS = "384wp"

    def __init__(self, template_path='.'):
        self.env = Environment(loader=FileSystemLoader(template_path))

    def renderPlate(self, plate_type):
        PLATE_SPECIFICATIONS = {
            self.PLATE_6_WELLS: {"columns": 3, "rows": 2},
            self.PLATE_12_WELLS: {"columns": 4, "rows": 3},
            self.PLATE_24_WELLS: {"columns": 6, "rows": 4},
            self.PLATE_48_WELLS: {"columns": 8, "rows": 6},
            self.PLATE_96_WELLS: {"columns": 12, "rows": 8},
            self.PLATE_384_WELLS: {"columns": 24, "rows": 16},
        }

        if plate_type not in PLATE_SPECIFICATIONS:
            raise ValueError(f"Unsupported plate type: {plate_type}")
        
        template = self.env.get_template('interface.html')
        specs = PLATE_SPECIFICATIONS[plate_type]

        rendered_html = template.render(columnCountFromPython=specs["columns"], rowCountFromPython=specs["rows"])
        encoded_html = base64.b64encode(rendered_html.encode('utf-8')).decode('utf-8')
        data_uri = f"data:text/html;base64,{encoded_html}"
        display(IFrame(src=data_uri, width=1200, height=700))
