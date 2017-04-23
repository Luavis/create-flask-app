from flask import Flask


__author__ = "${{ AUTHOR }}"
__copyright__ = "Copyright ${{ YEAR }}, ${{ AUTHOR }}"
__credits__ = ["${{ AUTHOR }}", ]
__license__ = "${{ LICENSE }}"
__version__ = "${{ VERSION }}"
__status__ = "Development"


app = Flask(__name__, static_url_path='/static')
