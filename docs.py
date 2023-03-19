# MIT License

# Copyright (c) 2023 PHYSCORP

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Try to import libraries
try:
    import os
    import sys
    from fpdf import FPDF
    from rich.progress import Progress, SpinnerColumn, BarColumn
    from rich import print
    from rich.traceback import install
    install()
except ImportError as e:
    print("Error: " + str(e))
    print("Please run `python3 -m pip install -r requirements.txt`")
    exit()

# Determine main program directory
maindirectory = os.path.dirname(os.path.abspath(__file__)) # The absolute path to this file

# Get arguments from kwargs
try:
    sys_args = sys.argv[1:]
    arguments = {}
    for value in sys_args:
        if value.startswith("--"):
            value = value[2:]
        value = value.split("=")
        arguments[value[0]] = value[1]
except IndexError:
    print("[ERROR]: No arguments were provided. You must provide arguments in the format of `argument=value`")
    print("Example: `python3 docs.py name=\"checkers.py\"`")
    quit()

# Get name
try:
    name = arguments["name"].lower()
    name_no_extension = name.split(".")[0]
except KeyError:
    print("[ERROR]: No name was provided. You must provide a name using the format of `name=\"checkers.py\"`")
    quit()

# Documentation
def documentation(page):
    # Failsafe, make everything lowercase
    page = page.lower()

    # [ If statements based on the page ]
    
    # Checkers
    if page == "checkers":
        return """
This is the text documentation for the Checkers game. Replace everything in between the triple quotes with the documentation.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lacus luctus accumsan tortor posuere ac ut consequat semper. Sed faucibus turpis in eu mi bibendum neque. Diam phasellus vestibulum lorem sed. Tristique magna sit amet purus gravida quis blandit. Sagittis nisl rhoncus mattis rhoncus urna neque. Dignissim convallis aenean et tortor at risus viverra. Magna fermentum iaculis eu non diam phasellus vestibulum lorem sed. Adipiscing commodo elit at imperdiet dui accumsan sit amet nulla. Nullam eget felis eget nunc lobortis mattis aliquam faucibus. Mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing.

Orci porta non pulvinar neque laoreet suspendisse interdum consectetur libero. Arcu risus quis varius quam quisque id diam vel quam. Faucibus turpis in eu mi bibendum neque egestas. Nunc consequat interdum varius sit amet mattis vulputate enim nulla. Id semper risus in hendrerit gravida rutrum quisque non tellus. Vulputate sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum. Malesuada fames ac turpis egestas maecenas. Eget mi proin sed libero enim sed. Morbi tincidunt ornare massa eget egestas purus. Sit amet aliquam id diam. Sociis natoque penatibus et magnis. Quam viverra orci sagittis eu volutpat odio facilisis mauris sit. Adipiscing elit duis tristique sollicitudin nibh. Sed odio morbi quis commodo. Convallis aenean et tortor at risus. Quis enim lobortis scelerisque fermentum dui faucibus in ornare quam. Tellus in metus vulputate eu. Hac habitasse platea dictumst quisque sagittis purus sit. Justo eget magna fermentum iaculis eu non diam.

Sollicitudin tempor id eu nisl nunc mi. Nibh mauris cursus mattis molestie a iaculis at. Gravida neque convallis a cras. Amet purus gravida quis blandit turpis cursus in hac. Erat imperdiet sed euismod nisi. Pharetra et ultrices neque ornare aenean euismod elementum nisi quis. Dui faucibus in ornare quam. Urna duis convallis convallis tellus id interdum velit. Feugiat vivamus at augue eget. Cursus in hac habitasse platea dictumst quisque sagittis purus sit.

Aenean euismod elementum nisi quis eleifend quam adipiscing vitae proin. Lectus vestibulum mattis ullamcorper velit. Ultricies leo integer malesuada nunc vel risus. Sit amet risus nullam eget felis eget nunc lobortis mattis. Eu augue ut lectus arcu bibendum. At ultrices mi tempus imperdiet. Est ultricies integer quis auctor elit sed vulputate. Netus et malesuada fames ac turpis egestas sed tempus urna. Aenean pharetra magna ac placerat vestibulum lectus mauris ultrices eros. Fermentum iaculis eu non diam phasellus vestibulum lorem. Enim diam vulputate ut pharetra. Consequat ac felis donec et odio pellentesque diam volutpat. Sed egestas egestas fringilla phasellus. Praesent tristique magna sit amet purus gravida quis. Bibendum neque egestas congue quisque egestas diam. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Condimentum vitae sapien pellentesque habitant. Et sollicitudin ac orci phasellus egestas tellus.

Quis risus sed vulputate odio ut enim blandit volutpat. Iaculis at erat pellentesque adipiscing commodo elit at. Elementum sagittis vitae et leo. A iaculis at erat pellentesque. Diam sit amet nisl suscipit adipiscing bibendum est ultricies integer. Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Porta non pulvinar neque laoreet suspendisse interdum. Vitae auctor eu augue ut. Dui id ornare arcu odio ut. Vivamus at augue eget arcu. Diam in arcu cursus euismod quis viverra nibh. Sit amet nisl purus in. Tellus at urna condimentum mattis pellentesque id. Felis eget velit aliquet sagittis id. Eget nunc lobortis mattis aliquam faucibus purus in.
    """

    # Chess
    if page == "chess":
        return """
This is the text documentation for the Chess game. Replace everything in between the triple quotes with the documentation.
    """

    # Failsafe, return error
    return "Error: Page not found, please check your spelling."

# Main execution
if __name__ == "__main__":
    with Progress("{task.description}", SpinnerColumn(), BarColumn()) as progress:
        program_name_task = progress.add_task(f"[bold green] ⚙ Attempting to make PDF of {name}", start=False)
    
        # Check if temp folder exists
        if not os.path.exists(os.path.join(maindirectory, "temp")):
            # If it doesn't, create it
            os.mkdir(os.path.join(maindirectory, "temp"))
            print(f"[INFO] Created temp folder in {maindirectory}")

        # Check if file exists in temp folder. Ex: "checkers.pdf"
        if os.path.exists(os.path.join(maindirectory, "temp", name_no_extension + ".pdf")):
            # If it does, delete it
            os.remove(os.path.join(maindirectory, "temp", name_no_extension + ".pdf"))
            print(f"[INFO] Deleted {name_no_extension}.pdf in temp folder")
        
        # Create a PDF object
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # Set header font
        pdf.set_font("Times", "B", 16)

        # Set header
        pdf.cell(0, 10, txt=f"Documentation for {name_no_extension.title()}", ln=1, align="C")

        # Set font
        pdf.set_font("Times", size=12)

        # Get documentation
        doc = documentation(name_no_extension)
        print(f"[INFO] Got documentation for {name_no_extension}")

        # Add text with multi_cell, spanning the entire page
        pdf.multi_cell(0, 10, txt=doc, align="L")

        # Save the PDF with name
        pdf.output(os.path.join(maindirectory, "temp", name_no_extension + ".pdf"))
        print(f"[INFO] Saved {name_no_extension}.pdf in temp folder")

        # Finish task
        progress.update(program_name_task, completed=100)
        progress.console.print(f"[bold green] ✔ Successfully made PDF of {name}!")