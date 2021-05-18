from jmd_imagescraper.core import * # pip install jmd-imagescraper
from pathlib import Path

root = Path().cwd()/"images"

duckduckgo_search(root, "Train","Mango", max_results=30000)

from jmd_imagescraper.imagecleaner import *

display_image_cleaner(root)
