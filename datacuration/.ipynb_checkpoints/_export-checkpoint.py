import ipynbname, nbconvert, os, subprocess, sys, time

# Construct the path to the jupyter executable in the virtual environment
venv_path = os.environ.get('VIRTUAL_ENV')
if venv_path:
    jupyter_path = os.path.join(venv_path, 'bin', 'jupyter')
else:
    raise RuntimeError("***ERROR: VIRTUAL_ENV environment variable not set.")

# Construct the nbconvert command
if not jupyter_path:
    raise RuntimeError("***ERROR: Could not construct jupyter_path")

    
def exportNotebookToReadme(strExportFilePathNoEx):
    """
    Generates a README.md file for a given input Notebook file.
    
    NOTE: tables and other output needs to be in Markdown format and **not HTML** since the notebook converter will not strip old HTML style tags and can throw errors
    Also the converter seems to have problems with including installer status (which we do not need anyway but just means we need to make sure to remove that cell output using the `ClearOutput` method for output we do not want to include in the README file).

     Parameters
     ----------
     strExportFilePathNoEx : string (Path to the final output file WITHOUT file extension since a `.md` extension is added by the export method))
    """
    strNotebookFileInput=ipynbname.name()+".ipynb"
    subprocess.run([jupyter_path, "nbconvert", strNotebookFileInput, "--to", "markdown", "--no-input", "--output", strExportFilePathNoEx], check=True)
    # adding the `--no-input` will exclude the python code blocks from the output


def exportSleep(intSeconds=120):
    '''
    We need to sleep the script until we expect the Jupyter notebook to autosave since we need the notebook saved with the codeblock output before we try to export the notebook to Markdown.

     Parameters
     ----------
     intSeconds : int (Number of seconds to sleep; default to 120)

     Example
     ----------
     objWorker.exportSleep(120)
    '''
    time.sleep(intSeconds) # we probably need to sleep the process since the `docmanager:save` method does not seem to work in this environment

