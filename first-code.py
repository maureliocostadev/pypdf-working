### references https://pypdf.readthedocs.io/en/stable/user/metadata.html

from datetime import datetime
from pypdf import PdfReader, PdfWriter
import subprocess

subprocess.run('clear', shell=True)

reader = PdfReader("example.pdf")
writer = PdfWriter(clone_from="example.pdf")

page = reader.pages[0]
print(page.extract_text())
print('--'*100)
print('--'*100)
# extract only text oriented up
print(page.extract_text(0))
print('--'*100)
print('--'*100)
# extract text oriented up and turned left
print(page.extract_text((0, 90)))
print('--'*100)
print('--'*100)
# extract text in a fixed width format that closely adheres to the rendered
# layout in the source pdf
print(page.extract_text(extraction_mode="layout"))
print('--'*100)
# extract text preserving horizontal positioning without excess vertical
# whitespace (removes blank and "whitespace only" lines)
print(page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False))
print('--'*100)
# adjust horizontal spacing
print(page.extract_text(extraction_mode="layout", layout_mode_scale_weight=1.0))
print('--'*100)
# exclude (default) or include (as shown below) text rotated w.r.t. the page
print(page.extract_text(extraction_mode="layout", layout_mode_strip_rotated=False))
print('--'*100)


# meta = reader.metadata

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # If you want to add the old metadata, include these two lines
# if reader.metadata is not None:
#     writer.add_metadata(reader.metadata)



# # All of the following could be None!
# print(meta.title)
# print(meta.author)
# print(meta.subject)
# print(meta.creator)
# print(meta.producer)
# print(meta.creation_date)
# print(meta.modification_date)



