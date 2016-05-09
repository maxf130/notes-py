#!/usr/bin/python3
import sys, os, shutil

import CommonMark

__copyright__ = "Copyright 2016, Maximilian Friedersdorff"
__license__ = "GPLv3"

def main(argv):
    import settings

    if (os.path.exists(settings.compile_path) and not 
            os.path.isdir(settings.compile_path)):
        raise NotADirectoryError("The compile target path '" + 
                                 settings.compile_path + 
                                 "'exists, but is not a directory!")

    def sep_filetype(root, ftype):
        """
        Walk along directory tree and separate contained by given ftype.

        Return 2-tuple (ftype_files, other_files) containing lists of files.
        root is the root of the fs tree from which to start the search.
        ftype is the file extention (including leading dot ('.')) by which to 
        separate the files.
        """
        if os.path.isfile(root): 
            if os.path.splitext(root)[-1] == ftype: 
                return ([root], [])
            else:
                return ([], [root])
        elif os.path.isdir(root):
            ret = ([], []) 
            for node in os.listdir(path=root):
                r = sep_filetype(os.path.join(root, node), ftype)
                ret = (ret[0] + r[0], ret[1] + r[1])

            return ret
        else:
            return []
        
    (mds, other) = sep_filetype(settings.content_path, ".md")

    # Prepare dir structure in compile_path
    if os.path.isdir(settings.compile_path):
        shutil.move(settings.compile_path, settings.compile_path + ".old") 

    os.mkdir(settings.compile_path)
   
    new_dirs = [os.path.dirname(path.replace(settings.content_path, 
                                             settings.compile_path))
                for path in (mds + other)] 
    
    for d in new_dirs:
        os.makedirs(d, exist_ok=True)

    # Copy all non md files
    for f in other:
        new_path = f.replace(settings.content_path, settings.compile_path)
        # Coply file to new path, but don't follow symlinks!
        shutil.copy2(f, new_path, follow_symlinks=False)

    for f in mds:
        with open(f, "r") as md_f:
            md = md_f.read()

        # Going to use simple str.format to build html to avoid deps with 
        # templating languages
        with open(settings.html_template, 'r') as template_f:
            template = template_f.read()

        compiled_html = template.format(body=CommonMark.commonmark(md), 
                                        stylesheet=settings.stylesheet)

        new_path = f.replace(settings.content_path, settings.compile_path)
        new_path = os.path.splitext(new_path)[0] + ".html"
        with open(new_path, "w") as html_f:
            html_f.write(compiled_html)

    if os.path.isdir(settings.compile_path + ".old"):
        shutil.rmtree(settings.compile_path + ".old")
    

if __name__ == "__main__":
    main(sys.argv[1:])
